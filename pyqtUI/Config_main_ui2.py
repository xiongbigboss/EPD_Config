# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Config_main_ui2.ui'
#
# Created: Sat Nov 26 18:58:34 2016
#      by: PyQt5 UI code generator 5.4
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(707, 543)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_title = QtWidgets.QWidget(Dialog)
        self.widget_title.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_title.sizePolicy().hasHeightForWidth())
        self.widget_title.setSizePolicy(sizePolicy)
        self.widget_title.setMinimumSize(QtCore.QSize(100, 33))
        self.widget_title.setObjectName("widget_title")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_title)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lab_Ico = QtWidgets.QLabel(self.widget_title)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lab_Ico.sizePolicy().hasHeightForWidth())
        self.lab_Ico.setSizePolicy(sizePolicy)
        self.lab_Ico.setMinimumSize(QtCore.QSize(40, 40))
        self.lab_Ico.setText("")
        self.lab_Ico.setAlignment(QtCore.Qt.AlignCenter)
        self.lab_Ico.setObjectName("lab_Ico")
        self.horizontalLayout_3.addWidget(self.lab_Ico)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.lab_Title = QtWidgets.QLabel(self.widget_title)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lab_Title.sizePolicy().hasHeightForWidth())
        self.lab_Title.setSizePolicy(sizePolicy)
        self.lab_Title.setStyleSheet("font: 10pt \"微软雅黑\";")
        self.lab_Title.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lab_Title.setObjectName("lab_Title")
        self.horizontalLayout_3.addWidget(self.lab_Title)
        self.btnMenu_Min = QtWidgets.QPushButton(self.widget_title)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnMenu_Min.sizePolicy().hasHeightForWidth())
        self.btnMenu_Min.setSizePolicy(sizePolicy)
        self.btnMenu_Min.setMinimumSize(QtCore.QSize(40, 40))
        self.btnMenu_Min.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.btnMenu_Min.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btnMenu_Min.setText("")
        self.btnMenu_Min.setFlat(True)
        self.btnMenu_Min.setObjectName("btnMenu_Min")
        self.horizontalLayout_3.addWidget(self.btnMenu_Min)
        self.btnMenu_Max = QtWidgets.QPushButton(self.widget_title)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnMenu_Max.sizePolicy().hasHeightForWidth())
        self.btnMenu_Max.setSizePolicy(sizePolicy)
        self.btnMenu_Max.setMinimumSize(QtCore.QSize(40, 40))
        self.btnMenu_Max.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.btnMenu_Max.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btnMenu_Max.setText("")
        self.btnMenu_Max.setFlat(True)
        self.btnMenu_Max.setObjectName("btnMenu_Max")
        self.horizontalLayout_3.addWidget(self.btnMenu_Max)
        self.btnMenu_Close = QtWidgets.QPushButton(self.widget_title)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnMenu_Close.sizePolicy().hasHeightForWidth())
        self.btnMenu_Close.setSizePolicy(sizePolicy)
        self.btnMenu_Close.setMinimumSize(QtCore.QSize(40, 40))
        self.btnMenu_Close.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.btnMenu_Close.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btnMenu_Close.setText("")
        self.btnMenu_Close.setFlat(True)
        self.btnMenu_Close.setObjectName("btnMenu_Close")
        self.horizontalLayout_3.addWidget(self.btnMenu_Close)
        self.verticalLayout.addWidget(self.widget_title)
        self.widget_menu = QtWidgets.QWidget(Dialog)
        self.widget_menu.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_menu.sizePolicy().hasHeightForWidth())
        self.widget_menu.setSizePolicy(sizePolicy)
        self.widget_menu.setMinimumSize(QtCore.QSize(100, 33))
        self.widget_menu.setObjectName("widget_menu")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_menu)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.btnMenu_help = QtWidgets.QPushButton(self.widget_menu)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnMenu_help.sizePolicy().hasHeightForWidth())
        self.btnMenu_help.setSizePolicy(sizePolicy)
        self.btnMenu_help.setMinimumSize(QtCore.QSize(40, 40))
        self.btnMenu_help.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.btnMenu_help.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btnMenu_help.setFlat(True)
        self.btnMenu_help.setObjectName("btnMenu_help")
        self.horizontalLayout_4.addWidget(self.btnMenu_help)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.verticalLayout.addWidget(self.widget_menu)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setContentsMargins(9, 9, 9, 9)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.groupBox_9 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_9.setObjectName("groupBox_9")
        self.formLayout = QtWidgets.QFormLayout(self.groupBox_9)
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName("formLayout")
        spacerItem2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(0, QtWidgets.QFormLayout.LabelRole, spacerItem2)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem3)
        self.pushButton_InfReadInformation = QtWidgets.QPushButton(self.groupBox_9)
        self.pushButton_InfReadInformation.setObjectName("pushButton_InfReadInformation")
        self.horizontalLayout_9.addWidget(self.pushButton_InfReadInformation)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem4)
        self.label_10 = QtWidgets.QLabel(self.groupBox_9)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_9.addWidget(self.label_10)
        self.progressBarInfRead = QtWidgets.QProgressBar(self.groupBox_9)
        self.progressBarInfRead.setProperty("value", 0)
        self.progressBarInfRead.setObjectName("progressBarInfRead")
        self.horizontalLayout_9.addWidget(self.progressBarInfRead)
        self.formLayout.setLayout(1, QtWidgets.QFormLayout.SpanningRole, self.horizontalLayout_9)
        self.label_27 = QtWidgets.QLabel(self.groupBox_9)
        self.label_27.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Sans")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_27.setFont(font)
        self.label_27.setObjectName("label_27")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_27)
        self.lineEdit_21 = QtWidgets.QLineEdit(self.groupBox_9)
        self.lineEdit_21.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_21.setFont(font)
        self.lineEdit_21.setObjectName("lineEdit_21")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_21)
        self.label_3 = QtWidgets.QLabel(self.groupBox_9)
        font = QtGui.QFont()
        font.setFamily("Sans")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.lineEdit_22 = QtWidgets.QLineEdit(self.groupBox_9)
        self.lineEdit_22.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_22.setFont(font)
        self.lineEdit_22.setObjectName("lineEdit_22")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEdit_22)
        self.label_26 = QtWidgets.QLabel(self.groupBox_9)
        self.label_26.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Sans")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_26.setFont(font)
        self.label_26.setObjectName("label_26")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_26)
        self.lineEdit_23 = QtWidgets.QLineEdit(self.groupBox_9)
        self.lineEdit_23.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.lineEdit_23.setFont(font)
        self.lineEdit_23.setObjectName("lineEdit_23")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.lineEdit_23)
        self.label_25 = QtWidgets.QLabel(self.groupBox_9)
        self.label_25.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Sans")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_25.setFont(font)
        self.label_25.setObjectName("label_25")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_25)
        self.lineEdit_24 = QtWidgets.QLineEdit(self.groupBox_9)
        self.lineEdit_24.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_24.setFont(font)
        self.lineEdit_24.setObjectName("lineEdit_24")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.lineEdit_24)
        self.label_24 = QtWidgets.QLabel(self.groupBox_9)
        self.label_24.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Sans")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_24.setFont(font)
        self.label_24.setObjectName("label_24")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_24)
        self.lineEdit_25 = QtWidgets.QLineEdit(self.groupBox_9)
        self.lineEdit_25.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_25.setFont(font)
        self.lineEdit_25.setObjectName("lineEdit_25")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.lineEdit_25)
        self.label_28 = QtWidgets.QLabel(self.groupBox_9)
        self.label_28.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Sans")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_28.setFont(font)
        self.label_28.setObjectName("label_28")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_28)
        self.lineEdit_26 = QtWidgets.QLineEdit(self.groupBox_9)
        self.lineEdit_26.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_26.setFont(font)
        self.lineEdit_26.setObjectName("lineEdit_26")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.lineEdit_26)
        self.label_20 = QtWidgets.QLabel(self.groupBox_9)
        self.label_20.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Sans")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.label_20)
        self.lineEdit_29 = QtWidgets.QLineEdit(self.groupBox_9)
        self.lineEdit_29.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_29.setFont(font)
        self.lineEdit_29.setObjectName("lineEdit_29")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.lineEdit_29)
        self.label_21 = QtWidgets.QLabel(self.groupBox_9)
        self.label_21.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Sans")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.label_21)
        self.lineEdit_30 = QtWidgets.QLineEdit(self.groupBox_9)
        self.lineEdit_30.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_30.setFont(font)
        self.lineEdit_30.setObjectName("lineEdit_30")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.lineEdit_30)
        self.gridLayout_2.addWidget(self.groupBox_9, 1, 1, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem5, 1, 1, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_OpenSerial = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_OpenSerial.setEnabled(True)
        self.pushButton_OpenSerial.setObjectName("pushButton_OpenSerial")
        self.horizontalLayout_2.addWidget(self.pushButton_OpenSerial)
        self.comboBox_ComNum = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_ComNum.setObjectName("comboBox_ComNum")
        self.horizontalLayout_2.addWidget(self.comboBox_ComNum)
        self.pushButton_UpdateSerialShow = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_UpdateSerialShow.setObjectName("pushButton_UpdateSerialShow")
        self.horizontalLayout_2.addWidget(self.pushButton_UpdateSerialShow)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.gridLayout.addItem(spacerItem6, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 1, 2)
        self.groupBox_7 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_7.setObjectName("groupBox_7")
        self.formLayout_2 = QtWidgets.QFormLayout(self.groupBox_7)
        self.formLayout_2.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_2.setObjectName("formLayout_2")
        spacerItem7 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout_2.setItem(0, QtWidgets.QFormLayout.LabelRole, spacerItem7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem8)
        self.pushButton_Style = QtWidgets.QPushButton(self.groupBox_7)
        self.pushButton_Style.setObjectName("pushButton_Style")
        self.horizontalLayout_8.addWidget(self.pushButton_Style)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem9)
        self.pushButton_InfWriteInformation = QtWidgets.QPushButton(self.groupBox_7)
        self.pushButton_InfWriteInformation.setObjectName("pushButton_InfWriteInformation")
        self.horizontalLayout_8.addWidget(self.pushButton_InfWriteInformation)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem10)
        self.label_9 = QtWidgets.QLabel(self.groupBox_7)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_8.addWidget(self.label_9)
        self.progressBarInfWrite = QtWidgets.QProgressBar(self.groupBox_7)
        self.progressBarInfWrite.setProperty("value", 0)
        self.progressBarInfWrite.setObjectName("progressBarInfWrite")
        self.horizontalLayout_8.addWidget(self.progressBarInfWrite)
        self.formLayout_2.setLayout(1, QtWidgets.QFormLayout.SpanningRole, self.horizontalLayout_8)
        self.label_16 = QtWidgets.QLabel(self.groupBox_7)
        self.label_16.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Sans")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_16)
        self.lineEdit_9 = QtWidgets.QLineEdit(self.groupBox_7)
        self.lineEdit_9.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.lineEdit_9.setFont(font)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_9)
        self.label_2 = QtWidgets.QLabel(self.groupBox_7)
        font = QtGui.QFont()
        font.setFamily("Sans")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.lineEdit_10 = QtWidgets.QLineEdit(self.groupBox_7)
        self.lineEdit_10.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_10.setFont(font)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEdit_10)
        self.label_19 = QtWidgets.QLabel(self.groupBox_7)
        self.label_19.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Sans")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_19)
        self.lineEdit_11 = QtWidgets.QLineEdit(self.groupBox_7)
        self.lineEdit_11.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_11.setFont(font)
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.lineEdit_11)
        self.label_14 = QtWidgets.QLabel(self.groupBox_7)
        self.label_14.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Sans")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_14)
        self.lineEdit_12 = QtWidgets.QLineEdit(self.groupBox_7)
        self.lineEdit_12.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_12.setFont(font)
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.lineEdit_12)
        self.label_12 = QtWidgets.QLabel(self.groupBox_7)
        self.label_12.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Sans")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_12)
        self.lineEdit_13 = QtWidgets.QLineEdit(self.groupBox_7)
        self.lineEdit_13.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_13.setFont(font)
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.lineEdit_13)
        self.label_18 = QtWidgets.QLabel(self.groupBox_7)
        self.label_18.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Sans")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.formLayout_2.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_18)
        self.lineEdit_14 = QtWidgets.QLineEdit(self.groupBox_7)
        self.lineEdit_14.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_14.setFont(font)
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.formLayout_2.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.lineEdit_14)
        self.label_15 = QtWidgets.QLabel(self.groupBox_7)
        self.label_15.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Sans")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.formLayout_2.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.label_15)
        self.lineEdit_17 = QtWidgets.QLineEdit(self.groupBox_7)
        self.lineEdit_17.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_17.setFont(font)
        self.lineEdit_17.setObjectName("lineEdit_17")
        self.formLayout_2.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.lineEdit_17)
        self.label_17 = QtWidgets.QLabel(self.groupBox_7)
        self.label_17.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Sans")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.formLayout_2.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.label_17)
        self.lineEdit_18 = QtWidgets.QLineEdit(self.groupBox_7)
        self.lineEdit_18.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_18.setFont(font)
        self.lineEdit_18.setObjectName("lineEdit_18")
        self.formLayout_2.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.lineEdit_18)
        self.gridLayout_2.addWidget(self.groupBox_7, 1, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.lab_Title.setText(_translate("Dialog", "个人剂量仪配置软件"))
        self.btnMenu_Min.setToolTip(_translate("Dialog", "最小化"))
        self.btnMenu_Max.setToolTip(_translate("Dialog", "最大化"))
        self.btnMenu_Close.setToolTip(_translate("Dialog", "关闭"))
        self.btnMenu_help.setToolTip(_translate("Dialog", "最小化"))
        self.btnMenu_help.setText(_translate("Dialog", "帮助"))
        self.groupBox_9.setTitle(_translate("Dialog", "读取信息"))
        self.pushButton_InfReadInformation.setText(_translate("Dialog", "获取信息"))
        self.label_10.setText(_translate("Dialog", "读取进度："))
        self.label_27.setText(_translate("Dialog", "仪器编号"))
        self.label_3.setText(_translate("Dialog", "用户编号"))
        self.label_26.setText(_translate("Dialog", "剂量阈值(uSv)"))
        self.label_25.setText(_translate("Dialog", "剂量率阈值(uSv)"))
        self.label_24.setText(_translate("Dialog", "时间间隔存储(s)"))
        self.label_28.setText(_translate("Dialog", "仪器日期"))
        self.label_20.setText(_translate("Dialog", "累积剂量清零"))
        self.label_21.setText(_translate("Dialog", "仪器出厂编号"))
        self.groupBox.setTitle(_translate("Dialog", "串口操作"))
        self.pushButton_OpenSerial.setText(_translate("Dialog", "打开串口"))
        self.pushButton_UpdateSerialShow.setText(_translate("Dialog", "更新串口"))
        self.groupBox_7.setTitle(_translate("Dialog", "配置信息"))
        self.pushButton_Style.setText(_translate("Dialog", "参考格式"))
        self.pushButton_InfWriteInformation.setText(_translate("Dialog", "开始配置"))
        self.label_9.setText(_translate("Dialog", "配置进度："))
        self.label_16.setText(_translate("Dialog", "仪器编号"))
        self.label_2.setText(_translate("Dialog", "用户编号"))
        self.label_19.setText(_translate("Dialog", "剂量阈值(uSv)"))
        self.label_14.setText(_translate("Dialog", "剂量率阈值(uSv)"))
        self.label_12.setText(_translate("Dialog", "时间间隔存储(s)"))
        self.label_18.setText(_translate("Dialog", "仪器日期"))
        self.label_15.setText(_translate("Dialog", "累积剂量清零"))
        self.label_17.setText(_translate("Dialog", "仪器出厂编号"))

