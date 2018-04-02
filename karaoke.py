import sys
from PyQt4.QtGui import *

sys.path.insert(0, './UI')

import mainWindows

class MainWindows(QDialog, mainWindows.Ui_Dialog):
    def __init__(self, parent=None):
        super(MainWindows, self).__init__(parent)
        self.setupUi(self)

    def fileSearchClick(self):
        print("file...")

    def ecouterClick(self):
        print("ecouter")

    def jouerClick(self):
        print("jouer")

app=QApplication(sys.argv)
form=MainWindows()
form.show()
app.exec_()
