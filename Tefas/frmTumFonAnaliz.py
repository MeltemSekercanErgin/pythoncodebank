# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 11:05:46 2021

@author: Meltem ERGİN :)
"""


from PyQt5 import QtCore, QtGui, QtWidgets
from datetime import date, datetime
import tarihselveriler as tveri
import pandas as pd



class Ui_frmTumFonAnaliz():
    
    @tveri.hatayakala
    def setupUi(self, frmTumFonAnaliz):
    
        frmTumFonAnaliz.setObjectName("frmTumFonAnaliz")
        frmTumFonAnaliz.resize(1320, 670)
        
        
        self.tabWidget = QtWidgets.QTabWidget(frmTumFonAnaliz)
        self.tabWidget.setGeometry(QtCore.QRect(10, 110, 1300, 550))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.lstAlSat = QtWidgets.QListWidget(self.tab)
        self.lstAlSat.setGeometry(QtCore.QRect(10, 10, 1270, 505))
        self.lstAlSat.setObjectName("listView")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.lstTrend = QtWidgets.QListWidget(self.tab_2)
        self.lstTrend.setGeometry(QtCore.QRect(10, 10, 1270, 505))
        self.lstTrend.setObjectName("listView1")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.lstKazanc = QtWidgets.QListWidget(self.tab_3)
        self.lstKazanc.setGeometry(QtCore.QRect(10, 10, 1270, 505))
        self.lstKazanc.setObjectName("listView2")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.txtOzet = QtWidgets.QPlainTextEdit(self.tab_4)
        self.txtOzet.setGeometry(QtCore.QRect(10, 10, 1270, 505))
        self.txtOzet.setObjectName("plainTextEdit")
        self.tabWidget.addTab(self.tab_4, "")
        self.groupBox = QtWidgets.QGroupBox(frmTumFonAnaliz)
        self.groupBox.setGeometry(QtCore.QRect(10, 60, 941, 51))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        
        self.dtTarih1 = QtWidgets.QDateEdit(self.groupBox)
        self.dtTarih1.setGeometry(QtCore.QRect(80, 13, 110, 22))
        self.dtTarih1.setObjectName("dtTarih1")
        dt = date.today()
        dt = dt.replace(year=dt.year-1)
        self.dtTarih1.setDate(dt)

        self.dtTarih2 = QtWidgets.QDateEdit(self.groupBox)
        self.dtTarih2.setGeometry(QtCore.QRect(200, 13, 110, 22))
        self.dtTarih2.setObjectName("dtTarih2")
        self.dtTarih2.setDate(date.today())
       
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(344, 13, 150, 16))
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 13, 61, 16))
        self.label.setObjectName("label")
        
        self.txtHO1 = QtWidgets.QLineEdit(self.groupBox)
        self.txtHO1.setGeometry(QtCore.QRect(494, 13, 70, 20))
        self.txtHO1.setObjectName("txtHO1")
        self.txtHO1.setText("30")
        self.txtHO2 = QtWidgets.QLineEdit(self.groupBox)
        self.txtHO2.setGeometry(QtCore.QRect(574, 13, 70, 20))
        self.txtHO2.setObjectName("txtHO2")
        self.txtHO2.setText("50")
        self.txtHO3 = QtWidgets.QLineEdit(self.groupBox)
        self.txtHO3.setGeometry(QtCore.QRect(654, 13, 70, 20))
        self.txtHO3.setObjectName("txtHO3")
        self.txtHO3.setText("200")
        
        self.btnFonAnaliz = QtWidgets.QPushButton(self.groupBox)
        self.btnFonAnaliz.setGeometry(QtCore.QRect(770, 13, 130, 20))
        self.btnFonAnaliz.setObjectName("btnFonAnaliz")
        
        
        self.retranslateUi(frmTumFonAnaliz)
        self.tabWidget.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(frmTumFonAnaliz)
        
        
        self.btnFonAnaliz.clicked.connect(self.fonAnaliz)
        
         
        self.veriYukle(0)
            
    @tveri.hatayakala
    def retranslateUi(self, frmTumFonAnaliz):
    
        _translate = QtCore.QCoreApplication.translate
        frmTumFonAnaliz.setWindowTitle(_translate("frmTumFonAnaliz", "Tüm Fonlar Analiz"))
        
        self.btnFonAnaliz.setText(_translate("frmTumFonAnaliz", "Fonları Analiz Et"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("frmTumFonAnaliz", "Al Sat Sinyalleri"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("frmTumFonAnaliz", "Trendler"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("frmTumFonAnaliz", "Kazanç"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("frmTumFonAnaliz", "İşlem Özeti"))
        self.label_2.setText(_translate("frmTumFonAnaliz", "Hareketli Ortalama Periyotları"))
        self.label.setText(_translate("frmTumFonAnaliz", "Tarih Aralığı"))
    
    @tveri.hatayakala   
    def veriYukle(self,e):
    
        global tdf
        tdf = tveri.veriYukle()
        
         
        now = datetime.now()
        self.txtOzet.setPlainText(   self.txtOzet.toPlainText() + now.strftime("%H:%M:%S") + "    Veriler yüklendi.\n")
    
    @tveri.hatayakala
    def fonAnaliz(self,e):
        
        
        tarih1 = '{:0>2}'.format(self.dtTarih1.date().month()) + "." '{:0>2}'.format(self.dtTarih1.date().day()) + "." + '{:0>4}'.format(self.dtTarih1.date().year()) 
        tarih2 = '{:0>2}'.format(self.dtTarih2.date().month()) + "." '{:0>2}'.format(self.dtTarih2.date().day()) + "." + '{:0>4}'.format(self.dtTarih2.date().year()) 
        
        HO1 = int(self.txtHO1.text())
        HO2 = int(self.txtHO2.text())
        HO3 = int(self.txtHO3.text())
        
        self.lstKazanc.clear()
        
        fondf = pd.DataFrame()
        for fon in tdf["Fon Kodu"].unique():
            mydf = tveri.fonAnaliz(fon , tdf, tarih1, tarih2, HO1, HO2, HO3)
            fondf = pd.concat([fondf, mydf], ignore_index = True)
            
            
            
            """KAZANÇ"""
            SonTarih = mydf["Tarih"].max()
            IlkTarih = mydf["Tarih"].min()
            SonFiyat = float(mydf[mydf["Tarih"]==SonTarih]["Fiyat"])
            IlkFiyat = float(mydf[mydf["Tarih"]==IlkTarih]["Fiyat"])
            if IlkFiyat == 0 :
                Artis = SonFiyat - IlkFiyat
                Birden = SonFiyat
                Yuzde = 100   
            else:
                Artis = SonFiyat - IlkFiyat
                Birden = SonFiyat/IlkFiyat
                Yuzde = Artis * 100 / IlkFiyat   
                            
            eleman =  fon + "   İlk Fiyatı=" +  str("{:.5f}".format(IlkFiyat))  + "   Son Fiyatı=" +  str("{:.5f}".format(SonFiyat)) + "   Fark=" +  str("{:.5f}".format(Artis))  + "   Bire Kaç=" +  str("{:.5f}".format(Birden))  + "   Yüzde=" +  str("{:.5f}".format(Yuzde))
            
            if IlkFiyat==0:
                renk = "#FFFF00"
            elif Artis>0:
                renk = "#00BF00"
            elif Artis<0:
                renk = "#FF0000"
            else:
                renk = "#FFFFFF"
            self.lstKazanc.addItem( eleman )
            self.lstKazanc.item(self.lstKazanc.count() - 1).setBackground(QtGui.QColor(renk))
        
        """------------------------"""
            
        """ YÜKSELİŞ ALÇALIŞ TRENDLERİ"""            
        trenddf = fondf.copy()
        SonTarih = trenddf["Tarih"].max()
        trenddf = trenddf[trenddf["Tarih"]==SonTarih]
        trenddf.sort_values("Fon Kodu", inplace=True)
        
        
        for index, row in trenddf.iterrows():
            eleman =  row["Fon Kodu"] + "     " +  str("{:.5f}".format(row["Fiyat"]))
            if row["UP"]:
                eleman += "   UP"
                renk = "#00BF00"
            elif row["DOWN"]:
                eleman += "   DOWN"
                renk = "#FF0000"
            else:
                renk = "#FFFFFF"
            self.lstTrend.addItem( eleman )
            self.lstTrend.item(self.lstTrend.count() - 1).setBackground(QtGui.QColor(renk))
        """------------------------"""
        
        
        
        """AL-SAT SİNYALLERİ"""
        alsatdf = fondf.copy()
        alsatdf["Sec"] = alsatdf["BUY"] + alsatdf["SELL"]
        alsatdf = alsatdf[alsatdf["Sec"]>0]
        alsatdf.sort_values("Tarih", ascending=False,  inplace=True)
        
        self.lstAlSat.clear()
        for index, row in alsatdf.iterrows():
            
            eleman =  str(row["Tarih"]) + "    " + row["Fon Kodu"] + "     " +  str("{:.5f}".format(row["Fiyat"]))
            if row["BUY"] == 1:
                eleman += "   AL"
                renk = "#00BF00"
            else:
                eleman += "   SAT"
                renk = "#FF0000"
            self.lstAlSat.addItem( eleman )
            self.lstAlSat.item(self.lstAlSat.count() - 1).setBackground(QtGui.QColor(renk))
        """------------------------"""
            
        now = datetime.now()
        self.txtOzet.setPlainText(   self.txtOzet.toPlainText() + now.strftime("%H:%M:%S") + "    Tüm fonlar analiz edildi.\n")
        
    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    frmTumFonAnaliz = QtWidgets.QWidget()
    ui = Ui_frmTumFonAnaliz()
    ui.setupUi(frmTumFonAnaliz)
    frmTumFonAnaliz.show()
    sys.exit(app.exec_())

