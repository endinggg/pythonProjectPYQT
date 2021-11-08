import sys

from PyQt5 import uic, QtCore
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QPushButton, QFileDialog, QWidget
from diet_add import AddDiet
from water_add import AddWater
from show_statistic import Statistics



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

        self.diet.clicked.connect(self.add_diet)
        self.water.clicked.connect(self.water_add)
        self.index_weight_body.clicked.connect(self.iwb_window)
        self.statistic.clicked.connect(self.statistic_show)

        self.save_characteristics.clicked.connect(self.characteristics)

    def change_avatar(self):
        f_change_avatar = QFileDialog.getOpenFileName(self, 'Выберите картинку', '', 'Images (*.png)')[0]
        self.avatar_image = f_change_avatar
        self.button_change_avatar.setIcon(QIcon(self.avatar_image))
        self.button_change_avatar.setIconSize(QSize(101, 101))

    def characteristics(self):
        self.user_weight = int(self.weight.text())
        self.user_height = int(self.height.text())
        self.user_age = self.age.value()
        self.index = round(self.user_weight / ((self.user_height / 100) ** 2), 1)
        return self.index

    def PFC(self):
        pass

    def calories(self):
        self.value_calories_2 = (self.user_weight * 10 + self.user_height * 6.75 - self.user_age * 5) \
                                * 1.2 - self.value_calories_1

    # я не знаю, что это за магические числа, что они обозначают. в формуле они уже были, не стал делать их константами

    def add_diet(self):
        self.diet2 = AddDiet()
        self.diet2.show()

    def water_add(self):
        self.water2 = AddWater()
        self.water2.show()

    def iwb_window(self):
        indexx = self.characteristics()
        self.iwb2 = CheckIWB()
        self.iwb2.show()
        self.iwb2.set_index(indexx)

    def statistic_show(self):
        self.statistic2 = Statistics()
        self.statistic2.show()


class CheckIWB(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('IWB.ui', self)
        self.setWindowTitle('ИМТ')

    def set_index(self, indexx):
        self.user_value.setText('{}'.format(indexx))

        if indexx < 18.5:
            self.user_status.setText('у вас дефицит массы тела')
        elif 18.5 <= indexx < 25:
            self.user_status.setText('у вас нормальная масса тела')
        elif 25 <= indexx < 30:
            self.user_status.setText('у вас избыточная масса тела')
        elif indexx > 30:
            self.user_status.setText('у вас ожирение')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindowApp()
    ex.show()
    sys.exit(app.exec())

