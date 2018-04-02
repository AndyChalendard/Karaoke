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


