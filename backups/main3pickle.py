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
import datetime 


from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import uic
from PyQt5.QtGui import QIntValidator, QPixmap
import image_rc

# from resource import image
from lib.Modeler import SimplePCB

form_class = uic.loadUiType('./resource/main.ui')[0]

class TestForm(QMainWindow, form_class): # UI를 상속 받음
    def __init__(self):
        super().__init__()
        self.setupUi(self) # setupUi는 상속 받은 UI안에 속해있기 때문에 실행 가능 

        # Variables
        self.limiteNumber = 20
        self.modelNumb = 0
        self.currentNumb = 0
        self.boardList = []
        # self.boardDict = {}


        # Initialize
        self._SetInitValue() # 초기값 설정 
        self.SetOptions() # 표 형태 설정 
        self.InitLock() # 초기 잠금 

        

        # 버튼 연결 
        # Main
        self.pushButton_NewModel.clicked.connect(self.NewModel)
        self.pushButton_SaveModel.clicked.connect(self.SaveModel)
        self.pushButton_RunSimulation.clicked.connect(self.RunSimulation)
        self.pushButton_Exit.clicked.connect(QCoreApplication.instance().quit)

        # PCB and Components
        self.pushButton_PcbLayerNumber.clicked.connect(self.PcbLayerApply)
        self.pushButton_ComponentsNumber.clicked.connect(self.ComponentsApply)

        # Results
        # self.comboBox_Boards.currentIndexChanged.connect(self.setCurrentBoard) 
        self.pushButton_LoadModel.clicked.connect(self.LoadModel)
        self.pushButton_DeleteModel.clicked.connect(self.DeleteModel)
        self.pushButton_CheckModel.clicked.connect(self.CheckModel)
        
    # def append_log_msg(self, message): # 로그 기록 
    #     now = datetime.datetime.now()
    #     nowDatetime = now.strftime('%Y-%m-%D %H:%M:%S')
    #     app_msg = '[' + nowDatetime + ']' + message # ID를 받거나, IP를 가져올까? 
    #     print(app_msg)

    def SetOptions(self): # 초기값 
        # pixmap1 = QPixmap("./resource/Tap2.png")
        # self.Image_Geometry.setPixmap(pixmap1)
        # Geometry 탭 초기값 
        self.tableWidget_PcbCaseInfor.setItem(0,4, QTableWidgetItem("[고정값]Copper, FR4"))
        self.tableWidget_PcbCaseInfor.setItem(0,3, QTableWidgetItem("[X] Meaningless"))
        self.tableWidget_PcbCaseInfor.setItem(1,0, QTableWidgetItem("[고정값] PCB Width"))
        self.tableWidget_PcbCaseInfor.setItem(1,1, QTableWidgetItem("[고정값] PCB Depth"))
        self.tableWidget_PcbCaseInfor.setItem(2,0, QTableWidgetItem("[고정값] PCB Width"))
        self.tableWidget_PcbCaseInfor.setItem(2,1, QTableWidgetItem("[고정값] PCB Depth"))
 
        self.UpperCaseMaterial = QComboBox()
        self.tableWidget_PcbCaseInfor.setCellWidget(1,4, self.UpperCaseMaterial)
        self.LowerCaseMaterial = QComboBox()
        self.tableWidget_PcbCaseInfor.setCellWidget(2,4, self.LowerCaseMaterial)
        
        self._setLayerInitValue() # PCB Layer 탭 초기값 
        self.setComponentOption() # 소자 부분 초기화, 길이에 따라 설정 개수가 많아짐 

 
        ## Table Type을 문자 들어오면 에러 메세지 띄우게
        ## Table 필요 없는 부분을 READ ONLY로 변경 

        
    def _SetInitValue(self): # 초기값 설정 
        #set Initial Value in each lineEdit
        self.lineEdit_AmbientTemp.setValidator(QIntValidator()) # Only Integer available.
        self.lineEdit_AmbientTemp.setText('70')
        self.lineEdit_PcbLayerNumber.setValidator(QIntValidator())
        self.lineEdit_PcbLayerNumber.setText('2')
        self.lineEdit_ComponentsNumber.setValidator(QIntValidator())
        self.lineEdit_ComponentsNumber.setText('1')

        self.tableWidget_PcbCaseInfor.setItem(0,0, QTableWidgetItem("100")) # PCB Width
        self.tableWidget_PcbCaseInfor.setItem(0,1, QTableWidgetItem("100")) # PCB Depth
        self.tableWidget_PcbCaseInfor.setItem(0,2, QTableWidgetItem("1.6")) # PCB Height
        self.tableWidget_PcbCaseInfor.setItem(1,2, QTableWidgetItem("10")) # Upper Height
        self.tableWidget_PcbCaseInfor.setItem(1,3, QTableWidgetItem("5")) # Upper Thickness
        self.tableWidget_PcbCaseInfor.setItem(2,2, QTableWidgetItem("7")) # Upper Height
        self.tableWidget_PcbCaseInfor.setItem(2,3, QTableWidgetItem("5")) # Upper Thickness

    def _setLayerInitValue(self):
        for i in range(int(self.lineEdit_PcbLayerNumber.text())):
            self.tableWidget_PcbLayers.setItem(i,0, QTableWidgetItem("0.035")) # Copper Thickness
            self.tableWidget_PcbLayers.setItem(i,1, QTableWidgetItem("80")) # Copper Percentage
        
    def setComponentOption(self):
        for i in range(int(self.lineEdit_ComponentsNumber.text())):
            Side = QComboBox()
            self.tableWidget_Components.setCellWidget(i,1, Side)
            Side.addItems(["Top", "Bottom"])
            TIM = QComboBox()
            self.tableWidget_Components.setCellWidget(i,7, TIM)
            TIM.addItems(["Yes", "No"])
            ModelType = QComboBox()
            self.tableWidget_Components.setCellWidget(i,8, ModelType)
            ModelType.addItems(["Simplified", "2R"])
            self.tableWidget_Components.setItem(i,9, QTableWidgetItem("For 2R"))
            self.tableWidget_Components.setItem(i,10, QTableWidgetItem("For 2R"))

    def InitLock(self):
        #LineEdit Inactive
        self.lineEdit_AmbientTemp.setEnabled(False)
        self.lineEdit_PcbLayerNumber.setEnabled(False)
        self.lineEdit_ComponentsNumber.setEnabled(False)
        #Button Inactive
        self.pushButton_SaveModel.setEnabled(False)
        self.pushButton_RunSimulation.setEnabled(False)
        self.pushButton_PcbLayerNumber.setEnabled(False)
        self.pushButton_ComponentsNumber.setEnabled(False)
        self.pushButton_CheckModel.setEnabled(False)
        self.pushButton_DeleteModel.setEnabled(False)
        #Table Inactive
        self.tableWidget_PcbCaseInfor.setEnabled(False)
        self.tableWidget_PcbLayers.setEnabled(False)
        self.tableWidget_Components.setEnabled(False)

    def InitActive(self):
        #lineEdit Active
        self.lineEdit_AmbientTemp.setEnabled(True)
        self.lineEdit_PcbLayerNumber.setEnabled(True)
        self.lineEdit_ComponentsNumber.setEnabled(True)
        #Button Active
        self.pushButton_SaveModel.setEnabled(True)
        self.pushButton_RunSimulation.setEnabled(True)
        self.pushButton_PcbLayerNumber.setEnabled(True)
        self.pushButton_ComponentsNumber.setEnabled(True)
        self.pushButton_CheckModel.setEnabled(True)
        self.pushButton_DeleteModel.setEnabled(True)
        #Table Active
        self.tableWidget_PcbCaseInfor.setEnabled(True)
        self.tableWidget_PcbLayers.setEnabled(True)
        self.tableWidget_Components.setEnabled(True)

    def PcbLayerApply(self): # 개수 받고, 테이블 이름 변경 
        if int(self.lineEdit_PcbLayerNumber.text()) <= self.limiteNumber:
            self.tableWidget_PcbLayers.setRowCount(int(self.lineEdit_PcbLayerNumber.text()))
            self._setTableVertical(self.lineEdit_PcbLayerNumber, self.tableWidget_PcbLayers, "Layer")
            self._setLayerInitValue()
        else:
            print("Error in Layer Number")


    def ComponentsApply(self): # 개수 받고, 테이블 이름 변경, 테이블 옵션(콤보박스) 설정 
        if int(self.lineEdit_ComponentsNumber.text()) <= self.limiteNumber:
            self.tableWidget_Components.setRowCount(int(self.lineEdit_ComponentsNumber.text()))
            self._setTableVertical(self.lineEdit_ComponentsNumber, self.tableWidget_Components, "IC")
            self.setComponentOption()
        else:
            print("Error in IC Number")
 


    def _setTableVertical(self, lineEdit, tableName, name): # Layer, Component Apply 버튼을 위한 내장 함수 
        if int(lineEdit.text()) > self.limiteNumber :
            print("Error : Too big number!")
            return None

        VerticalHeader=[]
        for i in range(int(lineEdit.text())):
            # self.tableWidget_PcbLayers.setItem(i,0, QTableWidgetItem("Hello"))
            VerticalHeader.append(name+ " " + str(i+1))
        if name == 'Layer':
            VerticalHeader[0]= VerticalHeader[0] + " [TOP]"
            VerticalHeader[-1]= VerticalHeader[-1] + " [BOT]"

        tableName.setVerticalHeaderLabels(VerticalHeader)

    def setCurrentBoard(self):
        # AllItems = [self.comboBox_Boards.itemText(i) for i in range(self.comboBox_Boards.count())]
        # print(AllItems)
        print(self.comboBox_Boards.currentText())
    
    def LoadModel(self):
        pass

    def DeleteModel(self):
        pass
    
    def CheckModel(self):
        pass


    def InitModel(self, ModelNumber, ModelName="SimplePCB"):
        self.Board = SimplePCB()
        
        # self.Board.Name = ModelName +"_"+ str(ModelNumber)
        # print(self.Board.Name)
        # self.Board._setResultPath()

        # Get Material Lists
        self.MaterialDict = self.Board.getMaterialList() 

        for key, value in self.Board.getMaterialList().items():
            print(key, ": ", value)
        
        self.UpperCaseMaterial.addItems(self.MaterialDict.keys())
        self.LowerCaseMaterial.addItems(self.MaterialDict.keys())



        
    def _getGeometry(self):
        self.Board.Name = self.lineEdit_ModelName.text()
        self.Board.setPcbInfo(Thickness=float(self.tableWidget_PcbCaseInfor.item(0, 2).text()), Width=float(self.tableWidget_PcbCaseInfor.item(0, 0).text()), Depth=float(self.tableWidget_PcbCaseInfor.item(0, 1).text()))
        self.Board.setCase(Upper_Height=float(self.tableWidget_PcbCaseInfor.item(1, 2).text()), Upper_Thickness=float(self.tableWidget_PcbCaseInfor.item(1, 3).text()), Upper_Material=str(self.tableWidget_PcbCaseInfor.cellWidget(1, 4).currentText()), Lower_Height=float(self.tableWidget_PcbCaseInfor.item(2, 2).text()), Lower_Thickness=float(self.tableWidget_PcbCaseInfor.item(2, 3).text()), Lower_Material=str(self.tableWidget_PcbCaseInfor.cellWidget(2, 4).currentText()))
        # print(str(self.tableWidget_PcbCaseInfor.cellWidget(1, 4).currentText()), str(self.tableWidget_PcbCaseInfor.cellWidget(2, 4).currentText()))
    
    def _getLayers(self):
        Layers_Thickness = []
        Layers_Percentage = []
        for i in range(int(self.lineEdit_PcbLayerNumber.text())):
            Layers_Thickness.append(float(self.tableWidget_PcbLayers.item(i, 0).text())) # Copper Thickness
            Layers_Percentage.append(float(self.tableWidget_PcbLayers.item(i,1).text())) # Copper Percentage

        self.Board.setLayersInfo(Layers=int(self.lineEdit_PcbLayerNumber.text()), Thickness=Layers_Thickness, Percentage=Layers_Percentage)
        # print(Layers_Thickness, Layers_Percentage)

    def _getComponents(self):
        for i in range(int(self.lineEdit_ComponentsNumber.text())):
            if str(self.tableWidget_Components.cellWidget(i, 8).currentText()) == 'Simplified':
                self.Board.addComponent(name=str(self.tableWidget_Components.item(i, 0).text()), X=float(self.tableWidget_Components.item(i, 2).text()), Z=float(self.tableWidget_Components.item(i, 3).text()), side=str(self.tableWidget_Components.cellWidget(i, 1).currentText()), width=float(self.tableWidget_Components.item(i, 4).text()), depth=float(self.tableWidget_Components.item(i, 5).text()), height=float(self.tableWidget_Components.item(i, 6).text()), material='Si(Silicon)', TIM=str(self.tableWidget_Components.cellWidget(i, 7).currentText()), powerType='Simplified', power=float(self.tableWidget_Components.item(i, 12).text()))

            elif str(self.tableWidget_Components.cellWidget(i, 8).currentText()) == '2R':
                self.Board.addComponent(name=str(self.tableWidget_Components.item(i, 0).text()), X=float(self.tableWidget_Components.item(i, 2).text()), Z=float(self.tableWidget_Components.item(i, 3).text()), side=str(self.tableWidget_Components.cellWidget(i, 1).currentText()), width=float(self.tableWidget_Components.item(i, 4).text()), depth=float(self.tableWidget_Components.item(i, 5).text()), height=float(self.tableWidget_Components.item(i, 6).text()), material='Si(Silicon)', TIM=str(self.tableWidget_Components.cellWidget(i, 7).currentText()), powerType='2R', power=float(self.tableWidget_Components.item(i, 12).text()), junction2Case = float(self.tableWidget_Components.item(i, 9).text()), junction2Board=float(self.tableWidget_Components.item(i, 10).text()))
            else:
                print("Exceptions in _getComponents")

    def _savePickle(self):
        FolderName = 'current'
        pass

    def _deletePickle(self):
        FolderName = 'deleted'
        pass
    
    def _saveXML(self):
        FolderName = 'temp'
        Board1._setPcbInfo()
        Board1._setLayersInfo()
        Board1._setPcbComponents()
        Board1._setCase()

        try:
            if not(os.path.isdir(FolderName)):
                os.makedirs(os.path.join(FolderName))
        except Exception as err:
            print("Failed to create temp directory", err)
        else:
            ResultFile= +'./'+ FolderName +'/'+ self.lineEdit_ModelName.text() +'.xml'
            Board1.saveXML(fileName=ResultFile)

    def NewModel(self):
        print(self.modelNumb)
        self.InitActive()
        self.InitModel(self.modelNumb)

    def SaveModel(self):
        print("Save Model")
        self._saveXML()

        #현재 상태를 현재 인스턴스에 반영 후, 새로운 인스턴스 생성 

    
    def RunSimulation(self):
        print("Run Simulation")
        
        #인스턴스 목록을 받아서 실행 
        #현재 상태를 현재 인스턴스에 반영 후, 실행 

    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TestForm()
    window.show()
    app.exec_()
    




