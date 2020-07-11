#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 15:39:02 2020

@author: sogentle
"""


import sys
import os
import time
import subprocess


from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import uic
from PyQt5.QtGui import QIntValidator


from lib.Modeler import SimplePCB

form_class = uic.loadUiType('./resource/main.ui')[0]

class TestForm(QMainWindow, form_class): # UI를 상속 받음
    def __init__(self):
        super().__init__()
        self.setupUi(self) # setupUi는 상속 받은 UI안에 속해있기 때문에 실행 가능 
        
        self.ModelNumb = 1

        self.SetInitValue()
        self.InitLock()

        self.SetOptions()

        # # Making Instance
        # InstNumb=1
        # self.MakePCB(InstNumb)
        
        # self.pushButton_PcbLayerNumber.connect()
        
        self.pushButton_Exit.clicked.connect(QCoreApplication.instance().quit)
        
        self.pushButton_PcbLayerNumber.clicked.connect(self.PcbLayerApply)
        self.pushButton_ComponentsNumber.clicked.connect(self.ComponentsApply)
        self.pushButton_DesignCheck.clicked.connect(self.ValidationCheck)
        self.pushButton_DesignDelete.clicked.connect(self.DeleteModel)


        # self.tableWidget_PcbCaseInfor.setCellWidget()
    def _setComponentCell(self, i, SideName, CaseContactName):
        self.SideName = QComboBox()
        self.SideName.addItems(["Top","Bottom"])
        self.tableWidget_Components.setCellWidget(i,1, self.SideName)

        self.CaseContactName = QComboBox()
        self.CaseContactName.addItems(["True","False"])
        self.tableWidget_Components.setCellWidget(i,7, self.CaseContactName)
        
    
    def SetOptions(self):
        UpperCaseMaterial = QComboBox()
        self.tableWidget_PcbCaseInfor.setCellWidget(1,4, UpperCaseMaterial)
        LowerCaseMaterial = QComboBox()
        self.tableWidget_PcbCaseInfor.setCellWidget(2,4, LowerCaseMaterial)

        for i in range(int(self.lineEdit_ComponentsNumber.text())):
            SideName = "IC"+str(i)+"Side"
            CaseContactName = "IC"+str(i)+"CaseContact"
            self._setComponentCell(i, SideName, CaseContactName)
        
        
    def SetInitValue(self):
        #set Initial Value in each lineEdit
        self.lineEdit_AmbientTemp.setValidator(QIntValidator())
        self.lineEdit_AmbientTemp.setText('70')
        self.lineEdit_PcbLayerNumber.setValidator(QIntValidator())
        self.lineEdit_PcbLayerNumber.setText('2')
        self.lineEdit_ComponentsNumber.setValidator(QIntValidator())
        self.lineEdit_ComponentsNumber.setText('1')

    def InitLock(self):
        #LineEdit Inactive
        self.lineEdit_AmbientTemp.setEnabled(False)
        self.lineEdit_PcbLayerNumber.setEnabled(False)
        self.lineEdit_ComponentsNumber.setEnabled(False)
        #Buttone Inactive
        self.pushButton_RunSimulation.setEnabled(False)
        self.pushButton_PcbLayerNumber.setEnabled(False)
        self.pushButton_ComponentsNumber.setEnabled(False)
        self.pushButton_DesignCheck.setEnabled(False)
        self.pushButton_DesignDelete.setEnabled(False)
        #Table Inactive
        self.tableWidget_PcbCaseInfor.setEnabled(False)
        self.tableWidget_PcbLayers.setEnabled(False)
        self.tableWidget_Components.setEnabled(False)




    def InitModel(self, InstNumb):
        pass
        # Making Instance
        # Board1 = SimplePCB()
        # Board1.Name = "Simplified_PCB"
        # print(Board1.Name)
        # Board1._setResultPath()

        # # Get Material Lists
        # for key, value in Board1.getMaterialList().items():
        #     print(key, ": ", value)

    def PcbLayerApply(self):
        if int(self.lineEdit_PcbLayerNumber.text()) >= 0:
            self.tableWidget_PcbLayers.setRowCount(int(self.lineEdit_PcbLayerNumber.text()))
            self.PcbLayerRename()
        else:
            print("Error in Layer Number")

    def PcbLayerRename(self):
        self._setTableVertical(self.lineEdit_PcbLayerNumber, self.tableWidget_PcbLayers, "Layer")


    def ComponentsApply(self):
        if int(self.lineEdit_ComponentsNumber.text()) >= 0:
            self.tableWidget_Components.setRowCount(int(self.lineEdit_ComponentsNumber.text()))
            self.ComponentsRename()
        else:
            print("Error in IC Number")
        
    def ComponentsRename(self):
        self._setTableVertical(self.lineEdit_ComponentsNumber, self.tableWidget_Components, "IC")

    def _setTableVertical(self, lineEdit, tableName, name):
        if int(lineEdit.text()) <= 0 :
            print("Error in Setting Layers")
            return None

        VerticalHeader=[]
        for i in range(int(lineEdit.text())):
            # self.tableWidget_PcbLayers.setItem(i,0, QTableWidgetItem("Hello"))
            VerticalHeader.append(name+ " " + str(i+1))
        if name == 'Layer':
            VerticalHeader[0]= VerticalHeader[0] + " [TOP]"
            VerticalHeader[-1]= VerticalHeader[-1] + " [BOT]"

        tableName.setVerticalHeaderLabels(VerticalHeader)
    

    def ValidationCheck(self):
        pass

    def DeleteModel(self):
        pass
    
    def AddModel(self):
        self.ModelNumb += 1 
        self.InitModel()
        
        
    
    def RunSimulation(self):
        pass

    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TestForm()
    window.show()
    app.exec_()
    

# self.table = QtGui.QTableWidget()
# self.table.setColumnCount(3)
# self.setCentralWidget(self.table)
# data1 = ['row1','row2','row3','row4']
# data2 = ['1','2.0','3.00000001','3.9999999']
# combo_box_options = ["Option 1","Option 2","Option 3"]

# self.table.setRowCount(4)

# for index in range(4):
#     item1 = QtGui.QTableWidgetItem(data1[index])
#     self.table.setItem(index,0,item1)
#     item2 = QtGui.QTableWidgetItem(data2[index])
#     self.table.setItem(index,1,item2)
#     combo = QtGui.QComboBox()
#     for t in combo_box_options:
#         combo.addItem(t)
#     self.table.setCellWidget(index,2,combo)







# # Set Parameters    
# Board1.setPcbInfo(Thickness=1.6, Width=100, Depth=90)

# Layers_Thickness=[0.035, 0.07, 0.035, 0.035, 0.03, 0.07, 0.07, 0.03, 0.035, 0.035, 0.07, 0.035]
# Layers_Percentage=[85, 75, 80, 90, 95, 95, 95, 95, 90, 80, 75, 85]

# Board1.setLayersInfo(Layers=12, Thickness=Layers_Thickness, Percentage=Layers_Percentage)

# Board1.addComponent(name="U_T_Sim", X=20, Z=50, side='Top', width=4, depth=5, height=3, material='Si(Silicon)', TIM='No', powerType='Simplified', power=1)
# Board1.addComponent(name="U_T_Sim_TIM", X=40, Z=50, side='Top', width=4, depth=5, height=3, material='Si(Silicon)', TIM='Yes', powerType='Simplified', power=1)
# Board1.addComponent(name="U_T_2R", X=60, Z=50, side='Top', width=4, depth=5, height=3, material='Si(Silicon)', TIM='No', powerType='2R', power=1, junction2Case = 1, junction2Board=10)
# Board1.addComponent(name="U_T_2R_TIM", X=80, Z=50, side='Top', width=4, depth=5, height=3, material='Si(Silicon)', TIM='Yes', powerType='2R', power=1, junction2Case = 1, junction2Board=10)

# Board1.setCase(Upper_Height=10, Upper_Thickness=5, Upper_Material='ADC12', Lower_Height=15, Lower_Thickness=3, Lower_Material='SECC')

# Board1._setPcbInfo()
# Board1._setLayersInfo()
# Board1._setPcbComponents()
# Board1._setCase()
# ResultFile='Result.xml'
# Board1.saveXML(fileName=ResultFile)
# #CurrentFolder=os.path.abspath(__file__)
# CurrentFolder=os.getcwd()
# ResultFileFullPath=os.path.join(CurrentFolder, ResultFile)
# print(ResultFileFullPath)
# ETSolver='"C:\\Program Files\\6SigmaETRelease14\\6SigmaEmbeddedSolver.exe"'

# BatchCommand = ETSolver + " -xmlmodel " + ResultFile + " -licenseserver 10.230.22.106 4242 -decodeSimulationResults"

# print("RunSimulation")

# while True:
#     try:
#         returend_output = subprocess.check_output(BatchCommand)
#         print("DONE")
#         break
#     except:
#         time.sleep(10)
    
# print("--------------------------------")
# print(returend_output)
# #os.system(BatchCommand)


# print("------------END--------------")