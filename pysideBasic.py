import sys

import os

from PySide2 import QtUiTools, QtGui

from PySide2.QtWidgets import QApplication, QMainWindow

 

class MainView(QMainWindow):    

    def __init__(self):

        super().__init__()

        self.setupUI()

 

    def setupUI(self):

        global UI_set

 

        UI_set = QtUiTools.QUiLoader().load(resource_path("main.ui"))
        #------------------------------------------------------------------
        
        
        #------------------------------------------------------------------
        self.setCentralWidget(UI_set)

        self.setWindowTitle("UI TEST")

        self.setWindowIcon(QtGui.QPixmap(resource_path("./images/jbmpa.png")))

        self.resize(800,600)

        self.show()

 

#파일 경로

#pyinstaller로 원파일로 압축할때 경로 필요함

def resource_path(relative_path):

    if hasattr(sys, '_MEIPASS'):

        return os.path.join(sys._MEIPASS, relative_path)

    return os.path.join(os.path.abspath("."), relative_path)

 

if __name__ == '__main__':

    app = QApplication(sys.argv)

    main = MainView()

    #main.show()

    sys.exit(app.exec_())