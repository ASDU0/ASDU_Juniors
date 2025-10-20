import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QTabWidget, QVBoxLayout,
    QHBoxLayout, QLineEdit, QPushButton, QListView,
    QTableView, QTreeView, QLabel, QMainWindow
)
from PyQt6.QtGui import QStandardItemModel, QStandardItem
from PyQt6.QtCore import Qt


class ModelViewDemo(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Model-View Programming en PyQt6")
        self.resize(800, 500)

        tabs = QTabWidget()
        tabs.addTab(self.tab_lista(), "Lista")
        tabs.addTab(self.tab_tabla(), "Tabla")
        tabs.addTab(self.tab_arbol(), "Árbol")

        self.setCentralWidget(tabs)

    # ----------------------------------------
    #TAB 1 - QListView
    # ----------------------------------------
    def tab_lista(self):
        tab = QWidget()
        layout = QVBoxLayout()

        self.input = QLineEdit()
        self.input.setPlaceholderText("Escribe y presiona 'Agregar'")
        layout.addWidget(self.input)

        btns = QHBoxLayout()
        self.btn_add = QPushButton("➕ Agregar")
        self.btn_del = QPushButton("🗑️ Eliminar")
        btns.addWidget(self.btn_add)
        btns.addWidget(self.btn_del)
        layout.addLayout(btns)

        self.view_list = QListView()
        layout.addWidget(self.view_list)

        self.model_list = QStandardItemModel()
        self.view_list.setModel(self.model_list)

        # señales
        self.btn_add.clicked.connect(self.add_item)
        self.btn_del.clicked.connect(self.remove_item)

        tab.setLayout(layout)
        return tab

    def add_item(self):
        text = self.input.text().strip()
        if text:
            item = QStandardItem(text)
            item.setEditable(False)
            self.model_list.appendRow(item)
            self.input.clear()

    def remove_item(self):
        index = self.view_list.currentIndex()
        if index.isValid():
            self.model_list.removeRow(index.row())

    # ----------------------------------------
    # TAB 2 - QTableView
    # ----------------------------------------
    def tab_tabla(self):
        tab = QWidget()
        layout = QVBoxLayout()

        self.table = QTableView()
        layout.addWidget(self.table)

        self.btn_add_row = QPushButton("➕ Agregar fila")
        layout.addWidget(self.btn_add_row)

        self.model_table = QStandardItemModel(0, 3)
        self.model_table.setHorizontalHeaderLabels(["Nombre", "Edad", "País"])
        self.table.setModel(self.model_table)

        self.btn_add_row.clicked.connect(self.add_row)

        tab.setLayout(layout)
        return tab

    def add_row(self):
        datos = ["Carlos", "22", "México"]
        fila = [QStandardItem(d) for d in datos]
        self.model_table.appendRow(fila)

    # ----------------------------------------
    # TAB 3 - QTreeView
    # ----------------------------------------
    def tab_arbol(self):
        tab = QWidget()
        layout = QVBoxLayout()

        self.tree = QTreeView()
        layout.addWidget(self.tree)

        self.model_tree = QStandardItemModel()
        self.model_tree.setHorizontalHeaderLabels(["Estructura de Carpetas"])

        root = self.model_tree.invisibleRootItem()

        carpeta1 = QStandardItem("📁Proyectos")
        carpeta1.appendRow(QStandardItem("📄 app.py"))
        carpeta1.appendRow(QStandardItem("📄 main.cpp"))

        carpeta2 = QStandardItem("📁 Recursos")
        carpeta2.appendRow(QStandardItem("🖼️ logo.png"))
        carpeta2.appendRow(QStandardItem("🎵 sonido.mp3"))

        root.appendRow(carpeta1)
        root.appendRow(carpeta2)

        self.tree.setModel(self.model_tree)
        self.tree.expandAll()

        tab.setLayout(layout)
        return tab


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ModelViewDemo()
    window.show()
    sys.exit(app.exec())
