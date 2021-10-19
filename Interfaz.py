# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Interfaz.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from Gestor import *

gestor = Gestor()
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1318, 700)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.txtCodigo = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.txtCodigo.setGeometry(QtCore.QRect(20, 40, 551, 611))
        self.txtCodigo.setObjectName("txtCodigo")
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_2.setGeometry(QtCore.QRect(590, 40, 711, 611))
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.lblCodigo = QtWidgets.QLabel(self.centralwidget)
        self.lblCodigo.setGeometry(QtCore.QRect(260, 10, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lblCodigo.setFont(font)
        self.lblCodigo.setObjectName("lblCodigo")
        self.lblSalida = QtWidgets.QLabel(self.centralwidget)
        self.lblSalida.setGeometry(QtCore.QRect(980, 10, 61, 16))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lblSalida.setFont(font)
        self.lblSalida.setObjectName("lblSalida")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1418, 21))
        self.menubar.setObjectName("menubar")
        self.menuCargar_Archivo = QtWidgets.QMenu(self.menubar)
        self.menuCargar_Archivo.setObjectName("menuCargar_Archivo")
        self.menuAnalizar = QtWidgets.QMenu(self.menubar)
        self.menuAnalizar.setObjectName("menuAnalizar")
        self.menuReportes = QtWidgets.QMenu(self.menubar)
        self.menuReportes.setObjectName("menuReportes")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionTokens = QtWidgets.QAction(MainWindow)
        self.actionTokens.setObjectName("actionTokens")
        self.actionErrores = QtWidgets.QAction(MainWindow)
        self.actionErrores.setObjectName("actionErrores")
        self.actionArbol_de_derivacion = QtWidgets.QAction(MainWindow)
        self.actionArbol_de_derivacion.setObjectName("actionArbol_de_derivacion")
        self.actionCargar = QtWidgets.QAction(MainWindow)
        self.actionCargar.setObjectName("actionCargar")
        self.actionAnalizar = QtWidgets.QAction(MainWindow)
        self.actionAnalizar.setObjectName("actionAnalizar")
        self.menuCargar_Archivo.addAction(self.actionCargar)
        self.menuAnalizar.addAction(self.actionAnalizar)
        self.menuReportes.addAction(self.actionTokens)
        self.menuReportes.addAction(self.actionErrores)
        self.menuReportes.addAction(self.actionArbol_de_derivacion)
        self.menubar.addAction(self.menuCargar_Archivo.menuAction())
        self.menubar.addAction(self.menuAnalizar.menuAction())
        self.menubar.addAction(self.menuReportes.menuAction())
        self.actionCargar.triggered.connect(gestor.CargarArchivo)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Proyecto 2"))
        self.lblCodigo.setText(_translate("MainWindow", "Codigo"))
        self.lblSalida.setText(_translate("MainWindow", "Salida"))
        self.menuCargar_Archivo.setTitle(_translate("MainWindow", "Cargar Archivo"))
        self.menuAnalizar.setTitle(_translate("MainWindow", "Analizar"))
        self.menuReportes.setTitle(_translate("MainWindow", "Reportes"))
        self.actionTokens.setText(_translate("MainWindow", "Tokens"))
        self.actionErrores.setText(_translate("MainWindow", "Errores"))
        self.actionArbol_de_derivacion.setText(_translate("MainWindow", "Arbol de derivacion"))
        self.actionCargar.setText(_translate("MainWindow", "Cargar"))
        self.actionAnalizar.setText(_translate("MainWindow", "Analizar"))


