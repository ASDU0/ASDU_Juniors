import sys
import time
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QProgressBar, QPushButton,
    QVBoxLayout, QHBoxLayout, QWidget, QLabel, QTableWidget,
    QTableWidgetItem, QHeaderView
)
from PyQt6.QtCore import Qt, QThread, pyqtSignal
from threading import Event




# Hilo para simular la descarga de un archivo
class HiloDescarga(QThread):
    progreso = pyqtSignal(int, int)   # (id, progreso)
    completado = pyqtSignal(int)      # id del archivo

    def __init__(self, id_descarga, pausa_event):
        super().__init__()
        self.id_descarga = id_descarga
        self.pausa_event = pausa_event
        self._is_running = True

    def run(self):
        progreso = 0
        while progreso <= 100 and self._is_running:
            if not self.pausa_event.is_set():
                self.pausa_event.wait()  # Espera si está en pausa
            time.sleep(0.05)
            progreso += 1
            self.progreso.emit(self.id_descarga, progreso)
        if self._is_running:
            self.completado.emit(self.id_descarga)

    def detener(self):
        self._is_running = False
        self.pausa_event.set()  # Evita bloqueo


# Ventana principal
class VentanaDescargas(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gestor de Descargas - PyQt6")
        self.resize(600, 400)

        # Tabla de descargas
        self.tabla = QTableWidget(3, 2)
        self.tabla.setHorizontalHeaderLabels(["Archivo", "Progreso"])
        self.tabla.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)
        self.tabla.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeMode.Stretch)
        self.tabla.verticalHeader().setVisible(False)
        self.tabla.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)

        for i in range(3):
            self.tabla.setItem(i, 0, QTableWidgetItem(f"Archivo_{i+1}.zip"))
            barra = QProgressBar()
            barra.setValue(0)
            self.tabla.setCellWidget(i, 1, barra)

        # Barra de progreso total
        self.label_general = QLabel("Progreso total:")
        self.barra_general = QProgressBar()
        self.barra_general.setValue(0)

        # Botones de control
        self.btn_iniciar = QPushButton("Iniciar descargas")
        self.btn_pausar = QPushButton("Pausar")
        self.btn_reanudar = QPushButton("Reanudar")
        self.btn_detener = QPushButton("Detener")

        self.btn_pausar.setEnabled(False)
        self.btn_reanudar.setEnabled(False)
        self.btn_detener.setEnabled(False)

        self.btn_iniciar.clicked.connect(self.iniciar_descargas)
        self.btn_pausar.clicked.connect(self.pausar_descargas)
        self.btn_reanudar.clicked.connect(self.reanudar_descargas)
        self.btn_detener.clicked.connect(self.detener_descargas)

        # Layouts
        controles = QHBoxLayout()
        controles.addWidget(self.btn_iniciar)
        controles.addWidget(self.btn_pausar)
        controles.addWidget(self.btn_reanudar)
        controles.addWidget(self.btn_detener)

        layout = QVBoxLayout()
        layout.addWidget(self.tabla)
        layout.addWidget(self.label_general)
        layout.addWidget(self.barra_general)
        layout.addLayout(controles)

        contenedor = QWidget()
        contenedor.setLayout(layout)
        self.setCentralWidget(contenedor)

        # Variables
        self.hilos = []
        self.pausa_event = Event()
        self.pausa_event.set()
        self.descargas_completadas = 0

    def iniciar_descargas(self):
        self.btn_iniciar.setEnabled(False)
        self.btn_pausar.setEnabled(True)
        self.btn_detener.setEnabled(True)

        self.hilos.clear()
        self.descargas_completadas = 0

        for i in range(3):
            hilo = HiloDescarga(i, self.pausa_event)
            hilo.progreso.connect(self.actualizar_progreso)
            hilo.completado.connect(self.finalizar_descarga)
            self.hilos.append(hilo)
            hilo.start()

    def pausar_descargas(self):
        self.pausa_event.clear()
        self.btn_pausar.setEnabled(False)
        self.btn_reanudar.setEnabled(True)

    def reanudar_descargas(self):
        self.pausa_event.set()
        self.btn_pausar.setEnabled(True)
        self.btn_reanudar.setEnabled(False)

    def detener_descargas(self):
        for hilo in self.hilos:
            hilo.detener()
        self.hilos.clear()
        self.barra_general.setValue(0)
        self.btn_iniciar.setEnabled(True)
        self.btn_pausar.setEnabled(False)
        self.btn_reanudar.setEnabled(False)
        self.btn_detener.setEnabled(False)

    def actualizar_progreso(self, id_descarga, progreso):
        barra = self.tabla.cellWidget(id_descarga, 1)
        barra.setValue(progreso)
        total = sum(self.tabla.cellWidget(i, 1).value() for i in range(3)) // 3
        self.barra_general.setValue(total)

    def finalizar_descarga(self, id_descarga):
        self.descargas_completadas += 1
        if self.descargas_completadas == 3:
            self.btn_iniciar.setEnabled(True)
            self.btn_pausar.setEnabled(False)
            self.btn_reanudar.setEnabled(False)
            self.btn_detener.setEnabled(False)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaDescargas()
    ventana.show()
    sys.exit(app.exec())
