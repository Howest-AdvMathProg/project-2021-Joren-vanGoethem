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
from gui.GraphView import GraphView
from gui.DatasetView import DatasetView
from gui.Login import Login

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, backend, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.connectSignalsSlots()
        self.backend = backend
        self.Login() # self.User will be created by the login class
           
    def Login(self):
        self._Login = Login(self)

    def connectSignalsSlots(self):
        self.actionAbout.triggered.connect(self.about)
        self.actionGraph_view.triggered.connect(self.graph_view)
        self.Searchbutton.clicked.connect(self.search)
        self.actionDataset_Info.triggered.connect(self.dataset_info)

    def dataset_info(self):
        self._DatasetView = DatasetView(self)


    def search(self):
        text = self.commandfield.toPlainText()
        print(text)
        #naar server

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

        self._GraphView.ChangeColor() # color in hex format optional. if not given will be random color

        # self._GraphView.plot([1,2,3,4,5,6,7,8,9,10], [24,28,14,26,28,31,17,15,12,10])
        # self._GraphView.plot([8,7,9,5,1,2,13,5,7,8], [24,18,17,25,31,12,24,25,31,27])
        self._GraphView.plot([1,2,3,4,5,6,7,8,9,10], [20,0,15,0,25,0,30,0,17,0])

