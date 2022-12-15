import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow,QMessageBox
from PyQt5.uic import loadUi
# import random
import MySQLdb as mdb

class login(QMainWindow):
    def __init__(self):
        super(login,self).__init__()
        loadUi("login.ui",self)
        self.loginbutton.clicked.connect(self.loginfunction)
        self.loginbutton.clicked.connect(self.gotoscreen2) 
        
    def gotoscreen2(self):
        screen2=verify()
        widget.addWidget(screen2)
        widget.setCurrentIndex(widget.currentIndex()+1)    

    def loginfunction(self):
        # mobile=self.mobile.text()
        # print("OTP is sent to",mobile)
        con=mdb.connect('localhost','root','','login')
        with con:
            cur=con.cursor()
            cur.execute("INSERT INTO login_db(mobile number)"
            "VALUES('%s')" % (''.join(self.mobile.text())))
        
            # QMessageBox.about(self,"Login output","Congrats party hard!!")
            self.close()
        

    # def get_otp():
    #     otp=""
        
    #     otp+= str(random.randint(1,9))
         

class verify(QMainWindow):
    def __init__(self):
        super(verify,self).__init__()
        loadUi("verify.ui",self)
        self.verifybutton.clicked.connect(self.verifyfunction)

    def verifyfunction(self):
        OTP=self.otp.text()
        print("Your OTP is",OTP) 

    



# Login.loginfunction.connect(Verify.open)

app=QApplication(sys.argv)
mainwindow=login()
screen2=verify()
widget=QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.addWidget(screen2)
widget.setFixedWidth(480)
widget.setFixedHeight(620)
widget.show()
app.exec_()          