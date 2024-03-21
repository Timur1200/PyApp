import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from configmain import Ui_Dialog
from confighelp import Ui_Help_window

app = QtWidgets.QApplication(sys.argv)

Dialog = QtWidgets.QDialog()
ui = Ui_Dialog()
ui.setupUi(Dialog)

govnoUi = Ui_Help_window()



Dialog.show()


#logic...
def openHelpWindow():
    global Help_window
    Help_window = QtWidgets.QDialog()
    #ui = Ui_Help_window()
    govnoUi.setupUi(Help_window)
    Help_window.show()
    #govnoUi.pushButton_5.clicked.connect(on_button_click)
    #Dialog.close()


    
    

ui.pushButton.clicked.connect(openHelpWindow)


sys.exit(app.exec_())
    
