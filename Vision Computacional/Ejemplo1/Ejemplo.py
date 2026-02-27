# ============================================
# IMPORTACIÓN DE LIBRERÍAS NECESARIAS
# ============================================

import tensorflow as tf                    # Librería principal de deep learning
from tensorflow.keras import layers, models  # Módulos para crear redes neuronales
import numpy as np                          # Para operaciones matemáticas y arrays
import tkinter as tk                         # Para crear la interfaz gráfica
from PIL import Image, ImageDraw, ImageOps   # Para manipular imágenes (dibujar, redimensionar, invertir)

# ============================================
# PARTE 1: CARGAR Y ENTRENAR EL MODELO MNIST
# ============================================

# Cargar el dataset MNIST (dígitos escritos a mano)
# MNIST contiene 70,000 imágenes de dígitos (0-9) de 28x28 píxeles
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()

# Normalizar los píxeles: convertir valores de 0-255 a 0-1
# Esto ayuda a que la red neuronal aprenda mejor y más rápido
x_train = x_train / 255.0
x_test = x_test / 255.0

# Agregar una dimensión extra para el canal (escala de grises = 1 canal)
# Las imágenes originales son 28x28, pero Keras espera (alto, ancho, canales)
x_train = x_train.reshape(-1, 28, 28, 1)  # -1 significa "el tamaño que sea"
x_test = x_test.reshape(-1, 28, 28, 1)    # 1 = un solo canal (blanco y negro)

# ============================================
# CREACIÓN DE LA RED NEURONAL CONVOLUCIONAL (CNN)
# ============================================

model = models.Sequential([                # Sequential = capas en secuencia
    
    # Primera capa convolucional
    layers.Conv2D(32, (3,3), activation='relu', input_shape=(28,28,1)),
    # 32 filtros de 3x3, detectan características básicas (bordes, esquinas)
    # input_shape define el tamaño de entrada: 28x28 con 1 canal
    
    # Capa de pooling: reduce el tamaño a la mitad (14x14)
    # Mantiene las características importantes y reduce el cómputo
    layers.MaxPooling2D(2,2),
    
    # Segunda capa convolucional
    layers.Conv2D(64, (3,3), activation='relu'),
    # 64 filtros, detectan características más complejas
    
    # Segunda capa de pooling: reduce a 7x7
    layers.MaxPooling2D(2,2),
    
    # Aplanar: convierte la matriz 2D en un vector 1D
    # De 7x7x64 = 3136 valores en una sola fila
    layers.Flatten(),
    
    # Capa densa (totalmente conectada) con 128 neuronas
    # Aprende a combinar las características detectadas
    layers.Dense(128, activation='relu'),
    
    # Capa de salida: 10 neuronas (una por cada dígito 0-9)
    # Softmax convierte las salidas en probabilidades que suman 1
    layers.Dense(10, activation='softmax')
])

# ============================================
# COMPILACIÓN DEL MODELO
# ============================================

model.compile(
    optimizer='adam',                    # Algoritmo de optimización (el más usado)
    loss='sparse_categorical_crossentropy',  # Función de pérdida para clasificación
    metrics=['accuracy']                  # Métrica para evaluar el modelo
)

print("Entrenando modelo...")

# Entrenar el modelo con los datos
# epochs = 3: pasar todo el dataset 3 veces
# verbose=1: mostrar barra de progreso
model.fit(x_train, y_train, epochs=3, verbose=1)

print("Modelo listo ✅")

# ============================================
# PARTE 2: INTERFAZ GRÁFICA PARA DIBUJAR
# ============================================

class App:
    """Aplicación para dibujar números y predecirlos con el modelo MNIST"""
    
    def __init__(self, master):
        """Constructor: inicializa la interfaz y variables"""
        self.master = master
        self.master.title("Dibuja un número (0-9)")
        
        # Canvas (lienzo) de 280x280 (10 veces más grande que 28x28)
        # Así es más fácil dibujar con el mouse
        self.canvas = tk.Canvas(master, width=280, height=280, bg="white")
        self.canvas.pack()
        
        # Botones y etiquetas
        self.button_predict = tk.Button(master, text="Predecir", command=self.predict)
        self.button_predict.pack()
        
        self.button_clear = tk.Button(master, text="Limpiar", command=self.clear)
        self.button_clear.pack()
        
        self.label_result = tk.Label(master, text="", font=("Helvetica", 18))
        self.label_result.pack()
        
        # Imagen en memoria para procesar (mismo tamaño que el canvas)
        # 'L' = modo escala de grises, color 255 = blanco
        self.image = Image.new("L", (280,280), color=255)
        self.draw = ImageDraw.Draw(self.image)
        
        # Vincular el movimiento del mouse con el método paint
        # <B1-Motion> = botón izquierdo presionado + movimiento
        self.canvas.bind("<B1-Motion>", self.paint)
    
    def paint(self, event):
        """Dibuja un círculo negro donde pasa el mouse"""
        # Crear un círculo de 16x16 píxeles (radio 8)
        x1, y1 = (event.x - 8), (event.y - 8)
        x2, y2 = (event.x + 8), (event.y + 8)
        
        # Dibujar en el canvas (visual)
        self.canvas.create_oval(x1, y1, x2, y2, fill="black")
        
        # Dibujar en la imagen (memoria) - fill=0 = negro
        self.draw.ellipse([x1, y1, x2, y2], fill=0)
    
    def clear(self):
        """Limpia el canvas y la imagen"""
        self.canvas.delete("all")
        self.draw.rectangle([0, 0, 280, 280], fill=255)  # Rectángulo blanco
        self.label_result.config(text="")
    
    def predict(self):
        """Procesa el dibujo y predice el número"""
        
        # PASO 1: Redimensionar la imagen de 280x280 a 28x28
        # El modelo fue entrenado con 28x28, debemos igualar ese tamaño
        img = self.image.resize((28,28))
        
        # PASO 2: Invertir colores
        # MNIST tiene fondo negro y dígito blanco
        # Nuestro canvas tiene fondo blanco y trazo negro
        # Invertir es necesario para que coincida con el entrenamiento
        img = ImageOps.invert(img)
        
        # PASO 3: Convertir imagen a array numpy y normalizar
        img_array = np.array(img) / 255.0
        
        # PASO 4: Redimensionar para el modelo (batch, alto, ancho, canales)
        # 1 = batch size (una sola imagen)
        img_array = img_array.reshape(1, 28, 28, 1)
        
        # PASO 5: Hacer la predicción
        prediction = model.predict(img_array)
        
        # PASO 6: Obtener el número con mayor probabilidad
        number = np.argmax(prediction)  # Índice del valor máximo
        confidence = np.max(prediction) * 100  # Probabilidad en porcentaje
        
        # Mostrar resultado
        self.label_result.config(
            text=f"Predicción: {number} ({confidence:.2f}%)"
        )

# ============================================
# PARTE 3: EJECUTAR LA APLICACIÓN
# ============================================

# Crear la ventana principal de tkinter
root = tk.Tk()

# Crear una instancia de nuestra aplicación
app = App(root)

# Iniciar el bucle principal de la interfaz
# Mantiene la ventana abierta y responde a eventos (clicks, dibujo)
root.mainloop()