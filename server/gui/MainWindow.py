import threading
# pylint: disable=no-name-in-module
from util.logger import Log

from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QMessageBox
from PyQt5.uic import loadUi

from gui.mainwindowui import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, backend, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.connectSignalsSlots()

        self._running = True

        self.backend = backend

    @property
    def running(self):
        return self._running
           
    def connectSignalsSlots(self):
        self.actionUser.triggered.connect(self.LoginDialog)
        self.actionModerator.triggered.connect(self.ModeratorDialog)

    def LoginDialog(self):
        dialog = LoginDialog(self)
        dialog.exec()

    def ModeratorDialog(self):
        dialog = ModeratorDialog(self)
        # dialog.exec()

    def run(self):
        Log.info('GUI', 'Running')
        
        while self._running:
            pass

    def terminate(self):
        Log.info('GUI', 'Terminating...')

        self._running = False

class LoginDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        loadUi('gui/Login.ui', self)
    
class ModeratorDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        loadUi('gui/ModeratorLogin.ui', self)