import sys
import images_rc
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QDialog,QMainWindow,QWidget
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QTableWidget,QTableWidgetItem

class showTab(QDialog):
    def __init__(self, current):
        super(showTab, self).__init__()
        loadUi('uploadDialog.ui', self)
        self.setWindowTitle('Finger Table and Files')
        self.fingerTab.setRowCount(4)
        self.fingerTab.setColumnCount(2)
        arr = []

        if current.files.__len__()==0:
            self.Files.addItem('No Files')
        else: 
            for i in current.files:
                self.Files.addItem(i[1])
            

        for i in current.fingerTable.keys():
            arr.append(i)
        for i in range(arr.__len__()):
            self.fingerTab.setItem(i,0, QTableWidgetItem(str(arr[i])))
            self.fingerTab.setItem(i,1, QTableWidgetItem(str(current.fingerTable[arr[i]][2])))



