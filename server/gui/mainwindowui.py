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
        MainWindow.resize(578, 418)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.actionUser = QAction(MainWindow)
        self.actionUser.setObjectName(u"actionUser")
        self.actionModerator = QAction(MainWindow)
        self.actionModerator.setObjectName(u"actionModerator")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setEnabled(True)
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tableView = QTableView(self.centralwidget)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setMinimumSize(QSize(300, 150))
        self.tableView.setMaximumSize(QSize(1000, 500))
        self.tableView.setAlternatingRowColors(False)
        self.tableView.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.tableView.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.tableView.setSortingEnabled(True)
        self.tableView.verticalHeader().setProperty("showSortIndicator", True)

        self.verticalLayout.addWidget(self.tableView)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 578, 30))
        self.menuLogin = QMenu(self.menubar)
        self.menuLogin.setObjectName(u"menuLogin")
        self.menuLog = QMenu(self.menubar)
        self.menuLog.setObjectName(u"menuLog")
        self.menuGraph = QMenu(self.menubar)
        self.menuGraph.setObjectName(u"menuGraph")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuLogin.menuAction())
        self.menubar.addAction(self.menuLog.menuAction())
        self.menubar.addAction(self.menuGraph.menuAction())
        self.menuLogin.addAction(self.actionUser)
        self.menuLogin.addAction(self.actionModerator)

        self.retranslateUi(MainWindow)
        self.actionUser.triggered.connect(self.actionUser.trigger)
        self.actionModerator.triggered.connect(self.actionModerator.trigger)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Python Client", None))
        self.actionUser.setText(QCoreApplication.translate("MainWindow", u"User", None))
        self.actionModerator.setText(QCoreApplication.translate("MainWindow", u"Moderator", None))
        self.menuLogin.setTitle(QCoreApplication.translate("MainWindow", u"Login", None))
        self.menuLog.setTitle(QCoreApplication.translate("MainWindow", u"Log", None))
        self.menuGraph.setTitle(QCoreApplication.translate("MainWindow", u"Graph", None))
    # retranslateUi