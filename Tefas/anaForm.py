# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 12:13:32 2021

@author: SS
"""

from PyQt5.QtWidgets import QApplication, QMainWindow, QMdiArea, QAction, QMdiSubWindow, QTextEdit
import sys
import frmFonIzle
from copy import copy

class MDIWindow(QMainWindow):

    count = 0
    def __init__(self):
        super().__init__()

        self.mdi = QMdiArea()
        self.setCentralWidget(self.mdi)
        bar = self.menuBar()

        mnuSecenekler = bar.addMenu("Seçenekler")
        mnuSecenekler.addAction("Kapat")
        #mnuSecenekler.addAction("Formları Diz")
        
        
        
        mnuFon = bar.addMenu("Fon")
        mnuFon.addAction("Fon İzleme")
        
        mnuFon.triggered[QAction].connect(self.WindowTrig)
        mnuSecenekler.triggered[QAction].connect(self.WindowTrig)
        self.setWindowTitle("MDI Application")
        
        global win_subwindow1
        win_subwindow1 = list()
        
    def WindowTrig(self, p):
        

        if p.text() == "Fon İzleme":
            
            MDIWindow.count = MDIWindow.count + 1
            sub = QMdiSubWindow()
            
            myForm = copy(frmFonIzle.Ui_frmFonIzle())
            
            win_subwindow1.append( myForm)
            win_subwindow1[-1].setupUi(sub)
            
            sub.setObjectName("Load_Input_window" + str(MDIWindow.count))
            self.mdi.addSubWindow(sub)
            sub.move(1, 1)
            sub.show()
        
        elif p.text() == "Kapat":
            
            self.mdi.close()
            
        elif p.text() == "Formları Diz":
            
            self.mdi.cascadeSubWindows()
        
app = QApplication(sys.argv)
mdi  =MDIWindow()
mdi.showMaximized()
app.exec_()

