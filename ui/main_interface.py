# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/main_interface.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(964, 746)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.ModelChoice = QtWidgets.QComboBox(self.centralwidget)
        self.ModelChoice.setGeometry(QtCore.QRect(480, 70, 421, 41))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(12)
        self.ModelChoice.setFont(font)
        self.ModelChoice.setObjectName("ModelChoice")
        self.ModelChoice.addItem("")
        self.ModelChoice.addItem("")
        self.QueryInput = QtWidgets.QTextEdit(self.centralwidget)
        self.QueryInput.setGeometry(QtCore.QRect(30, 80, 391, 121))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        self.QueryInput.setFont(font)
        self.QueryInput.setObjectName("QueryInput")
        self.Precision = QtWidgets.QLineEdit(self.centralwidget)
        self.Precision.setGeometry(QtCore.QRect(110, 590, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(10)
        self.Precision.setFont(font)
        self.Precision.setReadOnly(True)
        self.Precision.setObjectName("Precision")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(480, 300, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(480, 30, 271, 31))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 590, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.Recall = QtWidgets.QLineEdit(self.centralwidget)
        self.Recall.setGeometry(QtCore.QRect(320, 590, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(10)
        self.Recall.setFont(font)
        self.Recall.setReadOnly(True)
        self.Recall.setObjectName("Recall")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(260, 590, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.FMeasure = QtWidgets.QLineEdit(self.centralwidget)
        self.FMeasure.setGeometry(QtCore.QRect(190, 650, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(10)
        self.FMeasure.setFont(font)
        self.FMeasure.setText("")
        self.FMeasure.setReadOnly(True)
        self.FMeasure.setObjectName("FMeasure")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(100, 650, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(30, 30, 331, 41))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.Result = QtWidgets.QListWidget(self.centralwidget)
        self.Result.setGeometry(QtCore.QRect(480, 340, 441, 351))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(10)
        self.Result.setFont(font)
        self.Result.setObjectName("Result")
        self.treshold = QtWidgets.QLabel(self.centralwidget)
        self.treshold.setGeometry(QtCore.QRect(480, 250, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.treshold.setFont(font)
        self.treshold.setObjectName("treshold")
        self.SearchInput = QtWidgets.QPushButton(self.centralwidget)
        self.SearchInput.setGeometry(QtCore.QRect(170, 220, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(10)
        self.SearchInput.setFont(font)
        self.SearchInput.setObjectName("SearchInput")
        self.QueryNumber = QtWidgets.QSpinBox(self.centralwidget)
        self.QueryNumber.setGeometry(QtCore.QRect(30, 360, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(12)
        self.QueryNumber.setFont(font)
        self.QueryNumber.setMinimum(1)
        self.QueryNumber.setMaximum(64)
        self.QueryNumber.setProperty("value", 1)
        self.QueryNumber.setObjectName("QueryNumber")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(30, 320, 331, 41))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.SearchQueryText = QtWidgets.QPushButton(self.centralwidget)
        self.SearchQueryText.setGeometry(QtCore.QRect(160, 520, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(10)
        self.SearchQueryText.setFont(font)
        self.SearchQueryText.setObjectName("SearchQueryText")
        self.QueryText = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.QueryText.setGeometry(QtCore.QRect(30, 430, 391, 71))
        self.QueryText.setReadOnly(True)
        self.QueryText.setObjectName("QueryText")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(30, 390, 331, 41))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.MeasureChoice = QtWidgets.QComboBox(self.centralwidget)
        self.MeasureChoice.setGeometry(QtCore.QRect(480, 180, 421, 41))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(12)
        self.MeasureChoice.setFont(font)
        self.MeasureChoice.setObjectName("MeasureChoice")
        self.MeasureChoice.addItem("")
        self.MeasureChoice.addItem("")
        self.MeasureChoice.addItem("")
        self.MeasureChoice.addItem("")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(480, 140, 401, 31))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.Threshold = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.Threshold.setGeometry(QtCore.QRect(550, 250, 91, 31))
        self.Threshold.setMinimum(0.01)
        self.Threshold.setMaximum(7.0)
        self.Threshold.setSingleStep(0.1)
        self.Threshold.setProperty("value", 0.5)
        self.Threshold.setObjectName("Threshold")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 964, 23))
        self.menubar.setObjectName("menubar")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionCreated_by_Khouas_Aymen_and_Djebara_Aghiles = QtWidgets.QAction(MainWindow)
        self.actionCreated_by_Khouas_Aymen_and_Djebara_Aghiles.setObjectName("actionCreated_by_Khouas_Aymen_and_Djebara_Aghiles")
        self.actionNo_help_there = QtWidgets.QAction(MainWindow)
        self.actionNo_help_there.setObjectName("actionNo_help_there")
        self.menuHelp.addAction(self.actionNo_help_there)
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.ModelChoice.setItemText(0, _translate("MainWindow", "Le Model Boolean"))
        self.ModelChoice.setItemText(1, _translate("MainWindow", "Le Model Vectoriel"))
        self.QueryInput.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Open Sans\',\'Open Sans\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\';\"><br /></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "Resulats :"))
        self.label_3.setText(_translate("MainWindow", "Quel Model voullez-vous utiliser?"))
        self.label_4.setText(_translate("MainWindow", "Precision :"))
        self.label_5.setText(_translate("MainWindow", "Recall :"))
        self.label_6.setText(_translate("MainWindow", "F-Measure"))
        self.label_8.setText(_translate("MainWindow", "Ecriver votre requete : "))
        self.treshold.setText(_translate("MainWindow", "Seuile :"))
        self.SearchInput.setText(_translate("MainWindow", "Search"))
        self.label_12.setText(_translate("MainWindow", "Choisissez une requete du fichier query.text"))
        self.SearchQueryText.setText(_translate("MainWindow", "Search"))
        self.label_13.setText(_translate("MainWindow", "Requete :"))
        self.MeasureChoice.setItemText(0, _translate("MainWindow", "Produit Interne"))
        self.MeasureChoice.setItemText(1, _translate("MainWindow", "Coeficient de Dice"))
        self.MeasureChoice.setItemText(2, _translate("MainWindow", "Mesure de Cosinus"))
        self.MeasureChoice.setItemText(3, _translate("MainWindow", "Mesure de Jaccard"))
        self.label_7.setText(_translate("MainWindow", "Choisissez la mesure que vous voullez"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionCreated_by_Khouas_Aymen_and_Djebara_Aghiles.setText(_translate("MainWindow", "Created by Khouas Aymen and Djebara Aghiles"))
        self.actionNo_help_there.setText(_translate("MainWindow", "No help there"))
