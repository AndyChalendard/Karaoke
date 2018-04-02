import pyaudio
import wave


#phase 1: lecture d un fichier
def lecturefichier(fichieralire) :
    CHUNK = 1024
    lecfichier=wave.open(fichieralire,'r')      #on l ouvre en lecture seule
    p=pyaudio.PyAudio()         #necessaire pr le fonctionnement
    
    
    stream = p.open(format=p.get_format_from_width(lecfichier.getsampwidth()),
                channels=lecfichier.getnchannels(),
                rate=lecfichier.getframerate(),
                output=True)            #cree le flux desire
                

    data = lecfichier.readframes(CHUNK)    #lecture/recuperation des donnees du fichier

    while len(data) > 0:            #lecture du flux
        print("on nest pas la pour etre ici")
        stream.write(data)
        data = lecfichier.readframes(CHUNK)


    stream.stop_stream()     #fermeture du flux
    stream.close()

    p.terminate()           #fermeture de l outil pyaudio
    
    
    
    
