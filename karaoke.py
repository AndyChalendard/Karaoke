# -*- coding: utf-8 -*-

import sys
from PyQt4.QtGui import *

sys.path.insert(0, './UI')

import mainWindows

class MainWindows(QDialog, mainWindows.Ui_Dialog):
    def __init__(self, parent=None):
        super(MainWindows, self).__init__(parent)
        self.setupUi(self)
        self.progressBar.setValue(0)

    def fileSearchClick(self):
        file_dialog = QFileDialog(self)
        file_dialog.setNameFilters(["Fichier audio (*.wav)"])
        file_dialog.selectNameFilter("Fichier audio (*.wav)")
        if (file_dialog.exec_()):
            global AudioFile
            AudioFile = file_dialog.selectedFiles().first()

    def ecouterClick(self):
        if (AudioFile == None):
            self.fileSearchClick()

        if (AudioFile != None):
            print("ecouter")

    def jouerClick(self):
        if (AudioFile == None):
            self.fileSearchClick()

        if (AudioFile != None):
            print("jouer")

if __name__ == "__main__":
    app=QApplication(sys.argv)
    form=MainWindows()
    form.show()

    AudioFile = None;

    app.exec_()
