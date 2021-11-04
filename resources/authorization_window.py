import sys

from PyQt5 import uic
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel
from registory import Registory
from main_window import *
from sqlite3 import *


class Authorization(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('authorization.ui', self)

        self.setGeometry(700, 150, 560, 620)
        self.setWindowTitle('MyDiet - Ведение здорового образа жизни')

        self.icon_user1 = QPixmap('icon_user.png')
        self.icon_user = QLabel(self)
        self.icon_user.move(214, 217)
        self.icon_user.resize(50, 50)
        self.icon_user.setPixmap(self.icon_user1)

        self.icon_diet1 = QPixmap('icon_diet.png')
        self.icon_diet = QLabel(self)
        self.icon_diet.move(187, 75)
        self.icon_diet.resize(175, 140)
        self.icon_diet.setPixmap(self.icon_diet1)

        self.button_registory.clicked.connect(self.show_window_to_registration)
        self.button_entry.clicked.connect(self.show_main_window)

    def show_window_to_registration(self):
        self.window_2 = Registory()
        self.window_2.show()

    def show_main_window(self):
        self.main_wind = MainWindowApp()
        self.main_wind.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Authorization()
    ex.show()
    sys.exit(app.exec())
