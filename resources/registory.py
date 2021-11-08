import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit


class Registory(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('registory.ui', self)
        self.setWindowTitle('Регистрация')
        self.new_password.setEchoMode(QLineEdit.Password)
        self.password_again.setEchoMode(QLineEdit.Password)
        self.registration.clicked.connect(self.registration_1)

    def registration_1(self):
        name = self.new_login.text()
        password = self.new_password.text()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window_2 = Registory()
    window_2.show()  # открытие 1 окна
    sys.exit(app.exec_())
