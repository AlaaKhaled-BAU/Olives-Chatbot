const messages = document.getElementById("messages");
const form = document.getElementById("ask-form");
const questionInput = document.getElementById("question");
const companyLabel = document.getElementById("company-label");
const companySelect = document.getElementById("company-select");
const clientLabel = document.getElementById("client-label");
const asOfLabel = document.getElementById("as-of-label");

const ARABIC_RE = /[؀-ۿ]/;
const SESSION_KEY = "olives_session_id";

let contextAsOf = { calendar_today: null, max_invoice_date: null };

function sessionId() {
  let id = sessionStorage.getItem(SESSION_KEY);
  if (!id) {
    id = crypto.randomUUID();
    sessionStorage.setItem(SESSION_KEY, id);
  }
  return id;
}

function apiHeaders() {
  return {
    "Content-Type": "application/json",
    "X-Session-Id": sessionId(),
  };
}

function formatAsOfLine(calendarToday, maxInvoiceDate) {
  if (!calendarToday && !maxInvoiceDate) return "";
  const parts = [];
  if (calendarToday) parts.push(`اليوم: ${calendarToday}`);
  if (maxInvoiceDate) parts.push(`آخر فاتورة: ${maxInvoiceDate}`);
  return parts.join(" · ");
}

function updateAsOfLabel(calendarToday, maxInvoiceDate) {
  const line = formatAsOfLine(calendarToday, maxInvoiceDate);
  if (!line) {
    asOfLabel.classList.add("hidden");
    asOfLabel.textContent = "";
    return;
  }
  asOfLabel.textContent = line;
  asOfLabel.classList.remove("hidden");
}

function extractAsOfFromDone(data) {
  if (data.as_of && typeof data.as_of === "object") {
    return {
      calendar_today: data.as_of.calendar_today || data.as_of.calendarToday || null,
      max_invoice_date: data.as_of.max_invoice_date || data.as_of.maxInvoiceDate || null,
    };
  }
  return {
    calendar_today: data.calendar_today || null,
    max_invoice_date: data.max_invoice_date || null,
  };
}

async function loadContext() {
  try {
    const resp = await fetch(`/context?session_id=${encodeURIComponent(sessionId())}`);
    if (!resp.ok) return;
    const ctx = await resp.json();
    if (ctx.company) {
      companyLabel.textContent = `CompanyID: ${ctx.company.ID} — ${ctx.company.Name}`;
    } else if (ctx.company_id) {
      companyLabel.textContent = `CompanyID: ${ctx.company_id}`;
    }
    if (ctx.clients_active && ctx.clients_active.length) {
      const ca = ctx.clients_active[0];
      // Hide internal IDs that are empty/zero — meaningless to end users.
      const cid = Number(ca && ca.ClientID);
      clientLabel.textContent = cid > 0 ? `ClientID: ${cid}` : "";
    }
    contextAsOf = {
      calendar_today: ctx.calendar_today || null,
      max_invoice_date: ctx.max_invoice_date || null,
    };
    updateAsOfLabel(contextAsOf.calendar_today, contextAsOf.max_invoice_date);
    if (ctx.multi_company && ctx.companies.length > 1) {
      companySelect.classList.remove("hidden");
      companySelect.innerHTML = "";
      ctx.companies.forEach((c) => {
        const opt = document.createElement("option");
        opt.value = c.id;
        opt.textContent = `${c.name} (${c.id})`;
        if (c.id === ctx.company_id) opt.selected = true;
        companySelect.appendChild(opt);
      });
    }
  } catch (e) {
    companyLabel.textContent = "";
  }
}

companySelect.addEventListener("change", async () => {
  await fetch("/context", {
    method: "POST",
    headers: apiHeaders(),
    body: JSON.stringify({ session_id: sessionId(), company_id: Number(companySelect.value) }),
  });
  await // Auto theme: dark default, follows OS light preference (D1=A)
(function () {
  const root = document.documentElement;
  const mq = window.matchMedia("(prefers-color-scheme: light)");
  const apply = () => { root.setAttribute("data-theme", mq.matches ? "light" : "dark"); };
  apply();
  mq.addEventListener ? mq.addEventListener("change", apply) : mq.addListener(apply);
})();

// Empty-state starter questions
document.querySelectorAll("#empty-state .chip-btn").forEach((b) => {
  b.addEventListener("click", () => {
    const q = document.getElementById("question");
    q.value = b.dataset.q;
    document.getElementById("ask-form").requestSubmit();
  });
});

loadContext();
});

function addMessage(text, role) {
  const empty = document.getElementById("empty-state");
  if (empty && !empty.classList.contains("hidden")) empty.classList.add("hidden");
  const div = document.createElement("div");
  div.className = `msg ${role}`;
  if (!ARABIC_RE.test(text)) div.classList.add("en");
  if (role === "bot") {
    div.innerHTML = renderRich(text);
    div.style.unicodeBidi = "plaintext";
  } else {
    div.textContent = text;
    div.style.unicodeBidi = "plaintext";
  }
  messages.appendChild(div);
  messages.scrollTop = messages.scrollHeight;
  return div;
}

/* markdown-lite: escape-first, then transform — fences, inline code, bold,
   pipe-tables, lists. Kills raw ```sql leaks (qa ISSUE-002) safely. */
function escHtml(s) {
  return s.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
}

function renderRich(text) {
  const out = [];
  const lines = escHtml(text || "").split("\n");
  let i = 0, para = [];
  const flush = () => {
    if (para.length) { out.push(`<p>${para.join("<br>")}</p>`); para = []; }
  };
  while (i < lines.length) {
    const line = lines[i];
    const fence = line.match(/^```(\w*)\s*$/);
    if (fence) {
      flush();
      const body = [];
      i++;
      while (i < lines.length && !/^```\s*$/.test(lines[i])) { body.push(lines[i]); i++; }
      i++; // closing fence
      out.push(
        `<div class="md-codeblock"><span class="cb-lang">${fence[1] || "code"}</span>` +
        `<pre><code>${body.join("\n")}</code></pre></div>`);
      continue;
    }
    if (/^\s*\|.*\|\s*$/.test(line)) {
      flush();
      const rows = [];
      while (i < lines.length && /^\s*\|.*\|\s*$/.test(lines[i])) { rows.push(lines[i]); i++; }
      const cells = (l) => l.trim().replace(/^\||\|$/g, "").split("|").map((c) => c.trim());
      if (rows.length >= 2 && /^[\s|:-]+$/.test(rows[1])) {
        const head = cells(rows[0]);
        let html = '<div class="md-table-wrap"><table><thead><tr>' +
          head.map((h) => `<th>${/[\d٪%]/.test(h) ? ` class="num">${h}` : `>${h}`}`).join("") +
          "</tr></thead><tbody>";
        for (const r of rows.slice(2)) {
          const cs = cells(r);
          html += "<tr>" + cs.map((c, ci) => {
            const num = /^[\s\d.,٪%\-+]+$/.test(c);
            return `<td${num ? ' class="num"' : ""}>${c}</td>`;
          }).join("") + "</tr>";
        }
        html += "</tbody></table></div>";
        out.push(html);
      } else {
        para.push(...rows);
      }
      continue;
    }
    if (/^\s*[-•]\s+/.test(line) || /^\s*\d+[.)]\s+/.test(line)) {
      flush();
      const items = [];
      while (i < lines.length && (/^\s*[-•]\s+/.test(lines[i]) || /^\s*\d+[.)]\s+/.test(lines[i]))) {
        items.push(lines[i].replace(/^\s*([-•]|\d+[.)])\s+/, ""));
        i++;
      }
      out.push(`<ul>${items.map((it) => `<li>${it}</li>`).join("")}</ul>`);
      continue;
    }
    if (line.trim() === "") { flush(); }
    else { para.push(line); }
    i++;
  }
  flush();
  return out.join("")
    .replace(/\*\*([^*]+)\*\*/g, "<strong>$1</strong>")
    .replace(/`([^`\n]+)`/g, "<code>$1</code>");
}

function showTyping() {
  const t = document.createElement("div");
  t.className = "typing";
  t.id = "typing-indicator";
  t.innerHTML = "<i></i><i></i><i></i>";
  messages.appendChild(t);
  messages.scrollTop = messages.scrollHeight;
  return t;
}

async function ask(question) {
  const bot = addMessage("", "bot");
  bot.innerHTML = '<div class="typing"><i></i><i></i><i></i></div>';
  let resp;
  try {
    resp = await fetch("/ask", {
      method: "POST",
      headers: apiHeaders(),
      body: JSON.stringify({ question, session_id: sessionId() }),
    });
  } catch (e) {
    bot.innerHTML = "";
    bot.textContent = "تعذر الاتصال بالخادم";
    bot.className = "msg error";
    return;
  }

  if (!resp.ok) {
    bot.innerHTML = "";
    bot.textContent = `خطأ (${resp.status})`;
    bot.className = "msg error";
    return;
  }

  const reader = resp.body.getReader();
  const decoder = new TextDecoder();
  let buffer = "";
  let gotAnything = false;
  let streaming = false;
  let streamedText = "";
  let lastAnswerSql = null;

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
          bot.innerHTML = "";
          bot.textContent = `${data.step}…`;
          bot.classList.add("en");
        }
      } else if (data.answer_chunk) {
        if (!streaming) {
          streaming = true;
          bot.innerHTML = "";
          bot.textContent = "";
        }
        streamedText += data.answer_chunk;
        bot.textContent = streamedText;
        bot.classList.toggle("en", !ARABIC_RE.test(streamedText));
        messages.scrollTop = messages.scrollHeight;
      } else if (data.answer && String(data.answer).trim()) {
        bot.innerHTML = "";
        bot.innerHTML = renderRich(String(data.answer));
        bot.classList.toggle("en", !ARABIC_RE.test(data.answer));
        if (data.answer_sql) lastAnswerSql = data.answer_sql;
        const asOf = extractAsOfFromDone(data);
        if (asOf.calendar_today || asOf.max_invoice_date) {
          contextAsOf = asOf;
          updateAsOfLabel(asOf.calendar_today, asOf.max_invoice_date);
        }
        addFeedbackRow(bot);
        if (data.table) addResultTable(bot, data.table);
        if (data.chart) addResultChart(bot, data.chart, data.table);
        if (data.sources && data.sources.length) addSources(bot, data.sources);
        if (data.followups && data.followups.length) addFollowups(bot, data.followups);
        if (lastAnswerSql) addSqlPanel(bot, lastAnswerSql, data.table);
        if (data.report_name) addReportPanel(bot, data.report_name);
        const asOfLine = formatAsOfLine(
          asOf.calendar_today || contextAsOf.calendar_today,
          asOf.max_invoice_date || contextAsOf.max_invoice_date,
        );
        if (asOfLine) addAsOfPanel(bot, asOfLine);
      } else if (data.answer_sql && !data.answer) {
        lastAnswerSql = data.answer_sql;
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

function addSqlPanel(bot, sqlText, table) {
  const details = document.createElement("details");
  details.className = "sql-panel";
  const summary = document.createElement("summary");
  summary.textContent = "الاستعلام";
  details.appendChild(summary);
  if (table && table.rows && table.rows.length) {
    const hint = document.createElement("div");
    hint.className = "sql-hint";
    hint.textContent = `${table.rows.length} صف`;
    details.appendChild(hint);
  }
  const pre = document.createElement("pre");
  pre.className = "sql-text en";
  pre.textContent = sqlText;
  details.appendChild(pre);
  const copyBtn = document.createElement("button");
  copyBtn.type = "button";
  copyBtn.className = "ghost csv-btn";
  copyBtn.textContent = "نسخ";
  copyBtn.addEventListener("click", () => navigator.clipboard.writeText(sqlText));
  details.appendChild(copyBtn);
  bot.appendChild(details);
}

function addAsOfPanel(bot, asOfLine) {
  const div = document.createElement("div");
  div.className = "as-of-panel";
  div.textContent = asOfLine;
  bot.appendChild(div);
}

function addReportPanel(bot, reportName) {
  const div = document.createElement("div");
  div.className = "report-panel en";
  div.textContent = `Report: ${reportName}`;
  bot.appendChild(div);
}

function addFeedbackRow(bot) {
  const row = document.createElement("div");
  row.className = "feedback-row";
  row.innerHTML = `<button class="fb-btn" data-helpful="1" title="إجابة صحيحة">👍</button>
                    <button class="fb-btn" data-helpful="0" title="إجابة غير صحيحة">👎</button>`;
  bot.appendChild(row);
  row.querySelectorAll(".fb-btn").forEach((btn) => btn.addEventListener("click", async () => {
    row.querySelectorAll(".fb-btn").forEach((b) => b.disabled = true);
    const helpful = btn.dataset.helpful === "1";
    try {
      await fetch("/feedback", {
        method: "POST",
        headers: apiHeaders(),
        body: JSON.stringify({ session_id: sessionId(), helpful }),
      });
      row.textContent = helpful ? "✓ شكراً" : "✓ تم التسجيل";
    } catch (e) {
      row.textContent = "";
    }
  }));
}

function _csvCell(v) {
  const s = (v ?? "").toString();
  return /[",\n]/.test(s) ? `"${s.replace(/"/g, '""')}"` : s;
}

function downloadTableCsv(table) {
  const lines = [table.columns.map(_csvCell).join(",")];
  table.rows.forEach((r) => lines.push(r.map(_csvCell).join(",")));
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
  table.columns.forEach((c) => {
    const th = document.createElement("th");
    th.textContent = c;
    headRow.appendChild(th);
  });
  tbl.appendChild(headRow);
  table.rows.forEach((r) => {
    const tr = document.createElement("tr");
    r.forEach((v) => {
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
    const x = pad + i * stepX;
    const y = H - pad - (v / maxVal) * (H - pad * 2);
    if (i === 0) ctx.moveTo(x, y);
    else ctx.lineTo(x, y);
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
  const labels = table.rows.map((r) => r[0]);
  const values = table.rows.map((r) => Number(r[1]) || 0);
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
  div.style.unicodeBidi = "plaintext";
  div.textContent = `المصادر: ${sources.join("، ")}`;
  bot.appendChild(div);
}

function addFollowups(bot, followups) {
  const row = document.createElement("div");
  row.className = "followup-row";
  followups.forEach((q) => {
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
  if (!question) return;
  addMessage(question, "user");
  questionInput.value = "";
  ask(question);
});

// Auto theme: dark default, follows OS light preference (D1=A)
(function () {
  const root = document.documentElement;
  const mq = window.matchMedia("(prefers-color-scheme: light)");
  const apply = () => { root.setAttribute("data-theme", mq.matches ? "light" : "dark"); };
  apply();
  mq.addEventListener ? mq.addEventListener("change", apply) : mq.addListener(apply);
})();

// Empty-state starter questions
document.querySelectorAll("#empty-state .chip-btn").forEach((b) => {
  b.addEventListener("click", () => {
    const q = document.getElementById("question");
    q.value = b.dataset.q;
    document.getElementById("ask-form").requestSubmit();
  });
});

loadContext();


/* ===== مصدر البيانات — operator connection console ===== */
(function () {
  const el = (id) => document.getElementById(id);
  const card = el("db-console"), head = el("db-toggle"), body = el("db-body");
  const orb = el("db-orb"), badge = el("db-badge"), chev = el("db-chev");
  const serverIn = el("db-server"), portIn = el("db-port"), userIn = el("db-user");
  const passIn = el("db-pass"), eyeBtn = el("db-eye"), chipLocal = el("db-local-chip");
  const nameSel = el("db-name-select"), nameIn = el("db-name"), trustedChk = el("db-trusted");
  const testBtn = el("db-test"), saveBtn = el("db-save"), resetBtn = el("db-reset");
  const msgEl = el("db-msg");
  let lastProbe = null;

  function setMsg(text, kind) {
    msgEl.textContent = text || "";
    msgEl.className = kind ? `db-msg ${kind}` : "db-msg hidden";
    if (!kind) msgEl.classList.add("hidden");
  }

  async function jpost(url, payload) {
    const r = await fetch(url, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload),
    });
    return r.json();
  }

  function paintStatus(status) {
    const live = status.source === "live";
    orb.className = "orb " + (live ? "green" : "amber");
    badge.textContent = live ? "متصل مباشرة" : "نسخة محلية";
    badge.className = "badge " + (live ? "badge-live" : "badge-snapshot");
    resetBtn.classList.toggle("hidden", !live);
    if (live && status.active) {
      serverIn.value = status.active.host || "";
      portIn.value = status.active.port ?? 1433;
      userIn.value = status.active.user || "";
      passIn.value = "";
      passIn.placeholder = "•••••• (محفوظة)";
      nameIn.value = status.active.database || "";
    }
    setMsg(live
      ? `مصدر حي: ${status.active.host}:${status.active.port}/${status.active.database}`
      : "", "");
  }

  async function refreshStatus() {
    try { paintStatus(await (await fetch("/db/status")).json()); }
    catch { /* console is best-effort */ }
  }

  head.addEventListener("click", () => {
    // .open owns visibility (CSS); hidden class kept for aria/compat only.
    const open = card.classList.toggle("open");
    body.classList.toggle("hidden", !open);
    head.setAttribute("aria-expanded", String(open));
  });

  chipLocal.addEventListener("click", () => {
    serverIn.value = "(.)";
    portIn.value = 1433;
    userIn.focus();
  });

  eyeBtn.addEventListener("click", () => {
    passIn.type = passIn.type === "password" ? "text" : "password";
  });

  trustedChk.addEventListener("change", () => {
    const off = trustedChk.checked;
    userIn.disabled = off; passIn.disabled = off;
    saveBtn.disabled = true;
  });

  testBtn.addEventListener("click", async () => {
    setMsg("جارٍ الفحص…", "");
    const payload = {
      server: serverIn.value, port: portIn.value ? Number(portIn.value) : null,
      user: userIn.value, password: passIn.value,
      database: nameSel.classList.contains("hidden")
        ? (nameIn.value || null) : nameSel.value,
      trusted: trustedChk.checked,
    };
    try {
      lastProbe = await jpost("/db/test", payload);
    } catch { setMsg("تعذر الوصول للخدمة", "error"); return; }
    if (!lastProbe.ok) { setMsg(lastProbe.error || "فشل الاتصال", "error"); return; }
    const dbs = lastProbe.databases || [];
    if (dbs.length) {
      nameSel.innerHTML = "";
      for (const d of dbs) {
        const o = document.createElement("option");
        o.value = o.textContent = d;
        nameSel.appendChild(o);
      }
      const want = nameIn.value.trim();
      if (want && dbs.includes(want)) nameSel.value = want;
      else if (dbs.length === 1) nameSel.value = dbs[0];
      nameSel.classList.remove("hidden");
      nameIn.classList.add("hidden");
    } else {
      nameSel.classList.add("hidden"); nameIn.classList.remove("hidden");
    }
    saveBtn.disabled = false;
    setMsg(`✓ ${lastProbe.server_name} — ${lastProbe.version_line}\nقواعد متاحة: ${dbs.length}`, "ok");
  });

  saveBtn.addEventListener("click", async () => {
    const database = nameSel.classList.contains("hidden")
      ? (nameIn.value.trim() || null) : nameSel.value;
    const payload = {
      server: serverIn.value, port: portIn.value ? Number(portIn.value) : null,
      user: userIn.value, password: passIn.value,
      database, trusted: trustedChk.checked,
    };
    saveBtn.disabled = true; saveBtn.textContent = "جارٍ التثبيت…";
    try {
      const res = await jpost("/db/connect", payload);
      if (!res.ok) {
        setMsg(res.error || "فشل التثبيت", "error");
      } else {
        paintStatus({ source: "live", active: res.active });
        const n = (lastProbe && Array.isArray(lastProbe.databases)) ? lastProbe.databases.length : null;
        setMsg(`✓ تم تثبيت المصدر الحي: ${res.probe.server_name}${n !== null ? ` (${n} قاعدة)` : ""}`, "ok");
        try { await // Auto theme: dark default, follows OS light preference (D1=A)
(function () {
  const root = document.documentElement;
  const mq = window.matchMedia("(prefers-color-scheme: light)");
  const apply = () => { root.setAttribute("data-theme", mq.matches ? "light" : "dark"); };
  apply();
  mq.addEventListener ? mq.addEventListener("change", apply) : mq.addListener(apply);
})();

// Empty-state starter questions
document.querySelectorAll("#empty-state .chip-btn").forEach((b) => {
  b.addEventListener("click", () => {
    const q = document.getElementById("question");
    q.value = b.dataset.q;
    document.getElementById("ask-form").requestSubmit();
  });
});

loadContext(); } catch {}
      }
    } catch { setMsg("تعذر الوصول للخدمة", "error"); }
    saveBtn.textContent = "اتصال وتثبيت";
  });

  resetBtn.addEventListener("click", async () => {
    await fetch("/db/reset", { method: "POST" });
    refreshStatus();
    try { await // Auto theme: dark default, follows OS light preference (D1=A)
(function () {
  const root = document.documentElement;
  const mq = window.matchMedia("(prefers-color-scheme: light)");
  const apply = () => { root.setAttribute("data-theme", mq.matches ? "light" : "dark"); };
  apply();
  mq.addEventListener ? mq.addEventListener("change", apply) : mq.addListener(apply);
})();

// Empty-state starter questions
document.querySelectorAll("#empty-state .chip-btn").forEach((b) => {
  b.addEventListener("click", () => {
    const q = document.getElementById("question");
    q.value = b.dataset.q;
    document.getElementById("ask-form").requestSubmit();
  });
});

loadContext(); } catch {}
  });

  refreshStatus();
})();
