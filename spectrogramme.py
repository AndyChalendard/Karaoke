# -*- coding: utf-8 -*-

from PyQt4.QtCore import *
import pyqtgraph
import numpy
import spectrogrammeBlock

class SpectrogramWidget(pyqtgraph.PlotWidget):

    read_collected = pyqtSignal(numpy.ndarray)

    chunk = None
    rate = None

    def __init__(self, chunk, rate):
        super(SpectrogramWidget, self).__init__()

        # définition des variables
        self.chunk = chunk
        self.rate = rate

        self.img = pyqtgraph.ImageItem()
        self.addItem(self.img)

        # on calcul de nombre de point à retirer pour supprimer les frequence inférieur a 250 hertz
        freqMin = 250
        self.nbPointRetirer = (freqMin*2*(chunk/2+1))/rate

        # définition du tableau de valeurs pour l'image
        self.xSize = 300
        self.img_array = numpy.zeros((self.xSize, chunk/2+1))

        # variable pour la gestion des couleurs
        pos = numpy.array([0., 1., 0.5, 0.25, 0.75])
        color = numpy.array([[0,255,255,255], [255,255,0,255], [0,0,0,255], (0, 0, 255, 255), (255, 0, 0, 255)], dtype=numpy.ubyte)
        cmap = pyqtgraph.ColorMap(pos, color)
        lut = cmap.getLookupTable(0.0, 1.0, 256)

        self.img.setLookupTable(lut)
        self.img.setLevels([-50,40])

        freq = numpy.arange((chunk/2)+1) / (float(chunk)/rate)
        yscale = 1.0/(self.img_array.shape[1]/freq[-1])
        self.img.scale((1./rate)*chunk, yscale)

        self.setLabel('left', 'Frequency', units='Hz')

        # on définit la fenêtre pour la FFT
        self.win = numpy.hanning(chunk)

        # on définit le signal pyqt
        self.read_collected.connect(self.update)

        #on définit les blocks
        self.blocks = spectrogrammeBlock.SpectrogramBlock("block.data", chunk, rate);

        #on insère crée nos blocks
        for i in range(self.xSize/2, self.xSize):
            self.img_array[i:] = self.blocks.getFrame()*-20

    # Données entrante
    def update(self, data):
        # on passe nos données dans la fenêtre, calcul la FFT, et normalise
        spec = numpy.fft.rfft(data*self.win) / self.chunk

        psd = abs(spec)

        # on convertit en dB
        psd = 20 * numpy.log10(psd)

        # supression des basses fréquences
        for i in range(0,self.nbPointRetirer):
            psd[i] = 0

        # définition du seuil de détection
        psd = numpy.where(psd<20, 0, 40)

        # défilement des valeurs
        self.img_array = numpy.roll(self.img_array, -1, 0)

        # insertion des valeurs du micro
        self.img_array[self.xSize/2:self.xSize/2+1] += psd

        # on insère le nouveau block
        self.img_array[-1:] = self.blocks.getFrame()*-20

        # on définit l'image
        self.img.setImage(self.img_array, autoLevels=False)
