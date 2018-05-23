# -*- coding: utf-8 -*-

    #si on veut mettre des valeurs par défaut:
    #dico={'chunk' : 1024 , 'rate' : 8000 , 'channels' : 1}
    #print (dico['chunk'])             # affichage d un element

#stocker les elements avec un ß en fin de ligne

class config():


    dico={}     #création d'un dictionnaire vide


    def affichageDico(self):
        for key,value in self.dico.items():
            valtype=type(value)
            value_type=str(valtype)         #on récupère le type des valeurs sous forme de chaine de caractères
            print ("{0} : {1} :".format(key,value),value_type)      #on affiche les éléments avec leurs type
            print("\n")


    def __init__(self):
        print("initialisation, lecture des valeurs du fichier")
        fichier0=open("param.conf","r")
        if(fichier0!=None):
            ligne=fichier0.readline()
            while(ligne!=""):                        #tq on est pas en fin de fichier
                elt=ligne.split("ß")
                cleligne=elt[0]
                valeurligne=elt[1]
                typeligne=elt[2]

                if ("int" in typeligne):
                    self.dico[cleligne]=int(valeurligne)
                elif ("float" in typeligne):
                    self.dico[cleligne]=float(valeurligne)
                else:
                    self.dico[cleligne]=valeurligne
                ligne=fichier0.readline()
            fichier0.close()


    def close(self):                #on écrit les valeurs dans un fichier
        fichier=open("param.conf", "w")
        if(fichier!=None):
            for key,value in self.dico.items():
                if (key != ""):
                    value_type=str(type(value))
                    fichier.write("{0}ß{1}ß".format(key,value))      # on écrit clé:valeur:type pour chaque couple
                    fichier.write(value_type)
                    fichier.write("ß")
                    fichier.write("\n")
            print("Paramètres enregistrés !")
        fichier.close()


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
    print("afficher le dico sans la fonction")
    print (class5.dico)
    #class5.getValue('chunk',1024)
    #class5.setValue('chunk',1023)
    #print(class5.dico)
    #class5.getValue('boby',12)
    #class5.getValue('chunk',1024)
    print("le dico s affiche avec la fonction")
    class5.affichageDico()
    class5.close()
