import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from configmain import Ui_Dialog
from confighelp import Ui_Help_window

app = QtWidgets.QApplication(sys.argv)

Dialog = QtWidgets.QDialog()
ui = Ui_Dialog()
ui.setupUi(Dialog)
Dialog.show()


#logic...
def openHelpWindow():
    global Help_window
    Help_window = QtWidgets.QDialog()
    ui = Ui_Help_window()
    ui.setupUi(Help_window)
    Help_window.show()
    #Dialog.close()



ui.pushButton.clicked.connect(openHelpWindow)


sys.exit(app.exec_())
    
