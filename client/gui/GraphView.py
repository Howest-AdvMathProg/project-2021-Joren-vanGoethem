from PyQt5.QtWidgets import *
from PyQt5.uic import *
from PyQt5 import *
from pyqtgraph import *
import pyqtgraph as pg
import sys  # We need sys so that we can pass argv to QApplication
import os
import re
from random import randint
import json
import pandas as pd

from gui.ui.mainwindowui import Ui_MainWindow

class GraphView(QDialog):
    def __init__(self, MainWindow, parent=None):
        super().__init__(parent)
        loadUi('gui/ui/plot.ui', self)
        self.MainWindow = MainWindow

    def showGraph(self):
        self.send_receive("""{
            "query": {
                "column": "type",
                "value": "Movie"
            },
            "type": "column",
            "exact": false
        }""",'M')
        self.send_receive("""{
            "query": {
                "column": "type",
                "value": "TV Show"
            },
            "type": "column",
            "exact": false
        }""",'T')


    def send_receive(self,text,type):
        self.MainWindow.backend.send_event("SEARCH", json.loads(text))

        data = self.MainWindow.backend.get_data()
        if not data: # timeout
            return

        df = pd.DataFrame.from_dict(data)
        self.extract_values(df,type)

    def extract_values(self, df, type):
        x = df["release_year"].unique().tolist()
        y = df["release_year"].value_counts().tolist()
        x.sort()
        y.sort()
        self.plot(x,y,type)

    def ConfigureLayout(self):
        self.Graph.setTitle("Graph",color="#000000")
        self.Graph.setBackground('#e8e8e8')
        styles = {'color':'#000000', 'font-size':'12px'}
        self.Graph.setLabel('left', 'Count', **styles)
        self.Graph.setLabel('bottom', 'Release Year', **styles)
        self.Graph.showGrid(x=True, y=True)
        self._color = "#FF0000"

    def plot(self, x, y,type):
        if type == 'M':
            self.Graph.addLegend()
            self.line = pg.mkPen({"color":self._color, "width":2, "cosmetic": True, "style": QtCore.Qt.SolidLine})
            self.Graph.plot(x, y, pen=self.line, name='Movies')
        elif type == 'T':
            self.line = pg.mkPen({"color":self._color, "width":2, "cosmetic": True, "style": QtCore.Qt.SolidLine})
            self.Graph.plot(x, y, pen=self.line, name='TV Shows')
        self.ChangeColor()


    def ChangeColor(self, color="A"):
        if color == "A": #random color
            random_number = randint(1248576,15777215)
            hex_number = str(hex(random_number))
            hex_number ='#'+ hex_number[2:]
            self._color = hex_number
        else: #check if color is valid hex color code
            match = re.search(r'^#(?:[0-9a-fA-F]{3}){1,2}$', color)
            if match:
                self._color = color
            else:
                QMessageBox.about(
                    self,
                    "Error",
                    "the color code you provided was invalid"
                )

    def clear(self):
        self.Graph.clear()
