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
