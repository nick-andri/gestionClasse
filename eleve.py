
from matiere import Matiere

class Eleve():
    def __init__(self,dico_donnee=None):
        self.dico = dico_donnee
        self.nom = dico_donnee["nom"]
        self.prenom = dico_donnee["prenom"]
        self.adresse = dico_donnee["adresse"]
        self.appreciationPP = dico_donnee["appreciationPP"]
        self.listeMatiere = []

        for m in dico_donnee["matieres"]:
            # creation instance note
            mat = Matiere(m)
            self.listeMatiere.append(mat)

    def majDico(self):
        self.dico["nom"] = self.nom
        self.dico["prenom"] = self.prenom
        self.dico["adresse"] = self.adresse
        self.dico["appreciationPP"] = self.appreciationPP

        listeDicoMatieres = []

        for m in self.listeMatiere:


             listeDicoMatieres.append(m.majDico())

        self.dico["matieres"]= listeDicoMatieres

        return self.dico