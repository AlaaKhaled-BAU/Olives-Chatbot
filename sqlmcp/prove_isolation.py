"""Runs INSIDE the appnet test-client container (which has NO route to the DB).
Proves two things at once:
  1. ISOLATION -- the DB is NOT reachable directly from here, and
  2. FUNCTION  -- a real gated query STILL works, via the MCP.
Exit 0 only if both hold. If step 1 fails the whole test is meaningless (the client
could be cheating past the MCP), so it hard-fails before even trying the MCP.
"""
import asyncio
import json
import os
import socket
import sys

MCP_URL = os.environ.get("MCP_URL", "http://olives-sql-mcp:9000/sse")
DB_HOST = os.environ.get("DB_HOST", "drift-tool-mssql")
DB_PORT = int(os.environ.get("DB_PORT", "1433"))


def db_reachable() -> bool:
    try:
        with socket.create_connection((DB_HOST, DB_PORT), timeout=3):
            return True
    except OSError:
        return False


async def query_via_mcp():
    from mcp import ClientSession
    from mcp.client.sse import sse_client

    async with sse_client(MCP_URL) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            result = await session.call_tool(
                "run_select",
                {"sql_text": "SELECT COUNT(*) AS n FROM t.Customers", "company_id": 1, "client": "morec"},
            )
            return json.loads(result.content[0].text)


def main():
    # 1. isolation: must NOT be able to open the DB port directly
    if db_reachable():
        print(f"FAIL: {DB_HOST}:{DB_PORT} reachable directly from appnet -- NOT isolated")
        sys.exit(1)
    print(f"OK: {DB_HOST}:{DB_PORT} not reachable directly (isolated)")

    # 2. function: the gated query must still work through the MCP bridge
    rows = asyncio.run(query_via_mcp())
    print("MCP query result:", rows)
    n = rows[0].get("n") if rows else None
    if n and int(n) > 0:
        print(f"PASS: DB is reachable ONLY via the MCP; gated query returned n={n}")
        sys.exit(0)
    print("FAIL: MCP reachable but query returned nothing")
    sys.exit(2)


if __name__ == "__main__":
    main()
