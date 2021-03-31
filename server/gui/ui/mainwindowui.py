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
        MainWindow.resize(750, 325)
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
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.MainField = QTextEdit(self.centralwidget)
        self.MainField.setObjectName(u"MainField")

        self.verticalLayout.addWidget(self.MainField)

        self.gridLayout = QGridLayout()
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.CommandLabel = QLabel(self.centralwidget)
        self.CommandLabel.setObjectName(u"CommandLabel")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.CommandLabel.sizePolicy().hasHeightForWidth())
        self.CommandLabel.setSizePolicy(sizePolicy1)
        self.CommandLabel.setMinimumSize(QSize(100, 20))
        self.CommandLabel.setMaximumSize(QSize(300, 20))

        self.gridLayout.addWidget(self.CommandLabel, 0, 0, 1, 1)

        self.CommandField = QTextEdit(self.centralwidget)
        self.CommandField.setObjectName(u"CommandField")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(5)
        sizePolicy2.setVerticalStretch(5)
        sizePolicy2.setHeightForWidth(self.CommandField.sizePolicy().hasHeightForWidth())
        self.CommandField.setSizePolicy(sizePolicy2)
        self.CommandField.setMinimumSize(QSize(150, 35))
        self.CommandField.setMaximumSize(QSize(1920, 35))
        self.CommandField.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.gridLayout.addWidget(self.CommandField, 1, 0, 1, 1)

        self.CommandEnterBtn = QPushButton(self.centralwidget)
        self.CommandEnterBtn.setObjectName(u"CommandEnterBtn")
        self.CommandEnterBtn.setMinimumSize(QSize(70, 35))
        self.CommandEnterBtn.setMaximumSize(QSize(90, 35))

        self.gridLayout.addWidget(self.CommandEnterBtn, 1, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.verticalLayout.setStretch(0, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 750, 30))
        self.menuLog = QMenu(self.menubar)
        self.menuLog.setObjectName(u"menuLog")
        self.menuExtra = QMenu(self.menubar)
        self.menuExtra.setObjectName(u"menuExtra")
        MainWindow.setMenuBar(self.menubar)
#if QT_CONFIG(shortcut)
        self.CommandLabel.setBuddy(self.CommandField)
#endif // QT_CONFIG(shortcut)

        self.menubar.addAction(self.menuLog.menuAction())
        self.menubar.addAction(self.menuExtra.menuAction())
        self.menuLog.addAction(self.actionQuery_Log)
        self.menuLog.addAction(self.actionServer_Log)
        self.menuLog.addAction(self.actionActive_Users)
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
        self.CommandLabel.setText(QCoreApplication.translate("MainWindow", u"Command Input:", None))
        self.CommandEnterBtn.setText(QCoreApplication.translate("MainWindow", u"Enter", None))
        self.menuLog.setTitle(QCoreApplication.translate("MainWindow", u"Log", None))
        self.menuExtra.setTitle(QCoreApplication.translate("MainWindow", u"Extra", None))
    # retranslateUi