# -*- coding: utf-8 -*-

#travaux en cours
#je teste ces codes demain matin, car pb ac mon pc , je switcherai avec mon autre tkt

#ce qui est derriere les # sont des test ou des suggestions
def creerDictionnaire():
    #dictionnaire={}         #creer un dictionnaire vide
    #valeurs par defaut : 
    dico={'chunk' : 1024 , 'rate' : 8000 , 'channels' : 1}
    #print (dico)
    #print dico['chunk']
    return dico
    
def affichageDico(dictionnaire):
    for obj in dictionnaire.items()
        print "'{0}' : '{1}'".format(key,value)
    
def dataOnFile(dictionnaire):           #ecrit dans un fichier les elements du dictionnaire
    fichier=open("data.txt", "a")
    for obj in dictionnaire.items():
        fichier.write("'{0}':'{1}'".format(key,value))      # on ecrit clé:valeur pour chaque couple
    fichier.close()


class config():

    def __init__(self):
        dico=creerDictionnaire()
        print("test")

    def close(self):
        dataOnFile(dico)
        self.close()
        print("close")

    def setValue(self, name, value):    #attribution d une valeur à une clé
        dico[name]=value
        print("set")

    def getValue(self, name):               #recuperation d une valeur d une clé dans le dictionnaire
        valeur=dico.get(name)
        print("return value")
        return valeur


        
            

# si ce fichier correpond au fichier d'exécution python
if __name__ == "__main__":
    print("Test config")

