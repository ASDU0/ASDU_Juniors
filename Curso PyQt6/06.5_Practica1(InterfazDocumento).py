import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QTextEdit, QToolBar, QTabWidget,
    QWidget, QVBoxLayout, QToolButton, QLabel, QComboBox, QSpinBox,
    QDockWidget, QListWidget, QStatusBar, QMenuBar
)
from PyQt6.QtGui import QIcon, QAction
from PyQt6.QtCore import Qt, QSize


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Interfaz Demo")
        self.setGeometry(100, 100, 1000, 700)
        self._create_menu_bar()
        self._create_tool_bar()
        self._create_tab_widget()
        self._create_side_panel()
        self._create_status_bar()

    def _create_menu_bar(self):
        menu_bar = QMenuBar(self)
        self.setMenuBar(menu_bar)

        archivo_menu = menu_bar.addMenu("Archivo")
        editar_menu = menu_bar.addMenu("Editar")
        ver_menu = menu_bar.addMenu("Ver")
        ayuda_menu = menu_bar.addMenu("Ayuda")

    def _create_tool_bar(self):
        toolbar = QToolBar("Ribbon")
        toolbar.setIconSize(QSize(20, 20))
        self.addToolBar(Qt.ToolBarArea.TopToolBarArea, toolbar)

        action_new = QAction(QIcon.fromTheme("document-new"), "Nuevo", self)
        action_open = QAction(QIcon.fromTheme("document-open"), "Abrir", self)
        action_save = QAction(QIcon.fromTheme("document-save"), "Guardar", self)

        toolbar.addAction(action_new)
        toolbar.addAction(action_open)
        toolbar.addAction(action_save)
        toolbar.addSeparator()

        font_label = QLabel("Fuente:")
        toolbar.addWidget(font_label)

        font_combo = QComboBox()
        font_combo.addItems(["Arial", "Calibri", "Times New Roman"])
        toolbar.addWidget(font_combo)

        size_label = QLabel("Tamaño:")
        toolbar.addWidget(size_label)

        font_size = QSpinBox()
        font_size.setRange(8, 72)
        font_size.setValue(12)
        toolbar.addWidget(font_size)

    def _create_tab_widget(self):
        tabs = QTabWidget()
        tabs.addTab(QTextEdit(), "Documento 1")
        tabs.addTab(QTextEdit(), "Documento 2")
        self.setCentralWidget(tabs)

    def _create_side_panel(self):
        dock = QDockWidget("Panel lateral", self)
        dock.setAllowedAreas(Qt.DockWidgetArea.LeftDockWidgetArea | Qt.DockWidgetArea.RightDockWidgetArea)
        list_widget = QListWidget()
        list_widget.addItems(["Explorador", "Propiedades", "Comentarios"])
        dock.setWidget(list_widget)
        self.addDockWidget(Qt.DockWidgetArea.LeftDockWidgetArea, dock)

    def _create_status_bar(self):
        status_bar = QStatusBar()
        status_bar.showMessage("Listo ✔️")
        self.setStatusBar(status_bar)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
