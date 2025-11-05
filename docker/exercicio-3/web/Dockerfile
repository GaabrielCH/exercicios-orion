# Estágio Base
FROM python:3.11-alpine AS base
WORKDIR /app
COPY requirements.txt .

# Estágio de Desenvolvimento
FROM base AS dev
RUN pip install --no-cache-dir -r requirements.txt flask[async]
ENV FLASK_ENV=development
ENV FLASK_DEBUG=1
ENV PYTHONUNBUFFERED=1
EXPOSE 8000
CMD ["flask", "run", "--host=0.0.0.0", "--port=8000", "--reload"]

# Estágio de Produção
FROM base AS prod
RUN pip install --no-cache-dir -r requirements.txt && \
    pip install gunicorn && \
    addgroup -g 1000 appuser && \
    adduser -D -u 1000 -G appuser appuser
COPY app.py .
RUN chown -R appuser:appuser /app
USER appuser
ENV PYTHONUNBUFFERED=1
ENV FLASK_ENV=production
EXPOSE 8000
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "2", "--threads", "2", "app:app"]
