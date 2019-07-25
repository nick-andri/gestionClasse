import sys
from PySide2.QtWidgets import QApplication, QMainWindow,QFileDialog,QListWidgetItem
from PySide2.QtCore import QUrl,QTime,QFileInfo
import json






if __name__ == "__main__":


    # app = QApplication(sys.argv)
    filename = "data.json"
    with open(filename,'r') as json_file:
            dico = json.load(json_file)

            print(dico['academies'][0]['nom'])
            print(dico['academies'][0]['etablissements'][0]['nom'])
            print(dico['academies'][0]['etablissements'][0]['classes'][0]['anneeSco'])

    # sys.exit(app.exec_())