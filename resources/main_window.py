import sys

from PyQt5 import uic, QtCore
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QPushButton, QFileDialog
from authorization_window import *


class MainWindowApp(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main_window.ui', self)

        self.setGeometry(700, 150, 702, 728)
        self.setWindowTitle('MyDiet - Ведение здорового образа жизни')

        self.icon_health1 = QPixmap('icon_health.png')
        self.icon_health = QLabel(self)
        self.icon_health.move(125, 50)
        self.icon_health.resize(50, 50)
        self.icon_health.setPixmap(self.icon_health1)

        self.button_change_avatar = QPushButton(self)
        self.button_change_avatar.resize(101, 101)
        self.button_change_avatar.move(15, 15)
        self.button_change_avatar.setIcon(QIcon('user_avatar.png'))
        self.button_change_avatar.setIconSize(QSize(101, 101))

        self.button_change_avatar.clicked.connect(self.change_avatar)

        self.date.setDate(QtCore.QDate(2021, 11, 1))
        self.date.setDisplayFormat("dd/MM/yyyy")

        self.weight.textChanged[str].connect(self.characteristics)
        self.height.textChanged[str].connect(self.characteristics)
        self.age.valueChanged[int].connect(self.characteristics)

    def change_avatar(self):
        f_change_avatar = QFileDialog.getOpenFileName(self, 'Выберите картинку', '', 'Images (*.png)')[0]
        self.avatar_image = f_change_avatar
        self.button_change_avatar.setIcon(QIcon(self.avatar_image))
        self.button_change_avatar.setIconSize(QSize(101, 101))

    def characteristics(self):
        self.user_weight = self.weight.text()
        self.user_height = self.height.text()
        self.user_age = self.age.value()

    def PFC(self):
        pass

    def calories(self):
        self.value_calories_2 = (self.user_weight * 10 + self.user_height * 6.75 - self.user_age * 5) \
                                * 1.2 - self.value_calories_1


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindowApp()
    ex.show()
    sys.exit(app.exec())
