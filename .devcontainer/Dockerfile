# Imagen base Dev Containers (Ubuntu)
FROM mcr.microsoft.com/devcontainers/base:ubuntu

# Instalar Python, pip, venv, Node.js, npm, git, etc.
RUN apt-get update && apt-get install -y \
    python3 python3-pip python3-venv \
    curl git jq \
    && rm -rf /var/lib/apt/lists/*

# Instalar Node.js LTS (v20) usando NodeSource
RUN curl -fsSL https://deb.nodesource.com/setup_20.x | bash - \
    && apt-get update && apt-get install -y nodejs \
    && rm -rf /var/lib/apt/lists/*

# Verificación rápida (no falla el build si cambia la salida, solo informativo)
RUN node -v && npm -v && python3 --version && pip3 --version