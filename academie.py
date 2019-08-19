from etablissement import Etablissement

class Academie():
    def __init__(self,dico_donnee=None):
        self.dico = dico_donnee
        self.nom = dico_donnee["nom"]

        self.listeEtablissements = []

        for e in dico_donnee["etablissements"]:
            # creation instance classe
            etab = Etablissement(e)
            self.listeEtablissements.append(etab)

    def majDico(self):
        self.dico["nom"] = self.nom


        listeDicoEtablissements = []

        for e in self.listeEtablissements:


             listeDicoEtablissements.append(e.majDico())

        self.dico["etablissements"]= listeDicoEtablissements

        return self.dico


