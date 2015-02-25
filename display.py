import sys
import requests
import json
from PyQt4 import QtCore, QtGui, uic

form_class = uic.loadUiType("apergui.ui")[0]               # Load the UI

class MyWindowClass(QtGui.QMainWindow, form_class):

    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.fillcombo()
        self.translate.clicked.connect(self.initUI)
        self.input.textChanged.connect(self.initUI)

    def initUI(self):
        url = 'http://127.0.0.1:2737/translate?langpair=%s|%s&q=%s' % (self.sourcelang.currentText(),self.targetlang.currentText(),
            self.input.toPlainText())
        response = json.loads(requests.get(url).text)['responseData']['translatedText']
        self.output.setText(response)

    def fillcombo(self):
        url = 'http://localhost:2737/listPairs'
        response = json.loads(requests.get(url).text)['responseData']
        for x in response:
            self.targetlang.addItem(x['targetLanguage'])
            self.sourcelang.addItem(x['sourceLanguage'])

app = QtGui.QApplication(sys.argv)
myWindow = MyWindowClass(None)
myWindow.show()
app.exec_()