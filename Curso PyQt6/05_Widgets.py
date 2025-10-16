import sys
from PyQt6.QtWidgets import(QApplication,QMainWindow,QWidget,
                            QLabel,QPushButton,QLineEdit,
                            QTextEdit,QComboBox,QCheckBox,
                            QRadioButton,QSlider,QProgressBar,
                            QVBoxLayout,QHBoxLayout)
from PyQt6.QtCore import Qt
from PyQt6 import QtGui

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Widgets en PyQt6")
        self.setGeometry(100,100,500,600)

        #widget Central
        central_widget=QWidget()
        self.setCentralWidget(central_widget)

        #Layout Principal
        main_Layout=QVBoxLayout()
        central_widget.setLayout(main_Layout)

        #Label -> Texto
        label_texto=QLabel("Widgets en PyQt6")
        label_texto.setStyleSheet("font-size: 20px; font-weight: bold;")
        main_Layout.addWidget(label_texto)

        #label -> Imagen
        label_imagen=QLabel()
        label_imagen.setPixmap(QtGui.QPixmap("asduLogo2.png"))
        label_imagen.setScaledContents(True)
        label_imagen.setFixedSize(100,100)
        main_Layout.addWidget(label_imagen)

        #QLineEdit -> Texto Corto
        line_edit=QLineEdit()
        line_edit.setPlaceholderText("Esccribe algo aqui")
        main_Layout.addWidget(line_edit)

        #QtexEdit -> Entrada multilinea
        text_edit=QTextEdit()
        text_edit.setPlaceholderText("Escribe un comentario aqui")
        main_Layout.addWidget(text_edit)

        #ComboBox -> lista Desplegable
        Combo=QComboBox()
        Combo.addItems(["Opcion 1","Opcion 2","Opcion 3"])
        main_Layout.addWidget(Combo)

        #CheckBox 
        Check=QCheckBox("Acepto Terminos y Condiciones")
        main_Layout.addWidget(Check)

        #RasioButton
        Radio_Layout=QHBoxLayout()
        radio1=QRadioButton("Masculino")
        radio2=QRadioButton("Femenino")
        Radio_Layout.addWidget(radio1)
        Radio_Layout.addWidget(radio2)
        main_Layout.addLayout(Radio_Layout)

        #Slider
        Slider=QSlider(Qt.Orientation.Horizontal)
        Slider.setMinimum(0)
        Slider.setMaximum(100)
        Slider.setValue(0)
        main_Layout.addWidget(Slider)

        #ProgressBar
        ProhressBar=QProgressBar()
        ProhressBar.setValue(0)
        main_Layout.addWidget(ProhressBar)

        #PushButton
        boton=QPushButton("Mostrar Datos")
        main_Layout.addWidget(boton)

if __name__ == "__main__":
    app=QApplication(sys.argv)
    window=MainWindow()
    window.show()
    sys.exit(app.exec())