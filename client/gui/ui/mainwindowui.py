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
        self.actionGraph_view = QAction(MainWindow)
        self.actionGraph_view.setObjectName(u"actionGraph_view")
        self.actionDataset_Info = QAction(MainWindow)
        self.actionDataset_Info.setObjectName(u"actionDataset_Info")
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setEnabled(True)
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.Searchbutton = QPushButton(self.centralwidget)
        self.Searchbutton.setObjectName(u"Searchbutton")

        self.gridLayout.addWidget(self.Searchbutton, 2, 1, 1, 1)

        self.commandlabel = QLabel(self.centralwidget)
        self.commandlabel.setObjectName(u"commandlabel")

        self.gridLayout.addWidget(self.commandlabel, 0, 1, 1, 1)

        self.Resultlabel = QLabel(self.centralwidget)
        self.Resultlabel.setObjectName(u"Resultlabel")

        self.gridLayout.addWidget(self.Resultlabel, 0, 0, 1, 1)

        self.ResultTable = QTableView(self.centralwidget)
        self.ResultTable.setObjectName(u"ResultTable")
        self.ResultTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.ResultTable.setAlternatingRowColors(True)
        self.ResultTable.setSortingEnabled(True)
        self.ResultTable.verticalHeader().setProperty("showSortIndicator", True)

        self.gridLayout.addWidget(self.ResultTable, 1, 0, 2, 1)

        self.commandfield = QPlainTextEdit(self.centralwidget)
        self.commandfield.setObjectName(u"commandfield")

        self.gridLayout.addWidget(self.commandfield, 1, 1, 1, 1)

        self.gridLayout.setColumnStretch(0, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 703, 30))
        self.menubar.setDefaultUp(False)
        self.menubar.setNativeMenuBar(True)
        self.menuExtra = QMenu(self.menubar)
        self.menuExtra.setObjectName(u"menuExtra")
        self.menuAbout = QMenu(self.menubar)
        self.menuAbout.setObjectName(u"menuAbout")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuExtra.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())
        self.menuExtra.addAction(self.actionGraph_view)
        self.menuExtra.addAction(self.actionDataset_Info)
        self.menuAbout.addAction(self.actionAbout)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Python Client", None))
        self.actionGraph_view.setText(QCoreApplication.translate("MainWindow", u"Graph view", None))
        self.actionDataset_Info.setText(QCoreApplication.translate("MainWindow", u"Dataset Info", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.Searchbutton.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.commandlabel.setText(QCoreApplication.translate("MainWindow", u"Search Command", None))
        self.Resultlabel.setText(QCoreApplication.translate("MainWindow", u"Result", None))
        self.menuExtra.setTitle(QCoreApplication.translate("MainWindow", u"Extra", None))
        self.menuAbout.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

