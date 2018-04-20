# -*- coding: utf-8 -*-

#travaux en cours
    
    #valeurs par defaut : dico={'chunk' : 1024 , 'rate' : 8000 , 'channels' : 1}
    #print (dico['chunk'])             # affichage d un element
    
    
def dataOnFile(dictionnaire):           #ecrit dans un fichier les elements du dictionnaire,pas l'air de marcher
    fichier=open("data.txt", "a")
    for key,value in dictionnaire.items():
        fichier.write("'{0}':'{1}'".format(key,value))      # on ecrit clé:valeur pour chaque couple
    fichier.close()


class config():
    
    dico={}
    
    def affichageDico(self, dictionnaire):
        for key,value in dictionnaire.items():
            print ("{0} : Type('{1}') : {1}".format(key,value))
        
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

    def getValue(self, name, default):               #recuperation d une valeur d une clé dans le dio, sinon val. par defaut
        valeur=self.dico.get(name)
        if (valeur==None):
            valeur=default 
        print("return value")
        print(valeur)
        return valeur


        
            

# si ce fichier correpond au fichier d'exécution python
if __name__ == "__main__":
    print("Test config")
    
    class5=config()
    print (class5.dico)
    class5.getValue('chunk',1024)
    class5.setValue('chunk',1023)
    print(class5.dico)
    dataOnFile(class5.dico)
    class5.getValue('boby',12)
    class5.getValue('chunk',1024)
    class5.affichageDico(class5.dico)