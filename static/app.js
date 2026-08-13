const messages = document.getElementById("messages");
const form = document.getElementById("ask-form");
const questionInput = document.getElementById("question");
const submitBtn = form.querySelector("button[type=submit]");
const tokenInput = document.getElementById("token");
const connectBtn = document.getElementById("connect-btn");
const authStatus = document.getElementById("auth-status");

const ARABIC_RE = /[؀-ۿ]/;
// C1 fix: the token IS the tenant (server.py resolves client from it, the
// request body's `client` field is server-ignored) -- sessionStorage so it
// doesn't survive to a shared machine's next session, but does survive a
// page reload within this tab.
const TOKEN_KEY = "olives_token";
const SESSION_KEY = "olives_session_id";

function sessionId() {
  let id = sessionStorage.getItem(SESSION_KEY);
  if (!id) {
    id = crypto.randomUUID();
    sessionStorage.setItem(SESSION_KEY, id);
  }
  return id;
}

function getToken() {
  return sessionStorage.getItem(TOKEN_KEY) || "";
}

function setConnected(connected) {
  questionInput.disabled = !connected;
  submitBtn.disabled = !connected;
  if (connected) {
    authStatus.textContent = "✓ متصل";
    authStatus.className = "ok";
  }
}

function clearToken(reason) {
  sessionStorage.removeItem(TOKEN_KEY);
  setConnected(false);
  authStatus.textContent = reason || "";
  authStatus.className = "err";
}

function connect() {
  const t = tokenInput.value.trim();
  if (!t) return;
  sessionStorage.setItem(TOKEN_KEY, t);
  tokenInput.value = "";
  setConnected(true);
}

connectBtn.addEventListener("click", connect);
tokenInput.addEventListener("keydown", (e) => {
  if (e.key === "Enter") { e.preventDefault(); connect(); }
});

if (getToken()) setConnected(true); // restore a token saved earlier in this tab

function addMessage(text, role) {
  const div = document.createElement("div");
  div.className = `msg ${role}`;
  if (!ARABIC_RE.test(text)) div.classList.add("en");
  div.textContent = text;
  messages.appendChild(div);
  messages.scrollTop = messages.scrollHeight;
  return div;
}

async function ask(question) {
  const bot = addMessage("...", "bot");
  let resp;
  try {
    resp = await fetch("/ask", {
      method: "POST",
      headers: { "Content-Type": "application/json", "Authorization": `Bearer ${getToken()}` },
      body: JSON.stringify({ question, session_id: sessionId() }),
    });
  } catch (e) {
    bot.textContent = "تعذر الاتصال بالخادم";
    bot.className = "msg error";
    return;
  }

  // A 401/403 body is plain JSON, not an SSE stream -- reading it with the
  // SSE parser below would just silently find no "data: " lines and leave
  // the bubble stuck on "..." forever (the exact failure this UI shipped
  // with, since it never sent a token at all before this fix).
  if (resp.status === 401 || resp.status === 403) {
    bot.remove();
    clearToken(resp.status === 401 ? "الرجاء إدخال رمز الدخول" : "رمز الدخول غير صحيح");
    return;
  }
  if (!resp.ok) {
    bot.textContent = `خطأ (${resp.status})`;
    bot.className = "msg error";
    return;
  }

  const reader = resp.body.getReader();
  const decoder = new TextDecoder();
  let buffer = "";
  let gotAnything = false;
  // C7: real progress instead of one frame at the end. `streaming` flips
  // true on the first live answer token -- until then, a "step" frame
  // narrates what the agent is doing (never its SQL/tool arguments, the
  // server never sends those); after, step frames are ignored since real
  // content already speaks for itself.
  let streaming = false;
  let streamedText = "";

  while (true) {
    const { done, value } = await reader.read();
    if (done) break;
    buffer += decoder.decode(value, { stream: true });
    const lines = buffer.split("\n\n");
    buffer = lines.pop();
    for (const line of lines) {
      if (!line.startsWith("data: ")) continue;
      const payload = line.slice(6);
      if (payload === "[DONE]") continue;
      const data = JSON.parse(payload);
      gotAnything = true;
      if (data.step) {
        if (!streaming) {
          bot.textContent = `${data.step}…`;
          bot.classList.add("en");
        }
      } else if (data.answer_chunk) {
        if (!streaming) {
          streaming = true;
          bot.textContent = "";
        }
        streamedText += data.answer_chunk;
        bot.textContent = streamedText;
        bot.classList.toggle("en", !ARABIC_RE.test(streamedText));
        messages.scrollTop = messages.scrollHeight;
      } else if (data.answer) {
        // Authoritative full text -- client already has it assembled from
        // answer_chunk events above, this is a snap-to-correct safety net.
        bot.textContent = data.answer;
        bot.classList.toggle("en", !ARABIC_RE.test(data.answer));
        addFeedbackRow(bot);
        // C8: table/chart/sources/followups -- the structured envelope,
        // rendered after the prose so the answer itself is never delayed
        // waiting on them.
        if (data.table) addResultTable(bot, data.table);
        if (data.chart) addResultChart(bot, data.chart, data.table);
        if (data.sources && data.sources.length) addSources(bot, data.sources);
        if (data.followups && data.followups.length) addFollowups(bot, data.followups);
      } else if (data.needs_ask) {
        bot.textContent = data.needs_ask;
        bot.classList.toggle("en", !ARABIC_RE.test(data.needs_ask));
      } else if (data.error) {
        bot.textContent = data.error;
        bot.className = "msg error";
      }
    }
  }
  if (!gotAnything) {
    bot.textContent = "لم يرد الخادم بإجابة";
    bot.className = "msg error";
  }
}

// C3: thumbs-up promotes this turn's query to verified_queries (a real
// few-shot exemplar); thumbs-down clears its cached plan so the same wrong
// answer isn't served again next time. Never sends the question/SQL back --
// the server already remembered this turn server-side against session_id,
// so a client can't spoof feedback for a turn that didn't happen.
function addFeedbackRow(bot) {
  const row = document.createElement("div");
  row.className = "feedback-row";
  row.innerHTML = `<button class="fb-btn" data-helpful="1" title="إجابة صحيحة">👍</button>
                    <button class="fb-btn" data-helpful="0" title="إجابة غير صحيحة">👎</button>`;
  bot.appendChild(row);
  row.querySelectorAll(".fb-btn").forEach(btn => btn.addEventListener("click", async () => {
    row.querySelectorAll(".fb-btn").forEach(b => b.disabled = true);
    const helpful = btn.dataset.helpful === "1";
    try {
      await fetch("/feedback", {
        method: "POST",
        headers: { "Content-Type": "application/json", "Authorization": `Bearer ${getToken()}` },
        body: JSON.stringify({ session_id: sessionId(), helpful }),
      });
      row.textContent = helpful ? "✓ شكراً" : "✓ تم التسجيل";
    } catch (e) {
      row.textContent = "";  // feedback is best-effort -- a failed POST here must never disrupt the chat
    }
  }));
}

// C8: table -- inherits the page's dir="rtl" like everything else here (no
// override), so columns read right-to-left the same natural direction as
// the surrounding Arabic UI. Built with DOM methods (never innerHTML) since
// cell values come from real row data, not a fixed string.
function _csvCell(v) {
  const s = (v ?? "").toString();
  return /[",\n]/.test(s) ? `"${s.replace(/"/g, '""')}"` : s;
}

function downloadTableCsv(table) {
  const lines = [table.columns.map(_csvCell).join(",")];
  table.rows.forEach(r => lines.push(r.map(_csvCell).join(",")));
  const blob = new Blob([lines.join("\n")], { type: "text/csv" });
  const a = document.createElement("a");
  a.href = URL.createObjectURL(blob);
  a.download = "results.csv";
  a.click();
  URL.revokeObjectURL(a.href);
}

function addResultTable(bot, table) {
  const wrap = document.createElement("div");
  wrap.className = "table-wrap";

  const tbl = document.createElement("table");
  tbl.className = "result-table";
  const headRow = document.createElement("tr");
  table.columns.forEach(c => {
    const th = document.createElement("th");
    th.textContent = c;
    headRow.appendChild(th);
  });
  tbl.appendChild(headRow);
  table.rows.forEach(r => {
    const tr = document.createElement("tr");
    r.forEach(v => {
      const td = document.createElement("td");
      td.textContent = v === null || v === undefined ? "" : String(v);
      tr.appendChild(td);
    });
    tbl.appendChild(tr);
  });
  wrap.appendChild(tbl);

  const csvBtn = document.createElement("button");
  csvBtn.type = "button";
  csvBtn.className = "ghost csv-btn";
  csvBtn.textContent = "⭳ CSV";
  csvBtn.addEventListener("click", () => downloadTableCsv(table));
  wrap.appendChild(csvBtn);

  bot.appendChild(wrap);
}

// C8: two small canvas renderers, no chart library/CDN (clients are
// firewalled and on-prem) -- ~40 lines total for both, per the plan.
function _renderBarChart(ctx, W, H, pad, labels, values, maxVal) {
  const barW = (W - pad * 2) / values.length;
  values.forEach((v, i) => {
    const barH = (v / maxVal) * (H - pad * 2);
    const x = pad + i * barW + barW * 0.15;
    const w = barW * 0.7;
    ctx.fillStyle = "#2563eb";
    ctx.fillRect(x, H - pad - barH, w, barH);
    ctx.fillStyle = "#333";
    ctx.fillText(String(labels[i]).slice(0, 10), x + w / 2, H - pad + 14);
    ctx.fillText(String(v), x + w / 2, H - pad - barH - 4);
  });
}

function _renderLineChart(ctx, W, H, pad, labels, values, maxVal) {
  const stepX = (W - pad * 2) / Math.max(values.length - 1, 1);
  ctx.strokeStyle = "#2563eb";
  ctx.beginPath();
  values.forEach((v, i) => {
    const x = pad + i * stepX, y = H - pad - (v / maxVal) * (H - pad * 2);
    i === 0 ? ctx.moveTo(x, y) : ctx.lineTo(x, y);
  });
  ctx.stroke();
  ctx.fillStyle = "#333";
  labels.forEach((l, i) => ctx.fillText(String(l).slice(0, 10), pad + i * stepX, H - pad + 14));
}

function addResultChart(bot, chart, table) {
  if (!table || !table.rows.length) return;
  const canvas = document.createElement("canvas");
  canvas.className = "result-chart";
  canvas.width = 320;
  canvas.height = 160;
  bot.appendChild(canvas);

  const labels = table.rows.map(r => r[0]);
  const values = table.rows.map(r => Number(r[1]) || 0);
  const maxVal = Math.max(...values, 1);
  const ctx = canvas.getContext("2d");
  const pad = 28;
  ctx.font = "10px sans-serif";
  ctx.textAlign = "center";
  ctx.strokeStyle = "#8886";
  ctx.beginPath();
  ctx.moveTo(pad, canvas.height - pad);
  ctx.lineTo(canvas.width - pad, canvas.height - pad);
  ctx.stroke();

  if (chart.kind === "line") _renderLineChart(ctx, canvas.width, canvas.height, pad, labels, values, maxVal);
  else _renderBarChart(ctx, canvas.width, canvas.height, pad, labels, values, maxVal);
}

function addSources(bot, sources) {
  const div = document.createElement("div");
  div.className = "sources-row";
  div.textContent = `المصادر: ${sources.join("، ")}`;
  bot.appendChild(div);
}

// C8: "what turns a query box into an analyst" -- clicking a chip re-asks
// exactly like the user typed and submitted it themselves, reusing the
// existing form-submit flow rather than duplicating it.
function addFollowups(bot, followups) {
  const row = document.createElement("div");
  row.className = "followup-row";
  followups.forEach(q => {
    const chip = document.createElement("button");
    chip.type = "button";
    chip.className = "followup-chip";
    chip.textContent = q;
    chip.addEventListener("click", () => {
      questionInput.value = q;
      form.requestSubmit();
    });
    row.appendChild(chip);
  });
  bot.appendChild(row);
}

form.addEventListener("submit", (e) => {
  e.preventDefault();
  const question = questionInput.value.trim();
  if (!question || !getToken()) return;
  addMessage(question, "user");
  questionInput.value = "";
  ask(question);
});
