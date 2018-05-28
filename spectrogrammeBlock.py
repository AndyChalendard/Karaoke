# -*- coding: utf-8 -*-

import numpy

#classe de gestions des blocks sur le spectrogramme
class SpectrogramBlock():

    blockCour = None
    blocks = []
    chunk = None
    rate = None

    chunkAct = 0

    def __init__(self, file, chunk, rate):
        # initialisation des variables
        blocks = []
        chunk = chunk
        rate = rate

        YnbrPt = 0

        # ouverture du fichier
        f = open(file, "r")

        if (f!=None):
            line = f.readline()

            # tant que nous avons pas lue tout le fichier
            while (line != ""):

                # on sépare les deux points
                data = line.split(";")

                # si on a bien deux points
                if (len(data)>=2):
                    a=data[0].split(":")
                    b=data[1].split(":")

                    # si les deux points correpondent bien à deux coordonnées
                    if (len(a)==2 and len(b)==2):
                        # On crée un block a ces coordonnées
                        self.blocks.append(Block(chunk, rate, int(a[0]), int(a[1]), int(b[0]), int(b[1])))
                    else:
                        print("Erreur de données dans le fichier audio.data")
                else:
                    print("Erreur de données dans le fichier audio.data")

                # on lit la ligne suivante
                line = f.readline()

            f.close()

        self.YnbrPt = chunk/2+1
        self.chunkAct = 0

    # fonction qui retourne le tableau 1 dimention corespondant aux rectangles actuel (0 pour pas de rectangles, 1 sinon)
    def getFrame(self):
        # on définit le tableau qui code nos rectangles
        rect = numpy.zeros(self.YnbrPt, dtype=int)

        # si il n'y a pas de blocks courant:
        if (self.blockCour == None):
            # on récupère le prochain block
            if (len(self.blocks)!=0):
                self.blockCour = self.blocks.pop(0)

        # notre chunk actuel est plus recent que notre block
        while (self.blockCour != None and self.blockCour.posFin[0] < self.chunkAct):
            self.blockCour = None
            # on récupère le prochain block
            if (len(self.blocks)!=0):
                self.blockCour = self.blocks.pop(0)

        # si notre block courant existe (il sera dans le bon chunk avec les lignes précédente) et que le block a bien débuté
        if (self.blockCour != None and self.blockCour.posDeb[0]<=self.chunkAct):

            #on définit les 1
            for i in range(self.blockCour.posDeb[1], self.blockCour.posFin[1]):
                rect[i] += 1

        # on incremente le numéro de chunk actuel
        self.chunkAct += 1

        return rect

# classe correspondant a un block
class Block():

    # les coordonnées du block
    posDeb = [0,0] # coordonnée basse à gauche
    posFin = [0,0] # coordonnée haute à droite

    def __init__(self, chunk, rate, x1, y1, x2, y2):
        #si les frequences entrée sont correct
        if (y1>0 and y1<rate/2 and y2>0 and y2<rate/2):
            self.posDeb = [x1, (y1*2*(chunk/2+1))/rate]
            self.posFin = [x2, (y2*2*(chunk/2+1))/rate]
        else:
            print("Mauvaise coordonnée !")
