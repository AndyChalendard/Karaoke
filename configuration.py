# -*- coding: utf-8 -*-

class config():

    dico={}     #création d'un dictionnaire vide

    def __init__(self):

        print("Chargement des paramètres")

        fichier0=open("param.conf","r")
        if(fichier0!=None):
            ligne=fichier0.readline()

            # Tant que l'on est pas en fin de fichier
            while(ligne!=""):
                # On sépare la ligne en éléments distinct
                elt=ligne.split("ß")
                cleligne=elt[0]
                valeurligne=elt[1]
                typeligne=elt[2]

                # On convertit l'élément dans son type
                if ("int" in typeligne):
                    self.dico[cleligne]=int(valeurligne)
                elif ("float" in typeligne):
                    self.dico[cleligne]=float(valeurligne)
                else:
                    self.dico[cleligne]=valeurligne

                # On lit la ligne suivante
                ligne=fichier0.readline()

            fichier0.close()

    # Fonction d'affichage du dictionnaire des paramètres
    def affichageDico(self):

        # On parcours tous les éléments
        for key,value in self.dico.items():
            valueType=str(type(value))

            #on affiche l'élément avec son type
            print ("{0} : {1} :".format(key,value),valueType)
            print("\n")

    # Fonction de libération de la classe
    def close(self):
        fichier=open("param.conf", "w")
        if(fichier!=None):

            # On parcours tous les éléments
            for key,value in self.dico.items():
                if (key != ""):

                    # On enregistre le paramètre de la forme: 'keyßvalueßtype'
                    valueType=str(type(value))
                    fichier.write("{0}ß{1}ß".format(key,value))
                    fichier.write(valueType)
                    fichier.write("ß")
                    fichier.write("\n")

            print("Paramètres enregistrés !")

        fichier.close()

    # Fonction de définition d'une clef
    def setValue(self, name, value):
        self.dico[name]=value

    # Fonction de récupération d'une valeur de clef, si la clef n'existe pas on retourne la valeur par défaut
    def getValue(self, name, default=None):
        valeur=self.dico.get(name)

        # Si la valeur est inexistante, alors on charge la valeur par défaut
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
