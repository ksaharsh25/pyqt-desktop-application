from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from login import Ui_Form
# from PyQt5.QtWidgets import 
from PyQt5.QtCore import QRegExp, QRegularExpression
import mysql.connector as mc
from PyQt5.QtWidgets import QWidget,QVBoxLayout,QLineEdit,QPushButton,QDialog,QMessageBox,QLabel,QMainWindow
from PyQt5.QtGui import QValidator,QRegExpValidator
class SecondWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('second window')
        self.setFixedWidth(500)
        self.setFixedHeight(400)
        self.label = QLabel('Welcome', self)
        # self.show()
        
        mainLayout = QVBoxLayout()

        self.input1 = QLineEdit()
        self.input2 = QLineEdit()
        mainLayout.addWidget(self.input1)
        mainLayout.addWidget(self.input2)
        self.updatebutton= QPushButton('Update')
        self.updatebutton.clicked.connect(self.Update)
        mainLayout.addWidget(self.updatebutton)
        self.deletebutton= QPushButton('Delete')
        self.deletebutton.clicked.connect(self.delete)
        mainLayout.addWidget(self.deletebutton)
        self.closeButton = QPushButton('Close')
        self.closeButton.clicked.connect(self.close)
        mainLayout.addWidget(self.closeButton)
        
        self.setLayout(mainLayout)

    def Update(self):

        try:
                db=mc.connect(
                        host="localhost",
                        user="root",
                        password="",
                        database="login"    
                )
                mycursor=db.cursor()   
                email=self.input1.text()
                Password=self.input2.text()
                
                updateq= "UPDATE login_db SET email=%s,Password=%s WHERE Password=%s"
                value=(email,Password)
                mycursor.execute(updateq,value)
                db.commit() 
                message_box=QMessageBox()
                message_box.warning(None,"Success","Updated")
                
                
        except:
                message_box=QMessageBox()
                message_box.warning(None,"Error","Not updated")
                print("Failed")      
    def delete(self):
        try:

                db=mc.connect(
                        host="localhost",
                        user="root",
                        password="",
                        database="login"    
                )
                mycursor=db.cursor()   
                email=self.input1.text()
                
                deleteq= "DELETE FROM login_db WHERE email=%s"
                value=(email,)
                mycursor.execute(deleteq,value)
                db.commit() 
                message_box=QMessageBox()
                message_box.warning(None,"Success","Deleted")
        except:
                message_box=QMessageBox()
                message_box.warning(None,"Error","Not deleted")
                print("Failed")

              
    def displayInfo(self):
        self.show() 
class Window(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui=Ui_Form()
        self.ui.setupUi(self)
        self.ui.loginbutton_2.clicked.connect(self.opensignup)
        self.show()        
            # self.loginbutton_2.clicked.connect(Form.close)
        reg_e = QRegExp("[a-z 0-9]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$")
        i = QRegExpValidator(reg_e, self.ui.email)
        self.ui.email.setValidator(i) 
        self.ui.Password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.ui.loginbutton_2.clicked.connect(self.close)
        # self.ui.loginbutton.clicked.connect(self.close) 
        # self.loginbutton.clicked.connect(self.passinginfo)
        self.ui.loginbutton.clicked.connect(self.insert_data) 
        self.secondWindow = SecondWindow()  
    def opensignup(self):
            from register import Ui_Form
            self.regwindow=QtWidgets.QMainWindow()
            self.ui=Ui_Form()
            self.ui.setupUi(self.regwindow)
            self.regwindow.show()      
    def insert_data(self):
    

            db=mc.connect(
                    host="localhost",
                    user="root",
                    password="",
                    database="login"    
            )
            mycursor=db.cursor()   
            email=self.ui.email.text()
            Password=self.ui.Password.text()

            query="SELECT * FROM login_db WHERE email=%s AND Password=%s"
            value=(email,Password)
            mycursor.execute(query,value)
            saharsh= mycursor.fetchall()
            # if (len(saharsh))>0:
                   
            #         # self.show()
                      
            # else:
                    
                    
                    
            
            if (len(email) and len(Password) )==0:

                    self.ui.email.setPlaceholderText('Please enter Email Id')
                    self.ui.Password.setPlaceholderText('Please enter Password')
                    self.ui.no_user.setText("User not found")
                    print("user not found")
            elif len(email)==0:
                    self.ui.email.setPlaceholderText('Please enter email id')
                    self.ui.no_user.setText("User not found")
                    print("user not found")

            elif len(Password)==0:
                    self.ui.Password.setPlaceholderText('Please enter Password') 
                    self.ui.no_user.setText("User not found")
                    print("user not found")  
            
            elif len(saharsh)>0:
                    self.secondWindow.input1.setText(self.ui.email.text())
                    self.secondWindow.input2.setText(self.ui.Password.text())
                    self.secondWindow.displayInfo()
                    self.close()
                    self.ui.no_user.hide()
                    # self.show()
                    print("user found")
                                                
        
                        # message_box=QMessageBox()
                        # message_box.warning(None,"Error","Input invalid") 
                        # print("user not found")
                        # self.Password_2.setPlaceholderText('Please enter Password')
    
 
        # setting title
        # self.setWindowTitle("Python ")
 
        # # setting geometry
        # self.setGeometry(100, 100, 600, 400)
 
        # calling method
        # self.UiComponents()
 
        # showing all the widgets
       
 
    # method for widgets
    # def UiComponents(self):
 
    #     # creating a push button
    #     button = QPushButton("CLICK", self)
 
    #     # setting geometry of button
    #     button.setGeometry(200, 150, 100, 30)
 
    #     # adding action to a button
    #     button.clicked.connect(self.clickme)
 
    # # action method
    # def clickme(self):
 
    #     # printing pressed
    #     print("pressed")

 
# create pyqt5 app
if __name__=="__main__":
    app = QApplication(sys.argv)
    
    # create the instance of our Window
    window = Window()
    
    # start the app
    sys.exit(app.exec_())