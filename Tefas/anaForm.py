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
        try :
            super().__init__()
    
            self.mdi = QMdiArea()
            self.setCentralWidget(self.mdi)
            self.bar = self.menuBar()
    
            self.mnuSecenekler = self.bar.addMenu("Dosya")
            self.mnuSecenekler.addAction("Kapat")
            #mnuSecenekler.addAction("Formları Diz")
            
            
            
            self.mnuFon = self.bar.addMenu("Fon")
            self.mnuFon.addAction("Fon İzleme")
            
            self.mnuFon.triggered[QAction].connect(self.WindowTrig)
            self.mnuSecenekler.triggered[QAction].connect(self.WindowTrig)
            self.setWindowTitle("MDI Application")
            
            global win_subwindow1
            win_subwindow1 = list()
        
        except BaseException as e:
            
            print("Bir Hata Oluştu : ", e)
        
    def WindowTrig(self, p):
        try :

            if p.text() == "Fon İzleme":
                
                MDIWindow.count = MDIWindow.count + 1
                sub = QMdiSubWindow()
                
                myForm = copy(frmFonIzle.Ui_frmFonIzle())
                
                win_subwindow1.append( myForm)
                win_subwindow1[-1].setupUi(sub)
                
                sub.setObjectName("Fon İzleme " + str(MDIWindow.count))
                sub.setWindowTitle("Fon İzleme " + str(MDIWindow.count))
                
                

                self.mdi.addSubWindow(sub)
                sub.move(1, 1)
                sub.show()
                
                self.mnuSecenekler.addAction("Fon İzleme " + str(MDIWindow.count))
                
                sub.windowStateChanged.connect(self.formKapa)
                
                
            elif p.text() == "Kapat":
                
                self.mdi.close()
                
            elif p.text() == "Formları Diz":
                
                self.mdi.cascadeSubWindows()
            
            else:
                myForm = self.findChild(QMdiSubWindow, p.text())
                self.mdi.setActiveSubWindow(myForm)
                
        except BaseException as e:
            
            print("Bir Hata Oluştu : ", e)
            
    def formKapa(p,q):
        #print("kapatma işlemi için ...")
        pass
        
app = QApplication(sys.argv)
mdi  =MDIWindow()
mdi.showMaximized()
app.exec_()

