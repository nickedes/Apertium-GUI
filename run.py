import json
import sys

from requests import get
from PyQt4 import QtGui, uic

# Load the UI
form_class = uic.loadUiType("apertium.ui")[0]

# Todo: Find a better way of populating this list.
key_lang = {
    "eng": "English",
    "epo": "Esperanto"
}

# http://stackoverflow.com/a/19165996
lang_key = dict(zip(key_lang.values(), key_lang.keys()))

# The localhost URLs can also be replaced with the Apertium API
URL = {
    "translate": "http://localhost:2737/translate?langpair=%s|%s&q=%s",
    "pairs": "http://localhost:2737/listPairs"
}


class ApertiumGUI(QtGui.QMainWindow, form_class):

    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.fillcombo()

        self.input.textChanged.connect(self.translate)
        self.translated.clicked.connect(self.translate)

    def translate(self):
        source_key = lang_key[self.sourcelang.currentText()]
        target_Key = lang_key[self.targetlang.currentText()]

        url = URL["translate"] % (source_key, target_Key,
                                  self.input.toPlainText())

        response = json.loads(get(url).text)["responseData"]["translatedText"]
        self.output.setText(response)

    def fillcombo(self):
        response = json.loads(get(URL["pairs"]).text)["responseData"]

        for res in response:
            self.targetlang.addItem(key_lang[res["targetLanguage"]])
            self.sourcelang.addItem(key_lang[res["sourceLanguage"]])


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    mainWindow = ApertiumGUI(None)
    mainWindow.show()
    app.exec_()
