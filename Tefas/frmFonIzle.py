# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\github\pythoncodebank\Tefas\FormIzleme.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from datetime import date, datetime
import tarihselveriler as tveri
import pandas as pd
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib import pyplot as plt

from tahmin import fon_LinearRegression, verihazirla, grafik_LinearRegression


class Ui_frmFonIzle():
    @tveri.hatayakala
    def setupUi(self, frmFonIzle):
        
        frmFonIzle.setObjectName("frmFonIzle")
        frmFonIzle.resize(1320, 670)
        
        self.cmbFon = QtWidgets.QComboBox(frmFonIzle)
        self.cmbFon.setGeometry(QtCore.QRect(330, 30, 491, 22))
        self.cmbFon.setObjectName("cmbFon")
        self.btnFonAnaliz = QtWidgets.QPushButton(frmFonIzle)
        self.btnFonAnaliz.setGeometry(QtCore.QRect(830, 30, 121, 23))
        self.btnFonAnaliz.setObjectName("btnFonAnaliz")
        
        self.tabWidget = QtWidgets.QTabWidget(frmFonIzle)
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
        self.lblTrend = QtWidgets.QLabel(self.tab_2)
        self.lblTrend.setGeometry(QtCore.QRect(10, 10, 250, 26))
        self.lblTrend.setObjectName("lblTrend")
        self.verticalLayoutWidget1 = QtWidgets.QWidget(self.tab_2)
        self.verticalLayoutWidget1.setGeometry(QtCore.QRect(10, 30, 1270, 505))
        self.verticalLayoutWidget1.setObjectName("verticalLayoutWidget1")
        self.verticalLayoutTrend = QtWidgets.QVBoxLayout(self.verticalLayoutWidget1)
        self.verticalLayoutTrend.setContentsMargins(0, 0, 0, 0)
        self.verticalLayoutTrend.setObjectName("verticalLayoutTrend")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.tab_3)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 1270, 505))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget.addTab(self.tab_3, "")
        
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.verticalLayoutWidget2 = QtWidgets.QWidget(self.tab_5)
        self.verticalLayoutWidget2.setGeometry(QtCore.QRect(0, 0, 1270, 505))
        self.verticalLayoutWidget2.setObjectName("verticalLayoutWidget2")
        self.verticalLayoutTahmin = QtWidgets.QVBoxLayout(self.verticalLayoutWidget2)
        self.verticalLayoutTahmin.setContentsMargins(0, 0, 0, 0)
        self.verticalLayoutTahmin.setObjectName("verticalLayoutTahmin")
        self.tabWidget.addTab(self.tab_5, "")
        
        
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.txtOzet = QtWidgets.QPlainTextEdit(self.tab_4)
        self.txtOzet.setGeometry(QtCore.QRect(10, 10, 1270, 505))
        self.txtOzet.setObjectName("plainTextEdit")
        self.tabWidget.addTab(self.tab_4, "")
        self.groupBox = QtWidgets.QGroupBox(frmFonIzle)
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
        
        self.retranslateUi(frmFonIzle)
        self.tabWidget.setCurrentIndex(4)
        QtCore.QMetaObject.connectSlotsByName(frmFonIzle)
        
        self.btnFonAnaliz.clicked.connect(self.fonAnaliz)
        
        self.veriYukle(0)
        
    @tveri.hatayakala
    def retranslateUi(self, frmFonIzle):
    
        _translate = QtCore.QCoreApplication.translate
        frmFonIzle.setWindowTitle(_translate("frmFonIzle", "Fon İzleme"))
        
        self.btnFonAnaliz.setText(_translate("frmFonIzle", "Fonu Analiz Et"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("frmFonIzle", "Al Sat Sinyalleri"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("frmFonIzle", "Trendler"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("frmFonIzle", "Grafik"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("frmFonIzle", "İşlem Özeti"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("frmFonIzle", "Tahmin Grafiği"))
        
        self.label_2.setText(_translate("frmFonIzle", "Hareketli Ortalama Periyotları"))
        self.label.setText(_translate("frmFonIzle", "Tarih Aralığı"))
    
       
    @tveri.hatayakala        
    def veri_birlestir(self,e):
    
        tveri.veribirlestir()
        
        now = datetime.now()
        self.txtOzet.setPlainText(   self.txtOzet.toPlainText() + now.strftime("%H:%M:%S") + "    Veriler birleştirildi.\n")
    
     
    @tveri.hatayakala
    def veriYukle(self,e):
    
        global tdf
        tdf = tveri.veriYukle()
        
        self.cmbFon.addItems(pd.unique(tdf['Fon Kodu'] + "  " + tdf['Fon Adı']))
        
        now = datetime.now()
        self.txtOzet.setPlainText(   self.txtOzet.toPlainText() + now.strftime("%H:%M:%S") + "    Veriler yüklendi.\n")
    
    @tveri.hatayakala
    def fonAnaliz(self,e):
    
        fon = self.cmbFon.currentText()[0:3]
        #01.01.2020 ay gun yil
        tarih1 = '{:0>2}'.format(self.dtTarih1.date().month()) + "." '{:0>2}'.format(self.dtTarih1.date().day()) + "." + '{:0>4}'.format(self.dtTarih1.date().year()) 
        tarih2 = '{:0>2}'.format(self.dtTarih2.date().month()) + "." '{:0>2}'.format(self.dtTarih2.date().day()) + "." + '{:0>4}'.format(self.dtTarih2.date().year()) 
        
        HO1 = int(self.txtHO1.text())
        HO2 = int(self.txtHO2.text())
        HO3 = int(self.txtHO3.text())
        
        
        global fondf
        fondf = tveri.fonAnaliz(fon , tdf, tarih1, tarih2, HO1, HO2, HO3)
        
        
        alsatdf = fondf.copy()
        alsatdf["Sec"] = alsatdf["BUY"] + alsatdf["SELL"]
        alsatdf = alsatdf[alsatdf["Sec"]>0]
        alsatdf.sort_values("Tarih", ascending=False,  inplace=True)
        
       
        
        self.lstAlSat.clear()
        for index, row in alsatdf.iterrows():
            
            eleman = str(row["Tarih"]) + "    " +  str("{:.5f}".format(row["Fiyat"]))
            if row["BUY"] == 1:
                eleman += "   AL"
                renk = "#00BF00"
            else:
                eleman += "   SAT"
                renk = "#FF0000"
            self.lstAlSat.addItem( eleman )
            self.lstAlSat.item(self.lstAlSat.count() - 1).setBackground(QtGui.QColor(renk))
            
            
        trenddf = alsatdf.head(1)
       
       
        if trenddf["UP"].max():
            self.lblTrend.setText("Fon Yükseliş Trendi Gösteriyor.")
        elif trenddf["DOWN"].max():
            self.lblTrend.setText("Fon Düşüş Trendi Gösteriyor.")
        else:
            self.lblTrend.setText("Fon Herhangi Bir Trend Eğilimi Göstermiyor.")
        
                
        """Fon Grafiği"""
        self.fig = tveri.fonGrafik(fon , fondf)
        self.canvas = FigureCanvas(self.fig)
        
        if self.verticalLayout.count()>0 :
            self.verticalLayout.itemAt(0).widget().deleteLater()
        self.verticalLayout.addWidget(self.canvas)
        
        """Trend Grafiği"""
        self.fig1 = tveri.fonTrend(fon , fondf)
        self.canvas1 = FigureCanvas(self.fig1)
        
        if self.verticalLayoutTrend.count()>0 :
            self.verticalLayoutTrend.itemAt(0).widget().deleteLater()
        self.verticalLayoutTrend.addWidget(self.canvas1)
        
        """Tahmin Grafiği"""
        
        
        self.fig2 = grafik_LinearRegression(fon , fondf)
        self.canvas2 = FigureCanvas(self.fig2)
        
        if self.verticalLayoutTahmin.count()>0 :
            self.verticalLayoutTahmin.itemAt(0).widget().deleteLater()
        self.verticalLayoutTahmin.addWidget(self.canvas2)
    
    
        now = datetime.now()
        self.txtOzet.setPlainText(   self.txtOzet.toPlainText() + now.strftime("%H:%M:%S") + "    " + fon + " fonu analiz edildi.\n")
        
        """Kazanç şimdilik özet textine yazıyorum."""
        SonTarih = fondf["Tarih"].max()
        IlkTarih = fondf["Tarih"].min()
        SonFiyat = float(fondf[fondf["Tarih"]==SonTarih]["Fiyat"])
        IlkFiyat = float(fondf[fondf["Tarih"]==IlkTarih]["Fiyat"])
        if IlkFiyat == 0 :
            Artis = SonFiyat - IlkFiyat
            Birden = SonFiyat
            Yuzde = 100   
        else:
            Artis = SonFiyat - IlkFiyat
            Birden = SonFiyat/IlkFiyat
            Yuzde = Artis * 100 / IlkFiyat   
        
        
        ozet = "\n\n"
        if Artis>0:
            ozet += "Yükseliş\n"
        elif Artis<0:
            ozet += "Düşüş\n"
        
        ozet += "İlk Fiyatı  =  " +  str("{:.5f}".format(IlkFiyat))  + "\nSon Fiyatı  =  " +  str("{:.5f}".format(SonFiyat)) + "\nFark  =  " +  str("{:.5f}".format(Artis))  + "\nBire Kaç Verdi  =  " +  str("{:.5f}".format(Birden))  + "\nYüzde Kar  =  " +  str("{:.5f}".format(Yuzde)) + "\n\n"
            
        self.txtOzet.setPlainText(   self.txtOzet.toPlainText() + ozet)
        
        
        """Tahmin"""
        fondf = verihazirla(fondf)
        if len(fondf)>0:
            SonTarih = fondf["Tarih"].max()
            fondf = fondf[fondf["Tarih"]==SonTarih]
            x = fondf[["Fiyat", "ho_short", "ho_middle", "ho_long"]].head(1)
            print(x)
            y_pred = fon_LinearRegression(fon, x)
            
            self.txtOzet.setPlainText(   self.txtOzet.toPlainText() + "\nTahmin Edilen Ertesi Gün Fiyatı : " + str(y_pred)  + "\n\n")
        
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    frmFonIzle = QtWidgets.QWidget()
    ui = Ui_frmFonIzle()
    ui.setupUi(frmFonIzle)
    frmFonIzle.show()
    sys.exit(app.exec_())

