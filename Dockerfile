# image
FROM python:3.12-alpine

# atualizador e instalador de dependencias NO SISTEMA
RUN apk update && apk add --no-cache \
    zlib \
    gcc \
    libffi-dev \
    musl-dev \
    python3-dev \
    build-base

# var de ambiente
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# diretorio
WORKDIR /app

# instalador de dependencias NO PROJETO
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# copia o codigo
COPY . .

# porta 8000
EXPOSE 8000

# comando para inicializacao do uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
