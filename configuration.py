# -*- coding: utf-8 -*-

class config():

    def __init__(self):
        print("test")

    def close(self):
        print("close")

    def setValue(self, name, value):
        print("set")

    def getValue(self, name):
        print("return value")


# si ce fichier correpond au fichier d'exécution python
if __name__ == "__main__":
    print("Test config")
