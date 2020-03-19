# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uploadDialog.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(424, 300)
        Dialog.setStyleSheet("#Dialog{background-image: url(:/images/15136(1).jpg);}")
        Dialog.setSizeGripEnabled(True)
        self.Files = QtWidgets.QListWidget(Dialog)
        self.Files.setGeometry(QtCore.QRect(90, 10, 321, 61))
        self.Files.setStyleSheet("border: 2px solid grey;\n"
"border-radius : 5px;")
        self.Files.setObjectName("Files")
        self.fingerTab = QtWidgets.QTableWidget(Dialog)
        self.fingerTab.setGeometry(QtCore.QRect(90, 90, 281, 181))
        self.fingerTab.setStyleSheet("border: 2px solid grey;\n"
"border-radius : 5px;")
        self.fingerTab.setObjectName("fingerTab")
        self.fingerTab.setColumnCount(2)
        self.fingerTab.setRowCount(5)
        item = QtWidgets.QTableWidgetItem()
        item.setText("New Row")
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        item.setFont(font)
        self.fingerTab.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.fingerTab.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.fingerTab.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.fingerTab.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.fingerTab.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.fingerTab.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.fingerTab.setHorizontalHeaderItem(1, item)
        self.fingerTab.horizontalHeader().setCascadingSectionResizes(False)
        self.fingerTab.verticalHeader().setCascadingSectionResizes(False)
        self.fingerTab.verticalHeader().setDefaultSectionSize(0)
        self.fingerTab.verticalHeader().setMinimumSectionSize(0)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 20, 67, 17))
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(30, 120, 67, 17))
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(30, 100, 67, 17))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        item = self.fingerTab.verticalHeaderItem(1)
        item.setText(_translate("Dialog", "New Row"))
        item = self.fingerTab.verticalHeaderItem(2)
        item.setText(_translate("Dialog", "New Row"))
        item = self.fingerTab.verticalHeaderItem(3)
        item.setText(_translate("Dialog", "New Row"))
        item = self.fingerTab.verticalHeaderItem(4)
        item.setText(_translate("Dialog", "New Row"))
        item = self.fingerTab.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Keys"))
        item = self.fingerTab.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Successor"))
        self.label.setText(_translate("Dialog", "  Files: "))
        self.label_3.setText(_translate("Dialog", "Table:"))
        self.label_2.setText(_translate("Dialog", "Finger"))


import images_rc
