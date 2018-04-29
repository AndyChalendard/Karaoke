# -*- coding: utf-8 -*-

import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import pyqtgraph

import numpy

sys.path.insert(0, './UI')
sys.path.insert(0, './Audio')

import mainWindows
import param
import Audio

import configuration

class MainWindows(QDialog, mainWindows.Ui_Dialog):

    progressChanged = pyqtSignal(int)

    def __init__(self, widgetFFT, parent=None):
        super(MainWindows, self).__init__(parent)
        self.setupUi(self)
        self.progressBar.setValue(0)
        self.progressChanged.connect(self.progressBar.setValue)
        self.dockWidget.setWidget(widgetFFT)

    def textBrowserSetText(self):
        global audioFile
        self.textBrowser.setText("Fichier selectionne: "+ str(audioFile))

    def setProgressBar(self, value):
        self.progressChanged.emit(value)

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
            lectureAudio.lectureFichier(audioFile)

    def parametreClick(self):
        formParam.show()

    # On veut jouer sur la musique actuelle
    def jouerClick(self):
        # si aucun fichier n'à été définit
        #if (audioFile == None):
            # on ouvre la boite de dialogue demandant le fichier
        #    self.fileSearchClick()

        # on joue sur le fichier
        #if (audioFile != None):
        if enregistrementAudio.recording() == False:
            if (config.getValue("path_saved") != None):
                enregistrementAudio.enregistrementFichier(config.getValue("path_saved")+"/Karaoke_Save.wav")
            print("enregi..")
        else:
            enregistrementAudio.enregistrementStop()
            print("enregistrer")

class ParamWindows(QDialog, param.Ui_Dialog):

    def __init__(self, parent=None):
        super(ParamWindows, self).__init__(parent)
        self.setupUi(self)

    def SetChunk(self, value):
        config.setValue("chunk", value)

    def SetRate(self, value):
        config.setValue("rate", value)

    def SetChannel(self, value):
        config.setValue("channel", value)

    def CheminDEnregistrementClick(self):
        value = str(QFileDialog.getExistingDirectory(self, "Select Directory"))

        if (value != ""):
            config.setValue("path_saved", value)

class SpectrogramWidget(pyqtgraph.PlotWidget):

    read_collected = pyqtSignal(numpy.ndarray)

    chunk = None
    rate = None

    def __init__(self, CHUNKSZ, FS):
        super(SpectrogramWidget, self).__init__()

        self.chunk = CHUNKSZ
        self.rate = FS

        self.img = pyqtgraph.ImageItem()
        self.addItem(self.img)

        self.img_array = numpy.zeros((1000, CHUNKSZ/2+1))

        # bipolar colormap

        pos = numpy.array([0., 1., 0.5, 0.25, 0.75])
        color = numpy.array([[0,255,255,255], [255,255,0,255], [0,0,0,255], (0, 0, 255, 255), (255, 0, 0, 255)], dtype=numpy.ubyte)
        cmap = pyqtgraph.ColorMap(pos, color)
        lut = cmap.getLookupTable(0.0, 1.0, 256)

        self.img.setLookupTable(lut)
        self.img.setLevels([-50,40])

        freq = numpy.arange((CHUNKSZ/2)+1)/(float(CHUNKSZ)/FS)
        yscale = 1.0/(self.img_array.shape[1]/freq[-1])
        self.img.scale((1./FS)*CHUNKSZ, yscale)

        self.setLabel('left', 'Frequency', units='Hz')

        self.win = numpy.hanning(CHUNKSZ)

        self.read_collected.connect(self.update)

    def update(self, data):
        # normalized, windowed frequencies in data chunk

        spec = numpy.fft.rfft(data*self.win) / self.chunk
        # get magnitude

        psd = abs(spec)
        # convert to dB scale

        psd = 20 * numpy.log10(psd)

        # roll down one and replace leading edge with new data

        self.img_array = numpy.roll(self.img_array, -1, 0)
        self.img_array[-1:] = psd

        self.img.setImage(self.img_array, autoLevels=False)

# si ce fichier correpond au fichier d'exécution python
if __name__ == "__main__":
    #on initialise la config
    config = configuration.config()

    #Initialisation de l'app PyQt
    app=QApplication([])

    #on définit le widget FFT
    widgetFFT = SpectrogramWidget(config.getValue("chunk", 1024), config.getValue("rate", 8000))
    widgetFFT.show()

    # on définit notre fenetre
    form=MainWindows(widgetFFT)
    form.show()

    #on définit la fenetre de paramètre
    formParam=ParamWindows(form)

    # on initialise la lecture audio
    lectureAudio = Audio.LectureAudio(form.setProgressBar)

    # on initialise l'Enregistrement audio
    enregistrementAudio = Audio.EnregistrementAudio(config.getValue("chunk", 1024), config.getValue("rate", 8000), config.getValue("channel", 1), widgetFFT.read_collected)

    # on définit le fichier audio
    audioFile = None;
    form.textBrowser.setText("Bienvenue sur Karaoke !\nAucun fichier audio a ete selectionne !")

    # on exécute l'application
    app.exec_()

    # fermeture de l'application
    print("Fermeture de Karaoke")

    # on libère la lecture audio
    lectureAudio.close()

    # on libère l'enregistrement audio
    enregistrementAudio.close()

    # on libère la configuration
    config.close()
