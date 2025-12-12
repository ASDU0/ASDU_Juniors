import sys
import mysql.connector
from mysql.connector import Error
from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton,
    QVBoxLayout, QHBoxLayout, QTableWidget, QTableWidgetItem, QMessageBox
)

class VentanaDatos(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Conexión y Visualización MySQL")
        self.setGeometry(200, 200, 700, 500)

        # Campos de conexión
        self.input_host = QLineEdit("localhost")
        self.input_port = QLineEdit("3307")
        self.input_user = QLineEdit("root")
        self.input_password = QLineEdit()
        self.input_password.setEchoMode(QLineEdit.EchoMode.Password)
        self.input_db = QLineEdit("test")

        # Botones
        self.btn_conectar = QPushButton("Conectar y Mostrar Datos")
        self.btn_conectar.clicked.connect(self.cargar_datos)

        # Tabla
        self.tabla = QTableWidget()
        self.tabla.setColumnCount(4)
        self.tabla.setHorizontalHeaderLabels(["ID", "Nombre", "Cargo", "Salario"])

        # Layout superior
        form_layout = QHBoxLayout()
        for w in [self.input_host, self.input_port, self.input_user, self.input_db]:
            form_layout.addWidget(w)
        form_layout.addWidget(self.btn_conectar)

        # Layout principal
        layout = QVBoxLayout()
        layout.addLayout(form_layout)
        layout.addWidget(self.tabla)
        self.setLayout(layout)

    def cargar_datos(self):
        """Conecta a MySQL y carga los registros de la tabla empleados"""
        try:
            conexion = mysql.connector.connect(
                host=self.input_host.text(),
                port=self.input_port.text(),
                user=self.input_user.text(),
                password=self.input_password.text(),
                database=self.input_db.text()
            )

            if conexion.is_connected():
                cursor = conexion.cursor()
                cursor.execute("SELECT * FROM empleados")
                resultados = cursor.fetchall()

                self.tabla.setRowCount(len(resultados))
                for fila, datos in enumerate(resultados):
                    for columna, valor in enumerate(datos):
                        self.tabla.setItem(fila, columna, QTableWidgetItem(str(valor)))

                QMessageBox.information(self, "Éxito", "Datos cargados correctamente ✅")

        except Error as e:
            QMessageBox.critical(self, "Error", f"No se pudo conectar o leer datos:\n{e}")

        finally:
            if 'conexion' in locals() and conexion.is_connected():
                conexion.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaDatos()
    ventana.show()
    sys.exit(app.exec())
