import sys
from mainWindow import MyWindow
from PySide6.QtWidgets import QApplication
from display import Display
from info import Info
from variables import ICON_PATH
from styles import setStyle
from buttons import ButtonGrid
from PySide6.QtGui import QIcon


if __name__ == '__main__':

    app = QApplication(sys.argv)
    setStyle()
    window = MyWindow()
    icon = QIcon(str(ICON_PATH))

    info = Info()
    window.addWidgetToLy(info)

    display = Display()
    window.addWidgetToLy(display)

    buttonGrid = ButtonGrid(display, info)
    window.ly.addLayout(buttonGrid)

    window.setWindowIcon(icon)
    app.setWindowIcon(icon)
    window.show()
    app.exec()
