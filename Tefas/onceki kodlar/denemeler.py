 # -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd

from PyQt5.QtCore import * 
from PyQt5.QtGui import * 
from PyQt5.QtWidgets import * 

import sys

import matplotlib.pyplot as plt

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas 
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar 


class pandasModel(QAbstractTableModel):

    def __init__(self, data):
        QAbstractTableModel.__init__(self)
        self._data = data

    def rowCount(self, parent=None):
        return self._data.shape[0]

    def columnCount(self, parnet=None):
        return self._data.shape[1]

    def data(self, index, role=Qt.DisplayRole):
        if index.isValid():
            if role == Qt.DisplayRole:
                return str(self._data.iloc[index.row(), index.column()])
        return None

    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self._data.columns[col]
        return None



class Ui_Form(object):
    
    
    
    def setupUi(self, Form):
        Form.setObjectName("Form")
        #Form.resize(1050, 510)
        
        
    
       
        self.lblDosya = QLabel(Form)
        self.lblDosya.setGeometry(5, 5, 345, 20)
        self.lblDosya.setText("Dosya İsmi")
        
        
        
        self.cmbSira = QComboBox(Form)
        self.cmbSira.setGeometry(5, 35, 170, 20)
        self.cmbSira.addItem ("Sıralama Kolonu")
        
        self.btnSira = QPushButton(Form)
        self.btnSira.setGeometry(340, 35, 40, 20)
        self.btnSira.setText("Sirala")
        
        self.optASC = QRadioButton(Form)
        self.optASC.setGeometry(180, 35, 80, 20)
        self.optASC.setText("Asc")
        self.optASC.setChecked(True)
        self.optDESC = QRadioButton(Form)
        self.optDESC.setGeometry(260, 35, 80, 20)
        self.optDESC.setText("Desc")
        
        """
        self.cmbGrX = QComboBox(Form)
        self.cmbGrX.setGeometry(5, 65, 170, 20)
        self.cmbGrX.addItem ("Graph X Value")
        
        self.cmbGrY = QComboBox(Form)
        self.cmbGrY.setGeometry(180, 65, 170, 20)
        self.cmbGrY.addItem ("Graph Y Value")
        
        self.cmbGr = QComboBox(Form)
        self.cmbGr.setGeometry(5, 95, 170, 20)
        #Grafik tipleri. Arttırılabilir
        self.cmbGr.addItems (["plot", "scatter", "plot_date", "bar", "barh", "stem", "pie", "hist", "boxplot"])
        
        self.btnGr = QPushButton(Form)
        self.btnGr.setGeometry(350, 95, 40, 20)
        self.btnGr.setText("Çiz")
        """
        """self.dock = QDockWidget()
        self.dock.setGeometry(5, 105, 345, 345)"""
        
        
        self.view = QTableView(Form)
        self.view.setGeometry(380, 5, 950, 550)
        
        self.btnDosya = QPushButton(Form)
        self.btnDosya.setGeometry(350, 5, 30, 20)
        self.btnDosya.setText("Seç")
        
        self.btnDosya.clicked.connect(lambda : self.DosyaSec())
        
        #self.cmbSira.currentIndexChanged.connect(lambda : self.Sirala())
    
       
        
        self.btnSira.clicked.connect(lambda : self.Sirala())
        """self.btnGr.clicked.connect(lambda : self.Grafik())"""


        
        
        """self.layout = QVBoxLayout()
        self.layout.addWidget(self.canvas)
        self.layout.
        
        Form.setLayout(self.layout)"""
        
    def veriyukle(self, df, newDF = True ):
        model = pandasModel(df)
        self.view.setModel(model )
        self.view.setSortingEnabled(True)
        
        if newDF :
            self.cmbSira.clear()
            self.cmbSira.addItem ("Sıralama Kolonu")
            self.cmbSira.addItems(df.columns)
               
            """self.cmbGrX.clear()
            self.cmbGrX.addItem ("Graph X Value")
            self.cmbGrX.addItems(df.columns)
            
            self.cmbGrY.clear()
            self.cmbGrY.addItem ("Graph Y Value")
            self.cmbGrY.addItems(df.columns)"""
            
            j= 0
            for i in df.columns :
                j +=1
                lblName = "lbl" + str(j)
                
                self.lblDosya1 = QLabel(lblName )
                self.lblDosya1.setGeometry(5, 165, 345, 20)
                self.lblDosya1.setText(i)
                
        
    def DosyaSec(self):
        dosya = QFileDialog.getOpenFileName( caption ="Dosya Seç", filter="Excell dosyası (*.xlsx)")[0]
     
        self.lblDosya.setText(dosya)
        
        self.lblDosya.setText(dosya)
        
        global df
        global df_copy
        df = pd.read_excel(dosya)
        df_copy = df
        
        
        
        self.veriyukle(df)
        
    def Sirala(self):
        
        if self.cmbSira.currentIndex() != 0 :
           
            global df
            df = df.sort_values(self.cmbSira.currentText(), ascending=self.optASC.isChecked(), axis=0)   
            self.veriyukle(df, False) 
            
            """def Grafik (self):
                
                if self.cmbGrX.currentIndex() != 0 and self.cmbGrY.currentIndex() != 0 : 
                    x = df[self.cmbGrX.currentText()]
                    y = df[self.cmbGrY.currentText()]
                    
                    #df.plot(x = self.cmbGrX.currentText(), y = self.cmbGrY.currentText())
                    
                    self.figure = plt.figure() 
                    
                    self.canvas = FigureCanvas(self.figure)
                    
                    self.figure.clear()
                    ax =  self.figure.add_subplot(111) 
                    
                    if self.cmbGr.currentText() == "plot":
                        ax.plot(x,y)
                    elif self.cmbGr.currentText() == "scatter":
                        ax.plot(x,y)
                    elif self.cmbGr.currentText() == "plot_date":
                        ax.scatter(x,y)
                    elif self.cmbGr.currentText() == "bar":
                        ax.bar(x,y)
                    elif self.cmbGr.currentText() == "barh":
                        ax.barh(x,y)
                    elif self.cmbGr.currentText() == "stem":
                        ax.stem(x,y)
                    elif self.cmbGr.currentText() == "pie":
                        ax.pie(x,y)
                    elif self.cmbGr.currentText() == "hist":
                        ax.hist(x,y)
                    elif self.cmbGr.currentText() == "boxplot":
                        ax.boxplot(x,y)
                        
                
                    
                    ax.set_title (self.cmbGrX.currentText() + " & " + self.cmbGrY.currentText())
                    ax.set_xlabel(self.cmbGrX.currentText())
                    ax.set_ylabel(self.cmbGrY.currentText())
                    
                    self.canvas.draw()"""
            
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    Form = QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    #Form.show()
    Form.showMaximized()
    #Form.showFullScreen()
    sys.exit(app.exec_())




