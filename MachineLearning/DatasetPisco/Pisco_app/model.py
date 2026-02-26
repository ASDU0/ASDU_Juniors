import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib
import os

DATA_PATH = "data/pisco_dataset_sin_cepa.csv"
MODEL_PATH = "pisco_model.pkl"

def train_model():

    if not os.path.exists(DATA_PATH):
        raise FileNotFoundError("No se encontró el dataset.")

    df = pd.read_csv(DATA_PATH)

    # X = todas menos la variable objetivo
    X = df.drop("aditivo", axis=1)

    # y = variable objetivo
    y = df["aditivo"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y,
        test_size=0.2,
        random_state=42
    )

    model = RandomForestClassifier(
        n_estimators=200,
        random_state=42
    )

    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)

    joblib.dump(model, MODEL_PATH)

    print("Modelo entrenado correctamente.")
    print(f"Accuracy: {accuracy:.4f}")

if __name__ == "__main__":
    train_model()
