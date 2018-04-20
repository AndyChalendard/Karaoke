# -*- coding: utf-8 -*-

#travaux en cours

#ce qui est derriere les # sont des tests
def creerDictionnaire():
    #dictionnaire={}        
    #valeurs par defaut : 
    dico={'chunk' : 1024 , 'rate' : 8000 , 'channels' : 1}
    print (dico)
    #print (dico['chunk'])             # affichage d un element
    return dico
    
def affichageDico(dictionnaire):
    for key,value in dictionnaire.items():
        print ("'{0}' : '{1}'".format(key,value))
    
def dataOnFile(dictionnaire):           #ecrit dans un fichier les elements du dictionnaire,pas l'air de marcher
    fichier=open("data.txt", "a")
    for key,value in dictionnaire.items():
        fichier.write("'{0}':'{1}'".format(key,value))      # on ecrit clé:valeur pour chaque couple
    fichier.close()


class config():
    
    dico=creerDictionnaire()

    def __init__(self):
        print("test")

    def close(self):
        #dataOnFile(self.dico)
        self.close()
        print("close")

    def setValue(self, name, value):    #attribution d une valeur à une clé
        self.dico[name]=value
        print("set")
        #print(self.dico[name])

    def getValue(self, name):               #recuperation d une valeur d une clé dans le dictionnaire
        valeur=self.dico.get(name)
        print("return value")
        #print(valeur)
        return valeur


        
            

# si ce fichier correpond au fichier d'exécution python
if __name__ == "__main__":
    print("Test config")
    
    class5=config()
    print (class5.dico)
    class5.getValue('chunk')
    class5.setValue('chunk',1023)
    print(class5.dico)
    dataOnFile(class5.dico)
    class5.close()