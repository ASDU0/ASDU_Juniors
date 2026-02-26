import streamlit as st
import os
from utils import load_model, predict_sample

st.set_page_config(
    page_title="Sistema de Análisis de Pisco",
    layout="centered"
)

st.title("Clasificación de Pisco Peruano")

# -------------------------
# CARGAR MODELO
# -------------------------
try:
    model = load_model()
except FileNotFoundError as e:
    st.error(str(e))
    st.stop()

# -------------------------
# INICIALIZAR SESSION STATE
# -------------------------
if "alcohol_pct" not in st.session_state:
    st.session_state.alcohol_pct = 40.0
    st.session_state.metanol_mg_L = 50.0
    st.session_state.acetato_etilo_mg_L = 100.0
    st.session_state.linalool_mg_L = 5.0
    st.session_state.isoamyl_alcohol_mg_L = 150.0
    st.session_state.propanol_mg_L = 120.0
    st.session_state.intensidad_aromatica = 5.0
    st.session_state.cuerpo = 5.0

# -------------------------
# SIDEBAR - MODO
# -------------------------
st.sidebar.header("Modo de Entrada")

modo = st.sidebar.radio(
    "Selecciona el modo:",
    ["Manual", "Automático por Tipo"]
)

# -------------------------
# MODO AUTOMÁTICO
# -------------------------
if modo == "Automático por Tipo":

    tipo = st.sidebar.radio(
        "Tipo de Pisco:",
        ["puro", "caramelo", "azucar", "madera"]
    )

    if st.sidebar.button("Asignar Parámetros"):

        if tipo == "puro":
            st.session_state.alcohol_pct = 42.0
            st.session_state.metanol_mg_L = 60.0
            st.session_state.acetato_etilo_mg_L = 90.0
            st.session_state.linalool_mg_L = 8.0
            st.session_state.isoamyl_alcohol_mg_L = 140.0
            st.session_state.propanol_mg_L = 110.0
            st.session_state.intensidad_aromatica = 7.0
            st.session_state.cuerpo = 6.0

        elif tipo == "caramelo":
            st.session_state.alcohol_pct = 38.0
            st.session_state.metanol_mg_L = 80.0
            st.session_state.acetato_etilo_mg_L = 120.0
            st.session_state.linalool_mg_L = 4.0
            st.session_state.isoamyl_alcohol_mg_L = 170.0
            st.session_state.propanol_mg_L = 130.0
            st.session_state.intensidad_aromatica = 5.0
            st.session_state.cuerpo = 4.0

        elif tipo == "azucar":
            st.session_state.alcohol_pct = 35.0
            st.session_state.metanol_mg_L = 90.0
            st.session_state.acetato_etilo_mg_L = 150.0
            st.session_state.linalool_mg_L = 3.0
            st.session_state.isoamyl_alcohol_mg_L = 180.0
            st.session_state.propanol_mg_L = 140.0
            st.session_state.intensidad_aromatica = 4.0
            st.session_state.cuerpo = 3.0

        elif tipo == "madera":
            st.session_state.alcohol_pct = 40.0
            st.session_state.metanol_mg_L = 70.0
            st.session_state.acetato_etilo_mg_L = 100.0
            st.session_state.linalool_mg_L = 6.0
            st.session_state.isoamyl_alcohol_mg_L = 160.0
            st.session_state.propanol_mg_L = 120.0
            st.session_state.intensidad_aromatica = 8.0
            st.session_state.cuerpo = 8.0

        st.success("Parámetros asignados correctamente")

# -------------------------
# SLIDERS (CONTROL PRINCIPAL)
# -------------------------
st.subheader("Parámetros Químicos")

alcohol_pct = st.slider(
    "Alcohol (%)",
    0.0, 60.0,
    st.session_state.alcohol_pct,
    0.1
)

metanol_mg_L = st.slider(
    "Metanol (mg/L)",
    0.0, 500.0,
    st.session_state.metanol_mg_L,
    1.0
)

acetato_etilo_mg_L = st.slider(
    "Acetato de Etilo (mg/L)",
    0.0, 500.0,
    st.session_state.acetato_etilo_mg_L,
    1.0
)

linalool_mg_L = st.slider(
    "Linalool (mg/L)",
    0.0, 50.0,
    st.session_state.linalool_mg_L,
    0.1
)

isoamyl_alcohol_mg_L = st.slider(
    "Isoamyl Alcohol (mg/L)",
    0.0, 500.0,
    st.session_state.isoamyl_alcohol_mg_L,
    1.0
)

propanol_mg_L = st.slider(
    "Propanol (mg/L)",
    0.0, 500.0,
    st.session_state.propanol_mg_L,
    1.0
)

intensidad_aromatica = st.slider(
    "Intensidad Aromática",
    0.0, 10.0,
    st.session_state.intensidad_aromatica,
    0.1
)

cuerpo = st.slider(
    "Cuerpo",
    0.0, 10.0,
    st.session_state.cuerpo,
    0.1
)

# -------------------------
# BOTÓN ANALIZAR
# -------------------------
# -------------------------
# BOTÓN ANALIZAR
# -------------------------
if st.button("Analizar Pisco"):

    # Obtener predicción y probabilidades
    prediccion, probabilidades = predict_sample(
        model,
        alcohol_pct,
        metanol_mg_L,
        acetato_etilo_mg_L,
        linalool_mg_L,
        isoamyl_alcohol_mg_L,
        propanol_mg_L,
        intensidad_aromatica,
        cuerpo
    )

    # Obtener clase con mayor probabilidad
    max_index = probabilidades.argmax()
    clase_mayor = model.classes_[max_index]
    prob_mayor = probabilidades[max_index]

    # Mapear "Ninguno" a "Puro"
    if clase_mayor == "Ninguno":
        clase_mostrar = "puro"
    else:
        clase_mostrar = clase_mayor

    st.success(f"Tipo Detectado: {clase_mostrar} ({prob_mayor:.2%})")

    st.subheader("Probabilidades:")

    for clase, prob in zip(model.classes_, probabilidades):

        if clase == "Ninguno":
            clase = "puro"

        st.write(f"{clase}: {prob:.2%}")

    # Mostrar imagen del mayor porcentaje
    image_name = clase_mostrar.lower().replace(" ", "_")
    image_path = f"images/botella_{image_name}.png"

    if os.path.exists(image_path):
        st.image(image_path, width=250)
    else:
        st.warning("No se encontró imagen para este tipo.")
