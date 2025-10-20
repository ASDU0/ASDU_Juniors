import sys
import random
import time
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout,
    QTableWidget, QTableWidgetItem, QPushButton, QLabel
)
from PyQt6.QtCore import QThread, pyqtSignal


# === Hilo que simula una API de precios ===
class HiloDatos(QThread):
    datos_actualizados = pyqtSignal(list)
    detenido = False

    def run(self):
        criptos = ["Bitcoin", "Ethereum", "Litecoin", "Dogecoin", "Solana"]
        while not self.detenido:
            time.sleep(2)  # Simula retardo de red
            nuevos_datos = [
                (c, round(random.uniform(1000, 50000), 2)) for c in criptos
            ]
            self.datos_actualizados.emit(nuevos_datos)

    def detener(self):
        self.detenido = True


# === Ventana principal ===
class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Actualización en tiempo real con hilos")
        self.resize(500, 300)

        self.label_estado = QLabel("Presiona 'Iniciar' para comenzar la actualización.")
        self.tabla = QTableWidget(0, 2)
        self.tabla.setHorizontalHeaderLabels(["Criptomoneda", "Precio (USD)"])
        self.boton_iniciar = QPushButton("Iniciar actualización")
        self.boton_detener = QPushButton("Detener")
        self.boton_detener.setEnabled(False)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.label_estado)
        layout.addWidget(self.tabla)
        layout.addWidget(self.boton_iniciar)
        layout.addWidget(self.boton_detener)

        contenedor = QWidget()
        contenedor.setLayout(layout)
        self.setCentralWidget(contenedor)

        # Conexiones
        self.boton_iniciar.clicked.connect(self.iniciar_hilo)
        self.boton_detener.clicked.connect(self.detener_hilo)

        self.hilo_datos = None

    def iniciar_hilo(self):
        self.label_estado.setText("Obteniendo datos...")
        self.hilo_datos = HiloDatos()
        self.hilo_datos.datos_actualizados.connect(self.mostrar_datos)
        self.hilo_datos.start()
        self.boton_iniciar.setEnabled(False)
        self.boton_detener.setEnabled(True)

    def mostrar_datos(self, datos):
        self.tabla.setRowCount(len(datos))
        for fila, (nombre, precio) in enumerate(datos):
            self.tabla.setItem(fila, 0, QTableWidgetItem(nombre))
            self.tabla.setItem(fila, 1, QTableWidgetItem(str(precio)))
        self.label_estado.setText("Datos actualizados correctamente.")

    def detener_hilo(self):
        if self.hilo_datos:
            self.hilo_datos.detener()
            self.hilo_datos.wait()
        self.label_estado.setText("Actualización detenida.")
        self.boton_iniciar.setEnabled(True)
        self.boton_detener.setEnabled(False)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    ventana.show()
    sys.exit(app.exec())
