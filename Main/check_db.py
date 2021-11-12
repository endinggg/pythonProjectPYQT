from PyQt5 import QtCore

from db_handler import *


class CheckThread(QtCore.QThread):
    my_signal = QtCore.pyqtSignal(str)

    def check_login(self, name, password):
        k = login(name, password, self.my_signal)
        return k

    def check_register(self, name, password):
        register(name, password, self.my_signal)
