# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindowIhOskZ.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

# from PySide2.QtCore import *
# from PySide2.QtGui import *
# from PySide2.QtWidgets import *

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(490, 349)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.actionUser = QAction(MainWindow)
        self.actionUser.setObjectName(u"actionUser")
        self.actionModerator = QAction(MainWindow)
        self.actionModerator.setObjectName(u"actionModerator")
        self.actiontest = QAction(MainWindow)
        self.actiontest.setObjectName(u"actiontest")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setEnabled(True)
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(u"textEdit")

        self.verticalLayout.addWidget(self.textEdit)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 490, 30))
        self.menuLogin = QMenu(self.menubar)
        self.menuLogin.setObjectName(u"menuLogin")
        self.menuLog = QMenu(self.menubar)
        self.menuLog.setObjectName(u"menuLog")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuLogin.menuAction())
        self.menubar.addAction(self.menuLog.menuAction())
        self.menuLogin.addAction(self.actionUser)
        self.menuLogin.addAction(self.actionModerator)
        self.menuLog.addAction(self.actiontest)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Python Client", None))
        self.actionUser.setText(QCoreApplication.translate("MainWindow", u"User", None))
        self.actionModerator.setText(QCoreApplication.translate("MainWindow", u"Moderator", None))
        self.actiontest.setText(QCoreApplication.translate("MainWindow", u"test", None))
        self.menuLogin.setTitle(QCoreApplication.translate("MainWindow", u"Login", None))
        self.menuLog.setTitle(QCoreApplication.translate("MainWindow", u"Log", None))
    # retranslateUi