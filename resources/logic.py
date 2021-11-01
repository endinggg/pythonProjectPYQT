from PyQt5.QtCore import QSize
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QFileDialog


def change_avatar(self):
    f_change_avatar = QFileDialog.getOpenFileName(self, 'Выберите картинку', '', 'Images (*.png)')[0]
    self.avatar_image = f_change_avatar
    self.button_change_avatar.setIcon(QIcon(self.avatar_image))
    self.button_change_avatar.setIconSize(QSize(101, 101))


def characteristics(self):
    self.user_weight = self.weight.text()
    self.user_height = self.height.text()
    self.user_age = self.age.value()


def PGC(self):
    pass


def calories(self):
    self.value_calories_2 = (self.user_weight * 10 + self.user_height * 6.75 - self.user_age * 5) \
                            * 1.2 - self.value_calories_1
# Не понял как вызывать эти функции в main_window
