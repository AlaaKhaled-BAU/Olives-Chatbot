#!/usr/bin/env bash
# docker commit does NOT capture bind-mounted /var/opt/mssql — use build-mssql-demo.sh instead.
set -euo pipefail
echo "ERROR: docker commit cannot freeze bind-mounted SQL data (/var/opt/mssql)."
echo "Your local 'mssql' container stores data at /media/alaa/data/mssql-data (not in the image layer)."
echo ""
echo "Use instead:"
echo "  bash docker/build-mssql-demo.sh     # restores 105/olives_bo.bak (ships to boss)"
echo "  bash docker/gen-local-parity-compose.sh && docker compose -f docker-compose.local-parity.yml up"
exit 1
