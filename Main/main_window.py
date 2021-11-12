import sys

from PyQt5 import uic
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QPushButton, QFileDialog, QWidget, QMessageBox

from db_handler import users_parametrs, give_values
from diet_add import AddDiet
from water_add import AddWater
from food_db import return_values


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

        self.change_characteristics.clicked.connect(self.change_values)
        self.save_characteristics.clicked.connect(self.save_values)

        self.updates_values.clicked.connect(self.updating)

        self.first_values()

    def change_avatar(self):
        f_change_avatar = QFileDialog.getOpenFileName(self, 'Выберите картинку', '', 'Images (*.png)')[0]
        self.avatar_image = f_change_avatar
        self.button_change_avatar.setIcon(QIcon(self.avatar_image))
        self.button_change_avatar.setIconSize(QSize(101, 101))

    def change_values(self):
        self.height.setEnabled(True)
        self.weight.setEnabled(True)
        self.age.setEnabled(True)

    def first_values(self):
        value = give_values()
        self.user_height, self.user_weight, self.user_age = value
        self.height.setText('{}'.format(self.user_height))
        self.weight.setText('{}'.format(self.user_weight))
        self.age.setValue(self.user_age)

    def save_values(self):
        try:
            self.user_height = int(self.height.text())
            self.user_weight = int(self.weight.text())
            self.user_age = self.age.value()
            users_parametrs(self.user_height, self.user_weight, self.user_age)
            self.index = round(self.user_weight / ((self.user_height / 100) ** 2), 1)
            self.height.setEnabled(False)
            self.weight.setEnabled(False)
            self.age.setEnabled(False)
            return self.index
        except ValueError:
            QMessageBox.warning(self, 'Ошибка!', 'Неверный ввод данных', QMessageBox.Retry)

    def add_diet(self):
        self.diet2 = AddDiet()
        self.diet2.show()

    def updating(self):
        val = return_values()
        self.ccalories.setText(f'{val[0]}')
        self.protein.setText(f'{val[1]}')
        self.fats.setText(f'{val[2]}')
        self.carbohydrates.setText(f'{val[3]}')
        self.value_calories = val[0]
        self.value_calories_1.setText(f'{val[0]} ккал')
        self.value_calories2 = round((self.user_weight * 10 + self.user_height * 6.75 - self.user_age * 5) \
                                * 1.2 - self.value_calories)
        self.value_calories_2.setText(f'{self.value_calories2} ккал')

    def water_add(self):
        self.water2 = AddWater()
        self.water2.show()

    def iwb_window(self):
        indexx = self.save_values()
        self.iwb2 = CheckIWB()
        self.iwb2.show()
        self.iwb2.set_index(indexx)


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
