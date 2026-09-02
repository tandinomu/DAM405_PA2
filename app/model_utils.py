import joblib
import json
import os

MODEL_PATH = os.path.join(os.path.dirname(__file__), "..", "model", "model.joblib")
META_PATH = os.path.join(os.path.dirname(__file__), "..", "model", "metadata.json")

_model = None
_meta = None

def load_model():
    global _model, _meta
    if _model is None:
        _model = joblib.load(MODEL_PATH)
        with open(META_PATH) as f:
            _meta = json.load(f)
    return _model, _meta

def predict(features: list[float]):
    model, meta = load_model()
    pred = model.predict([features])[0]
    proba = model.predict_proba([features])[0].tolist()
    return {
        "prediction": meta["target_names"][pred],
        "confidence": max(proba)
    }