# -*- coding: utf-8 -*-

import pyaudio
import wave
import time
import numpy

# classe de lecture d un fichier
class LectureAudio():
    pyAudio = None

    setProgress = None

    lecFichier = None
    stream = None

    frameCounter = 0;

    # initialisation de la classe de lecture
    def __init__(self, setProgress):
        self.pyAudio = pyaudio.PyAudio()
        self.setProgress = setProgress

    # retourne l'état de lecture
    def playing(self):
        return self.stream != None

    # callback pour la lecture des données audio
    def callback(self, in_data, frame_count, time_info, status):
        #on récupère nos données
        data = self.lecFichier.readframes(frame_count)
        self.frameCounter+=frame_count

        # si la barre de progression est définit, alors on définit sa valeur via le signal PyQt
        if self.setProgress != None:
            self.setProgress(self.frameCounter*100/self.lecFichier.getnframes())

        return (data, pyaudio.paContinue)

    # lit un fichier wav
    def lectureFichier(self, fichieralire):
        self.frameCounter = 0
        self.progress = 0
        self.lectureStop()

        # on l'ouvre en lecture seule
        self.lecFichier=wave.open(fichieralire,'rb')

        #cree le flux desire
        self.stream = self.pyAudio.open(format=self.pyAudio.get_format_from_width(self.lecFichier.getsampwidth()),
                    channels=self.lecFichier.getnchannels(),
                    rate=self.lecFichier.getframerate(),
                    output=True,
                    stream_callback=self.callback)

    # arrete la lecture
    def lectureStop(self):
        if self.playing() == True:
            # arret du stream et déchargement des variables
            self.stream.stop_stream()
            self.stream.close()
            self.lecFichier.close()

            self.lecFichier = None
            self.stream = None

    # libère la lecture audio
    def close(self):
        if self.playing() == True:
            self.lectureStop()

        self.pyAudio.terminate()
        self.pyAudio = None



# Classe d'enregistrement un fichier audio
class EnregistrementAudio():
    pyAudio = None

    stream = None

    output = None
    frames = None
    framesInt = None
    signal = None

    CHUNK = None
    RATE = None
    FORMAT = None
    CHANNELS = None

    # Fonction d'initialisation de la classe
    def __init__(self, chunk = 1024, rate = 8000, channels = 1, signal = None):
        self.pyAudio = pyaudio.PyAudio()
        self.FORMAT = pyaudio.paInt16
        self.CHUNK = chunk
        self.RATE = rate
        self.CHANNELS = channels
        self.signal = signal

    # retourne l'état de l'enregistrement
    def recording(self):
        return self.stream != None

    # callback de d'enregistrement des données
    def callback(self, in_data, frame_count, time_info, status):
        # on ajoute nos données à la frame total pour l'enregistrement en wav
        self.frames.append(in_data)

        # on convertit les données en tableau numpy
        NpFrameInt = numpy.fromstring(in_data, numpy.int16)
        self.framesInt.extend(NpFrameInt.tolist())

        # on émet nos données via un signal PyQt pour le spectrogramme
        if (self.signal != None):
            self.signal.emit(NpFrameInt)

        return (in_data, pyaudio.paContinue)

    # Fonction d'enregistrement du fichier audio
    def enregistrementFichier(self, nomfichier):
        self.enregistrementStop()

        self.output = nomfichier
        self.frames = []
        self.framesInt = []

        #création du stream d'enregistrement
        self.stream = self.pyAudio.open(format=self.FORMAT, channels=self.CHANNELS,
                        rate=self.RATE, input=True,
                        frames_per_buffer=self.CHUNK,
                        stream_callback=self.callback)

    # Fonction d'arret de l'enregistrement
    def enregistrementStop(self):

        #si on enregistre
        if self.recording():

            #fermeture du stream
            self.stream.stop_stream()
            self.stream.close()
            self.stream = None

            #enregistrement dans le fichier en wav
            fichierEcriture = wave.open(self.output, 'wb')
            fichierEcriture.setnchannels(self.CHANNELS)
            fichierEcriture.setsampwidth(pyaudio.get_sample_size(self.FORMAT))
            fichierEcriture.setframerate(self.RATE)
            fichierEcriture.writeframes(b''.join(self.frames))
            fichierEcriture.close()

    # Foncion de libération de la classe
    def close(self):
        if self.recording():
            self.enregistrementStop()
            
        self.pyAudio.terminate()
        self.pyAudio = None
