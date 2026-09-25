# Olives chatbot — Docker demo kit

Two images:

| Image | Role | Size (approx.) |
|-------|------|----------------|
| `olives-chatbot:latest` | FastAPI UI + vault notes + baked `work/105/` | ~400–600 MB |
| `olives-mssql-demo:latest` | SQL Server 2022 + restored `Olives_BO` + `chatbot_ro` | ~3–4 GB |

## Build (your machine)

**Shippable demo (105 snapshot, 21 companies — matches `CHATBOT_CLIENT=105`):**

```bash
bash docker/build-chatbot.sh
bash docker/build-mssql-demo.sh   # restores data/db-snapshots/backup test/105/olives_bo.bak
```

**Dev parity (literally the same DB files as `run.sh` on this machine):**

```bash
bash docker/gen-local-parity-compose.sh
docker compose -f docker-compose.local-parity.yml up
```

Uses bind mount `/media/alaa/data/mssql-data` — not shippable to boss.

Outputs: `docker/out/olives-chatbot.tar`, `docker/out/olives-mssql-demo.tar`

## Boss — Option A (demo, no SQL setup)

1. Install [Docker Desktop](https://www.docker.com/products/docker-desktop/).
2. Load images:
   ```bash
   docker load -i olives-chatbot.tar
   docker load -i olives-mssql-demo.tar
   ```
3. Copy `docker-compose.demo.yml` and `.env` (from `docker/.env.example`, set `DEEPSEEK_API_KEY`).
4. Run:
   ```bash
   docker compose -f docker-compose.demo.yml up
   ```
5. Open **http://localhost:8100** — leave **مصدر محلي** ON.

## Boss — Option B (his own SQL Server)

1. Load only `olives-chatbot.tar`.
2. `docker compose up` (uses `docker-compose.yml`).
3. Settings → turn **local OFF** → enter IP, port, user, password.
   - SQL on the **same PC**: use `host.docker.internal` (not `.`).
   - SQL on LAN: use that machine's IP.
4. Server must already have `chatbot_ro` + `t.` views (run `setup/native_bootstrap.py` once).

## Notes

- `.` in the IP field means **container localhost** — not the host PC. Use `host.docker.internal` on Docker Desktop.
- `work/ro_password.txt` inside the image matches the demo DB's `chatbot_ro` login.
- Sessions/cache persist in the `chatbot-work` volume.
