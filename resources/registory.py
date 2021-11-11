import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QMessageBox

from check_db import CheckThread


class Registory(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('registory.ui', self)
        self.setWindowTitle('Регистрация')
        self.new_password.setEchoMode(QLineEdit.Password)
        self.password_again.setEchoMode(QLineEdit.Password)
        self.registration.clicked.connect(self.reg)

        self.check_db = CheckThread()
        self.check_db.my_signal.connect(self.signal_handler)

    def signal_handler(self, value):
        QMessageBox.about(self, 'Оповещение', value)

    def reg(self):
        name = self.new_login.text()
        password = self.new_password.text()
        if self.new_password.text() == self.password_again.text():
            self.check_db.check_register(name, password)
        else:
            QMessageBox.warning(self, 'Оповещение', 'Пароли должны совпадать!')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window_2 = Registory()
    window_2.show()
    sys.exit(app.exec_())
