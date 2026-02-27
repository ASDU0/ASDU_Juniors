# Visión por Computador: Teoría Fundamental (Resumen)

## 1️⃣ ¿Qué es la Visión por Computador?
Es un campo de la inteligencia artificial que entrena a las computadoras para **interpretar y entender el mundo visual** (imágenes, videos). El objetivo es replicar la capacidad humana de percibir objetos, personas, escenas y contextos, pero a través de algoritmos y modelos matemáticos.

**Analogía:** Así como nuestros ojos envían señales al cerebro para que las procese, en visión artificial, una cámara captura píxeles y un algoritmo los procesa para extraer información significativa.

---

## 2️⃣ Niveles de Procesamiento Visual
El análisis de imágenes se puede dividir en tres niveles jerárquicos:

### a) Procesamiento de Bajo Nivel
- **Qué hace:** Opera directamente sobre los píxeles.
- **Tareas:**
    - **Filtrado:** Suavizar (desenfocar) o resaltar bordes.
    - **Detección de bordes:** Identificar cambios bruscos de intensidad (ej. algoritmo Canny).
    - **Operaciones morfológicas:** Erosión y dilatación para limpiar ruido.

### b) Procesamiento de Nivel Intermedio
- **Qué hace:** Agrupa píxeles para formar estructuras.
- **Tareas:**
    - **Segmentación:** Dividir la imagen en regiones de interés (ej. separar el fondo del objeto).
    - **Extracción de características:** Identificar formas, texturas o colores específicos.

### c) Procesamiento de Alto Nivel
- **Qué hace:** Asigna significado semántico a la imagen.
- **Tareas:**
    - **Clasificación:** ¿Qué objeto es este? (ej. "es un gato").
    - **Detección:** ¿Dónde está el objeto? (dibuja un recuadro a su alrededor).
    - **Reconocimiento:** ¿Quién es esta persona? (identificación facial).

---

## 3️⃣ Tareas Principales en Visión por Computador

### 📸 Clasificación de Imágenes
- **Objetivo:** Dado un input (imagen), asignarle una única etiqueta de clase.
- **Ejemplo:** Esta foto contiene un "perro".

### 🔍 Detección de Objetos
- **Objetivo:** Identificar *múltiples* objetos dentro de una misma imagen y ubicarlos espacialmente con *bounding boxes* (cajas delimitadoras).
- **Ejemplo:** Encontrar todos los coches y peatones en una foto de calle.

### 🎨 Segmentación Semántica
- **Objetivo:** Clasificar *cada píxel* de la imagen en una categoría. No distingue instancias (todos los coches son "coche", sin diferenciar coche1 de coche2).
- **Ejemplo:** Pintar la carretera de gris, el cielo de azul y los peatones de rojo.

### 🧩 Segmentación de Instancias
- **Objetivo:** Es la combinación de detección + segmentación. Clasifica cada píxel *y* distingue entre instancias individuales.
- **Ejemplo:** Pintar cada persona de un color diferente, aunque estén superpuestas.

---

## 4️⃣ Evolución Técnica: De lo Clásico al Deep Learning

### 🧮 Enfoque Clásico (Tradicional)
Se basaba en ingeniería de características hechas a mano.
1.  **Extracción de Características:** Algoritmos como SIFT (Scale-Invariant Feature Transform) o HOG (Histogram of Oriented Gradients) detectaban bordes, esquinas y texturas.
2.  **Clasificación:** Esas características se pasaban a un clasificador clásico como **SVM (Support Vector Machine)** o Random Forest.

**Limitación:** Dependían del conocimiento del experto para diseñar las características; no generalizaban bien a escenarios no vistos.

### 🤖 Enfoque de Deep Learning (Actual)
Las redes neuronales, especialmente las **Redes Neuronales Convolucionales (CNNs)** , automatizan todo el proceso.
1.  **Aprendizaje de Características:** La red aprende automáticamente qué bordes, texturas o formas son relevantes para la tarea.
2.  **End-to-End:** La imagen entra y la predicción sale, sin pasos intermedios manuales.

**Ventaja:** Mucho mayor precisión y robustez, capaces de aprender representaciones jerárquicas complejas.

---

## 5️⃣ Arquitectura Clave: Redes Neuronales Convolucionales (CNN)
Son el pilar del Deep Learning aplicado a imágenes.

### Componentes Principales
1.  **Capas de Convolución:** Aplican filtros (kernels) a la imagen para extraer características. El filtro "desliza" sobre la imagen produciendo un *mapa de características*.
2.  **Capas de Pooling (Submuestreo):** Reducen la dimensionalidad de los mapas de características (ej. Max Pooling, que se queda con el valor máximo de una región). Sirve para hacer el modelo más robusto a pequeñas variaciones.
3.  **Capas Fully Connected (FC):** Al final de la red, "aplanan" la información y actúan como un clasificador tradicional para dar el resultado final.

### Arquitectos CNN Populares
- **AlexNet:** Pionera que ganó ImageNet en 2012.
- **VGG16:** Demostró que la profundidad (muchas capas) mejora el rendimiento.
- **ResNet:** Introdujo las "conexiones residuales" (saltos) para poder entrenar redes extremadamente profundas (>100 capas) sin perder precisión.
- **YOLO (You Only Look Once):** Arquitectura famosa por su velocidad en detección de objetos en tiempo real.

---

## 6️⃣ Desafíos Actuales y Conceptos Clave
- **Iluminación y Escala:** Un objeto se ve diferente con luz solar que con luz artificial, o de cerca que de lejos. Los modelos deben ser **invariantes** a estos cambios.
- **Oclusión:** Cuando el objeto está parcialmente tapado por otro.
- **Punto de Vista:** Un objeto visto desde un ángulo puede parecer muy diferente que desde otro.
- **Datos Etiquetados:** El Deep Learning requiere grandes volúmenes de datos anotados manualmente, lo cual es costoso y lento (de ahí el auge del *Aprendizaje Semi-Supervisado* y *Self-Supervisado*).
- **Aprendizaje por Transferencia (*Transfer Learning*):** Técnica estrella. Se toma un modelo ya entrenado (ej. en ImageNet) y se re-entrena (*fine-tuning*) la última capa para una tarea específica con pocos datos. Ahorra tiempo y recursos.

---

## 📌 Conclusión
La Visión por Computador ha evolucionado de ser un sistema de reglas hechas a mano a un campo dominado por el aprendizaje profundo. Hoy permite desde el filtro de una cámara de smartphone hasta coches autónomos que entienden su entorno en tiempo real. La clave está en entrenar modelos capaces de **generalizar** el conocimiento visual a un mundo infinitamente variado.


## 7️⃣ Librerías Esenciales para Visión por Computador

Para implementar sistemas de visión artificial, los desarrolladores utilizan un ecosistema de librerías que van desde el procesamiento clásico hasta el deep learning de última generación.

### 🟢 Librerías Fundamentales (Open Source)

| Librería | Descripción | Casos de Uso | Enlace |
| :--- | :--- | :--- | :--- |
| **OpenCV (Open Source Computer Vision Library)** | Es la librería estándar de la industria. Contiene más de **2500 algoritmos optimizados** para tareas de visión en tiempo real [citation:5][citation:7]. Soporta C++, Python, Java y está optimizada para ejecución en CPU. | - Detección de rostros y objetos <br>- Procesamiento de imágenes (filtros, transformaciones) <br>- Calibración de cámaras <br>- Seguimiento de movimiento | [OpenCV.org](https://opencv.org) |
| **Scikit-image** | Construida sobre SciPy, es excelente para tareas de procesamiento clásico. Es más fácil de usar que OpenCV para principiantes, pero menos eficiente para tiempo real. | - Segmentación (Superpíxeles, cuencas) <br>- Extracción de características <br>- Restauración de imágenes | [Scikit-image.org](https://scikit-image.org) |
| **PIL / Pillow** | La librería amigable para operaciones básicas de imagen: abrir, manipular, recortar, redimensionar y guardar [citation:8]. | - Preprocesamiento rápido <br>- Conversión de formatos <br>- Generación de thumbnails | [Python-Pillow.org](https://python-pillow.org) |

### 🔵 Librerías de Deep Learning

| Librería | Descripción | Cuándo Usarla |
| :--- | :--- | :--- |
| **PyTorch (Meta/FAIR)** | La favorita en investigación. Ofece gráficos de computación dinámicos, lo que facilita la depuración y experimentación [citation:9]. | - Investigación académica <br>- Modelos personalizados complejos <br>- NLP + Visión (multimodal) |
| **TensorFlow / Keras (Google)** | Más estable en producción. Keras es su API de alto nivel, ideal para principiantes. TensorFlow Serving permite desplegar modelos en servidores. | - Despliegue industrial <br>- Aplicaciones móviles (TensorFlow Lite) <br>- Prototipado rápido con Keras |
| **Create ML (Apple)** | Herramienta de Apple para entrenar modelos en Mac sin necesidad de ser experto en ML. Permite entrenar modelos de *object tracking* para visionOS desde la línea de comandos [citation:2]. | - Aplicaciones para Apple Vision Pro, iOS y macOS. <br>- Flujos de trabajo integrados con Xcode. |

### 🟣 Librerías Especializadas por Tarea

#### 🚀 Modelos Pre-entrenados (SOTA)

- **Ultralytics YOLO (You Only Look Once):** Es el estándar de facto para detección de objetos en tiempo real.
    - **Novedad:** La versión **YOLO26** (lanzada en 2026) elimina la necesidad de post-procesamiento (Non-Maximum Suppression - NMS), lo que lo hace hasta **43% más rápido en CPUs** y nativamente compatible con dispositivos edge [citation:10]. Soporta detección, segmentación, clasificación, pose estimation y tracking.
- **Hugging Face Transformers:** Ofrece acceso a modelos de última generación como **DETR** (Detección con Transformers), **DINO** y **SAM (Segment Anything Model)** de Meta.

#### ⚡ Aceleración GPU

- **CV-CUDA (NVIDIA):** Librería open-source para acelerar pipelines completos de procesamiento de imágenes en la nube usando GPUs [citation:3].

---

## 8️⃣ Pasos a Seguir: Pipeline Completo de un Proyecto

Desarrollar un sistema de visión por computador no es solo entrenar un modelo. Sigue este flujo de trabajo profesional para garantizar el éxito [citation:6][citation:9].

### Fase 1: Definición y Recolección de Datos
1.  **Definir el Objetivo:** ¿Clasificación, detección, segmentación o tracking?
2.  **Recolectar Imágenes:** Captura datos representativos del mundo real.
    - *Ejemplo:* Usar una cámara RTSP para capturar 1 frame por segundo y almacenarlos [citation:6].
    - **Herramientas:** `OpenCV` (`cv2.VideoCapture`) para capturar de cámaras, scripts de descarga web.
3.  **Calidad sobre Cantidad:** Filtra imágenes borrosas, oscuras o corruptas.
    - **Acción:** Ejecutar un análisis de calidad previo (*Quality Analyzer*) para depurar el dataset [citation:9].

### Fase 2: Curación y Etiquetado
4.  **Curación de Datos:** Selecciona el subconjunto más valioso para etiquetar. No necesitas etiquetar todo; a veces con un 25% de las imágenes bien seleccionadas es suficiente [citation:6].
    - **Técnica:** Usar *embeddings* visuales para seleccionar la mayor diversidad posible (Auto-Curate).
5.  **Anotación (Labeling):** Dibuja las cajas (bounding boxes) o máscaras sobre los objetos.
    - **Herramientas:** Superb AI, LabelImg, CVAT, Roboflow.
    - **Optimización:** Usa *Auto-Labeling*: un modelo pre-entrenado etiqueta automáticamente y un humano solo revisa y corrige [citation:6].

### Fase 3: Entrenamiento del Modelo
6.  **Preparar el Entorno:** Configura un entorno aislado.
    - **Herramientas:** Anaconda o Virtualenv.
    - **Comando:**
        ```bash
        conda create -n vision_project python=3.10 -y
        conda activate vision_project
        pip install torch torchvision opencv-python ultralytics [citation:9]
        ```
7.  **Seleccionar Arquitectura:** Elige el modelo base.
    - *Si buscas velocidad:* **YOLO26** (nano o small) [citation:10].
    - *Si buscas precisión:* **DETR** o **Mask2Former**.
8.  **Entrenar (Transfer Learning):** No entrenes desde cero. Usa un modelo pre-entrenado (ej. en ImageNet) y ajústalo (*fine-tuning*) con tus datos.
    - **Configuración:** Define épocas, tamaño de lote (*batch size*) y tasa de aprendizaje.
9.  **Evaluar:** Revisa las métricas (Precisión, Recall, mAP - mean Average Precision). Usa **Matrices de Confusión** y revisa los **Falsos Positivos** de alta confianza para diagnosticar errores [citation:6].

### Fase 4: Despliegue e Inferencia
10. **Exportar el Modelo:** Convierte el modelo al formato óptimo para tu hardware.
    - **Formatos:** ONNX (intercambio universal), TensorRT (NVIDIA), CoreML (Apple), OpenVINO (Intel) [citation:10].
11. **Crear el Pipeline de Inferencia:**
    - **Código de producción:** Un script que recibe imágenes (de una cámara en vivo o archivo), las preprocesa, las pasa al modelo y procesa los resultados.
    - **Ejemplo conceptual:**
        ```python
        # 1. Cargar modelo exportado
        # 2. Capturar frame (cap.read() de OpenCV)
        # 3. Preprocesar (redimensionar, normalizar)
        # 4. Inferencia (modelo.predict(frame))
        # 5. Post-procesar (filtrar por confianza, dibujar bounding boxes)
        # 6. Mostrar o guardar resultado
        ```
12. **Iterar:** Los datos de producción (imágenes con baja confianza) deben realimentar el dataset para una nueva ronda de entrenamiento, mejorando el modelo continuamente (MLOps) [citation:6].

---

##  Ejemplo de Stack Tecnológico (Caso Real)
Basado en un pipeline para detección de objetos en investigación [citation:9]:

- **Gestor de Entorno:** Anaconda
- **Framework DL:** PyTorch (con soporte CUDA)
- **Modelo:** DINO / Grounding DINO (detección por texto)
- **Procesamiento:** OpenCV, Pillow-SIMD (optimizado)
- **Utilidades:** Pandas (para reportes CSV), tqdm (barras de progreso), PyYAML (configuración)
- **Hardware:** GPU NVIDIA (RTX serie 20-40) para aceleración [citation:9].