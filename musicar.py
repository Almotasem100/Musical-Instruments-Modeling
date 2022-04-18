from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QMainWindow, QTextEdit, 
    QAction, QFileDialog, QApplication,QMessageBox)
from PyQt5.QtCore import Qt   
from gui import *
import numpy as np

class Musicar(Ui_MainWindow):
    def __init__(self,mainwindow):
        super(Musicar,self).setupUi(mainwindow)
        










if __name__=="__main__":
    import sys
    app=QtWidgets.QApplication(sys.argv)
    MainWindow=QtWidgets.QMainWindow()
    ui=Musicar(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())