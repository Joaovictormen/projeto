
from PySide6.QtWidgets import QLineEdit
from variables import BIG_FONT
from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QKeyEvent
from valida_num import isEmpty, isNumOrDot


class Display(QLineEdit):
    eqPressed = Signal()
    delPressed = Signal()
    clearPressed = Signal()
    numOrDot = Signal(str)
    theOperator = Signal(str)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()

    def configStyle(self):
        self.setStyleSheet(f'font-size: {BIG_FONT}px')
        self.setMinimumHeight(BIG_FONT * 2)
        self.setAlignment(Qt.AlignmentFlag.AlignRight)

    def keyPressEvent(self, event: QKeyEvent) -> None:
        text = event.text().strip()
        key = event.key()
        KEYS = Qt.Key
        isEnter = key in [KEYS.Key_Enter, KEYS.Key_Return]
        isBackSpace = key == KEYS.Key_Backspace
        isEsc = key == KEYS.Key_Escape
        isOperator = text in '+-*/'

        if isEnter:
            self.eqPressed.emit()
            return event.ignore()

        if isBackSpace:
            self.delPressed.emit()
            return event.ignore()

        if isEsc:
            self.clearPressed.emit()
            return event.ignore()

        if isOperator:
            self.theOperator.emit(text)
            return event.ignore()

        if isEmpty(text):
            return event.ignore()

        if isNumOrDot(text):

            self.numOrDot.emit(text)
            return event.ignore()
