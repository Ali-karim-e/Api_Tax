from PyQt5 import QtCore, QtGui, QtWidgets
import pandas as pd

from JsonReader    import  UpdateDB
from SqlConnection.SqlConnection import SQL_Database





class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 20, 731, 91))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(25)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.Taxtab = QtWidgets.QFrame(self.centralwidget)
        self.Taxtab.setGeometry(QtCore.QRect(20, 120, 751, 421))
        font = QtGui.QFont()
        font.setBold(False)
        self.Taxtab.setFont(font)
        self.Taxtab.setAutoFillBackground(False)
        self.Taxtab.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Taxtab.setFrameShadow(QtWidgets.QFrame.Plain)
        self.Taxtab.setObjectName("Taxtab")
        self.label_2 = QtWidgets.QLabel(self.Taxtab)
        self.label_2.setGeometry(QtCore.QRect(80, 30, 391, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.Taxtab)
        self.lineEdit.setGeometry(QtCore.QRect(492, 31, 141, 31))
        self.lineEdit.setStyleSheet("")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.scrollArea = QtWidgets.QScrollArea(self.Taxtab)
        self.scrollArea.setGeometry(QtCore.QRect(20, 90, 341, 320))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 339, 318))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.pushButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton.setGeometry(QtCore.QRect(110, 10, 121, 41))
        self.pushButton.setObjectName("pushButton")
        self.textBrowser = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents)
        self.textBrowser.setGeometry(QtCore.QRect(20, 60, 300, 241))
        self.textBrowser.setObjectName("textBrowser")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.scrollArea_2 = QtWidgets.QScrollArea(self.Taxtab)
        self.scrollArea_2.setGeometry(QtCore.QRect(390, 90, 341, 321))
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 339, 319))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_2)
        self.pushButton_2.setGeometry(QtCore.QRect(110, 10, 121, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents_2)
        self.textBrowser_2.setGeometry(QtCore.QRect(20, 60, 300, 241))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.label_3 = QtWidgets.QLabel(self.Taxtab)
        self.label_3.setEnabled(False)
        self.label_3.setGeometry(QtCore.QRect(490, 60, 211, 21))
        self.label_3.setObjectName("label_3")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:36pt; color:#12098d;\">Tax App</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "Please enter your ID in the opposite box :"))
        self.lineEdit.setToolTip(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.lineEdit.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "Send"))
        self.pushButton_2.setText(_translate("MainWindow", "Inquiry"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ff0000;\">Please enter the correct value !!!!!</span></p></body></html>"))
        self.label_3.setHidden(True)

        """edit by mee"""
        self.pushButton_2.clicked.connect(self.inquiry)
        self.lineEdit.setValidator(QtGui.QIntValidator())
        self.pushButton.clicked.connect(self.send)



    def validation(self):
        Id = self.lineEdit.text()
        conn = SQL_Database().create_server_connection()
        query =f"Select  Id from Msg_TaxQueueHeader Where	Id	=  {Id} "
        sqlid = pd.read_sql(query, conn)
        try:
            sqlid = sqlid['Id'][0]
        except:
            sqlid= 0
        return sqlid

        
    def send(self):
        self.textBrowser.append("This butten not set!!!!! ")

    def inquiry(self):
        Id = self.validation()
        if Id   == 0:
            self.label_3.setHidden(False)
            self.textBrowser_2.clear()
        else:
            Text = UpdateDB(Id).sendingstatuserror()
            if Text == "SUCCESS":
                self.textBrowser_2.setStyleSheet("color: rgb(0, 255, 0);font-size:25pt;")
            elif Text == "ERROR":
                self.textBrowser_2.setStyleSheet("color: rgb(255, 0, 0);font-size:25pt;")
            elif Text == "PENDING":
                self.textBrowser_2.setStyleSheet("color: rgb(255, 255, 0);font-size:25pt;")
            else:
                self.textBrowser_2.setStyleSheet("color: rgb(255, 255, 0);font-size:25pt;")
            self.textBrowser_2.append(Text)
            self.label_3.setHidden(True) 

       
        
        
            




        

    


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
