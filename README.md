# Iris Classifier Service

## Setup
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

## Train the model
python train.py

## Run locally
uvicorn app.main:app --reload --port 8000

## Run tests
pytest -v

## Run with Docker
docker build -t iris-service .
docker run -p 8000:8000 iris-service

## Run with Docker Compose
docker compose up --build

## Endpoints
- GET /health
- POST /predict  { "features": [5.1, 3.5, 1.4, 0.2] }

## AI tool declaration
[Declare any AI tool use here per your module policy.]