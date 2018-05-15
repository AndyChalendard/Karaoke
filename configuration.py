# -*- coding: utf-8 -*-

    #si on veut mettre des valeurs par défaut:
    #dico={'chunk' : 1024 , 'rate' : 8000 , 'channels' : 1}
    #print (dico['chunk'])             # affichage d un element

#On suppose qu'on a en entree un fichier avec des valeurs par defaut dedans (j ai supposé 3 constantes pour l instant) (ligne32)
#je suppose egalemnt que le type d un objet est representé sur 3 caracteres ( int , str....)  (ligne 38)
#j ai supposé enfin , qu on avait que deux types : str, int (lignes 44)

class config():


    dico={}     #création d'un dictionnaire vide


    def affichageDico(self):
        for key,value in self.dico.items():
            valtype=type(value)
            value_type=str(valtype)         #on récupère le type des valeurs sous forme de chaine de caractères
            value_type=value_type.replace('<class \'','')
            value_type=value_type.replace('\'>','')
            print ("{0} : {1} :".format(key,value),value_type)      #on affiche les éléments avec leurs type
            print("\n")
            

    def __init__(self):
        print("initialisation, lecture des valeurs du fichier")
        fichier0=open("param.conf","r")
       # print("testboucle")
        ligne=fichier0.readline()
        for i in range(3):                        #tq on est pas en fin de fichier , a la limite compter le nb de lignes
           # print("debuttour")
            p0=ligne.find(' : ')        #p0 est l indice du premier ' : ' , qui est un séparateur d'information
            p1=p0+3+ligne[p0+3:].find(' : ') #p1 est le deuxieme
            cleligne=ligne[:p0]         #nickel
            valeurligne=ligne[p0+3:p1]
            typeligne=ligne[p1+3:p1+6]
            #print(p0)
            #print(p1)
            #print(cleligne)
            #print(valeurligne)
            #print(typeligne)
            if (typeligne=="int"):
                self.dico[cleligne]=int(valeurligne)
            else:                               #autre type de donnees a prevoir
                self.dico[cleligne]=valeurligne #a voir 
            ligne=fichier0.readline()
           # print("fintour")
       # print("fintestboucle")
        


    def close(self):                #on écrit les valeurs dans un fichier
        fichier=open("param.conf", "w")
        for key,value in self.dico.items():
            valtype=type(value)
            value_type=str(valtype)
            value_type=value_type.replace('<class \'','')
            value_type=value_type.replace('\'>','')
            fichier.write("{0} : {1} : ".format(key,value))      # on écrit clé:valeur:type pour chaque couple
            fichier.write(value_type)
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
    #class5.setValue('chunk',1023)
    #print(class5.dico)
    #class5.getValue('boby',12)
    #class5.getValue('chunk',1024)
    print("le dico s affiche")
    class5.affichageDico()
    class5.close()

#voir comment est representé la fin d un fichier , la fin d une ligne dans un fichier , voir tous les types d objets possibles