from PyQt5.QtWidgets import *
from PyQt5.uic import *
from PyQt5 import *
from pyqtgraph import *
import pyqtgraph as pg
import sys  # We need sys so that we can pass argv to QApplication
import os
import re
from random import randint

from gui.ui.mainwindowui import Ui_MainWindow

class GraphView(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        loadUi('gui/ui/plot.ui', self)
    
    def ConfigureLayout(self):
        self.Graph.setTitle("Graph",color="#000000")
        self.Graph.setBackground('#e8e8e8')
        styles = {'color':'#000000', 'font-size':'12px'}
        self.Graph.setLabel('left', 'Temperature (°C)', **styles)
        self.Graph.setLabel('bottom', 'Hour (H)', **styles)
        self.Graph.showGrid(x=True, y=True)
        self._color = "#FF0000"

    def plot(self, x, y):
        self.line = pg.mkPen({"color":self._color, "width":2, "cosmetic": True, "style": QtCore.Qt.SolidLine})
        self.Graph.plot(x, y, pen=self.line)
        self.ChangeColor()
    
    def ChangeColor(self, color="A"):
        if color == "A": #random color
            random_number = randint(1048576,16777215)
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