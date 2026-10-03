const messages = document.getElementById("messages");
const form = document.getElementById("ask-form");
const questionInput = document.getElementById("question");
const companyLabel = document.getElementById("company-label");
const companySelect = document.getElementById("company-select");
const clientLabel = document.getElementById("client-label");
const asOfLabel = document.getElementById("as-of-label");
const sessionList = document.getElementById("session-list");
const newChatBtn = document.getElementById("new-chat-btn");
const sidebar = document.getElementById("sidebar");
const sidebarToggleBtn = document.getElementById("sidebar-toggle-btn");
const sidebarCloseBtn = document.getElementById("sidebar-close-btn");
const sidebarBackdrop = document.getElementById("sidebar-backdrop");

const ARABIC_RE = /[؀-ۿ]/;
const SESSION_KEY = "olives_session_id";

let contextAsOf = { calendar_today: null, max_invoice_date: null };

function scrollToBottom() {
  const scrollArea = document.querySelector(".chat-scroll-area");
  if (scrollArea) {
    scrollArea.scrollTop = scrollArea.scrollHeight;
  } else if (messages) {
    messages.scrollTop = messages.scrollHeight;
  }
}

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
    const dbBtn = document.getElementById("db-open-btn");
    if (dbBtn) dbBtn.classList.remove("hidden");
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
    const companies = ctx.companies || [];
    const multi = !!(ctx.multi_company || ctx.multi_company || companies.length > 1);
    if (companies.length) {
      companySelect.innerHTML = "";
      companies.forEach((c) => {
        const opt = document.createElement("option");
        opt.value = c.id;
        opt.textContent = `${c.name} (${c.id})`;
        if (Number(c.id) === Number(ctx.company_id)) opt.selected = true;
        companySelect.appendChild(opt);
      });
      companySelect.classList.toggle("hidden", !multi);
      if (companySelect.value) {
        await fetch("/context", {
          method: "POST",
          headers: apiHeaders(),
          body: JSON.stringify({
            session_id: sessionId(),
            company_id: Number(companySelect.value),
          }),
        });
      }
    }
    const msgs = document.getElementById("messages");
    if (!msgs.querySelector(".msg")) {
      replayTranscript(ctx.transcript || []);
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
  document.getElementById("messages").innerHTML = "";
  await loadContext();
});

function replayTranscript(transcript) {
  const empty = document.getElementById("empty-state");
  if (!transcript || !transcript.length) {
    if (empty) empty.classList.remove("hidden");
    return;
  }
  if (empty && !empty.classList.contains("hidden")) empty.classList.add("hidden");
  for (const row of transcript) {
    addMessage(row.q, "user");
    const bot = addMessage(row.a, "bot");
    if (row.sql) addSqlPanel(bot, row.sql, null);
    addFeedbackRow(bot, row.id);
  }
  scrollToBottom();
}

function addMessage(text, role) {
  const empty = document.getElementById("empty-state");
  if (empty && !empty.classList.contains("hidden")) empty.classList.add("hidden");
  const div = document.createElement("div");
  div.className = `msg ${role}`;
  if (!ARABIC_RE.test(text)) div.classList.add("en");
  if (role === "bot") div.innerHTML = renderRich(text);
  else div.textContent = text;
  div.style.unicodeBidi = "plaintext";
  messages.appendChild(div);
  scrollToBottom();
  return div;
}

/* markdown-lite: escape-first, then transform — fences, inline code, bold,
   pipe-tables, lists (kills raw sql-fence leaks, qa ISSUE-002). */
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
      i++;
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
          head.map((h) => `<th>${h}</th>`).join("") +
          "</tr></thead><tbody>";
        for (const r of rows.slice(2)) {
          const cs = cells(r);
          html += "<tr>" + cs.map((c) => {
            const num = /^[\s\d.,%\-+]+$/.test(c);
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
    if (/^\s*[-\u2022]\s+/.test(line) || /^\s*\d+[.)]\s+/.test(line)) {
      flush();
      const items = [];
      while (i < lines.length && (/^\s*[-\u2022]\s+/.test(lines[i]) || /^\s*\d+[.)]\s+/.test(lines[i]))) {
        items.push(lines[i].replace(/^\s*([-\u2022]|\d+[.)])\s+/, ""));
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

async function ask(question) {
  if (!companySelect.value) {
    await loadContext();
  }
  const bot = addMessage("...", "bot");
  let resp;
  try {
    const companyId = companySelect.value ? Number(companySelect.value) : undefined;
    resp = await fetch("/ask", {
      method: "POST",
      headers: apiHeaders(),
      body: JSON.stringify({
        question,
        session_id: sessionId(),
        company_id: companyId,
      }),
    });
  } catch (e) {
    bot.textContent = "تعذر الاتصال بالخادم";
    bot.className = "msg error";
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
        bot.textContent = `${data.step}…`;
        bot.classList.add("en");
      } else if (data.answer_chunk) {
        streamedText += data.answer_chunk;
      } else if (data.needs_ask) {
        bot.textContent = data.needs_ask;
        bot.classList.toggle("en", !ARABIC_RE.test(data.needs_ask));
      } else if (data.error) {
        bot.textContent = data.error;
        bot.className = "msg error";
      } else if ("answer" in data) {
        const holdStream = data.hold_stream === true;
        let displayText = "";
        if (holdStream) {
          displayText = data.answer != null ? String(data.answer) : "";
        } else {
          const trimmedAnswer = data.answer != null ? String(data.answer).trim() : "";
          displayText = trimmedAnswer ? data.answer : streamedText;
        }
        if (displayText) {
          bot.textContent = displayText;
          bot.classList.toggle("en", !ARABIC_RE.test(displayText));
        }
        if (data.answer_sql) lastAnswerSql = data.answer_sql;
        const asOf = extractAsOfFromDone(data);
        if (asOf.calendar_today || asOf.max_invoice_date) {
          contextAsOf = asOf;
          updateAsOfLabel(asOf.calendar_today, asOf.max_invoice_date);
        }
        addFeedbackRow(bot, data.turn_id);
        if (data.table) addResultTable(bot, data.table);
        if (data.chart) addResultChart(bot, data.chart, data.table);
        if (data.sources && data.sources.length) addSources(bot, data.sources);
        if (data.followups && data.followups.length) addFollowups(bot, data.followups);
        if (lastAnswerSql) addSqlPanel(bot, lastAnswerSql, data.table);
        if (data.prompt_tokens != null) addUsagePanel(bot, data);
        if (data.report_name) addReportPanel(bot, data.report_name);
        const asOfLine = formatAsOfLine(
          asOf.calendar_today || contextAsOf.calendar_today,
          asOf.max_invoice_date || contextAsOf.max_invoice_date,
        );
        if (asOfLine) addAsOfPanel(bot, asOfLine);
        loadSessionsList();
        scrollToBottom();
      } else if (data.answer_sql && !data.answer) {
        lastAnswerSql = data.answer_sql;
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

// DeepSeek pricing per 1M tokens — deepseek-flash (DeepSeek-V4.1-Flash)
// Peak hours (UTC, Mon–Fri only): 01:00–04:00 and 06:00–10:00
// Weekends and Chinese public holidays are always off-peak.
// Source: https://api-docs.deepseek.com/quick_start/pricing
const DS_PRICE = {
  peak:    { cached: 0.006, input: 0.30,  output: 1.20 },
  offpeak: { cached: 0.003, input: 0.15,  output: 0.60 },
};

function _isPeakUtc(d) {
  const day = d.getUTCDay(); // 0=Sun, 6=Sat
  if (day === 0 || day === 6) return false; // weekends always off-peak
  const h = d.getUTCHours();
  return (h >= 1 && h < 4) || (h >= 6 && h < 10);
}

function addUsagePanel(bot, data) {
  const prompt   = data.prompt_tokens      || 0;
  const out      = data.completion_tokens  || 0;
  const cached   = data.cache_hit_tokens   || 0;
  const uncached = prompt - cached;
  const tier     = _isPeakUtc(new Date());
  const p        = tier ? DS_PRICE.peak : DS_PRICE.offpeak;
  const cost     = (uncached * p.input + cached * p.cached + out * p.output) / 1e6;
  const costStr  = cost < 0.0001 ? "< $0.0001" : `$${cost.toFixed(4)}`;
  const tierLbl  = tier ? "⚡ peak" : "🌙 off-peak";

  const details = document.createElement("details");
  details.className = "sql-panel usage-panel";
  const summary = document.createElement("summary");
  summary.textContent = "الاستهلاك";
  details.appendChild(summary);

  const hint = document.createElement("div");
  hint.className = "sql-hint";
  hint.textContent = `${prompt.toLocaleString()} in · ${out.toLocaleString()} out · ${costStr} · ${tierLbl}`;
  details.appendChild(hint);

  const grid = document.createElement("div");
  grid.className = "usage-grid en";
  grid.innerHTML = [
    `<span>Prompt tokens</span><span>${prompt.toLocaleString()}</span>`,
    `<span>&nbsp;&nbsp;— cached</span><span>${cached.toLocaleString()}</span>`,
    `<span>&nbsp;&nbsp;— uncached</span><span>${uncached.toLocaleString()}</span>`,
    `<span>Completion tokens</span><span>${out.toLocaleString()}</span>`,
    `<span>LLM calls</span><span>${data.llm_calls || 1}</span>`,
    `<span>Rate tier</span><span>${tierLbl}</span>`,
    `<span>Estimated cost</span><span>${costStr}</span>`,
  ].join("");
  details.appendChild(grid);
  bot.appendChild(details);
}

function addReportPanel(bot, reportName) {
  const div = document.createElement("div");
  div.className = "report-panel en";
  div.textContent = `Report: ${reportName}`;
  bot.appendChild(div);
}

function addFeedbackRow(bot, turnId) {
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
        body: JSON.stringify({ session_id: sessionId(), helpful, turn_id: turnId || undefined }),
      });
      row.textContent = helpful ? "✓ شكراً" : "✓ تم التسجيل";
    } catch (e) {
      row.textContent = "";
    }
  }));
}

function _csvCell(v) {
  let s = (v ?? "").toString();
  // Neutralize spreadsheet formula injection (=, +, -, @)
  if (/^[=\-+@]/.test(s)) {
    s = "'" + s;
  }
  return /[",\r\n]/.test(s) ? `"${s.replace(/"/g, '""')}"` : s;
}

function downloadTableCsv(table, btn) {
  const lines = [table.columns.map(_csvCell).join(",")];
  table.rows.forEach((r) => lines.push(r.map(_csvCell).join(",")));
  // Prepend UTF-8 BOM (\uFEFF) for Excel on Windows compatibility
  const bom = "\uFEFF";
  const csvContent = bom + lines.join("\r\n");
  const blob = new Blob([csvContent], { type: "text/csv;charset=utf-8;" });
  const a = document.createElement("a");
  const dateStr = new Date().toISOString().slice(0, 10);
  a.href = URL.createObjectURL(blob);
  a.download = `olives_report_${dateStr}.csv`;
  a.click();
  URL.revokeObjectURL(a.href);

  if (btn) {
    const prevText = btn.textContent;
    btn.textContent = "✓ تم التحميل";
    btn.classList.add("btn-downloaded");
    setTimeout(() => {
      btn.textContent = prevText;
      btn.classList.remove("btn-downloaded");
    }, 1800);
  }
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
  csvBtn.addEventListener("click", () => downloadTableCsv(table, csvBtn));
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

document.querySelectorAll(".chip-btn, .chip-btn").forEach((btn) => {
  btn.addEventListener("click", () => {
    const q = btn.dataset.q;
    if (!q) return;
    addMessage(q, "user");
    ask(q);
  });
});

loadContext();

/* ===== إدارة المحادثات والشريط الجانبي (ChatGPT-like Sessions) ===== */
function isMobile() {
  return window.innerWidth <= 768;
}

function toggleSidebar(open) {
  if (!sidebar) return;
  if (open === undefined) {
    sidebar.classList.toggle("collapsed");
  } else if (open) {
    sidebar.classList.remove("collapsed");
  } else {
    sidebar.classList.add("collapsed");
  }
  const isCollapsed = sidebar.classList.contains("collapsed");
  if (sidebarBackdrop) {
    if (isMobile() && !isCollapsed) {
      sidebarBackdrop.classList.remove("hidden");
    } else {
      sidebarBackdrop.classList.add("hidden");
    }
  }
}

if (sidebarToggleBtn) {
  sidebarToggleBtn.addEventListener("click", () => toggleSidebar());
}
if (sidebarCloseBtn) {
  sidebarCloseBtn.addEventListener("click", () => toggleSidebar(false));
}
if (sidebarBackdrop) {
  sidebarBackdrop.addEventListener("click", () => toggleSidebar(false));
}
if (isMobile() && sidebar) {
  sidebar.classList.add("collapsed");
}

async function loadSessionsList() {
  if (!sessionList) return;
  try {
    const resp = await fetch("/sessions");
    if (!resp.ok) return;
    const data = await resp.json();
    renderSessionsList(data.sessions || []);
  } catch (e) {
    console.error("Failed to load sessions:", e);
  }
}

function renderSessionsList(sessions) {
  if (!sessionList) return;
  sessionList.innerHTML = "";
  const curSid = sessionId();
  if (!sessions.length) {
    const emptyNotice = document.createElement("div");
    emptyNotice.className = "sidebar-section-title";
    emptyNotice.style.padding = "12px 8px";
    emptyNotice.textContent = "لا توجد محادثات سابقة";
    sessionList.appendChild(emptyNotice);
    return;
  }

  sessions.forEach((s) => {
    const item = document.createElement("div");
    item.className = "session-item";
    if (s.id === curSid) item.classList.add("active");

    const titleEl = document.createElement("span");
    titleEl.className = "session-item-title";
    titleEl.textContent = s.title || "محادثة سابقة";
    if (!ARABIC_RE.test(titleEl.textContent)) titleEl.classList.add("en");

    const delBtn = document.createElement("button");
    delBtn.type = "button";
    delBtn.className = "session-delete-btn";
    delBtn.title = "حذف المحادثة";
    delBtn.setAttribute("aria-label", "حذف");
    delBtn.innerHTML = "✕";
    delBtn.addEventListener("click", (e) => {
      e.stopPropagation();
      deleteSession(s.id);
    });

    item.appendChild(titleEl);
    item.appendChild(delBtn);

    item.addEventListener("click", () => {
      selectSession(s.id);
    });

    sessionList.appendChild(item);
  });
}

async function selectSession(sid) {
  if (sid === sessionId() && messages.children.length > 0) {
    if (isMobile()) toggleSidebar(false);
    return;
  }
  sessionStorage.setItem(SESSION_KEY, sid);
  messages.innerHTML = "";
  const empty = document.getElementById("empty-state");
  if (empty) empty.classList.add("hidden");

  document.querySelectorAll(".session-item").forEach((el) => el.classList.remove("active"));
  await loadContext();
  loadSessionsList();
  if (isMobile()) toggleSidebar(false);
  scrollToBottom();
}

async function newChat() {
  const newSid = crypto.randomUUID();
  sessionStorage.setItem(SESSION_KEY, newSid);
  messages.innerHTML = "";
  const empty = document.getElementById("empty-state");
  if (empty) empty.classList.remove("hidden");

  document.querySelectorAll(".session-item").forEach((el) => el.classList.remove("active"));
  questionInput.value = "";
  questionInput.focus();
  await loadContext();
  loadSessionsList();
  if (isMobile()) toggleSidebar(false);
}

async function deleteSession(sid) {
  try {
    await fetch(`/sessions/${encodeURIComponent(sid)}`, { method: "DELETE" });
  } catch (e) {
    console.error("Failed to delete session:", e);
  }
  if (sid === sessionId()) {
    await newChat();
  } else {
    await loadSessionsList();
  }
}

if (newChatBtn) {
  newChatBtn.addEventListener("click", () => newChat());
}

loadSessionsList();


/* ===== إعدادات الاتصال ===== */
(function () {
  const el = (id) => document.getElementById(id);
  const modal = el("db-modal"), openBtn = el("db-open-btn"), closeBtn = el("db-close");
  if (!modal || !openBtn || !closeBtn) return;
  const orb = el("db-orb"), badge = el("db-badge");
  const serverIn = el("db-server"), portIn = el("db-port"), userIn = el("db-user");
  const passIn = el("db-pass"), eyeBtn = el("db-eye");
  const localToggle = el("db-local-toggle");
  const bakPath = el("db-bak-path");
  const remoteFields = el("db-remote-fields");
  const remoteActions = el("db-remote-actions");
  const statusLine = el("db-status-line");
  const testBtn = el("db-test"), saveBtn = el("db-save");
  const msgEl = el("db-msg");
  let snapshotDb = "";
  let filling = false;

  function openModal() {
    modal.classList.remove("hidden");
    openBtn.setAttribute("aria-expanded", "true");
  }
  function closeModal() {
    modal.classList.add("hidden");
    openBtn.setAttribute("aria-expanded", "false");
  }

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
    const local = status.source !== "live";
    const connected = !!status.connected;
    const a = status.active || {};
    const d = status.defaults || {};
    snapshotDb = d.database || a.database || "";
    filling = true;
    localToggle.checked = local;
    remoteFields.classList.toggle("is-disabled", local);
    remoteActions.classList.toggle("hidden", local);
    [serverIn, portIn, userIn, passIn, testBtn, saveBtn].forEach((n) => {
      if (n) n.disabled = local;
    });
    serverIn.value = a.host || d.host || "";
    portIn.value = a.port ?? d.port ?? 1433;
    userIn.value = a.user || d.user || "";
    passIn.value = "";
    passIn.placeholder = a.has_password || local ? "••••••" : "";
    if (bakPath) {
      bakPath.textContent = d.bak_mount ? ` ${d.bak_mount}` : "";
    }
    filling = false;

    orb.className = "orb " + (connected ? "green" : "red");
    badge.textContent = connected
      ? (local ? "محلي · متصل" : "خادم · متصل")
      : (local ? "محلي · غير متصل" : "خادم · غير متصل");
    badge.className = "badge " + (connected ? "badge-live" : "badge-snapshot");
    const probe = status.probe || {};
    const where = `${a.host || "—"}:${a.port || "—"}`;
    if (statusLine) {
      if (connected) {
        statusLine.textContent = `متصل — ${where}`
          + (probe.server_name ? ` (${probe.server_name})` : "")
          + (probe.database ? ` / ${probe.database}` : "");
        statusLine.className = "db-status-line ok";
      } else {
        statusLine.textContent = `غير متصل — ${where}`
          + (probe.error ? ` · ${probe.error}` : "");
        statusLine.className = "db-status-line err";
      }
    }
  }

  async function refreshStatus() {
    try { paintStatus(await (await fetch("/db/status")).json()); }
    catch { /* console is best-effort */ }
  }

  openBtn.addEventListener("click", openModal);
  closeBtn.addEventListener("click", closeModal);
  modal.addEventListener("click", (e) => { if (e.target === modal) closeModal(); });
  document.addEventListener("keydown", (e) => {
    if (e.key === "Escape" && !modal.classList.contains("hidden")) closeModal();
  });

  eyeBtn.addEventListener("click", () => {
    passIn.type = passIn.type === "password" ? "text" : "password";
  });

  localToggle.addEventListener("change", async () => {
    if (filling) return;
    if (localToggle.checked) {
      await fetch("/db/reset", { method: "POST" });
      await refreshStatus();
      try { await loadContext(); } catch {}
      setMsg("يعمل على النسخة المحلية", "ok");
    } else {
      remoteFields.classList.remove("is-disabled");
      remoteActions.classList.remove("hidden");
      [serverIn, portIn, userIn, passIn, testBtn, saveBtn].forEach((n) => {
        if (n) n.disabled = false;
      });
      setMsg("أدخل عنوان الخادم ثم «حفظ واتصال»", "");
    }
  });

  function remotePayload() {
    return {
      server: serverIn.value,
      port: portIn.value ? Number(portIn.value) : null,
      user: userIn.value,
      password: passIn.value,
      database: snapshotDb || null,
      trusted: false,
    };
  }

  testBtn.addEventListener("click", async () => {
    setMsg("جارٍ الفحص…", "");
    let probe;
    try {
      probe = await jpost("/db/test", remotePayload());
    } catch { setMsg("تعذر الوصول للخدمة", "error"); return; }
    if (!probe.ok) { setMsg(probe.error || "فشل الاتصال", "error"); return; }
    setMsg(`✓ ${probe.server_name} — ${probe.version_line || ""}`.trim(), "ok");
  });

  saveBtn.addEventListener("click", async () => {
    saveBtn.disabled = true;
    const prev = saveBtn.textContent;
    saveBtn.textContent = "جارٍ الاتصال…";
    try {
      const res = await jpost("/db/connect", remotePayload());
      if (!res.ok) {
        setMsg(res.error || "فشل الاتصال", "error");
      } else {
        await refreshStatus();
        setMsg(`✓ تم الاتصال: ${res.probe && res.probe.server_name ? res.probe.server_name : ""}`.trim(), "ok");
        try { await loadContext(); } catch {}
      }
    } catch { setMsg("تعذر الوصول للخدمة", "error"); }
    saveBtn.disabled = false;
    saveBtn.textContent = prev;
  });

  refreshStatus();
})();
