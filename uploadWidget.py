# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uploadWidget.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Upload(object):
    def setupUi(self, Upload):
        Upload.setObjectName("Upload")
        Upload.resize(400, 238)
        Upload.setMaximumSize(QtCore.QSize(400, 400))
        Upload.setStyleSheet("#Upload{background-image: url(:/images/15136(1).jpg);}")
        self.label = QtWidgets.QLabel(Upload)
        self.label.setGeometry(QtCore.QRect(0, 20, 67, 17))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Upload)
        self.label_2.setGeometry(QtCore.QRect(10, 100, 67, 17))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Upload)
        self.label_3.setGeometry(QtCore.QRect(10, 120, 67, 17))
        self.label_3.setObjectName("label_3")
        self.fingerTab = QtWidgets.QTableWidget(Upload)
        self.fingerTab.setGeometry(QtCore.QRect(70, 80, 321, 141))
        self.fingerTab.setStyleSheet("border: 2px solid grey;\n"
"border-radius : 5px;")
        self.fingerTab.setObjectName("fingerTab")
        self.fingerTab.setColumnCount(0)
        self.fingerTab.setRowCount(0)
        self.Files = QtWidgets.QListWidget(Upload)
        self.Files.setGeometry(QtCore.QRect(70, 10, 321, 61))
        self.Files.setStyleSheet("border: 2px solid grey;\n"
"border-radius : 5px;")
        self.Files.setObjectName("Files")

        self.retranslateUi(Upload)
        QtCore.QMetaObject.connectSlotsByName(Upload)

    def retranslateUi(self, Upload):
        _translate = QtCore.QCoreApplication.translate
        Upload.setWindowTitle(_translate("Upload", "Form"))
        self.label.setText(_translate("Upload", "  Files: "))
        self.label_2.setText(_translate("Upload", "Finger"))
        self.label_3.setText(_translate("Upload", "Table:"))


import images_rc
