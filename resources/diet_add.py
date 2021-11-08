import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget


class Food(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('add_food.ui', self)
        self.setWindowTitle('Еда')

        self.add_user_food.clicked.connect(self.add_food)

    def add_food(self):
        self.food.addItem('{}'.format(self.user_food.text()))
        self.return_food()

    def return_food(self):
        return self.user_food.text()


class AddDiet(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('Diet.ui', self)

        self.setWindowTitle('Рацион')

        self.add_to_breakfast.clicked.connect(self.food)
        self.add_to_lunch.clicked.connect(self.food)
        self.add_to_dinner.clicked.connect(self.food)
        self.add_to_snack.clicked.connect(self.food)

    def food(self):
        self.app1 = Food()
        self.app1.show()
        self.val_list = self.app1.return_food().split(', ')
        self.val_food = self.val_list[1]
        print(self.val_food)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = AddDiet()
    ex.show()
    sys.exit(app.exec())
