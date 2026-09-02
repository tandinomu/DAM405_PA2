from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, conlist
from app.model_utils import predict, load_model

@asynccontextmanager
async def lifespan(app: FastAPI):
    load_model()  # runs on startup
    yield

app = FastAPI(title="Iris Classifier Service", version="1.0.0", lifespan=lifespan)

class PredictRequest(BaseModel):
    features: conlist(float, min_length=4, max_length=4)

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/predict")
def predict_endpoint(req: PredictRequest):
    try:
        result = predict(req.features)
        return result
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Prediction failed: {str(e)}")