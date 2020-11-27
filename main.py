import sys
from random import randint

from PyQt5.QtGui import QPainter, QBrush, QPen
from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        uic.loadUi("UI.ui", self)

        self.do_paint = False
        self.btn.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            painter = QPainter(self)
            painter.setBrush(QBrush(Qt.yellow, Qt.SolidPattern))
            x = randint(10, 400)
            painter.drawEllipse(180, 70, x, x)

    def paint(self):
        self.do_paint = True
        self.repaint()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    ex.show()
    sys.exit(app.exec())

