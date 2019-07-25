import sys
from PySide2.QtWidgets import QApplication, QMainWindow,QFileDialog,QListWidgetItem
from PySide2.QtCore import QUrl,QTime,QFileInfo
import json






if __name__ == "__main__":
    app = QApplication(sys.argv)
    filename = "data.json"
    with open(filename,'r') as json_file:
            dico = json.load(json_file)

            print(dico)

    sys.exit(app.exec_())