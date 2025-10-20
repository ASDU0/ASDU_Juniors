import sys
from PyQt6.QtWidgets import (
    QApplication,QWidget,QVBoxLayout,QPushButton,QLineEdit,
    QSlider,QLabel,QFrame
    )

from PyQt6.QtCore import Qt

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Señales y Slots")
        self.setGeometry(90,90,500,400)

        layout=QVBoxLayout()


        #Pantalla principal
        self.display=QLabel("Pantalla")
        self.display.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.display.setStyleSheet("""
            QLabel{
                    background_color: #1e1e1e;
                    color:white;
                    font-size:28px solid #555;
                    border-radius:8px;
                    padding:15px;
                }
            """)
        layout.addWidget(self.display)

        #Widgets
        self.button=QPushButton("has click")
        self.line=QLineEdit()
        self.line.setPlaceholderText("Escribe aqui ...")
        self.slider = QSlider(Qt.Orientation.Horizontal)
        self.slider.setRange(0,100)

        #Estilos de los Widgets
        self.button.setStyleSheet("font-size: 16px;padding:8px;")
        self.line.setStyleSheet("font-size:16px;padding:5px;")
        self.slider.setStyleSheet("padding:5px;")

        layout.addWidget(self.button)
        layout.addWidget(self.line)
        layout.addWidget(self.slider)

        #Seccion Comentarios
        self.comment=QLabel("Comentarios: ....")
        self.comment.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.comment.setStyleSheet("""
            QLabel{
                font-size:14px;
                color:#333;
                background-color:#f0f0f0;
                border: 1px solid #ccc;
                border-radius: 5px;
                padding: 8px;
            }
        """)

        layout.addWidget(self.comment)
        self.setLayout(layout)

        #Señales y Slots
        self.button.clicked.connect(self.click_boton)
        self.line.textChanged.connect(self.Cambiar_texto)
        self.slider.valueChanged.connect(self.Cambiar_Slider)

    #Slots
    def click_boton(self):
        self.display.setText("Boton Presionado")
        self.comment.setText("Comentario: Se hizo click en el boton")
    
    def Cambiar_texto(self,text):
        self.display.setText(text if text else "Pantalla")
        self.comment.setText(f"Comnetario: Se escribio en la caja de texto: {text}")

    def Cambiar_Slider(self,value):
        self.display.setText(f"Valor del Slider: {value}")
        self.comment.setText(f"Comentario: Se movio el slider a {value}")



if __name__ =="__main__":
    app=QApplication(sys.argv)
    window=MainWindow()
    window.show()
    sys.exit(app.exec())