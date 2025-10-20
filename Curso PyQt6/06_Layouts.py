import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QFormLayout,
    QLabel, QLineEdit, QPushButton, QComboBox
)
from PyQt6.QtCore import Qt

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Layouts")
        self.setGeometry(100, 100, 500, 500)

        #Estilos modernos (QSS)
        self.setStyleSheet("""
            QWidget {
                background-color: #f0f2f5;
                font-family: 'Segoe UI', sans-serif;
                font-size: 14px;
            }

            QLabel {
                color: #333;
                font-weight: 500;
            }

            QLineEdit, QComboBox {
                background-color: white;
                border: 1px solid #ccc;
                border-radius: 6px;
                padding: 6px;
            }
            QLineEdit:focus, QComboBox:focus {
                border: 1px solid #0078d4;
                box-shadow: 0 0 5px #0078d4;
            }

            QPushButton {
                background-color: #0078d4;
                color: white;
                border: none;
                border-radius: 6px;
                padding: 8px 16px;
                font-weight: 600;
            }
            QPushButton:hover {
                background-color: #005ea2;
            }
            QPushButton:pressed {
                background-color: #004578;
            }
        """)

        #Layout principal vertical
        main_layout = QVBoxLayout()
        main_layout.setSpacing(20)  # espacio entre secciones
        main_layout.setContentsMargins(30, 30, 30, 30)

        #Formulario (QFormLayout)
        form_layout = QFormLayout()
        form_layout.setLabelAlignment(Qt.AlignmentFlag.AlignRight)

        name_input = QLineEdit()
        email_input = QLineEdit()
        role_combo = QComboBox()
        role_combo.addItems(["Estudiante", "Profesor", "Otro"])

        form_layout.addRow("Nombre:", name_input)
        form_layout.addRow("Email:", email_input)
        form_layout.addRow("Rol:", role_combo)

        main_layout.addLayout(form_layout)

        #Sección con QGridLayout
        grid_layout = QGridLayout()
        grid_layout.setSpacing(10)

        grid_layout.addWidget(self._label_box("Celda 0,0"), 0, 0)
        grid_layout.addWidget(self._label_box("Celda 0,1"), 0, 1)
        grid_layout.addWidget(self._label_box("Celda 1,0"), 1, 0)
        grid_layout.addWidget(self._label_box("Celda 1,1"), 1, 1)

        main_layout.addLayout(grid_layout)

        #Botones (QHBoxLayout)
        button_layout = QHBoxLayout()
        button_layout.addStretch()  # empuja los botones a la derecha
        button_layout.addWidget(QPushButton("Aceptar"))
        button_layout.addWidget(QPushButton("Cancelar"))
        main_layout.addLayout(button_layout)

        # Asignar layout principal
        self.setLayout(main_layout)

    def _label_box(self, text):
        """Helper para crear labels de la cuadrícula con estilo."""
        lbl = QLabel(text)
        lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
        lbl.setStyleSheet("""
            QLabel {
                background-color: white;
                border: 1px solid #ccc;
                border-radius: 6px;
                padding: 10px;
            }
        """)
        return lbl


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
