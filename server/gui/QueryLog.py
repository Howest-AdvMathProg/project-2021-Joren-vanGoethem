from PyQt5.QtWidgets import *
from PyQt5.uic import *
from PyQt5 import *
import sys  # We need sys so that we can pass argv to QApplication
import os
import re
from random import randint

from gui.ui.mainwindowui import Ui_MainWindow

class QueryLog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        loadUi('gui/ui/QueryLog.ui', self)
        self.show()
    
    