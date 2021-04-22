from PyQt5.QtWidgets import *
from PyQt5.uic import *
from PyQt5 import *
import sys  # We need sys so that we can pass argv to QApplication
import os
import re
from random import randint
import pandas as pd
from util.PandasModel import PandasModel

from gui.ui.mainwindowui import Ui_MainWindow

class ActiveUsers(QDialog):
    def __init__(self, MainWindow, parent=None):
        super().__init__(parent)
        loadUi('gui/ui/ActiveUsers.ui', self)

        self.MainWindow = MainWindow
        self.run()

    def run(self):
        clients = []

        for key, value in self.MainWindow.backend.clients.items():
            clients.append(value.identity)

        df = pd.DataFrame(clients)

        tablemodel = PandasModel(df)
        self.UsersTable.setModel(tablemodel)

        self.show()
