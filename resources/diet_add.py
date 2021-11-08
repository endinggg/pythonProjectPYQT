import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget


class Food(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('add_food.ui', self)
        self.setWindowTitle('Еда')

        self.add_user_food.clicked.connect(self.add_food)

        self.food.itemActivated.connect(self.elements)

    def elements(self, item):
        value = item.text().split(', ')
        self.elements_value = value[1:]
        self.return_val()

    def add_food(self):
        self.food.addItem('{}'.format(self.user_food.text()))

    def return_val(self):
        print(self.elements_value)
        return self.elements_value


class AddDiet(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('Diet.ui', self)

        self.setWindowTitle('Рацион')

        self.add_to_breakfast.clicked.connect(self.food)
        self.add_to_lunch.clicked.connect(self.food)
        self.add_to_dinner.clicked.connect(self.food)
        self.add_to_snack.clicked.connect(self.food)
        self.ccalories()

    def food(self):
        self.app1 = Food()
        self.app1.show()

    def ccalories(self):
        self.x = int(self.breakfast_change.text()) + int(self.lunch_change.text()) + int(self.dinner_change.text()) + \
                 int(self.snack_change.text())
        return self.x


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = AddDiet()
    ex.show()
    sys.exit(app.exec())
