# -*- coding: utf-8 -*-

#travaux en cours
#je teste ces codes demain matin, car pb ac mon pc , je switcheri avec mon autre tkt

#ce qui est derriere les # sont des test ou des suggestions
def creerdictionnaire():
    #dictionnaire={}         #creer un dictionnaire vide
    #valeurs par defaut : 
    dico={'chunk' : 1024 , 'rate' : 8000 , 'channels' : 1}
    #print (dico)
    #print dico['chunk']
    return dico

class config():

    def __init__(self):
        dico=creerdictionnaire()
        print("test")

    def close(self):
        self.close()
        print("close")

    def setValue(self, name, value):    #attribution d une valeur à une clé
        dico=creerdictionnaire()
        dico[name]=value
        print("set")

    def getValue(self, name):
        valeur=dico.get(name)
        print("return value")
        return valeur

    def dataOnFile():
        fichier=open("data.txt", "a")
        for obj in dico.items():
            fichier.write("'{0}':'{1}'".format(key,value))      # on ecrit clé:valeur pour chaque couple
        fichier.close()
        
            

# si ce fichier correpond au fichier d'exécution python
if __name__ == "__main__":
    print("Test config")

