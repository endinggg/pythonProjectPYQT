import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox
from food_db import add_components, deleting, save_values


class AddDiet(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('add_food.ui', self)

        self.setWindowTitle('Рацион')

        self.user_food.setEnabled(False)
        self.accept.clicked.connect(self.accepting)
        self.add_user_food.clicked.connect(self.add_food)
        self.delete_food.clicked.connect(self.food_del)

        self.add_to_breakfast.clicked.connect(self.breakfast)
        self.add_to_lunch.clicked.connect(self.lunch)
        self.add_to_dinner.clicked.connect(self.dinner)
        self.add_to_snack.clicked.connect(self.snack)

        self.save_food.clicked.connect(self.save_val)
        self.delete_food.clicked.connect(self.food_del)

        self.ccal_breakfast = 0
        self.ccal_lunch = 0
        self.ccal_dinner = 0
        self.ccal_snack = 0

        self.proteins = 0
        self.all_fats = 0
        self.carbohs = 0

    def breakfast(self):
        val = self.elements()
        if val:
            self.ccal_breakfast += int(val[0])
            self.breakfast_label.setText(f'Завтрак: {self.ccal_breakfast} ккал')
            self.proteins += int(val[1])
            self.all_fats += int(val[2])
            self.carbohs += int(val[3])

    def lunch(self):
        val = self.elements()
        if val:
            self.ccal_lunch += int(val[0])
            self.lunch_label.setText(f'Обед: {self.ccal_lunch} ккал')
            self.proteins += int(val[1])
            self.all_fats += int(val[2])
            self.carbohs += int(val[3])

    def dinner(self):
        val = self.elements()
        if val:
            self.ccal_dinner += int(val[0])
            self.dinner_label.setText(f'Ужин: {self.ccal_dinner} ккал')
            self.proteins += int(val[1])
            self.all_fats += int(val[2])
            self.carbohs += int(val[3])

    def snack(self):
        val = self.elements()
        if val:
            self.ccal_snack += int(val[0])
            self.snack_label.setText(f'Перекус: {self.ccal_snack} ккал')
            self.proteins += int(val[1])
            self.all_fats += int(val[2])
            self.carbohs += int(val[3])

    def accepting(self):
        self.food_list.addItem('{}'.format(self.user_food.text()))

    def elements(self):
        try:
            self.value = self.user_food.text().split(', ')
            self.name = self.value[0]
            self.calories = self.value[1]
            self.protein = self.value[2]
            self.fats = self.value[3]
            self.carbohydrates = self.value[4]
            add_components(self.name, self.calories, self.protein, self.fats, self.carbohydrates)
            return self.calories, self.protein, self.fats, self.carbohydrates
        except IndexError:
            QMessageBox.warning(self, 'Ошибка!', 'Неверный ввод данных', QMessageBox.Retry)

    def add_food(self):
        self.user_food.setEnabled(True)

    def food_del(self):
        deleting(self.name)
        self.food_list.clear()

    def save_val(self):
        self.summ_cal = self.ccal_breakfast + self.ccal_lunch + self.ccal_dinner + self.ccal_snack
        save_values(self.summ_cal, self.proteins, self.all_fats, self.carbohs)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = AddDiet()
    ex.show()
    sys.exit(app.exec())
