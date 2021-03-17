# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 12:13:32 2021

@author: Meltem ERGİN :)
"""

from PyQt5.QtWidgets import QApplication, QMainWindow, QMdiArea, QAction, QMdiSubWindow, QTextEdit, QMessageBox
import sys
import frmFonIzle
import frmTumFonAnaliz
from copy import copy
import tarihselveriler as tveri

class MDIWindow(QMainWindow):

    count = 0
    @tveri.hatayakala
    def __init__(self):
    
        super().__init__()

        self.mdi = QMdiArea()
        self.setCentralWidget(self.mdi)
        self.bar = self.menuBar()

        self.mnuSecenekler = self.bar.addMenu("Dosya")
        self.mnuSecenekler.addAction("Kapat")
        self.mnuSecenekler.addSeparator()
        #mnuSecenekler.addAction("Formları Diz")
        
        
        
        self.mnuFon = self.bar.addMenu("Fon")
        self.mnuFon.addAction("Fon İzleme")
        self.mnuFon.addAction("Tüm Fonlar İzleme")
        self.mnuFon.addSeparator()
        self.mnuFon.addAction("Veri Birleştir")
        
        self.mnuFon.triggered[QAction].connect(self.WindowTrig)
        self.mnuSecenekler.triggered[QAction].connect(self.WindowTrig)
        self.setWindowTitle("MDI Application")
        
        
        global win_subwindow1
        win_subwindow1 = list()
        
        global sub
        sub = list()
            
    """
    @tveri.hatayakala
    def closeEvent(self, event):
        #print("ana form kapat")
        
        event.accept()"""
        
    @tveri.hatayakala
    def WindowTrig(self, p):
   

        if p.text() == "Tüm Fonlar İzleme":
            
            MDIWindow.count = MDIWindow.count + 1
            sub.append( QMdiSubWindow())
            
            myForm = copy(frmTumFonAnaliz.Ui_frmTumFonAnaliz())
            
            win_subwindow1.append( myForm)
            win_subwindow1[-1].setupUi(sub[-1])
            
            strTitle = "Tüm Fonlar İzleme " + str(MDIWindow.count)
            sub[-1].setObjectName(strTitle)
            sub[-1].setWindowTitle(strTitle)
            
            

            self.mdi.addSubWindow(sub[-1])
            sub[-1].move(1, 1)
            sub[-1].show()
            
            myMnu = self.mnuSecenekler.addAction(strTitle)
            
            sub[-1].closeEvent = lambda x: self.Kapa(x, strTitle, myMnu)
            
        elif p.text() == "Fon İzleme":
            
            MDIWindow.count = MDIWindow.count + 1
            sub.append( QMdiSubWindow())
            
            myForm = copy(frmFonIzle.Ui_frmFonIzle())
            
            win_subwindow1.append( myForm)
            win_subwindow1[-1].setupUi(sub[-1])
            
            strTitle = "Fon İzleme " + str(MDIWindow.count)
            sub[-1].setObjectName(strTitle)
            sub[-1].setWindowTitle(strTitle)
            
            

            self.mdi.addSubWindow(sub[-1])
            sub[-1].move(1, 1)
            sub[-1].show()
            
            myMnu = self.mnuSecenekler.addAction(strTitle)
            
            sub[-1].closeEvent = lambda x: self.Kapa(x, strTitle, myMnu)
            
            
        elif p.text() == "Kapat":
            
            self.mdi.close()
            
        elif p.text() == "Formları Diz":
            
            self.mdi.cascadeSubWindows()
            
        elif p.text() == "Veri Birleştir":
            
            tveri.veribirlestir()
            
            mesaj = QMessageBox()
            mesaj.setWindowTitle("Bilgi")
            mesaj.setText("Veri Birleştirme Gerçekleşti.")
            mesaj.setIcon(QMessageBox.Information)
            mesaj.exec()
        
        else:
            myForm = self.findChild(QMdiSubWindow, p.text())
            self.mdi.setActiveSubWindow(myForm)
            
        
    @tveri.hatayakala
    def Kapa(self,event , subName, myMenu):
        
        self.mnuSecenekler.removeAction(myMenu)
        
        
app = QApplication(sys.argv)
mdi  =MDIWindow()
mdi.showMaximized()
app.exec_()

