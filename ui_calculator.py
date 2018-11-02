# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\Qt\projects\Calculator\mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Calculator(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(359, 441)
        MainWindow.setMinimumSize(QtCore.QSize(359, 441))
        MainWindow.setMaximumSize(QtCore.QSize(359, 441))
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(60, 0, 301, 81))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setStyleSheet("QLabel {\n"
"  qproperty-alignment: \'AlignVCenter | AlignRight\';\n"
"  border: 1px solid gray;\n"
"}\n"
"\n"
"background-color : white;")
        self.label.setObjectName("label")
        self.pushButton_sin = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_sin.setGeometry(QtCore.QRect(60, 80, 61, 61))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        self.pushButton_sin.setFont(font)
        self.pushButton_sin.setStyleSheet("QPushButton {\n"
"  background-color: rgb(255, 151, 57);\n"
"  color: white; \n"
"  border: 1px solid gray;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #FF7832, stop: 1 #FF9739);\n"
"}")
        self.pushButton_sin.setFlat(True)
        self.pushButton_sin.setObjectName("pushButton_sin")
        self.pushButton_tg = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_tg.setGeometry(QtCore.QRect(120, 80, 61, 61))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        self.pushButton_tg.setFont(font)
        self.pushButton_tg.setStyleSheet("QPushButton {\n"
"  background-color: rgb(255, 151, 57);\n"
"  color: white; \n"
"  border: 1px solid gray;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #FF7832, stop: 1 #FF9739);\n"
"}")
        self.pushButton_tg.setFlat(True)
        self.pushButton_tg.setObjectName("pushButton_tg")
        self.pushButton_ctg = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_ctg.setGeometry(QtCore.QRect(180, 80, 61, 61))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        self.pushButton_ctg.setFont(font)
        self.pushButton_ctg.setStyleSheet("QPushButton {\n"
"  background-color: rgb(255, 151, 57);\n"
"  color: white; \n"
"  border: 1px solid gray;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #FF7832, stop: 1 #FF9739);\n"
"}")
        self.pushButton_ctg.setFlat(True)
        self.pushButton_ctg.setObjectName("pushButton_ctg")
        self.pushButton_hexB = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_hexB.setGeometry(QtCore.QRect(60, 140, 61, 81))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        self.pushButton_hexB.setFont(font)
        self.pushButton_hexB.setStyleSheet("QPushButton {\n"
"   border: 1px solid gray;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"")
        self.pushButton_hexB.setFlat(True)
        self.pushButton_hexB.setObjectName("pushButton_hexB")
        self.pushButton_hexB.setDisabled(True)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_2.setGeometry(QtCore.QRect(180, 140, 61, 61))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton {\n"
"   border: 1px solid gray;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"")
        self.pushButton_2.setFlat(True)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_1 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_1.setGeometry(QtCore.QRect(120, 140, 61, 61))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        self.pushButton_1.setFont(font)
        self.pushButton_1.setStyleSheet("QPushButton {\n"
"   border: 1px solid gray;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"")
        self.pushButton_1.setFlat(True)
        self.pushButton_1.setObjectName("pushButton_1")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_5.setGeometry(QtCore.QRect(180, 200, 61, 61))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("QPushButton {\n"
"   border: 1px solid gray;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"")
        self.pushButton_5.setFlat(True)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_hexD = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_hexD.setGeometry(QtCore.QRect(60, 220, 61, 81))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        self.pushButton_hexD.setFont(font)
        self.pushButton_hexD.setStyleSheet("QPushButton {\n"
"   border: 1px solid gray;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"")
        self.pushButton_hexD.setFlat(True)
        self.pushButton_hexD.setObjectName("pushButton_hexD")
        self.pushButton_hexD.setDisabled(True)
        self.pushButton_4 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_4.setGeometry(QtCore.QRect(120, 200, 61, 61))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("QPushButton {\n"
"   border: 1px solid gray;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"")
        self.pushButton_4.setFlat(True)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_8.setGeometry(QtCore.QRect(180, 260, 61, 61))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setStyleSheet("QPushButton {\n"
"   border: 1px solid gray;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"")
        self.pushButton_8.setFlat(True)
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_hexF = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_hexF.setGeometry(QtCore.QRect(60, 300, 61, 81))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        self.pushButton_hexF.setFont(font)
        self.pushButton_hexF.setStyleSheet("QPushButton {\n"
"   border: 1px solid gray;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"")
        self.pushButton_hexF.setFlat(True)
        self.pushButton_hexF.setObjectName("pushButton_hexF")
        self.pushButton_hexF.setDisabled(True)
        self.pushButton_hexE = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_hexE.setGeometry(QtCore.QRect(0, 300, 61, 81))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        self.pushButton_hexE.setFont(font)
        self.pushButton_hexE.setStyleSheet("QPushButton {\n"
"   border: 1px solid gray;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"")
        self.pushButton_hexE.setFlat(True)
        self.pushButton_hexE.setObjectName("pushButton_hexE")
        self.pushButton_hexE.setDisabled(True)
        self.pushButton_7 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_7.setGeometry(QtCore.QRect(120, 260, 61, 61))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setStyleSheet("QPushButton {\n"
"   border: 1px solid gray;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"")
        self.pushButton_7.setFlat(True)
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_0 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_0.setGeometry(QtCore.QRect(180, 320, 61, 61))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        self.pushButton_0.setFont(font)
        self.pushButton_0.setStyleSheet("QPushButton {\n"
"   border: 1px solid gray;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"")
        self.pushButton_0.setFlat(True)
        self.pushButton_0.setObjectName("pushButton_0")
        self.pushButton_plusMinus = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_plusMinus.setGeometry(QtCore.QRect(120, 320, 61, 61))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        self.pushButton_plusMinus.setFont(font)
        self.pushButton_plusMinus.setStyleSheet("QPushButton {\n"
"  background-color: rgb(215, 215, 215);\n"
"  border: 1px solid gray;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #BEBEBE, stop: 1 #D7D7D7);\n"
"}")
        self.pushButton_plusMinus.setFlat(True)
        self.pushButton_plusMinus.setObjectName("pushButton_plusMinus")
        self.pushButton_divide = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_divide.setGeometry(QtCore.QRect(300, 140, 61, 61))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        self.pushButton_divide.setFont(font)
        self.pushButton_divide.setStyleSheet("QPushButton {\n"
"  background-color: rgb(255, 151, 57);\n"
"  color: white; \n"
"  border: 1px solid gray;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #FF7832, stop: 1 #FF9739);\n"
"}")
        self.pushButton_divide.setFlat(True)
        self.pushButton_divide.setObjectName("pushButton_divide")
        self.pushButton_clear = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_clear.setGeometry(QtCore.QRect(300, 80, 61, 61))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        self.pushButton_clear.setFont(font)
        self.pushButton_clear.setStyleSheet("QPushButton {\n"
"  background-color: rgb(215, 215, 215);\n"
"  border: 1px solid gray;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #BEBEBE, stop: 1 #D7D7D7);\n"
"}")
        self.pushButton_clear.setFlat(True)
        self.pushButton_clear.setObjectName("pushButton_clear")
        self.pushButton_multiply = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_multiply.setGeometry(QtCore.QRect(300, 200, 61, 61))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        self.pushButton_multiply.setFont(font)
        self.pushButton_multiply.setStyleSheet("QPushButton {\n"
"  background-color: rgb(255, 151, 57);\n"
"  color: white; \n"
"  border: 1px solid gray;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #FF7832, stop: 1 #FF9739);\n"
"}")
        self.pushButton_multiply.setFlat(True)
        self.pushButton_multiply.setObjectName("pushButton_multiply")
        self.pushButton_add = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_add.setGeometry(QtCore.QRect(300, 260, 61, 61))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        self.pushButton_add.setFont(font)
        self.pushButton_add.setStyleSheet("QPushButton {\n"
"  background-color: rgb(255, 151, 57);\n"
"  color: white; \n"
"  border: 1px solid gray;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #FF7832, stop: 1 #FF9739);\n"
"}")
        self.pushButton_add.setFlat(True)
        self.pushButton_add.setObjectName("pushButton_add")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_9.setGeometry(QtCore.QRect(240, 260, 61, 61))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setStyleSheet("QPushButton {\n"
"   border: 1px solid gray;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"")
        self.pushButton_9.setFlat(True)
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_6.setGeometry(QtCore.QRect(240, 200, 61, 61))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("QPushButton {\n"
"   border: 1px solid gray;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"")
        self.pushButton_6.setFlat(True)
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_substract = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_substract.setGeometry(QtCore.QRect(300, 320, 61, 61))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        self.pushButton_substract.setFont(font)
        self.pushButton_substract.setStyleSheet("QPushButton {\n"
"  background-color: rgb(255, 151, 57);\n"
"  color: white; \n"
"  border: 1px solid gray;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #FF7832, stop: 1 #FF9739);\n"
"}")
        self.pushButton_substract.setFlat(True)
        self.pushButton_substract.setObjectName("pushButton_substract")
        self.pushButton_percent = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_percent.setGeometry(QtCore.QRect(240, 80, 61, 61))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        self.pushButton_percent.setFont(font)
        self.pushButton_percent.setStyleSheet("QPushButton {\n"
"  background-color: rgb(215, 215, 215);\n"
"  border: 1px solid gray;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #BEBEBE, stop: 1 #D7D7D7);\n"
"}")
        self.pushButton_percent.setFlat(True)
        self.pushButton_percent.setObjectName("pushButton_percent")
        self.pushButton_decimal = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_decimal.setGeometry(QtCore.QRect(240, 320, 61, 61))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        self.pushButton_decimal.setFont(font)
        self.pushButton_decimal.setStyleSheet("QPushButton {\n"
"  background-color: rgb(215, 215, 215);\n"
"  border: 1px solid gray;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #BEBEBE, stop: 1 #D7D7D7);\n"
"}")
        self.pushButton_decimal.setFlat(True)
        self.pushButton_decimal.setObjectName("pushButton_decimal")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_3.setGeometry(QtCore.QRect(240, 140, 61, 61))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("QPushButton {\n"
"   border: 1px solid gray;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"")
        self.pushButton_3.setFlat(True)
        self.pushButton_3.setObjectName("pushButton_3")
        self.radioButton_DEC = QtWidgets.QRadioButton(self.centralWidget)
        self.radioButton_DEC.setGeometry(QtCore.QRect(10, 10, 82, 17))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.radioButton_DEC.setFont(font)
        self.radioButton_DEC.setChecked(True)
        self.radioButton_DEC.setObjectName("radioButton_DEC")
        self.radioButton_BIN = QtWidgets.QRadioButton(self.centralWidget)
        self.radioButton_BIN.setGeometry(QtCore.QRect(10, 30, 82, 17))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.radioButton_BIN.setFont(font)
        self.radioButton_BIN.setObjectName("radioButton_BIN")
        self.radioButton_HEX = QtWidgets.QRadioButton(self.centralWidget)
        self.radioButton_HEX.setGeometry(QtCore.QRect(10, 50, 82, 17))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.radioButton_HEX.setFont(font)
        self.radioButton_HEX.setObjectName("radioButton_HEX")
        self.pushButton_toBIN = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_toBIN.setGeometry(QtCore.QRect(60, 380, 61, 61))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.pushButton_toBIN.setFont(font)
        self.pushButton_toBIN.setStyleSheet("QPushButton {\n"
"  background-color: rgb(255, 151, 57);\n"
"  color: white; \n"
"  border: 1px solid gray;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #FF7832, stop: 1 #FF9739);\n"
"}")
        self.pushButton_toBIN.setFlat(True)
        self.pushButton_toBIN.setObjectName("pushButton_toBIN")
        self.pushButton_toDEC = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_toDEC.setGeometry(QtCore.QRect(0, 380, 61, 61))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.pushButton_toDEC.setFont(font)
        self.pushButton_toDEC.setStyleSheet("QPushButton {\n"
"  background-color: rgb(255, 151, 57);\n"
"  color: white; \n"
"  border: 1px solid gray;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #FF7832, stop: 1 #FF9739);\n"
"}")
        self.pushButton_toDEC.setFlat(True)
        self.pushButton_toDEC.setObjectName("pushButton_toDEC")
        self.pushButton_toHEX = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_toHEX.setGeometry(QtCore.QRect(120, 380, 61, 61))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.pushButton_toHEX.setFont(font)
        self.pushButton_toHEX.setStyleSheet("QPushButton {\n"
"  background-color: rgb(255, 151, 57);\n"
"  color: white; \n"
"  border: 1px solid gray;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #FF7832, stop: 1 #FF9739);\n"
"}")
        self.pushButton_toHEX.setFlat(True)
        self.pushButton_toHEX.setObjectName("pushButton_toHEX")
        self.pushButton_equals = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_equals.setGeometry(QtCore.QRect(180, 380, 181, 61))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        self.pushButton_equals.setFont(font)
        self.pushButton_equals.setStyleSheet("QPushButton {\n"
"  background-color: rgb(255, 151, 57);\n"
"  color: white; \n"
"  border: 1px solid gray;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #FF7832, stop: 1 #FF9739);\n"
"}")
        self.pushButton_equals.setFlat(True)
        self.pushButton_equals.setObjectName("pushButton_equals")
        self.pushButton_hexC = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_hexC.setGeometry(QtCore.QRect(0, 220, 61, 81))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        self.pushButton_hexC.setFont(font)
        self.pushButton_hexC.setStyleSheet("QPushButton {\n"
"   border: 1px solid gray;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"")
        self.pushButton_hexC.setFlat(True)
        self.pushButton_hexC.setObjectName("pushButton_hexC")
        self.pushButton_hexC.setDisabled(True)
        self.pushButton_hexA = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_hexA.setGeometry(QtCore.QRect(0, 140, 61, 81))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        self.pushButton_hexA.setFont(font)
        self.pushButton_hexA.setStyleSheet("QPushButton {\n"
"   border: 1px solid gray;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"")
        self.pushButton_hexA.setFlat(True)
        self.pushButton_hexA.setObjectName("pushButton_hexA")
        self.pushButton_hexA.setDisabled(True)
        self.pushButton_cos = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_cos.setGeometry(QtCore.QRect(0, 80, 61, 61))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        self.pushButton_cos.setFont(font)
        self.pushButton_cos.setStyleSheet("QPushButton {\n"
"  background-color: rgb(255, 151, 57);\n"
"  color: white; \n"
"  border: 1px solid gray;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #FF7832, stop: 1 #FF9739);\n"
"}")
        self.pushButton_cos.setFlat(True)
        self.pushButton_cos.setObjectName("pushButton_cos")
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Calculator"))
        self.label.setText(_translate("MainWindow", "0"))
        self.pushButton_sin.setText(_translate("MainWindow", "sin"))
        self.pushButton_tg.setText(_translate("MainWindow", "tg"))
        self.pushButton_ctg.setText(_translate("MainWindow", "ctg"))
        self.pushButton_hexB.setText(_translate("MainWindow", "B"))
        self.pushButton_2.setText(_translate("MainWindow", "2"))
        self.pushButton_1.setText(_translate("MainWindow", "1"))
        self.pushButton_5.setText(_translate("MainWindow", "5"))
        self.pushButton_hexD.setText(_translate("MainWindow", "D"))
        self.pushButton_4.setText(_translate("MainWindow", "4"))
        self.pushButton_8.setText(_translate("MainWindow", "8"))
        self.pushButton_hexF.setText(_translate("MainWindow", "F"))
        self.pushButton_hexE.setText(_translate("MainWindow", "E"))
        self.pushButton_7.setText(_translate("MainWindow", "7"))
        self.pushButton_0.setText(_translate("MainWindow", "0"))
        self.pushButton_plusMinus.setText(_translate("MainWindow", "+/-"))
        self.pushButton_divide.setText(_translate("MainWindow", "/"))
        self.pushButton_clear.setText(_translate("MainWindow", "C"))
        self.pushButton_multiply.setText(_translate("MainWindow", "X"))
        self.pushButton_add.setText(_translate("MainWindow", "+"))
        self.pushButton_9.setText(_translate("MainWindow", "9"))
        self.pushButton_6.setText(_translate("MainWindow", "6"))
        self.pushButton_substract.setText(_translate("MainWindow", "-"))
        self.pushButton_percent.setText(_translate("MainWindow", "%"))
        self.pushButton_decimal.setText(_translate("MainWindow", "."))
        self.pushButton_3.setText(_translate("MainWindow", "3"))
        self.radioButton_DEC.setText(_translate("MainWindow", "DEC"))
        self.radioButton_BIN.setText(_translate("MainWindow", "BIN"))
        self.radioButton_HEX.setText(_translate("MainWindow", "HEX"))
        self.pushButton_toBIN.setText(_translate("MainWindow", "To BIN"))
        self.pushButton_toDEC.setText(_translate("MainWindow", "To DEC"))
        self.pushButton_toHEX.setText(_translate("MainWindow", "To HEX"))
        self.pushButton_equals.setText(_translate("MainWindow", "="))
        self.pushButton_hexC.setText(_translate("MainWindow", "C"))
        self.pushButton_hexA.setText(_translate("MainWindow", "A"))
        self.pushButton_cos.setText(_translate("MainWindow", "cos"))

