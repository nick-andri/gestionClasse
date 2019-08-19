
from classe import Classe

class Etablissement():
    def __init__(self,dico_donnee=None):
        self.dico = dico_donnee
        self.nom = dico_donnee["nom"]
        self.adresse = dico_donnee["adresse"]


        self.listeClasses = []

        for c in dico_donnee["classes"]:
            # creation instance classe
            classe = Classe(c)
            self.listeClasses.append(classe)

    def majDico(self):
        self.dico["nom"] = self.nom
        self.dico["adresse"] = self.adresse

        listeDicoClasses = []

        for c in self.listeClasses:


             listeDicoClasses.append(c.majDico())

        self.dico["classes"]= listeDicoClasses

        return self.dico