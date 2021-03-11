# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 12:13:32 2021

@author: SS
"""

from PyQt5.QtWidgets import QApplication, QMainWindow, QMdiArea, QAction, QMdiSubWindow, QTextEdit
import sys
import frmFonIzle


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

    def WindowTrig(self, p):
        

        if p.text() == "Fon İzleme":
            
            MDIWindow.count = MDIWindow.count + 1
            sub = QMdiSubWindow()
            self.win_subwindow = frmFonIzle.Ui_frmFonIzle()
            self.win_subwindow.setupUi(sub)
    
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

