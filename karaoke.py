# -*- coding: utf-8 -*-

import sys
from PyQt4.QtGui import *

sys.path.insert(0, './UI')
sys.path.insert(0, './Audio')

import mainWindows
import Audio

class MainWindows(QDialog, mainWindows.Ui_Dialog):
    def __init__(self, parent=None):
        super(MainWindows, self).__init__(parent)
        self.setupUi(self)
        self.progressBar.setValue(0)

    def textBrowserSetText(self):
        global audioFile
        self.textBrowser.setText("Fichier selectionne: "+ str(audioFile));

    #Rechercher un nouveau fichier audio
    def fileSearchClick(self):
        file_dialog = QFileDialog(self)

        #Définition des différents filtres
        file_dialog.setNameFilters(["Fichier audio (*.wav)"])
        file_dialog.selectNameFilter("Fichier audio (*.wav)")

        #ouverture de la boite de dialogue
        if (file_dialog.exec_()):
            #Définition de la variable global contenant le fichier à lire
            global audioFile
            audioFile = str(file_dialog.selectedFiles().first())
            self.textBrowserSetText();

    # Ecouter la musique à lire
    def ecouterClick(self):
        # si aucun fichier n'à été définit
        if (audioFile == None):
            # on ouvre la boite de dialogue demandant le fichier
            self.fileSearchClick()

        # on écoute ensuite le fichier
        if (audioFile != None):
            Audio.lecturefichier(audioFile)

    # On veut jouer sur la musique actuelle
    def jouerClick(self):
        # si aucun fichier n'à été définit
        if (audioFile == None):
            # on ouvre la boite de dialogue demandant le fichier
            self.fileSearchClick()

        # on joue sur le fichier
        if (audioFile != None):
            print("jouer")

# si ce fichier correpond au fichier d'exécution python
if __name__ == "__main__":
    # on définit notre fenetre
    app=QApplication(sys.argv)
    form=MainWindows()
    form.show()

    # on définit le fichier audio
    audioFile = None;
    form.textBrowser.setText("Bienvenue sur Karaoke !\n Aucun fichier audio a ete selectionne !");

    # on exécute l'application
    app.exec_()
