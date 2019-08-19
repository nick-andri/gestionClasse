
from eleve import Eleve

class Classe():
    def __init__(self,dico_donnee=None):
        self.dico = dico_donnee
        self.nom = dico_donnee["nom"]
        self.anneeSco = dico_donnee["anneeSco"]
        self.PP = dico_donnee["PP"]

        self.listeEleves = []

        for e in dico_donnee["eleves"]:
            # creation instance eleve
            elev = Eleve(e)
            self.listeEleves.append(elev)

    def majDico(self):
        self.dico["nom"] = self.nom
        self.dico["anneeSco"] = self.anneeSco
        self.dico["PP"] = self.PP

        listeDicoEleves = []

        for e in self.listeEleves:


             listeDicoEleves.append(e.majDico())

        self.dico["eleves"]= listeDicoEleves

        return self.dico