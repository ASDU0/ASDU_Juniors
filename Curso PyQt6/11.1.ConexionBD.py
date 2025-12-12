import sys
import mysql.connector
from mysql.connector import Error
from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit,
    QPushButton, QVBoxLayout, QMessageBox
)

class VentanaConexion(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Conexión a MySQL")
        self.setGeometry(200, 200, 400, 300)

        # Widgets
        self.label_host = QLabel("Host:")
        self.input_host = QLineEdit("localhost")

        self.label_port = QLabel("Puerto:")
        self.input_port = QLineEdit("3307")

        self.label_user = QLabel("Usuario:")
        self.input_user = QLineEdit("root")

        self.label_password = QLabel("Contraseña:")
        self.input_password = QLineEdit()
        self.input_password.setEchoMode(QLineEdit.EchoMode.Password)

        self.label_db = QLabel("Base de datos:")
        self.input_db = QLineEdit("pruebas")

        self.boton_conectar = QPushButton("Probar conexión")
        self.boton_conectar.clicked.connect(self.probar_conexion)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.label_host)
        layout.addWidget(self.input_host)
        layout.addWidget(self.label_port)
        layout.addWidget(self.input_port)
        layout.addWidget(self.label_user)
        layout.addWidget(self.input_user)
        layout.addWidget(self.label_password)
        layout.addWidget(self.input_password)
        layout.addWidget(self.label_db)
        layout.addWidget(self.input_db)
        layout.addWidget(self.boton_conectar)

        self.setLayout(layout)

    def probar_conexion(self):
        host = self.input_host.text()
        port = self.input_port.text()
        user = self.input_user.text()
        password = self.input_password.text()
        database = self.input_db.text()

        try:
            conexion = mysql.connector.connect(
                host=host,
                port=port,
                user=user,
                password=password,
                database=database
            )
            if conexion.is_connected():
                info = conexion.server_info
                QMessageBox.information(self, "Éxito",
                    f"Conectado correctamente a MySQL\nVersión del servidor: {info}")
        except Error as e:
            QMessageBox.critical(self, "Error", f"No se pudo conectar:\n{e}")
        finally:
            if 'conexion' in locals() and conexion.is_connected():
                conexion.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaConexion()
    ventana.show()
    sys.exit(app.exec())
