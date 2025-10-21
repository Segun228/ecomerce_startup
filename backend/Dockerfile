FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN adduser --system --group appuser

RUN apt-get update && apt-get install -y \
    postgresql-client \
    libpq-dev \
    gcc \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt


COPY . /app

USER appuser


ENV DJANGO_SETTINGS_MODULE=backend.settings
CMD ["gunicorn", "backend.wsgi:application", "--bind", "0.0.0.0:8000"]