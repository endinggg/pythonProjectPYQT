import sys

from PyQt5 import uic
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel
from registory import Registory
from main_window import *
from sqlite3 import *


class AddDiet(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Diet.ui', self)

        self.setGeometry(700, 150, 560, 620)
        self.setWindowTitle('MyDiet - Ведение здорового образа жизни')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = AddDiet()
    ex.show()
    sys.exit(app.exec())
