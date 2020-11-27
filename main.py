import sys
from random import randint, choice

from PyQt5.QtGui import QPainter, QBrush
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QApplication

from UI import Ui_MainWindow


class Window(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        # Вызываем метод для загрузки интерфейса из класса Ui_MainWindow,
        # остальное без изменений
        self.setupUi(self)

        self.do_paint = False
        self.btn.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            painter = QPainter(self)
            color = [Qt.yellow, Qt.blue, Qt.red, Qt.green, Qt.black, Qt.white, Qt.darkYellow,
                     Qt.darkMagenta, Qt.darkCyan]
            painter.setBrush(QBrush(choice(color), Qt.SolidPattern))
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

