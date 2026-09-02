from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib
import json
import os

def main():
    data = load_iris()
    X_train, X_test, y_train, y_test = train_test_split(
        data.data, data.target, test_size=0.2, random_state=42
    )

    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    acc = accuracy_score(y_test, model.predict(X_test))
    print(f"Test accuracy: {acc:.4f}")

    os.makedirs("model", exist_ok=True)
    joblib.dump(model, "model/model.joblib")

    with open("model/metadata.json", "w") as f:
        json.dump({
            "feature_names": data.feature_names,
            "target_names": data.target_names.tolist(),
            "accuracy": acc
        }, f, indent=2)

    print("Model saved to model/model.joblib")

if __name__ == "__main__":
    main()