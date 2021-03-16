# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 12:13:32 2021

@author: Meltem ERGİN :)
"""

from PyQt5.QtWidgets import QApplication, QMainWindow, QMdiArea, QAction, QMdiSubWindow, QTextEdit
import sys
import frmFonIzle
import frmTumFonAnaliz
from copy import copy


class MDIWindow(QMainWindow):

    count = 0
    def __init__(self):
        try :
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
            
            self.mnuFon.triggered[QAction].connect(self.WindowTrig)
            self.mnuSecenekler.triggered[QAction].connect(self.WindowTrig)
            self.setWindowTitle("MDI Application")
            
            
            global win_subwindow1
            win_subwindow1 = list()
            
            global sub
            sub = list()
            
        except BaseException as e:
            
            print("Bir Hata Oluştu : ", e)
            
    def closeEvent(self, event):
        #print("ana form kapat")
        event.accept()
        
    
    def WindowTrig(self, p):
        try :

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
            
            else:
                myForm = self.findChild(QMdiSubWindow, p.text())
                self.mdi.setActiveSubWindow(myForm)
                
        except BaseException as e:
            
            print("Bir Hata Oluştu : ", e)
            
    def Kapa(self,event , subName, myMenu):
        
        self.mnuSecenekler.removeAction(myMenu)
        
        
app = QApplication(sys.argv)
mdi  =MDIWindow()
mdi.showMaximized()
app.exec_()

