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


class Ui_frmFonIzle(object):
    def setupUi(self, frmFonIzle):
        frmFonIzle.setObjectName("frmFonIzle")
        frmFonIzle.resize(961, 552)
        self.btnBirlestir = QtWidgets.QPushButton(frmFonIzle)
        self.btnBirlestir.setGeometry(QtCore.QRect(10, 10, 91, 23))
        self.btnBirlestir.setObjectName("btnBirlestir")
        self.btnYukle = QtWidgets.QPushButton(frmFonIzle)
        self.btnYukle.setGeometry(QtCore.QRect(110, 10, 91, 23))
        self.btnYukle.setObjectName("btnYukle")
        
        self.cmbFon = QtWidgets.QComboBox(frmFonIzle)
        self.cmbFon.setGeometry(QtCore.QRect(330, 10, 491, 22))
        self.cmbFon.setObjectName("cmbFon")
        self.btnFonAnaliz = QtWidgets.QPushButton(frmFonIzle)
        self.btnFonAnaliz.setGeometry(QtCore.QRect(830, 10, 121, 23))
        self.btnFonAnaliz.setObjectName("btnFonAnaliz")
        
        self.tabWidget = QtWidgets.QTabWidget(frmFonIzle)
        self.tabWidget.setGeometry(QtCore.QRect(10, 110, 941, 431))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.lstAlSat = QtWidgets.QListWidget(self.tab)
        self.lstAlSat.setGeometry(QtCore.QRect(10, 10, 911, 381))
        self.lstAlSat.setObjectName("listView")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.listView_2 = QtWidgets.QListView(self.tab_2)
        self.listView_2.setGeometry(QtCore.QRect(10, 10, 911, 381))
        self.listView_2.setObjectName("listView_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.tab_3)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 921, 391))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.txtOzet = QtWidgets.QPlainTextEdit(self.tab_4)
        self.txtOzet.setGeometry(QtCore.QRect(10, 10, 921, 391))
        self.txtOzet.setObjectName("plainTextEdit")
        self.tabWidget.addTab(self.tab_4, "")
        self.groupBox = QtWidgets.QGroupBox(frmFonIzle)
        self.groupBox.setGeometry(QtCore.QRect(10, 40, 941, 51))
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
        self.tabWidget.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(frmFonIzle)
        
        self.btnBirlestir.clicked.connect(self.veribirlestir)
        self.btnYukle.clicked.connect(self.veriYukle)
        
        self.btnFonAnaliz.clicked.connect(self.fonAnaliz)
        
        

        
        
    def retranslateUi(self, frmFonIzle):
        _translate = QtCore.QCoreApplication.translate
        frmFonIzle.setWindowTitle(_translate("frmFonIzle", "Fon İzleme"))
        self.btnBirlestir.setText(_translate("frmFonIzle", "Veri Birleştir"))
        self.btnYukle.setText(_translate("frmFonIzle", "Veri Yükle"))
        
        self.btnFonAnaliz.setText(_translate("frmFonIzle", "Fonu Analiz Et"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("frmFonIzle", "Al Sat Sinyalleri"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("frmFonIzle", "Trendler"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("frmFonIzle", "Grafik"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("frmFonIzle", "İşlem Özeti"))
        self.label_2.setText(_translate("frmFonIzle", "Hareketli Ortalama Periyotları"))
        self.label.setText(_translate("frmFonIzle", "Tarih Aralığı"))
    
    def veribirlestir(self):
        tveri.veribirlestir
        
        now = datetime.now()
        self.txtOzet.setPlainText(   self.txtOzet.toPlainText() + now.strftime("%H:%M:%S") + "    Veriler birleştirildi.\n")
        
        
    def veriYukle(self):
        global tdf
        tdf = tveri.veriYukle()
        
        self.cmbFon.addItems(pd.unique(tdf['Fon Kodu'] + "  " + tdf['Fon Adı']))
        
        now = datetime.now()
        self.txtOzet.setPlainText(   self.txtOzet.toPlainText() + now.strftime("%H:%M:%S") + "    Veriler yüklendi.\n")
        
    
    def fonAnaliz(self):
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
            
            
        now = datetime.now()
        self.txtOzet.setPlainText(   self.txtOzet.toPlainText() + now.strftime("%H:%M:%S") + "    " + fon + " fonu analiz edildi.\n")
        
        
        
        self.fig = tveri.fonGrafik(fon , fondf, tarih1, tarih2)
        self.canvas = FigureCanvas(self.fig)
        
        if self.verticalLayout.count()>0 :
            self.verticalLayout.itemAt(0).widget().deleteLater()
        self.verticalLayout.addWidget(self.canvas)
        
    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    frmFonIzle = QtWidgets.QWidget()
    ui = Ui_frmFonIzle()
    ui.setupUi(frmFonIzle)
    frmFonIzle.show()
    sys.exit(app.exec_())
