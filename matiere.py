from note import Note

class Matiere():
    def __init__(self,dico_donnee=None):
        self.dico = dico_donnee
        self.nom = dico_donnee["nom"]
        self.coef = dico_donnee["coef"]
        self.appreciation = dico_donnee["appreciation"]
        self.listeNotes = []

        for n in dico_donnee["notes"]:
            # creation instance note
            note = Note(n)
            self.listeNotes.append(note)

    def majDico(self):
        self.dico["nom"] = self.nom
        self.dico["coef"] = self.coef
        self.dico["appreciation"] = self.appreciation
        listeDicoNotes = []

        for n in self.listeNotes:


             listeDicoNotes.append(n.majDico())

        self.dico["notes"]= listeDicoNotes

        return self.dico