import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget

from db_handler import users_parametrs


class Checking(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('user_parametrs.ui', self)

        self.setWindowTitle('Введите ваши данные')

        self.save_characteristics.clicked.connect(self.saving)

    def saving(self):
        self.user_height = int(self.height.text())
        self.user_weight = int(self.weight.text())
        self.user_age = self.age.value()
        users_parametrs(self.user_height, self.user_weight, self.user_age)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Checking()
    ex.show()
    sys.exit(app.exec())
