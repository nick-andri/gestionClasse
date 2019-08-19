import sys
from PySide2.QtWidgets import QApplication, QMainWindow,QFileDialog,QListWidgetItem,QWidget
from PySide2.QtCore import QUrl,QTime,QFileInfo
import json
from ui_interface import Ui_Form
from note import Note

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

            # print(dico['academies'][0]['nom'])
            # print(dico['academies'][0]['etablissements'][0]['nom'])
            # print(dico['academies'][0]['etablissements'][0]['classes'][0]['anneeSco'])
            n = Note(dico['academies'][0]['etablissements'][0]['classes'][0]['eleves'][0]['matieres'][0]['notes'][0])
            print(n.nom,n.coef,n.valeur)
            print(n.dico)
            n.nom='nouveau nom'
            print(n.nom)
            n.majDico()
            print(n.dico)
    # window = Fenetre()
    # window.show()
    #
    # sys.exit(app.exec_())