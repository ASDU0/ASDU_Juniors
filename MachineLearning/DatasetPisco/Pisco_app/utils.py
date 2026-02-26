import joblib
import os
import pandas as pd

MODEL_PATH = "pisco_model.pkl"

def load_model():
    if not os.path.exists(MODEL_PATH):
        raise FileNotFoundError(
            "El modelo no existe. Ejecuta primero: python model.py"
        )
    return joblib.load(MODEL_PATH)


def create_input_dataframe(
    alcohol_pct,
    metanol_mg_L,
    acetato_etilo_mg_L,
    linalool_mg_L,
    isoamyl_alcohol_mg_L,
    propanol_mg_L,
    intensidad_aromatica,
    cuerpo
):
    return pd.DataFrame([[
        alcohol_pct,
        metanol_mg_L,
        acetato_etilo_mg_L,
        linalool_mg_L,
        isoamyl_alcohol_mg_L,
        propanol_mg_L,
        intensidad_aromatica,
        cuerpo
    ]], columns=[
        "alcohol_pct",
        "metanol_mg_L",
        "acetato_etilo_mg_L",
        "linalool_mg_L",
        "isoamyl_alcohol_mg_L",
        "propanol_mg_L",
        "intensidad_aromatica",
        "cuerpo"
    ])


def predict_sample(
    model,
    alcohol_pct,
    metanol_mg_L,
    acetato_etilo_mg_L,
    linalool_mg_L,
    isoamyl_alcohol_mg_L,
    propanol_mg_L,
    intensidad_aromatica,
    cuerpo
):
    datos = create_input_dataframe(
        alcohol_pct,
        metanol_mg_L,
        acetato_etilo_mg_L,
        linalool_mg_L,
        isoamyl_alcohol_mg_L,
        propanol_mg_L,
        intensidad_aromatica,
        cuerpo
    )

    prediccion = model.predict(datos)[0]
    probabilidades = model.predict_proba(datos)[0]

    return prediccion, probabilidades
