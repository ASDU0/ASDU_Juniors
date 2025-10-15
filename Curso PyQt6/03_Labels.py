import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QVBoxLayout
from PyQt6.QtGui import QPixmap

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ejemplos de QLabel")
        self.setGeometry(100, 100, 400, 500)

        # Contenedor central
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        # 1️Texto simple
        label_texto = QLabel("Esto es un QLabel con texto simple")
        layout.addWidget(label_texto)

        # Texto con HTML (formato)
        label_html = QLabel("<h2 style='color: blue;'>Texto con <i>HTML</i> y estilo</h2>")
        layout.addWidget(label_html)

        #Imagen
        label_imagen = QLabel()
        pixmap = QPixmap("ASDU_VIDEOS/asduLogo2.png")  
        label_imagen.setPixmap(pixmap)
        label_imagen.setScaledContents(True)  # Ajusta la imagen al tamaño del QLabel
        label_imagen.setFixedSize(200, 150)   # Tamaño fijo para mostrar la imagen
        layout.addWidget(label_imagen)

        #Enlace clicable
        label_enlace = QLabel('<a href="https://www.python.org">Ir a Python.org</a>')
        label_enlace.setOpenExternalLinks(True)  # Permite abrir el enlace en el navegador
        layout.addWidget(label_enlace)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
