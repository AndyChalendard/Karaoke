# -*- coding: utf-8 -*-

import pyaudio
import wave
import time


#phase 1: lecture d un fichier
class LectureAudio():
    pyAudio = None

    setProgress = None

    lecFichier = None
    stream = None

    frameCounter = 0;

    # initialisation de la classe de lecture
    def __init__(self, setProgress):
        self.pyAudio=pyaudio.PyAudio()
        self.setProgress = setProgress

    # retourne l'état de lecture
    def playing(self):
        return self.stream != None

    def callback(self, in_data, frame_count, time_info, status):
        data = self.lecFichier.readframes(frame_count)
        self.frameCounter+=frame_count

        if self.setProgress != None:
            self.setProgress(self.frameCounter*100/self.lecFichier.getnframes())

        return (data, pyaudio.paContinue)

    # lit un fichier wav
    def lectureFichier(self, fichieralire):
        self.frameCounter = 0
        self.progress = 0
        self.lectureStop()

        self.lecFichier=wave.open(fichieralire,'rb')      #on l ouvre en lecture seule

        self.stream = self.pyAudio.open(format=self.pyAudio.get_format_from_width(self.lecFichier.getsampwidth()),
                    channels=self.lecFichier.getnchannels(),
                    rate=self.lecFichier.getframerate(),
                    output=True,
                    stream_callback=self.callback)            #cree le flux desire

        #self.stream.start_stream()

    # arrete la lecture
    def lectureStop(self):
        if self.playing() == True:
            self.stream.stop_stream()                #arret du stream
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



#phase 2: enregistrer un fichier audio grace a un micro

class EnregistrementAudio():
    pyAudio = None

    stream = None

    output = None
    frames = None

    CHUNK = 1024
    RATE = 8000        #nombre de frames par seconde , on trouve 44100 ou 8000 ...
    FORMAT = None
    CHANNELS = 1

    def __init__(self):
        self.pyAudio = pyaudio.PyAudio()
        self.FORMAT = pyaudio.paInt16

    # retourne l'état de l'enregistrement
    def recording(self):
        return self.stream != None

    def callback(self, in_data, frame_count, time_info, status):
        self.frames.append(in_data)
        return (in_data, pyaudio.paContinue)

    def enregistrementFichier(self, nomfichier):
        self.enregistrementStop()

        self.output = nomfichier           #fichier de sortie
        self.frames = []

        self.stream = self.pyAudio.open(format=self.FORMAT, channels=self.CHANNELS,       #debut de l enregistrement
                        rate=self.RATE, input=True,                  # pour avoir le micro
                        frames_per_buffer=self.CHUNK,
                        stream_callback=self.callback)

    def enregistrementStop(self):
        if self.recording():
            self.stream.stop_stream()                            #fermeture du stream
            self.stream.close()
            self.stream = None

            fichierEcriture = wave.open(self.output, 'wb')              #enregistrement dans le fichier
            fichierEcriture.setnchannels(self.CHANNELS)
            fichierEcriture.setsampwidth(pyaudio.get_sample_size(self.FORMAT))         #calcule la taille d'un echantillon
            fichierEcriture.setframerate(self.RATE)
            fichierEcriture.writeframes(b''.join(self.frames))
            fichierEcriture.close()
            #chaque frame sur 2 channels (chaque channel sur 2 octet)
            #une donnee du tableau receuilli est sur 4*chunk=4096bits
            #pour que ca marche correctement il faut verifier les parametres du micro.

    def close(self):
        if self.recording():
            self.enregistrementStop()
        self.pyAudio.terminate()
        self.pyAudio = None
