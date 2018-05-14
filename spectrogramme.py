# -*- coding: utf-8 -*-

from PyQt4.QtCore import *
import pyqtgraph
import numpy

class SpectrogramWidget(pyqtgraph.PlotWidget):

    read_collected = pyqtSignal(numpy.ndarray)

    chunk = None
    rate = None

    def __init__(self, chunk, rate):
        super(SpectrogramWidget, self).__init__()

        self.chunk = chunk
        self.rate = rate

        self.img = pyqtgraph.ImageItem()
        self.addItem(self.img)

        self.img_array = numpy.zeros((1000, chunk/2+1))

        # bipolar colormap
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

        self.win = numpy.hanning(chunk)

        self.read_collected.connect(self.update)

    def update(self, data):
        # normalized, windowed frequencies in data chunk
        spec = numpy.fft.rfft(data*self.win) / self.chunk

        # get magnitude
        psd = abs(spec)

        # convert to dB scale
        psd = 20 * numpy.log10(psd)

        #définition du seuil de détection
        psd = numpy.where(psd<20, 0, -20)

        # roll down one and replace leading edge with new data
        self.img_array = numpy.roll(self.img_array, -1, 0)
        self.img_array[-1:] = psd

        self.img.setImage(self.img_array, autoLevels=False)
