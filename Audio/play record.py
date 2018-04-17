#ce fichier est une fonction a mettre apres le premier fichier audio
#si on veut replay ce qu'on a enregistrer via le micro
#dans ce cas on doit mettre en return de la fonction de l autre fichier le tableau frame.

def lecturerecord(frames) :
    
    play=pyaudio.PyAudio()
    CHUNK = 1024
    RATE = 8000
    FORMAT = pyaudio.paInt16            
    CHANNELS = 1
    
    stream_play=play.open(format=FORMAT,
                      channels=CHANNELS,
                      rate=RATE,
                      output=True)
                      
    for data in frames: 
        stream_play.write(data)
        
    stream_play.stop_stream()
    stream_play.close()
    play.terminate()