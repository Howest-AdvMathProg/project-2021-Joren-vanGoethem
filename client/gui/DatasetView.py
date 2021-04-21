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

    def GetDatasetInfo(self):
        self._df = pd.read_csv("dataset/netflix_titles.csv")
        self.columns = list(self._df.columns)
        self.datasethead = self._df.tail(10)
        # self.columns = self.MainWindow.backend.send("COLUMNS OFZO")
        # self.datasethead = self.MainWindow.backend.send("HEAD 10 OFZO")
        pass
    
    def run(self):
        self.GetDatasetInfo()

        self.tablemodel = PandasModel(self.datasethead)
        self.DataframeTable.setModel(self.tablemodel)
        
        for i in self.columns:
            item = QtGui.QStandardItem(i)
            self.listmodel.appendRow(item)
        self.show()


