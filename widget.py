from PySide6.QtWidgets import QWidget

from ui_widget import Ui_widget

class Widget(QWidget, Ui_widget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Upper Tools")
