import sys
from PySide2.QtWidgets import QApplication, QMainWindow,QFileDialog,QListWidgetItem,QWidget
from PySide2.QtCore import QUrl,QTime,QFileInfo
import json
from ui_interface import Ui_Form
from note import Note
from matiere import Matiere
from eleve import Eleve
from classe import Classe


class Fenetre(QWidget):
    def __init__(self,parent = None):
        super(Fenetre,self).__init__(parent)

        self.ui = Ui_Form()
        self.ui.setupUi(self)


if __name__ == "__main__":


    app = QApplication(sys.argv)
    filename = "data.json"
    with open(filename,'r') as json_file:
            dico = json.load(json_file)
            # print("dico non modifie")
            # print(dico)
            # print(dico['academies'][0]['nom'])
            # print(dico['academies'][0]['etablissements'][0]['nom'])
            # print(dico['academies'][0]['etablissements'][0]['classes'][0]['anneeSco'])

            ######################################## test objet note #####################################################
            # n = Note(dico['academies'][0]['etablissements'][0]['classes'][0]['eleves'][0]['matieres'][0]['notes'][0])
            # print(n.nom,n.coef,n.valeur)
            # print(n.dico)
            # n.nom='nouveau nom'
            # print(n.nom)
            # n.majDico()
            # print(n.dico)
            #
            # dico['academies'][0]['etablissements'][0]['classes'][0]['eleves'][0]['matieres'][0]['notes'][0]=n.majDico()
            # print("dico final modifier : ")
            # print
            ########################################################## test objet matiere #################################################

            # mat = Matiere(dico['academies'][0]['etablissements'][0]['classes'][0]['eleves'][0]['matieres'][0])
            #
            # print(mat.dico)
            # print(mat.coef)
            #
            # # test ecriture et modif
            # mat.nom = "nouveau nom matiere"
            # print("dico non modifier :")
            # print(mat.dico)
            # # print(mat.nom)
            # print("dico modifier :")
            #
            # dico['academies'][0]['etablissements'][0]['classes'][0]['eleves'][0]['matieres'][0]=mat.majDico()
            # print("dico objet maj:")
            # print(mat.dico)
            # print("dico general maj")
            # print(dico)

            ######################################  test objet eleves #######################################################

            # elf=Eleve(dico['academies'][0]['etablissements'][0]['classes'][0]['eleves'][0])
            # # print(elf.dico)
            # # print(elf.prenom)
            # print(elf.appreciationPP)
            # # test ecriture et modif
            # elf.nom = "nouveau nom eleve"
            # print("dico non modifier :")
            # print(elf.dico)
            #
            # print("dico modifier :")
            #
            # dico['academies'][0]['etablissements'][0]['classes'][0]['eleves'][0]=elf.majDico()
            # print("dico objet maj:")
            # print(elf.dico)
            # print("dico general maj")
            # print(dico)

            #################################### test objet classe ####################################################
            # test creation objet
            classe = Classe(dico['academies'][0]['etablissements'][0]['classes'][0])
            # print(classe.dico)
            # print(classe.nom)
            # print(classe.listeEleves[0].nom)
            # test ecriture et modif
            classe.nom = "nouveau nom de classe"
            print("dico non modifier :")
            print(classe.dico)

            print("dico modifier :")

            dico['academies'][0]['etablissements'][0]['classes'][0] = classe.majDico()
            print("dico objet maj:")
            print(classe.dico)
            print("dico general maj")
            print(dico)



    # window = Fenetre()
    # window.show()
    #
    # sys.exit(app.exec_())