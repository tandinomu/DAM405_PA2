# ---- build stage ----
FROM python:3.11-slim AS base

WORKDIR /app

# install deps first -> cached layer, only reinstalled when requirements.txt changes
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# now copy app code (changes more often, so it's a separate, later layer)
COPY app/ ./app/
COPY model/ ./model/

# create non-root user
RUN useradd --create-home appuser
USER appuser

EXPOSE 8000

HEALTHCHECK --interval=30s --timeout=3s \
  CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:8000/health')" || exit 1

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]