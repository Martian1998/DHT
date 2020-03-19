# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dhtgui.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(599, 458)
        MainWindow.setMaximumSize(QtCore.QSize(800, 600))
        MainWindow.setStyleSheet("#centralwidget{background-image: url(:/images/background(2).jpg);}\n"
"")
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.leaveBtn = QtWidgets.QPushButton(self.centralwidget)
        self.leaveBtn.setGeometry(QtCore.QRect(370, 380, 201, 25))
        self.leaveBtn.setStyleSheet("#leaveBtn {background-color: rgb(204, 0, 0);border: 1px solid red;\n"
"    background-color: rgb(245, 121, 0);\n"
"border-radius: 4px;}")
        self.leaveBtn.setObjectName("leaveBtn")
        self.appTitle = QtWidgets.QLabel(self.centralwidget)
        self.appTitle.setGeometry(QtCore.QRect(130, 0, 331, 41))
        self.appTitle.setObjectName("appTitle")
        self.status = QtWidgets.QLabel(self.centralwidget)
        self.status.setGeometry(QtCore.QRect(10, 410, 71, 31))
        self.status.setObjectName("status")
        self.statusVal = QtWidgets.QLabel(self.centralwidget)
        self.statusVal.setGeometry(QtCore.QRect(70, 410, 101, 31))
        self.statusVal.setObjectName("statusVal")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(50, 140, 401, 151))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.downloadFile = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.downloadFile.setObjectName("downloadFile")
        self.horizontalLayout_4.addWidget(self.downloadFile)
        self.downloadBtn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.downloadBtn.setStyleSheet("background-color: rgb(138, 226, 52); border: 0.5 px solid rgb(195, 252, 27);\n"
"border-radius: 3px;\n"
"margin:10px;\n"
"padding : 5px;")
        self.downloadBtn.setObjectName("downloadBtn")
        self.horizontalLayout_4.addWidget(self.downloadBtn)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.uploadFile = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.uploadFile.setObjectName("uploadFile")
        self.horizontalLayout_6.addWidget(self.uploadFile)
        self.uploadBtn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.uploadBtn.setStyleSheet("background-color: rgb(138, 226, 52);border: 0.5px solid rgb(195, 252, 27); border-radius: 4px; padding: 5px; margin:10px;")
        self.uploadBtn.setObjectName("uploadBtn")
        self.horizontalLayout_6.addWidget(self.uploadBtn)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem1)
        self.showTab = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.showTab.setStyleSheet("background-color: rgb(245, 121, 0);")
        self.showTab.setObjectName("showTab")
        self.horizontalLayout_7.addWidget(self.showTab)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(10, 390, 160, 31))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.port = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        self.port.setObjectName("port")
        self.horizontalLayout_8.addWidget(self.port)
        self.portNo = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        self.portNo.setText("")
        self.portNo.setObjectName("portNo")
        self.horizontalLayout_8.addWidget(self.portNo)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 599, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.leaveBtn.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>Leave The DHT</p></body></html>"))
        self.leaveBtn.setText(_translate("MainWindow", "LEAVE"))
        self.appTitle.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:30pt; font-weight:600; color:#5c3566;\">DHT</span></p></body></html>"))
        self.status.setText(_translate("MainWindow", "Status:"))
        self.statusVal.setText(_translate("MainWindow", "Idle"))
        self.downloadBtn.setText(_translate("MainWindow", "Download"))
        self.uploadBtn.setText(_translate("MainWindow", "Upload"))
        self.showTab.setText(_translate("MainWindow", "Show Finger Table and Files"))
        self.port.setText(_translate("MainWindow", "Hash:"))


import Resources_rc
import images_rc
