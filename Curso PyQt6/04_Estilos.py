import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QVBoxLayout
from PyQt6.QtGui import QPixmap, QFont, QColor
from PyQt6.QtWidgets import QGraphicsDropShadowEffect


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Estilos en QLabel")
        self.setGeometry(100, 100, 450, 600)

        # Contenedor
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        # Texto con borde y fondo
        label_borde = QLabel("Label con borde y fondo")
        label_borde.setStyleSheet("""
            QLabel {
                background-color: #e3f2fd;
                border: 2px solid #1976d2;
                border-radius: 8px;
                color: #0d47a1;
                padding: 8px;
                font-size: 14px;
            }
        """)
        layout.addWidget(label_borde)

        # Texto con sombra (usando QGraphicsDropShadowEffect)
        label_sombra = QLabel("Label con sombra")
        label_sombra.setStyleSheet("font-size: 16px; background-color: brown; padding: 8px;")
        sombra = QGraphicsDropShadowEffect()
        sombra.setBlurRadius(15)
        sombra.setXOffset(3)
        sombra.setYOffset(3)
        sombra.setColor(QColor(0, 0, 0, 160))
        label_sombra.setGraphicsEffect(sombra)
        layout.addWidget(label_sombra)

        # Imagen con borde redondeado
        label_imagen = QLabel()
        pixmap = QPixmap("ASDU_VIDEOS/asduLogo2.png")  
        label_imagen.setPixmap(pixmap)
        label_imagen.setScaledContents(True)
        label_imagen.setFixedSize(200, 150)
        label_imagen.setStyleSheet("""
            QLabel {
                border: 3px solid #4caf50;
                border-radius: 10px;
                padding: 2px;
                background-color: #f1f8e9;
            }
        """)
        layout.addWidget(label_imagen)

        #Label con estilo tipo "etiqueta destacada"
        label_resaltado = QLabel("Etiqueta destacada")
        label_resaltado.setStyleSheet("""
            QLabel {
                background-color: #ffeb3b;
                color: #000;
                border: 2px dashed #f57f17;
                font-weight: bold;
                padding: 10px;
                font-size: 16px;
            }
        """)
        layout.addWidget(label_resaltado)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
