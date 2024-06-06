import math
from PySide6.QtWidgets import QPushButton, QGridLayout
from variables import MEDIUM_FONT
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from info import Info
    from display import Display

from valida_num import isNumber, isEmpty, isNumOrDot


class Button(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setStyle()

    def setStyle(self):
        font = self.font()
        font.setPixelSize(MEDIUM_FONT)
        self.setFont(font)


class ButtonGrid(QGridLayout):
    def __init__(self, display: 'Display', info: 'Info', *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._grid_mask = [
            ['C', '◀', '^', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['',  '0', '.', '='],
        ]
        self.display = display
        self.info = info
        self._equation = ''
        self.equation = None
        self.left = None
        self.right = None
        self.op = None
        self.makeGrid()

    @property
    def equation(self):
        return self._equation

    @equation.setter
    def equation(self, value):
        self._equation = value
        self.info.setText(value)

    def makeGrid(self):
        self.display.eqPressed.connect(self.equal)
        self.display.delPressed.connect(self.display.backspace)
        self.display.clearPressed.connect(self.clear)
        self.display.numOrDot.connect(self.insertTextToDisplay)
        self.display.theOperator.connect(
            self.operatorClicked)
        for i, row in enumerate(self._grid_mask):
            for j, buttonText in enumerate(row):
                button = Button(buttonText)

                if not isNumOrDot(buttonText) and not isEmpty(buttonText):
                    button.setProperty('cssClass', 'specialButton')
                    self.configSpecialButton(button)

                self.addWidget(button, i, j)
                slot = self.makeSlot(self.insertTextToDisplay, buttonText)
                self.connectButtonCliked(button, slot)

    def connectButtonCliked(self, button, slot):
        button.clicked.connect(slot)

    def configSpecialButton(self, button):
        text = button.text()

        if text == 'C':
            button.clicked.connect(self.clear)
            self.equation = None
            self.left = None
            self.right = None
            self.op = None

        if text == '◀':
            self.connectButtonCliked(button, self.display.backspace)

        if text in '+-*/^':
            self.connectButtonCliked(button, self.makeSlot(
                self.operatorClicked, text))

        if text == '=':
            self.connectButtonCliked(button, self.makeSlot(self.equal))

    def makeSlot(self, func, *args, **kwargs):
        def realSlot():
            func(*args, **kwargs)
        return realSlot

    def insertTextToDisplay(self, text):
        newDisplayText = self.display.text() + text
        if not isNumber(newDisplayText):
            return

        self.display.insert(text)

    def operatorClicked(self, text):
        displayText = self.display.text()
        print(displayText)
        self.display.clear()

        if not isNumber(displayText) and self.left is None:
            print('nada ainda')
            return
        if self.left is None:
            self.left = float(displayText)

        self.op = text
        self.equation = f'{self.left} {self.op} ??'

    def clear(self):
        self.display.clear()
        self.equation = None
        self.left = None
        self.right = None
        self.op = None

    def equal(self):
        displayText = self.display.text()
        result = 0

        if not isNumber(displayText) or self.left is None:
            return

        self.right = float(displayText)
        self.equation = f'{self.left} {self.op} {self.right}'
        try:
            if '^' in self.equation and isinstance(self.left, float):
                result = math.pow(self.left, self.right)
            else:
                result = eval(self.equation)
        except ZeroDivisionError:
            result = None

        self.display.clear()
        self.info.setText(f'{self.equation} = {result}')
        self.left = result
