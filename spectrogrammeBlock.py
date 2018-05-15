# -*- coding: utf-8 -*-

import numpy

class SpectrogramBlock():

    def __init__(self, file, chunk, rate):
        # initialisation des variables
        self.blocks = []

        # ouverture du fichier
        f = open(file, "r")

        if (f!=None):
            line = f.readline();

            # tant que nous avons pas lue tout le fichier
            while (line != ""):
                data = line.replace("\n","").split(";") # on sépare les deux points
                if (len(data)>=2): # si on a bien deux points
                    a=data[0].split(":")
                    b=data[1].split(":")

                    if (len(a)==2 and len(b)==2): # si les deux points correpondent bien à deux coordonnées
                        self.blocks.append(Block(int(a[0]), int(a[1]), int(b[0]), int(b[1])))
                    else:
                        print("Erreur de données dans le fichier audio.data")
                else:
                    print("Erreur de données dans le fichier audio.data")
                line = f.readline();
            f.close()

class Block():

    def __init__(self, x1, y1, x2, y2):
        print("initblock")
