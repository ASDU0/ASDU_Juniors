import sys 
from PyQt6.QtWidgets import QApplication,QLabel

app=QApplication(sys.argv)
label=QLabel("Hola Mundo,Somos ASDU :)")
label.show()
sys.exit(app.exec())