# -*- coding: utf-8 -*-

import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *

sys.path.insert(0, './UI')
sys.path.insert(0, './Audio')

# Import de la fenêtre principale
import mainWindows

# Import de la fenêtre des paramètres
import param

# Import des classes audio
import Audio

# Import du widget spectrogramme
import spectrogramme

# Import de la classe de gestion des paramètres
import configuration


class MainWindows(QDialog, mainWindows.Ui_Dialog):

    # Signal PyQt pour modifier la barre de progression lors de l'écoute d'un fichier audio
    progressChanged = pyqtSignal(int)

    # Fonction d'initialisation de la fenêtre principale
    def __init__(self, widgetSpectrogramme, parent=None):
        super(MainWindows, self).__init__(parent)
        self.setupUi(self)

        # Définition de la barre de progression ainsi que du signal PyQt
        self.progressBar.setValue(0)
        self.progressChanged.connect(self.progressBar.setValue)

        # On définit le widget du spectrogramme
        self.dockWidget.setWidget(widgetSpectrogramme)

    # Fonction de définition de la zone de texte
    def textBrowserSetText(self):
        global audioFile
        self.textBrowser.setText("Fichier selectionne: "+ str(audioFile))

    # Fonction de définition de la valeur de la barre de progression
    def setProgressBar(self, value):
        self.progressChanged.emit(value)

    #Rechercher un nouveau fichier audio
    def fileAudioSearch(self):
        file_dialog = QFileDialog(self)

        #Définition des différents filtres
        file_dialog.setNameFilters(["Fichier audio (*.wav)"])
        file_dialog.selectNameFilter("Fichier audio (*.wav)")

        #ouverture de la boîte de dialogue
        if (file_dialog.exec_()):
            #Définition de la variable globale contenant le fichier à lire
            global audioFile
            audioFile = str(file_dialog.selectedFiles().first())
            self.textBrowserSetText()

    # Fonction du bouton Ecouter (sert à écouter une piste audio)
    def ecouterClick(self):
        # On ouvre la boîte de dialogue demandant le fichier
        self.fileAudioSearch()

        # On écoute ensuite le fichier si il a été selectionné
        if (audioFile != None):
            lectureAudio.lectureFichier(audioFile)

    # Fonction d'ouverture de la fenêtre de configuration
    def parametreClick(self):
        formParam.show()

    # Fonction pour jouer sur une musique
    def jouerClick(self):

        # Si aucun enregistrement est en cours
        if (enregistrementAudio.recording() == False):

            # On enregistre l'audio si la valeur du chemin d'enregistrement est défini
            if (config.getValue("path_saved") != None):
                # on lance l'enregistrement
                enregistrementAudio.enregistrementFichier(config.getValue("path_saved")+"/Karaoke_Save.wav")

                print("Enregistrement..")
        else:
            # On arrête l'enregistrement
            enregistrementAudio.enregistrementStop()
            blockFile = None

            print("Enregistrée")


class ParamWindows(QDialog, param.Ui_Dialog):

    # Fonction d'initialisation de la fenêtre de paramétrage
    def __init__(self, parent=None, config=None):
        super(ParamWindows, self).__init__(parent)
        self.setupUi(self)

        # Si la classe d'enregistrement des paramètres est bien chargé
        if (config!=None):
            # On charge les valeurs dans les champs
            self.Box_Chunk.setValue(config.getValue("chunk", 128))
            self.Box_Rate.setValue(config.getValue("rate", 8000))
            self.Box_Channel.setValue(config.getValue("channel", 1))

    # Fonction de définition de chunk dans la classe d'enregistrement des paramètres
    def SetChunk(self, value):
        config.setValue("chunk", value)

    # Fonction de définition de rate dans la classe d'enregistrement des paramètres
    def SetRate(self, value):
        config.setValue("rate", value)

    # Fonction de définition de channel dans la classe d'enregistrement des paramètres
    def SetChannel(self, value):
        config.setValue("channel", value)

    # Fonction de définition du chemin d'enregistrement dans la classe d'enregistrement des paramètres
    def CheminDEnregistrementClick(self):
        value = str(QFileDialog.getExistingDirectory(self, "Select Directory"))

        #on enregistre si une valeur à été retournée
        if (value != ""):
            config.setValue("path_saved", value)

# si ce fichier correpond au fichier d'exécution python
if __name__ == "__main__":

    #on initialise la config
    config = configuration.config()

    #Initialisation de l'app PyQt
    app=QApplication([])

    #on définit le widget FFT
    widgetSpectrogramme = spectrogramme.SpectrogramWidget(config.getValue("chunk", 128), config.getValue("rate", 8000))

    # on définit notre fenêtre
    form=MainWindows(widgetSpectrogramme)
    form.show()

    #on définit la fenêtre de paramètre
    formParam=ParamWindows(form, config)

    # on initialise la lecture audio
    lectureAudio = Audio.LectureAudio(form.setProgressBar)

    # on initialise l'Enregistrement audio
    enregistrementAudio = Audio.EnregistrementAudio(config.getValue("chunk", 128), config.getValue("rate", 8000), config.getValue("channel", 1), widgetSpectrogramme.read_collected)

    # on définit le fichier audio
    audioFile = None
    form.textBrowser.setText("Bienvenue sur Karaoke !\nAucun fichier audio a ete selectionne !")

    # on exécute l'application
    app.exec_() # Fin lors de la fermeture de la fenêtre principale

    # fermeture de l'application
    print("Fermeture de Karaoke..")

    # on libère la lecture audio
    lectureAudio.close()

    # on libère l'enregistrement audio
    enregistrementAudio.close()

    # on libère la configuration
    config.close()
