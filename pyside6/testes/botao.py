import sys

from PySide6.QtWidgets import (QApplication, QPushButton, QWidget,
                               QVBoxLayout, QMainWindow)

app = QApplication(sys.argv)

central_widget = QWidget()
window = QMainWindow()
window.setCentralWidget(central_widget)

botao = QPushButton('Botão1')
botao2 = QPushButton('Botão2')
list = [1, 2, 3, 4]


layout = QVBoxLayout()
central_widget.setLayout(layout)
layout.addWidget(botao)
layout.addWidget(botao2)

menu = window.menuBar()
menu1 = menu.addMenu('Primeiro menu')
menu_action = menu1.addAction('Ação 1')


def slot():
    def realSlot():
        print('oi')
    return realSlot


botao.clicked.connect(slot)
botao2.clicked.connect(slot)

status_bar = window.statusBar()
status_bar.showMessage('Barra de mensagem')

window.show()
app.exec()
