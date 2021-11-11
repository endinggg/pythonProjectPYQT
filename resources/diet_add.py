import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget
from food_db import add_components

class AddDiet(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('Diet.ui', self)

        self.setWindowTitle('Рацион')

        self.list_to_del = []
        self.add_to_breakfast.clicked.connect(self.food)

        # self.add_to_breakfast.clicked.connect(self.breakfast)
        # self.add_to_lunch.clicked.connect(self.lunch)
        # self.add_to_dinner.clicked.connect(self.dinner)
        # self.add_to_snack.clicked.connect(self.snack)
        # self.ccalories()

    # def breakfast(self):
    #     self.app1 = Food()
    #     self.app1.show()
    #     k = self.app1.elements_value
    #     self.calories = k[0]
    #     self.protein = k[1]
    #     self.fats = k[2]
    #     self.carbohydrates = k[3]
    #     self.breakfast_change.setText()
    #
    # def lunch(self):
    #     self.app1 = Food()
    #     self.app1.show()
    #     k = self.app1.elements_value
    #     self.calories = k[0]
    #     self.protein = k[1]
    #     self.fats = k[2]
    #     self.carbohydrates = k[3]
    #     self.lunch_change.setText()
    #
    # def dinner(self):
    #     self.app1 = Food()
    #     self.app1.show()
    #     k = self.app1.elements_value
    #     self.calories = k[0]
    #     self.protein = k[1]
    #     self.fats = k[2]
    #     self.carbohydrates = k[3]
    #     self.dinner_change.setText()
    #
    # def snack(self):
    #     self.app1 = Food()
    #     self.app1.show()
    #     k = self.app1.elements_value
    #     self.calories = k[0]
    #     self.protein = k[1]
    #     self.fats = k[2]
    #     self.carbohydrates = k[3]
    #     self.snack_change.setText()

    #
    def food(self):
        self.app1 = Food()
        self.app1.show()
        print(self.list_to_del) #Название продукта, 0, 0, 0, 0
        # self.calories = k[0]
        # self.protein = k[1]
        # self.fats = k[2]
        # self.carbohydrates = k[3]
        # self.breakfast_change.setText(self.calories)
        # self.lunch_change.setText()
        # self.dinner_change.setText()
        # self.snack_change.setText()

    # def ccalories(self):
    #     self.x = int(self.breakfast_change.text()) + int(self.lunch_change.text()) + int(self.dinner_change.text()) + \
    #              int(self.snack_change.text())
    #     return self.x


class Food(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('add_food.ui', self)
        self.setWindowTitle('Еда')
        self.user_food.setEnabled(False)
        self.accept.clicked.connect(self.accepting)
        self.add_user_food.clicked.connect(self.add_food)

    def accepting(self):
        self.food_list.addItem('{}'.format(self.user_food.text()))
        self.value = self.user_food.text().split(', ')
        self.name = self.value[0]
        self.calories = self.value[1]
        self.protein = self.value[2]
        self.fats = self.value[3]
        self.carbohydrates = self.value[4]
        add_components(self.name, self.calories, self.protein, self.fats, self.carbohydrates)

    def add_food(self):
        self.user_food.setEnabled(True)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = AddDiet()
    ex.show()
    sys.exit(app.exec())
