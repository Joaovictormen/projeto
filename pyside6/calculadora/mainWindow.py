from PySide6.QtWidgets import (QMainWindow, QWidget, QVBoxLayout)


class MyWindow(QMainWindow):
    def __init__(self, parent: QWidget | None = None, *args, **kwargs) -> None:
        super().__init__(parent, *args, **kwargs)

        self.cw = QWidget()
        self.setCentralWidget(self.cw)

        self.ly = QVBoxLayout()
        self.cw.setLayout(self.ly)
        self.setWindowTitle('Calculadora')

    def addWidgetToLy(self, widget):
        self.ly.addWidget(widget)
