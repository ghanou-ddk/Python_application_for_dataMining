 # -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Ghanou\Desktop\memoire\gui1.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
import visualization as vis
import dataPreparation
import pandas as pd
import numpy as np
from PyQt5.QtWidgets import (QMainWindow, QLabel, QGridLayout, qApp,
                             QApplication, QWidget, QPushButton,QFileDialog,QTableView)
from PyQt5.QtWidgets import QTreeWidget, QTreeWidgetItem
        
import datamining

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1545, 879)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1541, 841))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.tabWidget.setFont(font)
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget.setMovable(False)
        self.tabWidget.setObjectName("tabWidget")
        
        #
        self.tab_feature_analysis = QtWidgets.QWidget()
        self.tab_feature_analysis.setObjectName("tab_feature_analysis")
        self.groupBox_feature_selection = QtWidgets.QGroupBox(self.tab_feature_analysis)
        self.groupBox_feature_selection.setGeometry(QtCore.QRect(910, 10, 591, 731))
        font = QtGui.QFont()
        font.setFamily("Dubai")
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.groupBox_feature_selection.setFont(font)
        self.groupBox_feature_selection.setObjectName("groupBox_feature_selection")
        self.pushButton_20 = QtWidgets.QPushButton(self.groupBox_feature_selection)
        self.pushButton_20.setGeometry(QtCore.QRect(380, 260, 121, 31))
        self.pushButton_20.setObjectName("pushButton_20")
        self.pushButton_19 = QtWidgets.QPushButton(self.groupBox_feature_selection)
        self.pushButton_19.setGeometry(QtCore.QRect(370, 170, 151, 31))
        self.pushButton_19.setObjectName("pushButton_19")
        self.listWidget_2 = QtWidgets.QListWidget(self.groupBox_feature_selection)
        self.listWidget_2.setGeometry(QtCore.QRect(30, 70, 231, 551))
        self.listWidget_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.listWidget_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.listWidget_2.setObjectName("listWidget_2")
        self.groupBox_info_gain = QtWidgets.QGroupBox(self.tab_feature_analysis)
        self.groupBox_info_gain.setGeometry(QtCore.QRect(10, 10, 871, 731))
        font = QtGui.QFont()
        font.setFamily("Dubai")
        font.setPointSize(13)
        self.groupBox_info_gain.setFont(font)
        self.groupBox_info_gain.setObjectName("groupBox_info_gain")
        self.label_IG_img = QtWidgets.QLabel(self.groupBox_info_gain)
        self.label_IG_img.setGeometry(QtCore.QRect(50, 260, 781, 411))
        self.label_IG_img.setObjectName("label_IG_img")
        self.pushButton_IG = QtWidgets.QPushButton(self.groupBox_info_gain)
        self.pushButton_IG.setGeometry(QtCore.QRect(380, 160, 111, 41))
        self.pushButton_IG.setObjectName("pushButton_IG")
        self.label_IG_class = QtWidgets.QLabel(self.groupBox_info_gain)
        self.label_IG_class.setGeometry(QtCore.QRect(250, 60, 181, 31))
        self.label_IG_class.setObjectName("label_IG_class")
        self.comboBox_IG = QtWidgets.QComboBox(self.groupBox_info_gain)
        self.comboBox_IG.setGeometry(QtCore.QRect(440, 60, 161, 31))
        self.comboBox_IG.setObjectName("comboBox_IG")
        
        #ffffffffffffffffffffffffffffffffffffff
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.tableView = QtWidgets.QTableView(self.tab_5)
        self.tableView.setGeometry(QtCore.QRect(10, 240, 1521, 500))
        self.tableView.setAlternatingRowColors(True)
        self.tableView.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectItems)
        self.tableView.setObjectName("tableView")
        self.groupBox_6 = QtWidgets.QGroupBox(self.tab_5)
        self.groupBox_6.setGeometry(QtCore.QRect(1240, 0, 291, 231))
        self.groupBox_6.setObjectName("groupBox_6")
        self.listWidget = QtWidgets.QListWidget(self.groupBox_6)
        self.listWidget.setGeometry(QtCore.QRect(10, 50, 271, 181))
        self.listWidget.setObjectName("listWidget")
        self.pushButton_6 = QtWidgets.QPushButton(self.groupBox_6)
        self.pushButton_6.setGeometry(QtCore.QRect(10, 20, 221, 21))
        self.pushButton_6.setObjectName("pushButton_6")
        self.groupBox_7 = QtWidgets.QGroupBox(self.tab_5)
        self.groupBox_7.setGeometry(QtCore.QRect(620, 0, 311, 231))
        self.groupBox_7.setObjectName("groupBox_7")
        self.pushButton_10 = QtWidgets.QPushButton(self.groupBox_7)
        self.pushButton_10.setGeometry(QtCore.QRect(10, 30, 291, 31))
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_16 = QtWidgets.QPushButton(self.groupBox_7)
        self.pushButton_16.setGeometry(QtCore.QRect(10, 80, 291, 31))
        self.pushButton_16.setObjectName("pushButton_16")
        self.pushButton_5 = QtWidgets.QPushButton(self.groupBox_7)
        self.pushButton_5.setGeometry(QtCore.QRect(10, 130, 291, 31))
        self.pushButton_5.setObjectName("pushButton_5")
        self.groupBox_8 = QtWidgets.QGroupBox(self.tab_5)
        self.groupBox_8.setGeometry(QtCore.QRect(140, 0, 481, 231))
        self.groupBox_8.setObjectName("groupBox_8")
        self.pushButton_11 = QtWidgets.QPushButton(self.groupBox_8)
        self.pushButton_11.setGeometry(QtCore.QRect(260, 30, 171, 31))
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_13 = QtWidgets.QPushButton(self.groupBox_8)
        self.pushButton_13.setGeometry(QtCore.QRect(10, 92, 371, 31))
        self.pushButton_13.setObjectName("pushButton_13")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox_8)
        self.lineEdit_2.setGeometry(QtCore.QRect(410, 89, 61, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton_14 = QtWidgets.QPushButton(self.groupBox_8)
        self.pushButton_14.setGeometry(QtCore.QRect(10, 140, 331, 31))
        self.pushButton_14.setObjectName("pushButton_14")
        self.comboBox_3 = QtWidgets.QComboBox(self.groupBox_8)
        self.comboBox_3.setGeometry(QtCore.QRect(350, 140, 121, 31))
        self.comboBox_3.setObjectName("comboBox_3")
        self.pushButton_15 = QtWidgets.QPushButton(self.groupBox_8)
        self.pushButton_15.setGeometry(QtCore.QRect(20, 30, 171, 31))
        self.pushButton_15.setObjectName("pushButton_15")

       
        self.tabWidget.addTab(self.tab_5, "")
       




        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label_15 = QtWidgets.QLabel(self.tab)
        self.label_15.setGeometry(QtCore.QRect(210, 350, 111, 31))
        self.label_15.setText("")
        self.label_15.setObjectName("label_15")
        self.groupBox = QtWidgets.QGroupBox(self.tab)
        self.groupBox.setGeometry(QtCore.QRect(260, 20, 441, 261))
        self.groupBox.setObjectName("groupBox")
        self.comboBox = QtWidgets.QComboBox(self.groupBox)
        self.comboBox.setGeometry(QtCore.QRect(310, 30, 81, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(200, 90, 81, 21))
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(160, 220, 81, 31))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(200, 30, 91, 21))
        self.label.setObjectName("label")
        self.comboBox_2 = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_2.setGeometry(QtCore.QRect(310, 90, 81, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 30, 151, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(20, 50, 151, 51))
        self.label_4.setWordWrap(True)
        self.label_4.setObjectName("label_4")
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_4.setGeometry(QtCore.QRect(10, 120, 151, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(270, 160, 61, 21))
        self.lineEdit.setClearButtonEnabled(False)
        self.lineEdit.setObjectName("lineEdit")
        self.checkBox = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox.setGeometry(QtCore.QRect(180, 130, 271, 21))
        self.checkBox.setObjectName("checkBox")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(20, 150, 151, 51))
        self.label_5.setWordWrap(True)
        self.label_5.setObjectName("label_5")
        self.line = QtWidgets.QFrame(self.groupBox)
        self.line.setGeometry(QtCore.QRect(160, 20, 20, 181))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 10, 241, 261))
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_7 = QtWidgets.QLabel(self.groupBox_2)
        self.label_7.setGeometry(QtCore.QRect(100, 70, 71, 21))
        self.label_7.setObjectName("label_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_8.setGeometry(QtCore.QRect(0, 30, 91, 23))
        self.pushButton_8.setObjectName("pushButton_8")
        self.label_8 = QtWidgets.QLabel(self.groupBox_2)
        self.label_8.setGeometry(QtCore.QRect(100, 30, 71, 16))
        self.label_8.setObjectName("label_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_9.setGeometry(QtCore.QRect(0, 70, 91, 23))
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_2.setGeometry(QtCore.QRect(60, 220, 101, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_7 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_7.setGeometry(QtCore.QRect(0, 130, 91, 23))
        self.pushButton_7.setObjectName("pushButton_7")
        self.label_9 = QtWidgets.QLabel(self.groupBox_2)
        self.label_9.setGeometry(QtCore.QRect(100, 130, 71, 21))
        self.label_9.setObjectName("label_9")
        self.checkBox_2 = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_2.setGeometry(QtCore.QRect(10, 110, 191, 17))
        self.checkBox_2.setObjectName("checkBox_2")
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 280, 671, 471))
        self.groupBox_3.setObjectName("groupBox_3")
        self.label_12 = QtWidgets.QLabel(self.groupBox_3)
        self.label_12.setGeometry(QtCore.QRect(30, 30, 611, 411))
        self.label_12.setText("")
        self.label_12.setObjectName("label_12")
        self.groupBox_4 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_4.setGeometry(QtCore.QRect(700, 0, 821, 761))
        self.groupBox_4.setObjectName("groupBox_4")
        self.label_10 = QtWidgets.QLabel(self.groupBox_4)
        self.label_10.setGeometry(QtCore.QRect(20, 20, 790, 730))
        self.label_10.setText("")
        self.label_10.setObjectName("label_10")
        self.tabWidget.addTab(self.tab_feature_analysis, "")
#######data minig tab
        self.tab_dm = QtWidgets.QWidget()
        self.tab_dm.setObjectName("tab_dm")
        self.groupBox_9 = QtWidgets.QGroupBox(self.tab_dm)
        self.groupBox_9.setGeometry(QtCore.QRect(10, 10, 301, 741))
        self.groupBox_9.setObjectName("groupBox_9")
        self.listWidget_selected_features = QtWidgets.QListWidget(self.groupBox_9)
        self.listWidget_selected_features.setGeometry(QtCore.QRect(10, 40, 281, 671))
        self.listWidget_selected_features.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.listWidget_selected_features.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.listWidget_selected_features.setObjectName("listWidget_selected_features")
        self.groupBox_10 = QtWidgets.QGroupBox(self.tab_dm)
        self.groupBox_10.setGeometry(QtCore.QRect(310, 10, 401, 741))
        self.groupBox_10.setObjectName("groupBox_10")
        self.treeWidget_techniques_DM = QtWidgets.QTreeWidget(self.groupBox_10)
        self.treeWidget_techniques_DM.setGeometry(QtCore.QRect(10, 30, 251, 221))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.treeWidget_techniques_DM.setFont(font)
        self.treeWidget_techniques_DM.setAnimated(True)
        self.treeWidget_techniques_DM.setObjectName("treeWidget_techniques_DM")
        self.treeWidget_techniques_DM.headerItem().setText(0, "1")
        self.pushButton_select_DM = QtWidgets.QPushButton(self.groupBox_10)
        self.pushButton_select_DM.setGeometry(QtCore.QRect(280, 40, 81, 31))
        self.pushButton_select_DM.setObjectName("pushButton_select_DM")
        self.label_3 = QtWidgets.QLabel(self.groupBox_10)
        self.label_3.setGeometry(QtCore.QRect(30, 280, 101, 31))
        self.label_3.setObjectName("label_3")
        self.label_6 = QtWidgets.QLabel(self.groupBox_10)
        self.label_6.setEnabled(False)
        self.label_6.setGeometry(QtCore.QRect(30, 330, 231, 31))
        self.label_6.setObjectName("label_6")
        self.comboBox_class_DM = QtWidgets.QComboBox(self.groupBox_10)
        self.comboBox_class_DM.setGeometry(QtCore.QRect(130, 281, 161, 31))
        self.comboBox_class_DM.setObjectName("comboBox_class_DM")
        self.spinBox = QtWidgets.QSpinBox(self.groupBox_10)
        self.spinBox.setEnabled(False)
        self.spinBox.setGeometry(QtCore.QRect(260, 330, 51, 31))
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(30)
        self.spinBox.setObjectName("spinBox")
        self.spinBox_split_DM = QtWidgets.QSpinBox(self.groupBox_10)
        self.spinBox_split_DM.setGeometry(QtCore.QRect(160, 380, 61, 31))
        self.spinBox_split_DM.setMinimum(10)
        self.spinBox_split_DM.setMaximum(90)
        self.spinBox_split_DM.setSingleStep(10)
        self.spinBox_split_DM.setProperty("value", 70)
        self.spinBox_split_DM.setObjectName("spinBox_split_DM")
        self.label_11 = QtWidgets.QLabel(self.groupBox_10)
        self.label_11.setGeometry(QtCore.QRect(30, 380, 121, 31))
        self.label_11.setObjectName("label_11")
        self.pushButton_apply_DM = QtWidgets.QPushButton(self.groupBox_10)
        self.pushButton_apply_DM.setGeometry(QtCore.QRect(150, 560, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.pushButton_apply_DM.setFont(font)
        self.pushButton_apply_DM.setObjectName("pushButton_apply_DM")
        
        self.pushButton_compare_DM = QtWidgets.QPushButton(self.groupBox_10)
        self.pushButton_compare_DM.setGeometry(QtCore.QRect(50, 620, 301, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.pushButton_compare_DM.setFont(font)
        self.pushButton_compare_DM.setObjectName("pushButton_compare")


        self.label_14 = QtWidgets.QLabel(self.groupBox_10)
        self.label_14.setEnabled(True)
        self.label_14.setGeometry(QtCore.QRect(20, 440, 241, 31))
        self.label_14.setObjectName("label_14")
        self.spinBox_cfv_DM = QtWidgets.QSpinBox(self.groupBox_10)
        self.spinBox_cfv_DM.setEnabled(True)
        self.spinBox_cfv_DM.setGeometry(QtCore.QRect(270, 440, 51, 31))
        self.spinBox_cfv_DM.setMinimum(2)
        self.spinBox_cfv_DM.setMaximum(30)
        self.spinBox_cfv_DM.setObjectName("spinBox_cfv_DM")
        self.groupBox_11 = QtWidgets.QGroupBox(self.tab_dm)
        self.groupBox_11.setGeometry(QtCore.QRect(710, 10, 821, 741))
        self.groupBox_11.setObjectName("groupBox_11")
        self.plainTextEdit_results_DM = QtWidgets.QPlainTextEdit(self.groupBox_11)
        self.plainTextEdit_results_DM.setGeometry(QtCore.QRect(10, 20, 811, 701))
        self.plainTextEdit_results_DM.setReadOnly(True)
        self.plainTextEdit_results_DM.setObjectName("plainTextEdit_results_DM")
        self.tabWidget.addTab(self.tab_dm, "")

########end of dm tab

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1545, 21))
        self.menubar.setObjectName("menubar")
        self.menufichier = QtWidgets.QMenu(self.menubar)
        self.menufichier.setObjectName("menufichier")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionopen_dataset = QtWidgets.QAction(MainWindow)
        self.actionopen_dataset.setObjectName("actionopen_dataset")
        self.actionnew_empty = QtWidgets.QAction(MainWindow)
        self.actionnew_empty.setObjectName("actionnew_empty")
        self.actionsave_dataset = QtWidgets.QAction(MainWindow)
        self.actionsave_dataset.setObjectName("actionsave_dataset")
        self.actionSettings = QtWidgets.QAction(MainWindow)
        self.actionSettings.setObjectName("actionSettings")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionDelete_column = QtWidgets.QAction(MainWindow)
        self.actionDelete_column.setObjectName("actionDelete_column")
        self.actionDelete_selected_row = QtWidgets.QAction(MainWindow)
        self.actionDelete_selected_row.setObjectName("actionDelete_selected_row")
        self.actionOpen_data_file = QtWidgets.QAction(MainWindow)
        self.actionOpen_data_file.setObjectName("actionOpen_data_file")
        self.menufichier.addSeparator()
        self.menufichier.addAction(self.actionOpen_data_file)
        self.menufichier.addAction(self.actionExit)
        self.menubar.addAction(self.menufichier.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox_6.setTitle(_translate("MainWindow", "Statistics"))
        self.pushButton_6.setText(_translate("MainWindow", "Count frequencies in selected column"))
        self.groupBox_7.setTitle(_translate("MainWindow", "Data transformation"))
        self.pushButton_10.setText(_translate("MainWindow", "Load and apply text file that contains defenitions"))
        self.pushButton_16.setText(_translate("MainWindow", "Normalize all dataset"))
        self.pushButton_5.setText(_translate("MainWindow", "Fill all missing (Nan) values"))
        self.groupBox_8.setTitle(_translate("MainWindow", "Data Cleaning"))
        self.pushButton_11.setText(_translate("MainWindow", "Remove selected columns"))
        self.pushButton_13.setText(_translate("MainWindow", "Remove all columns with missing (Nan) values more than (%)"))
        self.lineEdit_2.setText(_translate("MainWindow", "1"))
        self.pushButton_14.setText(_translate("MainWindow", "Remove rows with missing (Nan) values at this column"))
        self.pushButton_15.setText(_translate("MainWindow", "Remove selected rows"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "Data Preaparation"))
        self.listWidget_2.setSortingEnabled(True)
        self.pushButton_19.setText(_translate("MainWindow", "add new features"))
        self.groupBox.setTitle(_translate("MainWindow", "map visualization edit"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Annaba"))
        self.label_2.setText(_translate("MainWindow", "Cancer type :"))
        self.pushButton.setText(_translate("MainWindow", "visualize"))
        self.label.setText(_translate("MainWindow", "Wilaya :"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "All types"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "type A"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "type B"))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "type C"))
        self.pushButton_3.setText(_translate("MainWindow", "Set cancer type columns"))
        self.label_4.setText(_translate("MainWindow", "the column where the type of the cancer for the patient is specified"))
        self.pushButton_4.setText(_translate("MainWindow", "Set region Columns"))
        self.checkBox.setText(_translate("MainWindow", "show cancer types with case morer than :"))
        self.label_5.setText(_translate("MainWindow", "the column that contain patient adress"))
        self.groupBox_2.setTitle(_translate("MainWindow", "graph edit"))
        self.label_7.setText(_translate("MainWindow", "TextLabel"))
        self.pushButton_8.setText(_translate("MainWindow", "verticall axe"))
        self.label_8.setText(_translate("MainWindow", "TextLabel"))
        self.pushButton_9.setText(_translate("MainWindow", "horizontal axe"))
        self.pushButton_2.setText(_translate("MainWindow", "Graph"))
        self.pushButton_7.setText(_translate("MainWindow", "color column"))
        self.label_9.setText(_translate("MainWindow", "TextLabel"))
        self.checkBox_2.setText(_translate("MainWindow", "use color as new dimension "))
        self.groupBox_3.setTitle(_translate("MainWindow", "graph"))
        self.groupBox_4.setTitle(_translate("MainWindow", "map"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Visualization"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Interpretation\\Evaluation"))
        self.menufichier.setTitle(_translate("MainWindow", "fichier"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.actionopen_dataset.setText(_translate("MainWindow", "open dataset"))
        self.actionnew_empty.setText(_translate("MainWindow", "new empty"))
        self.actionsave_dataset.setText(_translate("MainWindow", "save dataset"))
        self.actionSettings.setText(_translate("MainWindow", "Settings"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionDelete_column.setText(_translate("MainWindow", "Delete selected column "))
        self.actionDelete_selected_row.setText(_translate("MainWindow", "Delete selected row"))
        self.actionOpen_data_file.setText(_translate("MainWindow", "Open data file"))
 ############# feature selection tab       
        self.groupBox_feature_selection.setTitle(_translate("MainWindow", "Features selection"))
        self.pushButton_20.setText(_translate("MainWindow", "Clear all"))
        self.pushButton_19.setText(_translate("MainWindow", "Add new features"))
        self.listWidget_2.setSortingEnabled(True)
        self.groupBox_info_gain.setTitle(_translate("MainWindow", "Information gain calculation for each feature"))
        self.label_IG_img.setText(_translate("MainWindow", "                                                                                      plot will show here"))
        self.pushButton_IG.setText(_translate("MainWindow", "Calculate"))
        self.label_IG_class.setText(_translate("MainWindow", "Select the class column : "))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_feature_analysis), _translate("MainWindow", "Feature analysis"))
########## dm tab
        self.groupBox_9.setTitle(_translate("MainWindow", "Selected features"))
        self.listWidget_selected_features.setSortingEnabled(True)
        self.groupBox_10.setTitle(_translate("MainWindow", "Datamining techniques"))
        self.pushButton_select_DM.setText(_translate("MainWindow", "select"))
        self.label_3.setText(_translate("MainWindow", "Class column :"))
        self.label_6.setText(_translate("MainWindow", "Number of classes (only for clustering):"))
        self.label_11.setText(_translate("MainWindow", "Split train size (%)  :"))
        self.pushButton_apply_DM.setText(_translate("MainWindow", "Apply"))
        self.pushButton_compare_DM.setText(_translate("MainWindow", "Compare all data mining techniques"))

        self.label_14.setText(_translate("MainWindow", "Cross validation ( number of  fields ):"))
        self.groupBox_11.setTitle(_translate("MainWindow", "Results"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_dm), _translate("MainWindow", "Datamining"))


        #################
        l1=[]
        # l1.append(QTreeWidgetItem(["Clustering"]))#0
        l1.append(QTreeWidgetItem(["Classification"]))#1
        # l1[0].addChild(QTreeWidgetItem(["kmeans"]))
#        l1[0].addChild(QTreeWidgetItem(["k2"]))
        l1[0].addChild(QTreeWidgetItem(["Decision tree"]))
        l1[0].addChild(QTreeWidgetItem(["SVM"]))
        l1[0].addChild(QTreeWidgetItem(["Random forest"]))


        
#        l1[1].addChild(QTreeWidgetItem(["k2"]))
        

        self.treeWidget_techniques_DM.setColumnCount(1)
        self.treeWidget_techniques_DM.setHeaderLabels(["Column 1"])
        for i in l1:
            self.treeWidget_techniques_DM.addTopLevelItem(i)


        #################
        #################
        self.actionOpen_data_file.triggered.connect(self.loaddata)
         
         #########
        self.pushButton.clicked.connect(self.visualize)
        self.actionopen_dataset.triggered.connect(self.openDataset)
        self.pushButton_5.clicked.connect(self.intrf_missing_value_impute)
        self.pushButton_6.clicked.connect(self.groupdata)
        self.pushButton_8.clicked.connect(self.graph_select_v)
        self.pushButton_9.clicked.connect(self.graph_select_h)
        self.pushButton_2.clicked.connect(self.graph)
        self.pushButton_3.clicked.connect(self.map_select_cancer)
        self.pushButton_4.clicked.connect(self.map_select_region)
        self.pushButton_10.clicked.connect(self.replace_data_values)
#        self.pushButton_12.clicked.connect(self.remove_empty_columns)
        self.pushButton_11.clicked.connect(self.remove_selected_column)
        self.pushButton_15.clicked.connect(self.remove_selected_row)
#        self.pushButton_16.clicked.connect(self.norm_dataset)
#        self.pushButton_18.clicked.connect(self.describe_dataset)
        self.pushButton_19.clicked.connect(self.add_features)
        self.pushButton_20.clicked.connect(self.clear_all)
        self.pushButton_14.clicked.connect(self.intrf_remove_rows_with_nan_values_at_selected_column)
        self.pushButton_13.clicked.connect(self.intfr_remove_column_more_than_k_nan_values)
        self.pushButton_IG.clicked.connect(self.intrf_information_gain_calculate)
                            
        self.pushButton_select_DM.clicked.connect(self.select_dm)
        self.pushButton_apply_DM.clicked.connect(self.start_dm)
        self.pushButton_compare_DM.clicked.connect(self.compare)

######### dm tab

    def compare(self):
        print('                       acccuracy      sensitivity        precesion       specificity \n')
        text= '                       acccuracy      sensitivity        precesion       specificity \n'
        res2,res,encoder,model=datamining.svm_dm(self.df,self.features_list,self.comboBox_class_DM.currentText(),self.spinBox_split_DM.value(),self.spinBox_cfv_DM.value())
        print(res2)
        text+= str(res2)
        res2,res,encoder,model=datamining.decesion_tree(self.df,self.features_list,self.comboBox_class_DM.currentText(),self.spinBox_split_DM.value(),self.spinBox_cfv_DM.value())
        print(res2)
        text+= str(res2)

        res2,res,encoder,model=datamining.neural_network(self.df,self.features_list,self.comboBox_class_DM.currentText(),self.spinBox_split_DM.value(),self.spinBox_cfv_DM.value())
        print(res2)
        text+= str(res2)
        
        self.plainTextEdit_results_DM.appendPlainText(text)


        

    def select_dm(self):
        for ix in self.treeWidget_techniques_DM.selectedIndexes():
            self.text = ix.data() 
            print(self.text)
            
    def start_dm(self):
        if self.text=='SVM':
            res2,res,encoder,model=datamining.svm_dm(self.df,self.features_list,self.comboBox_class_DM.currentText(),self.spinBox_split_DM.value(),self.spinBox_cfv_DM.value())
            print('Svm ',res)
            self.plainTextEdit_results_DM.appendPlainText('Svm '+res)
     
        if self.text=='Decision tree':
            res2,res,encoder,model=datamining.decesion_tree(self.df,self.features_list,self.comboBox_class_DM.currentText(),self.spinBox_split_DM.value(),self.spinBox_cfv_DM.value())
          
            print('Decesion tree ',res)
            self.plainTextEdit_results_DM.appendPlainText('Decesion tree '+res)
 
        
 
    
 
        ##method 2
        # for i in res:
        #     self.plainTextEdit_results_DM.appendPlainText(i)
        
    


#3
        
    def clear_all(self):
        self.features_list=[]
        
        self.listWidget_2.clear()
    def add_features(self):
        self.winTable_1 = WinTable_1()
        self.listViewWin1 = QtWidgets.QListWidget(self.winTable_1)
        self.listViewWin1.setGeometry(QtCore.QRect(5, 20, 250, 600))
        self.listViewWin1.setObjectName("listViewWin1")
        self.listViewWin1.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.listViewWin1.clear()
        
        self.dataheaderslist1=list(self.df.columns.values)
        self.listViewWin1.addItems(self.dataheaderslist1)
        
        self.pushButtonWin2 = QtWidgets.QPushButton(self.winTable_1)
        self.pushButtonWin2.setGeometry(QtCore.QRect(300, 640, 80, 30))
        self.pushButtonWin2.setObjectName("pushButtonWin2")
        self.pushButtonWin2.setText('Ok')
        self.pushButtonWin2.clicked.connect(self.add_features_ok)
        self.winTable_1.show()
        
        
    def add_features_ok(self):
        self.features_list=[]
        for t in self.listViewWin1.selectedIndexes():
              self.features_list.append(t.data())
        self.listWidget_2.addItems(self.features_list)
        self.winTable_1.hide()
        self.comboBox_class_DM.addItems(self.df.columns)

#2
    def replace_data_values(self):
        self.f2, _ = QFileDialog.getOpenFileName(None, "choisir fichier", "","*.*")

        self.dd1=dataPreparation.dict_from__textfile(self.f2)
       
        self.winTable_1 = WinTable_1()
        self.listViewWin1 = QtWidgets.QListWidget(self.winTable_1)
        self.listViewWin1.setGeometry(QtCore.QRect(5, 20, 250, 600))
        self.listViewWin1.setObjectName("listViewWin1")
        self.listViewWin1.clear()
        self.dataheaderslist1=list(self.df.columns.values)
        self.listViewWin1.addItems(self.dataheaderslist1)

        
        self.listViewWin2 = QtWidgets.QListWidget(self.winTable_1)
        self.listViewWin2.setGeometry(QtCore.QRect(280, 20, 250, 600))
        self.listViewWin2.setObjectName("listViewWin1")
        self.listViewWin2.clear()
        self.dataheaderslist2=list(self.dd1.keys())
        self.listViewWin2.addItems(self.dataheaderslist2)

        self.pushButtonWin1 = QtWidgets.QPushButton(self.winTable_1)
        self.pushButtonWin1.setGeometry(QtCore.QRect(200, 640, 80, 30))
        self.pushButtonWin1.setObjectName("pushButtonWin1")
        self.pushButtonWin1.setText('add')
        self.pushButtonWin1.clicked.connect(self.wintable2_add)
        
        self.pushButtonWin2 = QtWidgets.QPushButton(self.winTable_1)
        self.pushButtonWin2.setGeometry(QtCore.QRect(300, 640, 80, 30))
        self.pushButtonWin2.setObjectName("pushButtonWin2")
        self.pushButtonWin2.setText('Done')
        self.pushButtonWin2.clicked.connect(self.wintable2_done)
        
        self.labelwin1 = QtWidgets.QLabel(self.winTable_1)
        self.labelwin1.setGeometry(QtCore.QRect(560, 20, 250, 600))
        self.labelwin1.setObjectName("labelwin1")
        self.labelwin1.setWordWrap(True)
        self.c=[]


        self.winTable_1.show()
    def wintable2_add(self):
        d1=self.listViewWin1.selectedIndexes()[0].data()
        d2=self.listViewWin2.selectedIndexes()[0].data()

        self.c.append([d1,d2])
        self.labelwin1.setText(self.labelwin1.text()+d2+'  '+d1+'\n')
        
    def wintable2_done(self):
      
        self.df=dataPreparation.replacewith(self.df,self.dd1,self.c)
        self.winTable_1.hide()     
        self.df=self.df.replace('nan',np.NaN)
        model=dataPreparation.getModel(self.df)
        self.tableView.setModel(model)
        
    def openDataset(self):
        print('dataset ready!!!!! ')
    def visualize(self):
        filtre_nbcase=0
        if self.checkBox.isChecked():     
            filtre_nbcase=int(str(self.lineEdit.text()))
        
        vis.staticMap(str(self.comboBox.currentText()),80,self.df,self.map_region_text,self.map_cancer_text,filtre_nbcase)
        p=QPixmap('img.png')
#        p1 = p.scaled(900, 900, QtCore.Qt.KeepAspectRatio)
        self.label_10.setPixmap(p)
        
    def graph(self):
        vis.graph(self.df,self.graph_h_text,self.graph_v_text)
        p=QPixmap('graph_img.png')
#        p1 = p.scaled(600, 400, QtCore.Qt.KeepAspectRatio)
        self.label_12.setPixmap(p)

       
    def map_select_region(self):
        self.winTable = WinTable()
        self.listViewWin1 = QtWidgets.QListWidget(self.winTable)
        self.listViewWin1.setGeometry(QtCore.QRect(5, 20, 200, 300))
        self.listViewWin1.setObjectName("listViewWin1")
        self.listViewWin1.clear()

        self.dataheaderslist1=list(self.df.columns.values)
        self.listViewWin1.addItems(self.dataheaderslist1)

        self.pushButtonWin1 = QtWidgets.QPushButton(self.winTable)
        self.pushButtonWin1.setGeometry(QtCore.QRect(50, 320, 80, 30))
        self.pushButtonWin1.setObjectName("pushButtonWin1")
        self.pushButtonWin1.setText('Select')
        self.pushButtonWin1.clicked.connect(self.map_get_selected_region)
        self.winTable.show()
    def map_get_selected_region(self):
        d1=self.listViewWin1.selectedIndexes()[0].data()
        self.map_region_text=d1
        self.winTable.hide()        


    def map_select_cancer(self):
        self.winTable = WinTable()
        self.listViewWin1 = QtWidgets.QListWidget(self.winTable)
        self.listViewWin1.setGeometry(QtCore.QRect(5, 20, 200, 300))
        self.listViewWin1.setObjectName("listViewWin1")
        self.listViewWin1.clear()

        self.dataheaderslist1=list(self.df.columns.values)
        self.listViewWin1.addItems(self.dataheaderslist1)

        self.pushButtonWin1 = QtWidgets.QPushButton(self.winTable)
        self.pushButtonWin1.setGeometry(QtCore.QRect(50, 320, 80, 30))
        self.pushButtonWin1.setObjectName("pushButtonWin1")
        self.pushButtonWin1.setText('Select')
        self.pushButtonWin1.clicked.connect(self.map_get_selected_cancer)
        self.winTable.show()
    def map_get_selected_cancer(self):
        d1=self.listViewWin1.selectedIndexes()[0].data()
        self.map_cancer_text=d1
        self.winTable.hide()        

       
    def graph_select_v(self):
       self.winTable = WinTable()
       self.listViewWin1 = QtWidgets.QListWidget(self.winTable)
       self.listViewWin1.setGeometry(QtCore.QRect(5, 20, 100, 200))
       self.listViewWin1.setObjectName("listViewWin1")
       self.dataheaderslist1=list(self.df.columns.values)
       self.listViewWin1.clear()
       self.listViewWin1.addItems(self.dataheaderslist1)
       
       self.listViewWin2 = QtWidgets.QListWidget(self.winTable)
       self.listViewWin2.setGeometry(QtCore.QRect(125, 20, 100, 200))
       self.listViewWin2.setObjectName("listViewWin2")
       self.listViewWin2.clear()

       self.listViewWin2.addItem('kdk')
       
       self.pushButtonWin1 = QtWidgets.QPushButton(self.winTable)
       self.pushButtonWin1.setGeometry(QtCore.QRect(50, 270, 80, 30))
       self.pushButtonWin1.setObjectName("pushButtonWin1")
       self.pushButtonWin1.setText('Select')
       self.pushButtonWin1.clicked.connect(self.graph_get_selected_v)
       self.winTable.show()
    def graph_get_selected_v(self):
        d1=self.listViewWin1.selectedIndexes()[0].data()
        self.label_8.setText(d1)
        self.graph_v_text=d1
        self.winTable.hide()

    def graph_select_h(self):
        self.winTable = WinTable()
        self.listViewWin1 = QtWidgets.QListWidget(self.winTable)
        self.listViewWin1.setGeometry(QtCore.QRect(5, 20, 100, 200))
        self.listViewWin1.setObjectName("listViewWin1")
        self.listViewWin1.clear()

        self.dataheaderslist1=list(self.df.columns.values)
        self.listViewWin1.addItems(self.dataheaderslist1)

        self.listViewWin2 = QtWidgets.QListWidget(self.winTable)
        self.listViewWin2.setGeometry(QtCore.QRect(125, 20, 100, 200))
        self.listViewWin2.setObjectName("listViewWin2")
        self.listViewWin2.clear()

        self.listViewWin2.addItem('kdk')
        self.pushButtonWin1 = QtWidgets.QPushButton(self.winTable)
        self.pushButtonWin1.setGeometry(QtCore.QRect(50, 270, 80, 30))
        self.pushButtonWin1.setObjectName("pushButtonWin1")
        self.pushButtonWin1.setText('Select')
        self.pushButtonWin1.clicked.connect(self.graph_get_selected_h)
        
        
        self.winTable.show()
    def graph_get_selected_h(self):
        d1=self.listViewWin1.selectedIndexes()[0].data()
        self.label_7.setText(d1)
        self.graph_h_text=d1
        self.winTable.hide()
        
    def loaddata(self):
        self.f1, _ = QFileDialog.getOpenFileName(None, "choisir fichier", "","*.*")
        self.df = pd.read_csv(self.f1,sep=',',na_values='na',dtype=object)
        #if errror here change qtable widget to qtableview
        model=dataPreparation.getModel(self.df)
        self.tableView.setModel(model)
        self.comboBox_3.addItems(self.df.columns)
        self.comboBox_IG.addItems(self.df.columns)
        
        
#cleaninig   
        
    def intrf_remove_rows_with_nan_values_at_selected_column(self):
        self.df=dataPreparation.remove_rows_with_nan_values_at_selected_column(self.df,self.comboBox_3.currentText())
        self.df = self.df.reset_index(drop=True)

        model=dataPreparation.getModel(self.df)
        self.tableView.setModel(model)
    def intfr_remove_column_more_than_k_nan_values(self):
        self.df=dataPreparation.remove_column_more_than_k_nan_values(self.df,int(str(self.lineEdit_2.text()))/100)
        self.df = self.df.reset_index(drop=True)

        model=dataPreparation.getModel(self.df)
        self.tableView.setModel(model)
        
#feature selection
    
    
    def intrf_information_gain_calculate(self):

        



        self.encoder,self.encoded_df=dataPreparation.label_encoder_df(self.df)
        dataPreparation.information_gain_calculate(self.encoded_df,self.comboBox_IG.currentText())
        p=QPixmap('graph_img_1.png')
        self.label_IG_img.setPixmap(p)   


        
        
 ## transformation
    def intrf_missing_value_impute (self):
        self.encoder,self.encoded_df=dataPreparation.label_encoder_df(self.df)
        self.encoded_df=dataPreparation.miss_forest_impute(self.encoded_df)
        self.df=dataPreparation.reverse_label_encoder_df(self.encoder,self.encoded_df)
        model=dataPreparation.getModel(self.df)
        self.tableView.setModel(model)
        
        
        
        
        
      ##########  
        
        
        
        
    def groupdata(self):
        indexes = self.tableView.selectionModel().selectedColumns()
        for index in sorted(indexes):
            print('column %d is selected' % index.column())
        col_name=self.df.columns[indexes[0].column()]
        print(col_name)
        glist = self.df[col_name].tolist()
        freqs = {}
        for w in glist:
            freqs[str(w)] = freqs.get(str(w), 0) + 1
        freqs = sorted(freqs.items(), key=lambda kv: kv[1])
        freqs1=[]
        for i in range(len(freqs)):
            freqs1.append(str(freqs[i][0])+' : '+str(freqs[i][1]))
        self.listWidget.clear()
        self.listWidget.addItems(freqs1)
        
    def remove_selected_row(self):
               
                rows = sorted(set(index.row() for index in
                      self.tableView.selectedIndexes()))
                
                self.df=dataPreparation.remove_selected_row(self.df,rows)
                model=dataPreparation.getModel(self.df)
                self.tableView.setModel(model)
    def remove_selected_column(self):
                indexes = self.tableView.selectionModel().selectedColumns()
                self.df=dataPreparation.remove_selected_column(self.df,indexes)
                model=dataPreparation.getModel(self.df)
                self.tableView.setModel(model)
    def remove_empty_columns(self):
        non_null_columns = [col for col in self.df.columns if self.df.loc[:, col].notna().any()]
        self.df=self.df[non_null_columns]
        model=dataPreparation.getModel(self.df)
        self.tableView.setModel(model)
    def norm_dataset(self):
        self.df=self.df.apply(lambda x: (x - np.mean(x)) / (np.max(x) - np.min(x)))
        model=dataPreparation.getModel(self.df)
        self.tableView.setModel(model)
    def describe_dataset(self):
        self.desc=self.df.describe()
        indx=self.desc.index[:]
        self.desc.insert(0,'index',indx,True)
        model=dataPreparation.getModel(self.desc)
        self.tableView_2.setModel(model)
        


#        
#
class featureSelection(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.title = "Feature selection tab"
        self.top    = 150
        self.left   = 300
        self.width  = 900
        self.height = 700
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height) 
        
        
        
        
class WinTable(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.title = "Table"
        self.top    = 150
        self.left   = 300
        self.width  = 300
        self.height = 300
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height) 
    
    
class WinTable_1(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.title = "select column to text file"
        self.top    = 150
        self.left   = 300
        self.width  = 750
        self.height = 800
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height) 
    

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
