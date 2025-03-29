# Stage 1: Builder
FROM python:3.9-slim as builder
WORKDIR /app
RUN pip install pdm==2.22.4
COPY pyproject.toml pdm.lock ./
RUN mkdir -p src/compiler_starter_aman \
    && touch README.md  # Ensure file exists
RUN pdm install --prod --no-lock

# Stage 2: Runtime
FROM python:3.9-slim
WORKDIR /app

# System dependencies for PyQt6
RUN apt-get update && apt-get install -y \
    libxcb-xinerama0 \
    && rm -rf /var/lib/apt/lists/*

# Copy virtualenv
COPY --from=builder /app/.venv .venv
ENV PATH="/app/.venv/bin:$PATH"

# Copy application
COPY . .

# Fallback if PDM fails
RUN [ -f requirements.txt ] && pip install -r requirements.txt || true

CMD ["python", "main.py"]