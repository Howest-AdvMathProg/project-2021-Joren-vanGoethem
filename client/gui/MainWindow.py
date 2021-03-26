from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi

from gui.ui.mainwindowui import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, backend, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.connectSignalsSlots()

        self.backend = backend
           
    def connectSignalsSlots(self):
        pass
#         self.actionUser.triggered.connect(self.LoginDialog)
#         self.actionModerator.triggered.connect(self.ModeratorDialog)

#     def LoginDialog(self):
#         dialog = LoginDialog(self)
#         dialog.exec()

#     def ModeratorDialog(self):
#         dialog = ModeratorDialog(self)
#         dialog.exec()

# class LoginDialog(QDialog):
#     def __init__(self, parent=None):
#         super().__init__(parent)
#         loadUi('gui/ui/Login.ui', self)
    
# class ModeratorDialog(QDialog):
#     def __init__(self, parent=None):
#         super().__init__(parent)
#         loadUi('gui/ui/ModeratorLogin.ui', self)
