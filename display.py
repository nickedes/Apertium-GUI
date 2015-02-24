import sys
from PyQt4 import QtCore, QtGui, uic
form_class = uic.loadUiType("apergui.ui")[0]                 # Load the UI
 
class MyWindowClass(QtGui.QMainWindow, form_class):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.initUI()

    def initUI(self):
    	url='http://127.0.0.1:2737/translate?langpair=en|eo&q=%s'%(self.input.currentText())

app = QtGui.QApplication(sys.argv)
myWindow = MyWindowClass(None)
myWindow.show()
app.exec_()
