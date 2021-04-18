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


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, backend, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.connectSignalsSlots()

        self.backend = backend
           
    def connectSignalsSlots(self):
        self.actionAbout.triggered.connect(self.about)
        self.actionGraph_view.triggered.connect(self.graph_view)
#         self.actionUser.triggered.connect(self.LoginDialog)
#         self.actionModerator.triggered.connect(self.ModeratorDialog)

    def about(self):
        QMessageBox.about(
            self,
            "About Client-Server App",
            "<p>A socket connection app built with:</p>"
            "<ul>"
            "<li> PyQt</li>"
            "<li> Qt Designer</li>"
            "<li> Python 3</li>"
            "</ul>"
            "<p>Made by:</p>"
            "<p>Andreas Maerten & Joren vanGoethem</p>",
        )

    def graph_view(self):
        self._GraphView = GraphView(self)
        self._GraphView.show()
        self._GraphView.ConfigureLayout()

        self._GraphView.plot([1,2,3,4,5,6,7,8,9,10], [24,28,14,26,28,31,17,15,12,10])
        self._GraphView.plot([8,7,9,5,1,2,13,5,7,8], [24,18,17,25,31,12,24,25,31,27])

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
        if color == "A":
            random_number = randint(1048576,16777215)
            hex_number = str(hex(random_number))
            hex_number ='#'+ hex_number[2:]
            self._color = hex_number
        else:
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