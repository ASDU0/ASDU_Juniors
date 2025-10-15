import sys
from PyQt6.QtWidgets import QApplication,QMainWindow,QWidget
from PyQt6.QtGui import QIcon

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("mi ventana ASDU")
        self.setGeometry(90,90,700,600)
        #self.setFixedSize(400,400)

        self.setWindowIcon(QIcon("ASDU_VIDEOS/asduLogo2.png"))
        
        central_widget=QWidget()
        central_widget.setStyleSheet("background-color: #e0f7f4;")
        self.setCentralWidget(central_widget)

        menu_bar=self.menuBar()
        menu_bar.addMenu("Archivo")
        menu_bar.addMenu("Ayuda")

        self.statusBar().showMessage("Asdu, derechos reservados")

        self.setWindowOpacity(0.98)

if __name__ == "__main__":
    app=QApplication(sys.argv)
    window=MainWindow()
    window.show()
    sys.exit(app.exec())