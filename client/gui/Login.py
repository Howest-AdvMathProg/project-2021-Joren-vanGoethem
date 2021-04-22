from PyQt5.QtWidgets import *
from PyQt5.uic import *
from PyQt5 import *
import sys  # We need sys so that we can pass argv to QApplication

from gui.ui.mainwindowui import Ui_MainWindow
from User import User

class Login(QDialog):
    def __init__(self, MainWindow, parent=None):
        super().__init__(parent)
        loadUi('gui/ui/Login.ui', self)
        self._MainWindow = MainWindow
        self.Logged_in = False
        self._input_fields = []
        self.get_input_fields()
        self.exec()

    #override van originele functie
    def accept(self):
        empty = []
        for field in self._input_fields:
            if field.text() == "":
                empty.insert(0,field) # insert to front of list so order is accurate in error message
            elif "nickname" in field.objectName().lower():
                NickName = field.text()
            elif "name" in field.objectName().lower():
                Name = field.text()
            elif "email" in field.objectName().lower():
                Email = field.text()
            elif "password" in field.objectName().lower():
                Password = field.text()

        matching = False
        if len(empty)>0:
            self.empty_fields(empty)
        else:
            matching = self.checkPasswords()

        if matching:
            self._MainWindow.User = User(Name, NickName, Email, Password)
            print('Login')
            self.Logged_in = True
            self.close()

    def checkPasswords(self):
        passwords = []
        for field in self._input_fields:
            if "password" in field.objectName().lower():
                passwords.append(field.text())

        if passwords[0] == passwords[1]:
            return True
        else:
            self.different_passwords()
            return False

    def empty_fields(self, fields):
        html = "<ul>"
        for field in fields:
            html += f"<li> {field.objectName()[:-5]}</li>" # remove Field at the end of the string
        html += "</ul>"

        QMessageBox.about(
            self,
            "login error",
            "<p>The following fields were not filled in correctly:</p>"
            f"{html}",
        )

    def different_passwords(self):
        QMessageBox.about(
            self,
            "login error",
            "<p>The passwords don't match</p>",
        )

    def closeEvent(self, event):
        if self.Logged_in:
            pass
        else:
            sys.exit() # let the window close

    def get_input_fields(self):
        for widget in self.children():
            if isinstance(widget, QPlainTextEdit) or isinstance(widget, QLineEdit):
                if "password" in widget.objectName().lower():
                    widget.setEchoMode(QtGui.QLineEdit.Password)
                self._input_fields.append(widget)


