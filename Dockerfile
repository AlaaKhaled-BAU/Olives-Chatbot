# Olives chatbot — Option B (app only) and Option A (pairs with olives-mssql-demo).
FROM python:3.13-slim-bookworm

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        gcc \
        freetds-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Almost the whole repo (vault notes, knowledge, prompts, work artifacts, setup scripts).
COPY . .
# Baked work/ copy — survives an empty Docker volume mount on first start.
RUN cp -a work /opt/olives-work-baked

COPY docker/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    CHATBOT_CLIENT=105 \
    DB_HOST=127.0.0.1 \
    DB_PORT=1433 \
    CHATBOT_MODEL_FAST=deepseek-v4-flash \
    CHATBOT_MODEL_HEAVY=deepseek-v4-pro

EXPOSE 8100

HEALTHCHECK --interval=30s --timeout=10s --start-period=40s --retries=3 \
    CMD python -c "import urllib.request; urllib.request.urlopen('http://127.0.0.1:8100/health', timeout=8)"

ENTRYPOINT ["/entrypoint.sh"]
