from PyQt5.QtWidgets import *
from PyQt5.uic import *
from PyQt5 import *
import sys


class DirectMessage(QDialog):
    def __init__(self, client, parent=None):
        super().__init__(parent)
        loadUi('gui/ui/Direct_Message.ui', self)
        self.Client = client

    def accept(self):
        message = self.plainTextEdit.toPlainText()
        self.Client.send_event("BROADCAST", message)
        self.close()
