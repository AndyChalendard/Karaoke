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
def enregistrer(nomfichier,tempsEnregistrement=10):            #choisir un tempsenregistrement avant de lancer le logiciel

    p = pyaudio.PyAudio()
    RECORD_SECONDS=tempsEnregistrement
    CHUNK = 1024
    RATE = 44100        #nombre de frames par seconde , on trouve 44100 ou 8000 ...
    FORMAT = pyaudio.paInt16
    CHANNELS = 2
    WAVE_OUTPUT_FILENAME = nomfichier           #fichier de sortie

    stream = p.open(format=FORMAT, channels=CHANNELS,       #debut de l enregistrement
                    rate=RATE, input=True,                  # pour avoir le micro
                    frames_per_buffer=CHUNK)

    print("debut recup donnees")

    frames = []

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):          #record par pacquets de 1024b=128o ?
        data = stream.read(CHUNK)           #frame/sec * sec / chunk
        frames.append(data)

    print("fin recup donnees")

    stream.stop_stream()                            #fermeture du stream
    stream.close()
    p.terminate()

    fichierEcriture = wave.open(nomfichier, 'wb')              #enregistrement dans le fichier
    fichierEcriture.setnchannels(CHANNELS)
    fichierEcriture.setsampwidth(audio.get_sample_size(FORMAT))         #calcule la taille d'un echantillon
    fichierEcriture.setframerate(RATE)
    fichierEcriture.writeframes(b''.join(frames))
    fichierEcriture.close()
    #chaque frame sur 2 channels (chaque channel sur 2 octet)
    #une donnee du tableau receuilli est sur 4*chunk=4096bits
    #pour que ca marche correctement il faut verifier les parametres du micro.
