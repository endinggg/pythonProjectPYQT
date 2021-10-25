import sys
from tkinter import Image

from PIL.ImageQt import ImageQt

from PyQt5 import uic
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QPushButton, QFileDialog


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main_window.ui', self)

        self.setGeometry(700, 150, 702, 728)
        self.setWindowTitle('MyDiet - Ведение здорового образа жизни')

        self.button_change_avatar = QPushButton(self)
        self.button_change_avatar.resize(101, 101)
        self.button_change_avatar.move(15, 15)
        self.button_change_avatar.setIcon(QIcon('user_avatar.png'))
        self.button_change_avatar.setIconSize(QSize(101, 101))
        self.show()

        self.button_change_avatar.clicked.connect(self.change_avatar)

        self.icon_health1 = QPixmap('icon_health.png')
        self.icon_health = QLabel(self)
        self.icon_health.move(10, 100)
        self.icon_health.resize(150, 150)
        self.icon_health.setPixmap(self.icon_health1)

    def change_avatar(self):
        f_change_avatar = QFileDialog.getOpenFileName(self, 'Выберите картинку', '', 'Images (*.png)')[0]
        self.avatar_image = Image.open(f_change_avatar)
        self.button_change_avatar.setIcon(QIcon(self.avatar_image))
        self.button_change_avatar.setIconSize(QSize(101, 101))

#         self.original_image = Image.open(self.filename)

#
#         self.a = ImageQt(self.image_for_edit)
#         self.pixmap = QPixmap.fromImage(self.a)
#         self.image.setPixmap(self.pixmap)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec())
