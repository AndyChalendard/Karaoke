# -*- coding: utf-8 -*-

#travaux en cours

#ce qui est derriere les # sont des test ou des suggestions
def creerdictionnaire():
    #dictionnaire={}         #creer un dictionnaire vide
    #valeurs par defaut : 
    dico={'chunk' : 1024 , 'rate' : 8000 , 'channels' : 1}
    #print (dico)
    #print dico['chunk']

class config():

    def __init__(self):
        creerdictionnaire()
        print("test")

    def close(self):
        print("close")

    def setValue(self, name, value):
        dico=creerdictionnaire()
        dico[name]=value
        print("set")

    def getValue(self, name):
        print("return value")


# si ce fichier correpond au fichier d'exécution python
if __name__ == "__main__":
    print("Test config")

