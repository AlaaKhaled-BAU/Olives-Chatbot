#!/usr/bin/env python3
"""
MCP Server for Obsidian Olives Vault.
Provides tools to search, read, and query notes.
Protocol: JSON-RPC 2.0 over stdio.
"""
import json
import os
import re
import sys
from collections import defaultdict

import yaml

VAULT = "/media/alaa/data/client-chatbot/obsidian/olives"
GRAPH_PATH = "/media/alaa/data/client-chatbot/db/vault_graph.json"

# ─── Tools ────────────────────────────────────────────────

TOOLS = [
    {
        "name": "search_notes",
        "description": "Full-text search across all vault notes. Returns matching note names and excerpts.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "pattern": {"type": "string", "description": "Regex pattern to search for (case-insensitive). Invalid regex returns a clean error."},
                "database": {"type": "string", "description": "Filter by database: Olives_BO, OSFA_DB, or omit for both"},
                "type": {"type": "string", "description": "Filter by type: table, procedure, relation, shared, or omit"},
                "limit": {"type": "integer", "description": "Max results (default 20)"},
            },
            "required": ["pattern"],
        },
    },
    {
        "name": "read_note",
        "description": "Read a specific note by name, by relative vault path, or by database+type. Returns full markdown content.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "name": {"type": "string", "description": "Note name (case-insensitive)"},
                "path": {"type": "string", "description": "Relative vault path, e.g. 'Shared/Runbooks/Duplicate-Keys.md' or 'OSFA_DB/Tables/OT_ItemsMF.md'"},
                "database": {"type": "string", "description": "Olives_BO or OSFA_DB (required if name exists in both)"},
                "type": {"type": "string", "description": "table, procedure, or relation (helps disambiguate)"},
            },
        },
    },
    {
        "name": "get_backlinks",
        "description": "Find ALL notes that link to a given note (incoming links).",
        "inputSchema": {
            "type": "object",
            "properties": {
                "name": {"type": "string", "description": "Target note name"},
                "database": {"type": "string", "description": "Olives_BO or OSFA_DB"},
            },
            "required": ["name"],
        },
    },
    {
        "name": "query_by_tag",
        "description": "Find notes by frontmatter tags.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "tag": {"type": "string", "description": "Tag to search for (e.g. customer, billing, inventory)"},
                "database": {"type": "string", "description": "Filter by database"},
                "type": {"type": "string", "description": "Filter by type: table, procedure, relation"},
            },
            "required": ["tag"],
        },
    },
    {
        "name": "query_by_field",
        "description": "Query notes by any frontmatter field value.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "field": {"type": "string", "description": "Frontmatter field name (e.g. support_relevance, database, type)"},
                "value": {"type": "string", "description": "Field value to match"},
                "database": {"type": "string", "description": "Filter by database"},
            },
            "required": ["field", "value"],
        },
    },
    {
        "name": "list_tables_db",
        "description": "List all tables in a database with their support_relevance and FK count.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "database": {"type": "string", "description": "Olives_BO or OSFA_DB"},
                "tag": {"type": "string", "description": "Optional filter by domain tag"},
                "min_relevance": {"type": "string", "description": "Minimum relevance: high, medium, low"},
            },
            "required": ["database"],
        },
    },
    {
        "name": "list_procs_db",
        "description": "List all procedures in a database with their support_relevance and table count.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "database": {"type": "string", "description": "Olives_BO or OSFA_DB"},
                "tag": {"type": "string", "description": "Optional filter by domain tag"},
            },
            "required": ["database"],
        },
    },
    {
        "name": "get_common_issues",
        "description": "Get Common Issues section from a table note — useful for triage.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "table_name": {"type": "string", "description": "Table name"},
                "database": {"type": "string", "description": "Olives_BO or OSFA_DB"},
            },
            "required": ["table_name", "database"],
        },
    },
    {
        "name": "get_when_to_run",
        "description": "Get the When-to-Run section from a procedure note — triage guidance.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "proc_name": {"type": "string", "description": "Procedure name"},
                "database": {"type": "string", "description": "Olives_BO or OSFA_DB"},
            },
            "required": ["proc_name", "database"],
        },
    },
    {
        "name": "get_impact",
        "description": "Impact analysis for a table: procedures that READ and WRITE it, plus upstream callers and downstream callees (from vault_graph.json).",
        "inputSchema": {
            "type": "object",
            "properties": {
                "name": {"type": "string", "description": "Table name"},
                "database": {"type": "string", "description": "Olives_BO or OSFA_DB (required if ambiguous)"},
            },
            "required": ["name"],
        },
    },
    {
        "name": "get_proc_deps",
        "description": "Procedure dependencies: tables read/written by the procedure and by its callers/callees (from vault_graph.json).",
        "inputSchema": {
            "type": "object",
            "properties": {
                "name": {"type": "string", "description": "Procedure name"},
                "database": {"type": "string", "description": "Olives_BO or OSFA_DB (required if ambiguous)"},
            },
            "required": ["name"],
        },
    },
]

# ─── Helpers ──────────────────────────────────────────────

def _split_flow(s):
    """Split a flow-sequence inner body on commas not nested inside []."""
    items, depth, cur = [], 0, ""
    for ch in s:
        if ch == '[':
            depth += 1
            cur += ch
        elif ch == ']':
            depth -= 1
            cur += ch
        elif ch == ',' and depth == 0:
            items.append(cur.strip())
            cur = ''
        else:
            cur += ch
    if cur.strip():
        items.append(cur.strip())
    return items


def _parse_yaml_block(block):
    """Parse the frontmatter block into a dict, handling scalar, flow-list and
    block-list values (including wiki-link items and '#'-prefixed flow tags)."""
    lines = block.split('\n')
    result = {}
    i, n = 0, len(lines)
    while i < n:
        line = lines[i]
        if not line.strip():
            i += 1
            continue
        mm = re.match(r'^([A-Za-z_][\w-]*):\s*(.*)$', line)
        if not mm:
            i += 1
            continue
        key, val = mm.group(1), mm.group(2).strip()
        if val == '':
            j = i + 1
            items = []
            while j < n and re.match(r'^\s*-\s*(.*)$', lines[j]):
                items.append(re.match(r'^\s*-\s*(.*)$', lines[j]).group(1).strip())
                j += 1
            result[key] = items if items else ""
            i = j
        elif val.startswith('['):
            buf, j = val, i
            while not buf.rstrip().endswith(']') and j + 1 < n:
                j += 1
                buf += ' ' + lines[j].strip()
            inner = buf.strip()[1:-1] if buf.strip().endswith(']') else buf.strip()[1:]
            result[key] = _split_flow(inner)
            i = j + 1
        else:
            result[key] = val
            i += 1
    return result


def _norm_value(v):
    """Normalize a frontmatter value for comparison: strip [[ ]] wiki-links and alias."""
    v = str(v).strip()
    if v.startswith('[['):
        v = v[2:]
    if v.endswith(']]'):
        v = v[:-2]
    return v.split('|')[0].strip().lower()


def parse_frontmatter(content):
    """Parse YAML frontmatter. Try PyYAML, then a robust block parser, then regex."""
    m = re.match(r'^---\s*\n(.*?)\n---', content, re.DOTALL)
    if not m:
        return {}
    block = m.group(1)
    try:
        data = yaml.safe_load(block)
        if isinstance(data, dict):
            return data
    except Exception:
        pass
    try:
        data = _parse_yaml_block(block)
        if data:
            return data
    except Exception:
        pass
    fm = {}
    for line in block.split('\n'):
        mm = re.match(r'^(\w+):\s*(.*)', line)
        if mm:
            fm[mm.group(1)] = mm.group(2).strip()
    return fm


# ─── Cached index + graph (built once at startup) ──────────

def _build_index():
    """Walk vault ONCE and return list of all notes with metadata."""
    notes = []
    for root, dirs, files in os.walk(VAULT):
        if '.obsidian' in root:
            continue
        for fname in files:
            if not fname.endswith('.md'):
                continue
            path = os.path.join(root, fname)
            rel = os.path.relpath(path, VAULT)
            parts = rel.split(os.sep)
            db_dir = parts[0] if len(parts) > 1 else "Shared"
            subdir = parts[1] if len(parts) > 2 else ""
            notes.append({"path": path, "rel": rel, "db": db_dir, "subdir": subdir, "fname": fname})
    return notes


NOTES_INDEX = _build_index()


def _load_graph():
    try:
        with open(GRAPH_PATH, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception:
        return {"tables": {}, "procedures": {}}


VAULT_GRAPH = _load_graph()


def find_notes():
    """Return the cached notes index (built once at startup)."""
    return NOTES_INDEX


def get_note_content(name, db_filter=None, type_filter=None):
    """Find and read a note by name using the cached index."""
    target = name.upper()
    for n in NOTES_INDEX:
        try:
            with open(n["path"], 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception:
            continue
        fm = parse_frontmatter(content)
        fm_name = str(fm.get("name", n["fname"].replace(".md", "")))
        if fm_name.upper() == target:
            note_db = n["db"]
            note_type = fm.get("type", "")
            if db_filter and db_filter.upper() != note_db.upper():
                continue
            if type_filter and type_filter.lower() != note_type.lower():
                continue
            return {"path": n["rel"], "name": fm_name, "type": note_type, "database": note_db,
                    "fm": fm, "content": content}
    return None


def extract_section(content, section_names):
    """Extract a section from markdown content. Accepts a name or list of names.
    Returns (body, matched_name) where matched_name is None if no heading found."""
    names = section_names if isinstance(section_names, (list, tuple)) else [section_names]
    for sn in names:
        pattern = rf'## {re.escape(sn)}\s*\n(.*?)(?=\n## |\Z)'
        m = re.search(pattern, content, re.DOTALL)
        if m:
            return m.group(1).strip(), sn
    return "", None


def _lookup(kind, name, database=None):
    """Find graph entries of kind ('tables'|'procedures') by name, optionally by db."""
    store = VAULT_GRAPH.get(kind, {})
    matches = []
    for key, entry in store.items():
        if entry.get("name", "").upper() == name.upper():
            if database and entry.get("database", "").upper() != database.upper():
                continue
            matches.append((key, entry))
    return matches


def _get_proc(name, database=None):
    """Get a single procedure entry by name."""
    matches = _lookup("procedures", name, database)
    return matches[0][1] if matches else None


# ─── MCP Protocol ─────────────────────────────────────────

def send(msg):
    sys.stdout.write(json.dumps(msg) + "\n")
    sys.stdout.flush()


def handle_request(req):
    method = req.get("method")
    req_id = req.get("id")
    params = req.get("params", {})

    if method == "initialize":
        send({"jsonrpc": "2.0", "id": req_id,
              "result": {"protocolVersion": "2024-11-05",
                         "capabilities": {"tools": {}},
                         "serverInfo": {"name": "obsidian-olives-mcp", "version": "1.0.0"}}})
        return

    if method == "notifications/initialized":
        return

    if method == "tools/list":
        send({"jsonrpc": "2.0", "id": req_id, "result": {"tools": TOOLS}})
        return

    if method == "tools/call":
        tool = params.get("name")
        args = params.get("arguments", {})
        try:
            result = handle_tool(tool, args)
            send({"jsonrpc": "2.0", "id": req_id, "result": {"content": [{"type": "text", "text": result}]}})
        except Exception as e:
            send({"jsonrpc": "2.0", "id": req_id, "error": {"code": -32603, "message": str(e)}})
        return

    send({"jsonrpc": "2.0", "id": req_id, "error": {"code": -32601, "message": f"Unknown method: {method}"}})


def handle_tool(tool, args):
    notes = find_notes()

    if tool == "search_notes":
        pattern = args["pattern"]
        db_filter = args.get("database", "")
        type_filter = args.get("type", "")
        limit = min(args.get("limit", 20), 100)
        try:
            rx = re.compile(pattern, re.IGNORECASE)
        except re.error as e:
            return f"Invalid regex pattern: {e}"
        results = []
        for n in notes:
            if db_filter and n["db"] != db_filter:
                continue
            try:
                with open(n["path"], 'r', encoding='utf-8') as f:
                    content = f.read()
            except:
                continue
            fm = parse_frontmatter(content)
            if type_filter and fm.get("type", "") != type_filter:
                continue
            matches = list(rx.finditer(content))
            if matches:
                excerpt = content[max(0, matches[0].start()-80):matches[0].start()+80].replace('\n', ' ')
                results.append(f"[{n['rel']}] {fm.get('name', n['fname'])} — ...{excerpt}...")
            if len(results) >= limit:
                break

        if not results:
            return f"No notes match pattern '{pattern}'."
        return "## Search Results\n" + "\n".join(results)

    if tool == "read_note":
        rel_path = args.get("path")
        if rel_path:
            cand = os.path.join(VAULT, rel_path)
            if not os.path.exists(cand) and not rel_path.endswith(".md"):
                cand = os.path.join(VAULT, rel_path + ".md")
            if os.path.exists(cand):
                try:
                    with open(cand, 'r', encoding='utf-8') as f:
                        return f.read()
                except Exception as e:
                    return f"Error reading '{rel_path}': {e}"
            # tolerate a doubled 'Shared/Shared' style accident
            alt = os.path.join(VAULT, rel_path.replace("Shared/Shared/", "Shared/"))
            if os.path.exists(alt):
                try:
                    with open(alt, 'r', encoding='utf-8') as f:
                        return f.read()
                except Exception as e:
                    return f"Error reading '{rel_path}': {e}"
            return f"Note at path '{rel_path}' not found."
        note = get_note_content(args.get("name", ""), args.get("database"), args.get("type"))
        if not note:
            return f"Note '{args.get('name', '')}' not found."
        return note["content"]

    if tool == "get_backlinks":
        target = args["name"].upper()
        results = []
        for n in notes:
            try:
                with open(n["path"], 'r', encoding='utf-8') as f:
                    content = f.read()
            except:
                continue
            links = re.findall(r'\[\[([^\]]+?)(?:\|[^\]]+)?\]\]', content)
            for link in links:
                link_clean = link.split("|")[0].strip()
                link_base = link_clean.split('/')[-1]
                if link_base.upper() == target:
                    fm = parse_frontmatter(content)
                    results.append(f"[{n['rel']}] {fm.get('name', n['fname'])}")
                    break
        if not results:
            return f"No backlinks to '{args['name']}'."
        return f"## Backlinks to [[{args['name']}]]\n" + "\n".join(sorted(results))

    if tool == "query_by_tag":
        tag = args["tag"]
        db_filter = args.get("database", "")
        type_filter = args.get("type", "")
        results = []
        for n in notes:
            if db_filter and n["db"] != db_filter:
                continue
            try:
                with open(n["path"], 'r', encoding='utf-8') as f:
                    content = f.read()
            except:
                continue
            fm = parse_frontmatter(content)
            if type_filter and fm.get("type", "") != type_filter:
                continue
            tags_val = fm.get("tags", [])
            if isinstance(tags_val, str):
                tags_list = [t.strip() for t in re.split(r'[,\s]+', tags_val) if t.strip()]
            else:
                tags_list = [str(t) for t in tags_val]
            if any(t.lower() == f"#{tag}".lower() or t.lower() == tag.lower() for t in tags_list):
                results.append(f"[{n['rel']}] {fm.get('name', n['fname'])} — relevance: {fm.get('support_relevance', 'N/A')}")
        if not results:
            return f"No notes with tag #{tag}."
        return f"## Notes tagged #{tag} ({len(results)})\n" + "\n".join(sorted(results))

    if tool == "query_by_field":
        field = args["field"]
        value = args["value"]
        db_filter = args.get("database", "")
        results = []
        for n in notes:
            if db_filter and n["db"] != db_filter:
                continue
            try:
                with open(n["path"], 'r', encoding='utf-8') as f:
                    content = f.read()
            except:
                continue
            fm = parse_frontmatter(content)
            fv = fm.get(field, "")
            if isinstance(fv, list):
                match = any(_norm_value(x) == value.lower() for x in fv)
            else:
                match = _norm_value(fv) == value.lower()
            if match:
                results.append(f"[{n['rel']}] {fm.get('name', n['fname'])}")
        if not results:
            return f"No notes with {field} = {value}."
        return f"## {field} = {value} ({len(results)})\n" + "\n".join(sorted(results))

    if tool == "list_tables_db":
        db = args["database"]
        tag = args.get("tag", "")
        min_rel = args.get("min_relevance", "")
        results = []
        for n in notes:
            if n["db"] != db or n["subdir"] != "Tables":
                continue
            try:
                with open(n["path"], 'r', encoding='utf-8') as f:
                    content = f.read()
            except:
                continue
            fm = parse_frontmatter(content)
            if tag and f"#{tag}" not in fm.get("tags", ""):
                continue
            rel = fm.get("support_relevance", "medium")
            if min_rel:
                order = {"high": 3, "medium": 2, "low": 1}
                if order.get(rel, 0) < order.get(min_rel, 0):
                    continue
            results.append(f"  {fm.get('name', n['fname'])} [{rel}] tags: {fm.get('tags', '')}")
        if not results:
            return f"No tables found."
        return f"## Tables in {db} ({len(results)})\n" + "\n".join(sorted(results))

    if tool == "list_procs_db":
        db = args["database"]
        tag = args.get("tag", "")
        results = []
        for n in notes:
            if n["db"] != db or n["subdir"] != "Procedures":
                continue
            try:
                with open(n["path"], 'r', encoding='utf-8') as f:
                    content = f.read()
            except:
                continue
            fm = parse_frontmatter(content)
            if tag and f"#{tag}" not in fm.get("tags", ""):
                continue
            results.append(f"  {fm.get('name', n['fname'])} [{fm.get('support_relevance', 'medium')}]")
        if not results:
            return f"No procedures found."
        return f"## Procedures in {db} ({len(results)})\n" + "\n".join(sorted(results))

    if tool == "get_common_issues":
        note = get_note_content(args["table_name"], args.get("database"))
        if not note:
            return f"Table '{args['table_name']}' not found."
        issues, found = extract_section(note["content"], "Common Issues")
        if found is None:
            return f"No Common Issues section found in {args['table_name']}."
        if not issues:
            return f"## Common Issues for {args['table_name']}\n(section present but empty)"
        return f"## Common Issues for {args['table_name']}\n{issues}"

    if tool == "get_when_to_run":
        note = get_note_content(args["proc_name"], args.get("database"))
        if not note:
            return f"Procedure '{args['proc_name']}' not found."
        wtr, found = extract_section(note["content"], ["When to Run This", "When to Run"])
        if found is None:
            return f"No When-to-Run section found in {args['proc_name']}."
        if not wtr:
            return f"## When to Run: {args['proc_name']}\n(section present but empty)"
        return f"## When to Run: {args['proc_name']}\n{wtr}"

    if tool == "get_impact":
        name = args["name"]
        database = args.get("database")
        tables = _lookup("tables", name, database)
        if not tables:
            return f"Table '{name}' not found" + (f" in {database}." if database else ".")
        if len(tables) > 1:
            dbs = [e.get("database") for _, e in tables]
            return f"Table '{name}' is ambiguous across databases {dbs}; specify the 'database' argument."
        key, table = tables[0]
        db = table.get("database")
        reading = table.get("procedures_reading") or []
        writing = table.get("procedures_writing") or []
        upstream = set()
        downstream = set()
        for pname in set(reading) | set(writing):
            pe = _get_proc(pname, db)
            if pe:
                upstream.update(pe.get("callers") or [])
                downstream.update(pe.get("called_by") or [])
        lines = [f"## Impact for table {name} ({db})"]
        lines.append(f"Procedures READING this table ({len(reading)}):")
        lines += [f"  - {p}" for p in sorted(reading)] or ["  (none)"]
        lines.append(f"Procedures WRITING this table ({len(writing)}):")
        lines += [f"  - {p}" for p in sorted(writing)] or ["  (none)"]
        lines.append(f"Upstream callers ({len(upstream)}):")
        lines += [f"  - {p}" for p in sorted(upstream)] or ["  (none)"]
        lines.append(f"Downstream callees ({len(downstream)}):")
        lines += [f"  - {p}" for p in sorted(downstream)] or ["  (none)"]
        cross_db = table.get("cross_db") or []
        lines.append(f"Cross-DB counterparts ({len(cross_db)}):")
        lines += [f"  - {c}" for c in sorted(cross_db)] or ["  (none)"]
        return "\n".join(lines)

    if tool == "get_proc_deps":
        name = args["name"]
        database = args.get("database")
        procs = _lookup("procedures", name, database)
        if not procs:
            return f"Procedure '{name}' not found" + (f" in {database}." if database else ".")
        if len(procs) > 1:
            dbs = [e.get("database") for _, e in procs]
            return f"Procedure '{name}' is ambiguous across databases {dbs}; specify the 'database' argument."
        key, proc = procs[0]
        db = proc.get("database")
        reads = list(proc.get("reads_from") or [])
        writes = list(proc.get("writes_to") or [])
        callers = list(proc.get("callers") or [])
        callees = list(proc.get("called_by") or [])
        extra_reads = set()
        extra_writes = set()
        for c in set(callers) | set(callees):
            ce = _get_proc(c, db)
            if ce:
                extra_reads.update(ce.get("reads_from") or [])
                extra_writes.update(ce.get("writes_to") or [])
        lines = [f"## Dependencies for procedure {name} ({db})"]
        lines.append(f"Tables READ ({len(reads)}):")
        lines += [f"  - {t}" for t in sorted(reads)] or ["  (none)"]
        lines.append(f"Tables WRITTEN ({len(writes)}):")
        lines += [f"  - {t}" for t in sorted(writes)] or ["  (none)"]
        lines.append(f"Callers ({len(callers)}):")
        lines += [f"  - {c}" for c in sorted(callers)] or ["  (none)"]
        lines.append(f"Callees ({len(callees)}):")
        lines += [f"  - {c}" for c in sorted(callees)] or ["  (none)"]
        if extra_reads or extra_writes:
            lines.append(f"Tables READ by callers/callees ({len(extra_reads)}):")
            lines += [f"  - {t}" for t in sorted(extra_reads)] or ["  (none)"]
            lines.append(f"Tables WRITTEN by callers/callees ({len(extra_writes)}):")
            lines += [f"  - {t}" for t in sorted(extra_writes)] or ["  (none)"]
        cross_db = proc.get("cross_db") or []
        lines.append(f"Cross-DB links ({len(cross_db)}):")
        lines += [f"  - {c}" for c in sorted(cross_db)] or ["  (none)"]
        return "\n".join(lines)

    return f"Unknown tool: {tool}"


# ─── Main ─────────────────────────────────────────────────

def main():
    buffer = ""
    while True:
        try:
            line = sys.stdin.readline()
            if not line:
                break
            buffer += line
            try:
                req = json.loads(buffer)
                buffer = ""
                handle_request(req)
            except json.JSONDecodeError:
                continue
        except EOFError:
            break
        except KeyboardInterrupt:
            break


if __name__ == "__main__":
    main()
