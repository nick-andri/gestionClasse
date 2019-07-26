

class Academie():
     def __init__(self,dico = None) :
         self.nom=dico["nom"]
         self.listeEtablissement=[]
         for e in dico["etablissements"]:
             #creation instance etablissement
             etab = Etablissement(e)
             self.listeEtablissement.append(etab)




