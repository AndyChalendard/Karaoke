# -*- coding: utf-8 -*-


    #valeurs par defaut : dico={'chunk' : 1024 , 'rate' : 8000 , 'channels' : 1}
    #print (dico['chunk'])             # affichage d un element

#probleme dans close , l28 on peut ecrire que des chaines

class config():

    dico={}

    def affichageDico(self):
        for key,value in self.dico.items():
            print ("{0} : {1} :".format(key,value))
            valtype=type(value)
            print(valtype)
            print("\n")

    def __init__(self):
        print("test")

    def close(self):                #on ecrit les valeurs dans un fichier
        fichier=open("param.conf", "w")
        for key,value in self.dico.items():
            valtype=type(value)
            fichier.write("{0} : {1} : ".format(key,value))      # on ecrit clé:valeur pour chaque couple
            #fichier.write(valtype)    <--- ENLEVER CE COMMENTAIRE SI PB RECTIFIÉ
            fichier.write("\n")
        fichier.close()
        print("Parametres enregistrés !")

    def setValue(self, name, value):    #attribution d une valeur à une clé
        self.dico[name]=value

    def getValue(self, name, default=None):         #recuperation d une valeur d une clé dans le dio, sinon val. par defaut
        valeur=self.dico.get(name)
        if (valeur==None):
            valeur=default
        return valeur


# si ce fichier correpond au fichier d'exécution python
if __name__ == "__main__":
    print("Test config")

    class5=config()
    print (class5.dico)
    class5.getValue('chunk',1024)
    class5.setValue('chunk',1023)
    print(class5.dico)
    class5.getValue('boby',12)
    class5.getValue('chunk',1024)
    class5.affichageDico()
    class5.close()
