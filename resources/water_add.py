import sys

from PyQt5 import uic
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QGraphicsTextItem


class AddWater(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('Water.ui', self)

        self.setWindowTitle('Вода')

        self.im_glass = QPixmap('../glass.png')
        self.image.move(120, 20)
        self.image.setPixmap(self.im_glass)

        self.values.activated[str].connect(self.water)
        self.val1 = 0

    def water(self, val):
        water2 = val.split()
        self.val1 += int(water2[0]) / 1000
        self.n = round(self.val1, 2)
        self.value_water.setText(f'{self.n} л из 2 л')
        self.percent.setText(f'{self.val1 * 100 // 2} %')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = AddWater()
    ex.show()
    sys.exit(app.exec())

