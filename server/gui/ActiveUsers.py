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
from gui.DirectMessage import DirectMessage

class ActiveUsers(QDialog):
    def __init__(self, MainWindow, parent=None):
        super().__init__(parent)
        loadUi('gui/ui/ActiveUsers.ui', self)

        self.MainWindow = MainWindow
        self.connectSignalsSlots()
        self.run()

    def connectSignalsSlots(self):
        self.refresh_users_button.clicked.connect(self.refresh)
        self.UsersTable.doubleClicked.connect(self.user_message)

    def refresh(self):
        self.clients = []
        for key, value in self.MainWindow.backend.clients.items():
            self.clients.append(value)

        df = pd.DataFrame([client.identity for client in self.clients])
        tablemodel = PandasModel(df)
        self.UsersTable.setModel(tablemodel)

    def user_message(self, item):
        print(f"row: {item.row()}, column: {item.column()}")
        client = self.clients[item.row()]
        self.DirectMessage = DirectMessage(client)
        self.DirectMessage.show()

    def run(self):
        self.refresh()
        self.show()
