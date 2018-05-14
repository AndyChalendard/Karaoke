# -*- coding: utf-8 -*-

    #si on veut mettre des valeurs par défaut:
    #dico={'chunk' : 1024 , 'rate' : 8000 , 'channels' : 1}
    #print (dico['chunk'])             # affichage d un element

#probleme dans close , l28 on peut ecrire que des chaines

class config():

    dico={}     #création d'un dictionnaire vide

    def affichageDico(self):
        for key,value in self.dico.items():
            print("ceci est un test ")
            valtype=type(value)
            value_type=str(valtype)
            value_type=value_type.replace('<class \'','')
            value_type=value_type.replace('\'>','')
            #print(type(value_type))
            #print(value_type)
            #print(valtype)
            print ("{0} : {1} :".format(key,value),value_type)
            print("\n")
            

    def __init__(self):
        print("test")

    def close(self):                #on écrit les valeurs dans un fichier
        fichier=open("param.conf", "w")
        for key,value in self.dico.items():
            valtype=type(value)
            value_type=str(valtype)
            value_type=value_type.replace('<class \'','')
            value_type=value_type.replace('\'>','')
            fichier.write("{0} : {1} : ".format(key,value))      # on écrit clé:valeur pour chaque couple
            fichier.write(value_type)    #<--- ENLEVER CE COMMENTAIRE SI PB RECTIFIÉ
            fichier.write("\n")
        fichier.close()
        print("Paramètres enregistrés !")

    def setValue(self, name, value):    #attribution d'une valeur à une clé
        self.dico[name]=value

    def getValue(self, name, default=None): #récupération d'une valeur de clé dans le dico, sinon renvoit une valeur par défaut
        valeur=self.dico.get(name)
        if (valeur==None):
            valeur=default
        return valeur


# si ce fichier correpond au fichier d'exécution python
if __name__ == "__main__":
    print("Test config")

    class5=config()
    print (class5.dico)
    #class5.getValue('chunk',1024)
    class5.setValue('chunk',1023)
    #print(class5.dico)
    #class5.getValue('boby',12)
    #class5.getValue('chunk',1024)
    class5.affichageDico()
    class5.close()
