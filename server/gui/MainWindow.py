from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi

from gui.ui.mainwindowui import Ui_MainWindow
from gui.QueryLog import QueryLog
from gui.ServerLog import ServerLog
from gui.ActiveUsers import ActiveUsers

from util.logger import Log

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, backend, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.connectSignalsSlots()

        self.backend = backend

        Log.on_log = self.update_log

    def connectSignalsSlots(self):
        self.actionAbout.triggered.connect(self.about)
        self.CommandEnterBtn.clicked.connect(self.test)
        self.actionQuery_Log.triggered.connect(self.Query_Log)
        self.actionServer_Log.triggered.connect(self.Server_Log)
        self.actionActive_Users.triggered.connect(self.Active_Users)
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

    def Query_Log(self):
        self._Query_Log = QueryLog(self)

    def Server_Log(self):
        self._Server_Log = ServerLog(self)

    def Active_Users(self):
        self._Active_Users = ActiveUsers(self)

    def update_log(self, log):
        self.MainField.moveCursor(QTextCursor.End)
        self.MainField.insertPlainText("%s\n" % log)
        self.MainField.moveCursor(QTextCursor.End)

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
