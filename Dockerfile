FROM python:3.12-slim

# Evita .pyc e garante logs sem buffer
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# Instala dependências primeiro (aproveita cache do Docker)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia o resto do código
COPY . .

# Ajuste o comando de entrada conforme sua aplicação
# Exemplos:
#   Flask/FastAPI com gunicorn -> CMD ["gunicorn", "-b", "0.0.0.0:8000", "app:app"]
#   Script simples             -> CMD ["python", "app.py"]
CMD ["python", "app.py"]
