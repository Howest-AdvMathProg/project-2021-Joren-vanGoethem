from PyQt5.QtWidgets import *
from PyQt5.uic import *
from PyQt5 import *

from gui.ui.mainwindowui import Ui_MainWindow
import pandas as pd
from util.PandasModel import PandasModel

class QueryLog(QDialog):
    def __init__(self, MainWindow, parent=None):
        super().__init__(parent)
        loadUi('gui/ui/QueryLog.ui', self)
        self.MainWindow = MainWindow
        self.connectSignalsSlots()
        self.run()

    def connectSignalsSlots(self):
        self.Refresh_button.clicked.connect(self.refresh)

    def refresh(self):
        self.searches = []
        for key, value in self.MainWindow.backend._eventhandler.searches.items():
            self.searches.append({ "query": key, "count": value })

        df = pd.DataFrame(self.searches)
        tablemodel = PandasModel(df)
        self.QueryTable.setModel(tablemodel)

    def run(self):
        self.refresh()
        self.show()
