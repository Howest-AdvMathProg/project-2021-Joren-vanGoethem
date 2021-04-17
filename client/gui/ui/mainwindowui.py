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
        MainWindow.resize(703, 414)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.actiontest = QAction(MainWindow)
        self.actiontest.setObjectName(u"actiontest")
        self.actionQuery_Log = QAction(MainWindow)
        self.actionQuery_Log.setObjectName(u"actionQuery_Log")
        self.actionServer_Log = QAction(MainWindow)
        self.actionServer_Log.setObjectName(u"actionServer_Log")
        self.actionActive_Users = QAction(MainWindow)
        self.actionActive_Users.setObjectName(u"actionActive_Users")
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setEnabled(True)
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.Resultlabel = QLabel(self.centralwidget)
        self.Resultlabel.setObjectName(u"Resultlabel")

        self.gridLayout.addWidget(self.Resultlabel, 0, 0, 1, 1)

        self.commandfield = QPlainTextEdit(self.centralwidget)
        self.commandfield.setObjectName(u"commandfield")

        self.gridLayout.addWidget(self.commandfield, 1, 1, 1, 1)

        self.commandlabel = QLabel(self.centralwidget)
        self.commandlabel.setObjectName(u"commandlabel")

        self.gridLayout.addWidget(self.commandlabel, 0, 1, 1, 1)

        self.Searchbutton = QPushButton(self.centralwidget)
        self.Searchbutton.setObjectName(u"Searchbutton")

        self.gridLayout.addWidget(self.Searchbutton, 2, 1, 1, 1)

        self.ResultTable = QTableView(self.centralwidget)
        self.ResultTable.setObjectName(u"ResultTable")
        self.ResultTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.ResultTable.setAlternatingRowColors(True)
        self.ResultTable.setSortingEnabled(True)
        self.ResultTable.verticalHeader().setProperty("showSortIndicator", True)

        self.gridLayout.addWidget(self.ResultTable, 1, 0, 2, 1)

        self.gridLayout.setColumnStretch(0, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 703, 30))
        self.menuExtra = QMenu(self.menubar)
        self.menuExtra.setObjectName(u"menuExtra")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuExtra.menuAction())
        self.menuExtra.addAction(self.actiontest)
        self.menuExtra.addAction(self.actionAbout)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Python Client", None))
        self.actiontest.setText(QCoreApplication.translate("MainWindow", u"test", None))
        self.actionQuery_Log.setText(QCoreApplication.translate("MainWindow", u"Query Log", None))
        self.actionServer_Log.setText(QCoreApplication.translate("MainWindow", u"Server Log", None))
        self.actionActive_Users.setText(QCoreApplication.translate("MainWindow", u"Active Users", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.Resultlabel.setText(QCoreApplication.translate("MainWindow", u"Result", None))
        self.commandfield.setPlainText(QCoreApplication.translate("MainWindow", u"{\n"
"  \"event\": \"SEARCH\",\n"
"  \"data\": {\n"
"    \"query\": {\n"
"      \"column\": \"\",\n"
"      \"value\": \"\"\n"
"    },\n"
"    \"type\": \"column\",\n"
"    \"exact\": false\n"
"  }\n"
"}", None))
        self.commandlabel.setText(QCoreApplication.translate("MainWindow", u"Search Command", None))
        self.Searchbutton.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.menuExtra.setTitle(QCoreApplication.translate("MainWindow", u"Extra", None))
    # retranslateUi

