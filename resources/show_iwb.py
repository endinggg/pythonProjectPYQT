import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget


class CheckIWB(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('IWB.ui', self)

        self.setWindowTitle('ИМТ')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = CheckIWB()
    ex.show()
    sys.exit(app.exec())
