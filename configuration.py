# -*- coding: utf-8 -*-

    #si on veut mettre des valeurs par défaut:
    #dico={'chunk' : 1024 , 'rate' : 8000 , 'channels' : 1}
    #print (dico['chunk'])             # affichage d un element



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
        if(fichier0!=None):
            ligne=fichier0.readline()
            while(ligne!=""):                        #tq on est pas en fin de fichier 
                print("debuttour")
                p0=ligne.find('ß')        #p0 est l indice du premier 'ß' , qui est un séparateur d'information
                p1=p0+1+ligne[p0+1:].find('ß') #p1 est le deuxieme
                p2=p1+1+ligne[p1+1:].find('\n')
                cleligne=ligne[:p0]        
                valeurligne=ligne[p0+1:p1]
                typeligne=ligne[p1+1:p2]
                #print(p0)
                #print(p1)
                #print(p2)
                #print(cleligne)
                #print(valeurligne)
                #print(typeligne)
                if (typeligne=="int"):
                    self.dico[cleligne]=int(valeurligne)
                elif (typeligne=="float"):                             
                    self.dico[cleligne]=float(valeurligne)
                else:
                    self.dico[cleligne]=valeurligne
                ligne=fichier0.readline()
            print("fintestboucle")
            fichier0.close()
        


    def close(self):                #on écrit les valeurs dans un fichier
        fichier=open("param.conf", "w")
        if(fichier!=None):
            for key,value in self.dico.items():
                valtype=type(value)
                value_type=str(valtype)
                value_type=value_type.replace('<class \'','')
                value_type=value_type.replace('\'>','')
                fichier.write("{0}ß{1}ß".format(key,value))      # on écrit clé:valeur:type pour chaque couple
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

