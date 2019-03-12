import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot,QObject
from pyhunter import PyHunter
import os
import csv

class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'Hunter_pro'
        self.left = 10
        self.top = 10
        self.width = 400
        self.height = 140
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # Create textbox
        self.textbox = QLineEdit(self)
        self.textbox.move(20, 20)
        self.textbox.resize(280,40)

        # Create a button in the window
        self.button1 = QPushButton('Text file', self)
        self.button1.move(20,80)
        self.button2 = QPushButton('spreadsheet', self)
        self.button2.move(120,80)

        # connect button to function on_click
        self.button1.clicked.connect(self.Text)
        self.button2.clicked.connect(self.spreadsheet)
        #QObject.connect(self.button2,SIGNAL("clicked()"),spreadsheet)
        self.show()

    @pyqtSlot()
    def Text(self):
        textboxValue = self.textbox.text()
        hunter=PyHunter('Enter key here')
        Temp=hunter.domain_search(textboxValue)
        Temp1=Temp['emails']
        for i in range (0,len(Temp1)):
            temp2=Temp1[i]
            Dom_em=temp2['value']
        file = open(textboxValue + ".txt",'w')
        for i in range (0,len(Temp1)):
            temp2=Temp1[i]
            file.write(temp2['value'])
            file.write('\n')
        QMessageBox.question(self, 'Emails', "The Emails are saved in a text file " , QMessageBox.Ok, QMessageBox.Ok)
        file.close()

    @pyqtSlot()
    def spreadsheet(self):
        textboxValue = self.textbox.text()
        hunter=PyHunter('Enter key here')
        Temp=hunter.domain_search(textboxValue)
        Temp1=Temp['emails']
        for i in range (0,len(Temp1)):
            temp2=Temp1[i]
            Dom_em=temp2['value']
        csv = open(textboxValue + ".csv",'w')
        Column_Title = "S.No.,Email\n"
        csv.write(Column_Title)
        for i in range (0,len(Temp1)):
            Sno = str(i+1)
            temp2=Temp1[i]
            email = temp2['value']
            row = Sno + "," + email + "\n"
            csv.write(row)
        QMessageBox.question(self, 'Emails', "The Emails are saved in a spreadsheet" , QMessageBox.Ok, QMessageBox.Ok)
        csv.close()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
