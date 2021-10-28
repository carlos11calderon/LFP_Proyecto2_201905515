# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Interfaz.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from AutomataLexico import AutomataLexico
from Gestor import *
from GestorSintactico import *
import webbrowser

gestorSintactico = GestorSintactico()
Auto = AutomataLexico()
gestor = Gestor()
listaTokens=[]
listaErrores=[]
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
        font = QtGui.QFont()
        font.setFamily('MingLiU-ExtB')
        font.setPointSize(11)
        self.plainTextEdit_2.setFont(font)
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.plainTextEdit_2.setReadOnly(True)
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
        self.actionCargar.triggered.connect(self.addFile)
        self.actionAnalizar.triggered.connect(self.Analizar)
        self.actionTokens.triggered.connect(self.ReporteTokens)
        self.actionArbol_de_derivacion.triggered.connect(self.ReporteArbol)
        self.actionErrores.triggered.connect(self.ReporteErrores)
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

    def addFile(self):
        self.plainTextEdit_2.clear()
        self.txtCodigo.clear()
        Text = gestor.CargarArchivo()
        self.txtCodigo.insertPlainText(Text)

    def Analizar(self):
        global listaTokens, listaErrores
        try:
            self.plainTextEdit_2.clear()
            Text = self.txtCodigo.toPlainText()
            listaTokens = Auto.analizar(Text)
            listaE = Auto.listE()
            textoSalida=gestorSintactico.analizar(listaTokens,listaE)
            listaErrores=gestorSintactico.listEr()
            self.plainTextEdit_2.insertPlainText(textoSalida)
        except:
            listaErrores=gestorSintactico.listEr()
            self.ReporteErrores()
            print('Murio xd')

    def ReporteTokens(self):
        global listaTokens
        Archivo = open("./Reportes/Tokens.html",'w')
        contenidoTabla = ''
        for i in range(len(listaTokens)):
            contenidoTabla+='<tr><th scope="row">'+str(i+1)+'</th>\n'
            contenidoTabla+='<td>'+listaTokens[i].token+'</td>\n'
            contenidoTabla+='<td>'+listaTokens[i].lexema+'</td>\n'
            contenidoTabla+='<td>'+str(listaTokens[i].Fila)+'</td>\n'
            contenidoTabla+='<td>'+str(listaTokens[i].Columna)+'</td>\n</tr>'
        contenidoHTML=(
              '<!DOCTYPE html>\n'
                ' <html>\n' 
                '<head> \n'
                '<meta charset="utf-8"> \n'
                '<link href="assets/css/bootstrap-responsive.css" type="text/css" rel="stylesheet">\n'
                '<link href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css" type="text/css" rel="stylesheet">\n'
                '<link rel="stylesheet" type="text/css" href="./css/bootstrap.css">\n'
                '<link rel="stylesheet" type="text/css"  href="css/Style.css">'
                '<title>Reporte de Tokens' '</title>\n'
                '</head>\n' 
                '<body>\n'
                '<div class="container-fluid welcome-page" id="home">\n'
                '   <div class="jumbotron">\n'
                '       <h1>\n <span>\nTokens\n</span>\n </h1>\n<p>Reporte con todos los tokens, lexemas, sus fila y sus columna</p>\n'
                '</div>'
                '</div>'
                '<div class="container-fluid " ><div class="jumbotron">'
                '<table class="table table-responsive">\n'
                '   <thead>\n'
                        '<tr>\n'
                            '<th scope="col">#</th>\n'
                            '<th scope="col">Token</th>\n'
                            '<th scope="col">Lexema</th>\n'
                            '<th scope="col">Fila</th>\n'
                            '<th scope="col">Columna</th>\n'
                        '</tr>\n'
                    '</thead>\n'
                    '<tbody>\n'
                    +contenidoTabla+
                    '</tbody>\n'
                    '</table>'   
                    '</div>'
                '</div>\n''</body>\n''</html>\n'
            )
        Archivo.write(contenidoHTML)
        Archivo.close()
        webbrowser.open("file:///"+os.getcwd()+"/Reportes/Tokens.html")

    def ReporteErrores(self):
        global listaErrores
        Archivo = open("./Reportes/Errores.html",'w')
        contenidoTabla = ''
        for i in range(len(listaErrores)):
            contenidoTabla+='<tr><th scope="row">'+str(i+1)+'</th>\n'
            contenidoTabla+='<td>'+listaErrores[i].Descripcion+'</td>\n'
            contenidoTabla+='<td>'+listaErrores[i].Token+'</td>\n'
            contenidoTabla+='<td>'+str(listaErrores[i].Fila)+'</td>\n'
            contenidoTabla+='<td>'+str(listaErrores[i].Columna)+'</td>\n</tr>'
        contenidoHTML=(
              '<!DOCTYPE html>\n'
                ' <html>\n' 
                '<head> \n'
                '<meta charset="utf-8"> \n'
                '<link href="assets/css/bootstrap-responsive.css" type="text/css" rel="stylesheet">\n'
                '<link href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css" type="text/css" rel="stylesheet">\n'
                '<link rel="stylesheet" type="text/css" href="./css/bootstrap.css">\n'
                '<link rel="stylesheet" type="text/css"  href="css/Style.css">'
                '<title>Reporte de Errores' '</title>\n'
                '</head>\n' 
                '<body>\n'
                '<div class="container-fluid welcome-page" id="home">\n'
                '   <div class="jumbotron">\n'
                '       <h1>\n <span>Errores\n</span>\n </h1>\n<p>Reporte con todos los Errores de lexemas y gramaticas, sus fila y sus columnas generados durante la ejecucion</p>\n'
                '</div>'
                '</div>'
                '<div class="container-fluid " ><div class="jumbotron">'
                '<table class="table table-responsive">\n'
                '   <thead>\n'
                        '<tr>\n'
                            '<th scope="col">#</th>\n'
                            '<th scope="col">Descripcion</th>\n'
                            '<th scope="col">Token que se esperaba</th>\n'
                            '<th scope="col">Fila</th>\n'
                            '<th scope="col">Columna</th>\n'
                        '</tr>\n'
                    '</thead>\n'
                    '<tbody>\n'
                    +contenidoTabla+
                    '</tbody>\n'
                    '</table>'   
                    '</div>'
                '</div>\n''</body>\n''</html>\n'
            )
        Archivo.write(contenidoHTML)
        Archivo.close()
        webbrowser.open("file:///"+os.getcwd()+"/Reportes/Errores.html")

    def ReporteArbol(self):
        gestorSintactico.ArbolDeDerivacion()
    