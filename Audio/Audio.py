import pyaudio
import wave
import time


#phase 1: lecture d un fichier
def lecturefichier(fichieralire) :
   
    lecfichier=wave.open(fichieralire,'r')      #on l ouvre en lecture seule
    p=pyaudio.PyAudio()         #necessaire pr le fonctionnement
    
    
    def callback(in_data, frame_count, time_info, status):
        data = wf.readframes(frame_count)
        return (data, pyaudio.paContinue)
    
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                channels=wf.getnchannels(),
                rate=wf.getframerate(),
                output=True,
                stream_callback=callback)            #cree le flux desire
                

    stream.start_stream()       
    
    while stream.is_active():
        time.sleep(0.1)


    stream.stop_stream()                #arret du stream
    stream.close()
    lecfichier.close()

    p.terminate()           #fermeture de l outil pyaudio
    
    
    
    
#phase 2: enregistrer un fichier audio grace a un micro


def enregistrer(nomfichier,tempsEnregistrement=10):            #choisir un tempsenregistrement avant de lancer le logiciel
    
    p = pyaudio.PyAudio()   
    RECORD_SECONDS=tempsEnregistrement
    CHUNK = 1024
    RATE = 44100        #nombre de frames par seconde , pk 44100?
    FORMAT = pyaudio.paInt16            #?
    CHANNELS = 2                    
    WAVE_OUTPUT_FILENAME = nomfichier           #fichier de sortie
    
    stream = p.open(format=FORMAT, channels=CHANNELS,       #debut de l enregistrement
                    rate=RATE, input=True,                  # pour avoir le micro
                    frames_per_buffer=CHUNK)
                    
    print("debut recup donnees")
    
    frames = []

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):          #record par pacquets de 1024b=128o ?
        data = stream.read(CHUNK)
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
