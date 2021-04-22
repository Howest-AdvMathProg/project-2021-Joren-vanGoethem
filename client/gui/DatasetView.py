from PyQt5.QtWidgets import *
from PyQt5.uic import *
from PyQt5 import *
from pyqtgraph import *
import pyqtgraph as pg
import sys  # We need sys so that we can pass argv to QApplication
import os
import re
from random import randint
import pandas as pd

from gui.ui.mainwindowui import Ui_MainWindow
from util.PandasModel import PandasModel

class DatasetView(QDialog):
    def __init__(self, MainWindow, parent=None):
        super().__init__(parent)
        loadUi('gui/ui/Dataset.ui', self)
        self.MainWindow = MainWindow

        self.listmodel = QtGui.QStandardItemModel()
        self.ColumnList.setModel(self.listmodel)

        self.run()

    def run(self):
        self.MainWindow.backend.send_event("GET_DATA_SAMPLE")

        data = self.MainWindow.backend.get_data()
        if not data: # timeout
            return

        df = pd.DataFrame.from_dict(data["sample"])

        tablemodel = PandasModel(df)
        self.DataframeTable.setModel(tablemodel)

        for i in data["columns"]:
            item = QtGui.QStandardItem(i)
            self.listmodel.appendRow(item)
        self.show()


