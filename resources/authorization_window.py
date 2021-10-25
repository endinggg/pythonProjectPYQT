import sys

from PyQt5.QtGui import QPixmap
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel


class AuthorizationWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('authorization.ui', self)

        self.setGeometry(700, 150, 560, 620)
        self.setWindowTitle('MyDiet - Ведение здорового образа жизни')

        self.icon_user1 = QPixmap('icon_user.png')
        self.icon_user = QLabel(self)
        self.icon_user.move(84, 160)
        self.icon_user.resize(50, 50)
        self.icon_user.setPixmap(self.icon_user1)

        self.icon_diet1 = QPixmap('icon_diet.png')
        self.icon_diet = QLabel(self)
        self.icon_diet.move(300, 130)
        self.icon_diet.resize(300, 300)
        self.icon_diet.setPixmap(self.icon_diet1)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = AuthorizationWindow()
    ex.show()
    sys.exit(app.exec())
