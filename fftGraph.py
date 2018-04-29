# -*- coding: utf-8 -*-

from PyQt4.QtCore import *
import pyqtgraph
import numpy

class widgetFFT(pyqtgraph.PlotWidget):

    read_collected = pyqtSignal(numpy.ndarray)

    chunk = None
    rate = None

    def __init__(self, chunk, rate):
        super(widgetFFT, self).__init__()

        self.chunk = chunk
        self.rate = rate

        self.win = numpy.hanning(chunk)

        self.setXRange(0, rate/2)
        self.setYRange(-70, 170)

        self.x = numpy.linspace(0, rate/2, (chunk+2)/2)
        self.mn = self.mx = numpy.zeros(len(self.x))
        self.curves = [self.plot(x=self.x, y=numpy.zeros(len(self.x)), pen='k') for i in range(4)]
        self.brushes = [0.4, (100, 100, 255), 0.4]
        self.fills = [pyqtgraph.FillBetweenItem(self.curves[i], self.curves[i+1], self.brushes[i]) for i in range(3)]
        for f in self.fills:
            self.addItem(f)

        self.read_collected.connect(self.update)

    def update(self, data):
        spec = numpy.fft.rfft(data*self.win) / self.chunk
        psd = abs(spec)
        psd = 20 * numpy.log10(psd)

        #partie positive
        y1=psd+numpy.abs(psd)

        #partie négative
        y2=psd-y1/2

        s = 0.01
        self.mn = numpy.where(y2<self.mn, y2, self.mn) * (1-s) + y2 * s
        self.mx = numpy.where(y1>self.mx, y1, self.mx) * (1-s) + y1 * s
        self.curves[0].setData(self.x, self.mn)
        self.curves[1].setData(self.x, y2)
        self.curves[2].setData(self.x, y1)
        self.curves[3].setData(self.x, self.mx)
