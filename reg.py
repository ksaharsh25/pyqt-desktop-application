from PyQt5 import QtCore, QtGui, QtWidgets

import mysql.connector as mc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.bgwidget = QtWidgets.QWidget(self.centralwidget)
        self.bgwidget.setGeometry(QtCore.QRect(-10, -40, 561, 671))
        self.bgwidget.setStyleSheet("QWidget#bgwidget{\n"
"background-color:qlineargradient(spread:pad, x1:0.091, y1:0.101636, x2:0.991379, y2:0.977, stop:0 rgba(209, 107, 165, 255), stop:1 rgba(255, 255, 255, 255));}")
        self.bgwidget.setObjectName("bgwidget")
        self.label = QtWidgets.QLabel(self.bgwidget)
        self.label.setGeometry(QtCore.QRect(100, 40, 291, 71))
        self.label.setStyleSheet("font: 36pt \"MS Shell Dlg 2\"; color:rgb(255, 255, 255)")
        self.label.setObjectName("label")
        self.loginbutton = QtWidgets.QPushButton(self.bgwidget)
        self.loginbutton.setGeometry(QtCore.QRect(100, 440, 341, 51))
        self.loginbutton.setStyleSheet("border-radius:20px;\n"
"background-color: rgb(170, 255, 255);\n"
"font: 14pt \"MS Shell Dlg 2\";")
        self.loginbutton.setObjectName("loginbutton")
        self.email = QtWidgets.QLineEdit(self.bgwidget)
        self.email.setGeometry(QtCore.QRect(100, 170, 341, 51))
        self.email.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.email.setObjectName("email")
        self.label_3 = QtWidgets.QLabel(self.bgwidget)
        self.label_3.setGeometry(QtCore.QRect(100, 140, 91, 20))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.label_3.setObjectName("label_3")
        self.error = QtWidgets.QLabel(self.bgwidget)
        self.error.setGeometry(QtCore.QRect(440, 456, 341, 20))
        self.error.setStyleSheet("font: 12pt \"MS Shell Dlg 2\"; color:red;")
        self.error.setText("")
        self.error.setObjectName("error")
        self.Password = QtWidgets.QLineEdit(self.bgwidget)
        self.Password.setGeometry(QtCore.QRect(100, 270, 341, 51))
        self.Password.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.Password.setObjectName("Password")
        self.label_4 = QtWidgets.QLabel(self.bgwidget)
        self.label_4.setGeometry(QtCore.QRect(100, 240, 91, 20))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.bgwidget)
        self.label_5.setGeometry(QtCore.QRect(100, 340, 111, 20))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.label_5.setObjectName("label_5")
        self.Password_2 = QtWidgets.QLineEdit(self.bgwidget)
        self.Password_2.setGeometry(QtCore.QRect(100, 370, 341, 51))
        self.Password_2.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.Password_2.setObjectName("Password_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.loginbutton.clicked.connect(self.openlogin)
        self.loginbutton.clicked.connect(self.insert)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def openlogin(self):
        from log import Ui_Form
        self.window=QtWidgets.QMainWindow()
        self.ui=Ui_Form()
        self.ui.setupUi(self.window)
        self.window.show()
    def insert(self):
    
        try:
                db=mc.connect(
                        host="localhost",
                        user="root",
                        password="",
                        database="login"    
                )
                mycursor=db.cursor()   
                email=self.email.text()
                Password=self.Password.text()

                query="INSERT INTO login_db (email,Password) VALUES (%s,%s)"
                value=(email,Password)
                mycursor.execute(query,value)
                db.commit()
                # self.label_4.setText("Data inserted")       
        except mc.Error as e:
                print("Error")  
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Register Page"))
        self.loginbutton.setText(_translate("MainWindow", "Sign Up"))
        self.label_3.setText(_translate("MainWindow", "Email Id"))
        self.label_4.setText(_translate("MainWindow", "Password"))
        self.label_5.setText(_translate("MainWindow", "Confirm Password"))
if __name__ == "__main__":
        import sys
        app=QtWidgets.QApplication(sys.argv)
        Form=QtWidgets.QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(Form)
        Form.show()
        sys.exit(app.exec_())