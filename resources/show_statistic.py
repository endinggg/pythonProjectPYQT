import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget


class Statistics(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('Statistiks.ui', self)

        self.setGeometry(700, 150, 500, 580)
        self.setWindowTitle('Статистика')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Statistics()
    ex.show()
    sys.exit(app.exec())
