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
        self.actionAbout.triggered.connect(self.about)
        self.CommandEnterBtn.clicked.connect(self.test)
    #     self.actionUser.triggered.connect(self.LoginDialog)
    #     self.actionModerator.triggered.connect(self.ModeratorDialog)

    def test(self):
        print('test')

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


    # def LoginDialog(self):
    #     dialog = LoginDialog(self)
    #     dialog.exec()

    # def ModeratorDialog(self):
    #     dialog = ModeratorDialog(self)
    #     dialog.exec()

# class LoginDialog(QDialog):
#     def __init__(self, parent=None):
#         super().__init__(parent)
#         loadUi('gui/ui/Login.ui', self)
    
# class ModeratorDialog(QDialog):
#     def __init__(self, parent=None):
#         super().__init__(parent)
#         loadUi('gui/ui/ModeratorLogin.ui', self)
