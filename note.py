

class Note():
    def __init__(self,dico_donnee=None):
        self.dico = dico_donnee
        self.nom = dico_donnee["nom"]
        self.valeur = dico_donnee["valeur"]
        self.coef = dico_donnee["coef"]


    def majDico(self):
        self.dico["nom"] = self.nom
        self.dico["valeur"] = self.valeur
        self.dico["coef"] = self.coef