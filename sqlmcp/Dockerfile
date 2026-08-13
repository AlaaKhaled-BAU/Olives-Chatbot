# Deps baked in at build time (build runs on the default network, has internet).
# The isolated test nets are --internal (no route out), so runtime pip would fail
# there -- everything the MCP + test-client need must already be in the image.
# Code is bind-mounted at run time, so editing sqlmcp/*.py needs no rebuild.
FROM python:3.12-slim
RUN pip install --no-cache-dir mcp pymssql sqlglot pyyaml
WORKDIR /app
