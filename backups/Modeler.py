#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 22:50:51 2020

@author: sogentle
"""

# %% import packages
import os.path
import xml.etree.ElementTree as ET

# %% Local import
from Components import Component_Simplified_XML, Component_2R_XML, Layer_XML

# %% Functions

class WrongInputs(Exception):
    def __init__(self):
        super().__init__("입력 값이 잘못되었습니다.")

# %% Modifying PCB contents
class SimplePCB():
    def __init__(self, filePath='Default_XML.xml', layerPath='Layer.xml', componentPath='Component.xml'):
        """
        

        Parameters
        ----------
        filePath : TYPE, optional
            DESCRIPTION. The default is 'Default_XML.xml'.
        layerPath : TYPE, optional
            DESCRIPTION. The default is 'Layer.xml'.
        componentPath : TYPE, optional
            DESCRIPTION. The default is 'Component.xml'.

        Returns
        -------
        None.

        """
        self._tree = ET.parse(filePath)
        DataDefinition = self._tree.getroot()
        
        self.layerPath=layerPath
        self.componentPath=componentPath
        
        self._ET_Project = DataDefinition.find('ET_Project')
        self._Chassis = self._ET_Project.find('ChassisLink/Chassis')
        self._name = "SimplePCB"
        self.getMaterialList()
        
        self.Components=[]
    
    @property
    def Name(self):
        return self._name
    
    @Name.setter 
    def Name(self, name):
        self._ET_Project.find('Identification/Name').text = name
        print(name + ": Name is changed")

    # def setChassis(self, size=[1000, 1000, 1000]):
    #     Height = self._Chassis.find('Geometry/Height')
    #     Width = self._Chassis.find('Geometry/Width')
    #     Depth = self._Chassis.find('Geometry/Depth')
    #     Height.text = size[0]
    #     Width.text = size[1]
    #     Depth.text = size[2]
    #     print("Height:"+str(Height.text)+'\n'+"Width:"+str(Width.text)+'\n'+"Depth:"+str(Depth.text))

    def getMaterialList(self):
        TagMaterial = self._ET_Project.findall('Materials/Material')
        self.MaterialDict={}
        for Material in TagMaterial:
            self.MaterialDict[Material.find("Name").text] = Material.attrib['id']
        return self.MaterialDict
    
    def _setResultPath(self, path=os.path.abspath(__file__)):
        self._ET_Project.find('SolutionControlLink/Solution_Control/Solution_Directory').text = path
        
    def setPcbInfo(self, Thickness=1.6, Width=100, Depth=90):
        self.PcbInfo = {'Width':Width, 'Depth':Depth, 'Thickness': Thickness}
        # self.PcbInfo['Thickness']
        # self.PcbInfo['Width']
        # self.PcbInfo['Depth']

    def _setPcbInfo(self):
        self._Chassis.find('PCBs/PCB/Geometry/Thickness').text = str(self.PcbInfo['Thickness']) + " mm"
        self._Chassis.find('PCBs/PCB/Geometry/Width').text = str(self.PcbInfo['Width']) + " mm"
        self._Chassis.find('PCBs/PCB/Geometry/Depth').text = str(self.PcbInfo['Depth']) + " mm"
        self._Chassis.find('PCBs/PCB/Placement/Y_Location').text = str(500+self.CaseInfo['Lower_Height']) + " mm"

    def _setPcbMaterials(self, Conductor="CU", Dielectric="FR4"):
        self._Chassis.find('PCBs/PCB/Construction/Conductor_Material').text = self.MaterialDict[Conductor]
        self._Chassis.find('PCBs/PCB/Construction/Dielectric_Material').text = self.MaterialDict[Dielectric]

    def setLayersInfo(self, Layers=10, Thickness=[], Percentage=[]):
        self.LayersInfo = {'Layers':Layers}

        # 입력오류에 관한 예외 처리 해야 함
        if Thickness == [] and Percentage == []:
            for numb in range(Layers):
                self.LayersInfo[numb]={'Thickness':0.035, 'Percentage':80}
        else:  
            for numb in range(Layers):
                self.LayersInfo[numb]={'Thickness':Thickness[numb], 'Percentage':Percentage[numb]}
        # if Layers != len(Thickness) or Layers != len(Percentage):
        #     raise WrongInputs
    
    def _setLayersInfo(self):
        self._TagConductor_Layers = self._Chassis.find('PCBs/PCB/Construction/Conductor_Layers')
        for i in range(self.LayersInfo['Layers']):
            layerTree = ET.parse(self.layerPath)
            _TagConductor_Layer = layerTree.getroot() # 외부에서 불러온 파일이고 내부에서만 사용 
            _TagConductor_Layer.attrib['id'] = "45995-"+str(47675+i)
            _TagConductor_Layer.find('Identification/Name').text = 'Conductor Layer '+ str(1+i)
            if i == 0:
                _TagConductor_Layer.find('Placement/Y_Location').text = str(self.PcbInfo['Thickness'] - self.LayersInfo[i]['Thickness']) + ' mm'
            else:
                _TagConductor_Layer.find('Placement/Y_Location').text = '0 mm'
            _TagConductor_Layer.find('Construction/Conductor_Thickness').text = str(self.LayersInfo[i]['Thickness']) + ' mm'
            _TagConductor_Layer.find('Construction/Conductor_Planar_Percentage').text = str(self.LayersInfo[i]['Percentage']) + ' %'
            self._TagConductor_Layers.insert(i, _TagConductor_Layer)

        
    def addComponent(self, name, X=0, Z=0, side='Top', width=5, depth=5, height=2, material='Si(Silicon)', TIM='No', powerType='Simplified', power=1, junction2Case = 1, junction2Board=10):
        if powerType == 'Simplified':
            self.Components.append({'Reference_Designator':name, 'X_Location': X, 'Z_Location':Z, 'Board_Side':side, 'Width':width, 'Depth':depth, 'Height':height, 'MaterialLink':material, 'TIM':TIM, 'Modelling_Level':'Simplified', 'Thermal_Design_Power': power })
        elif powerType == '2R':
            self.Components.append({'Reference_Designator':name, 'X_Location': X, 'Z_Location':Z, 'Board_Side':side, 'Width':width, 'Depth':depth, 'Height':height, 'MaterialLink':material, 'TIM':TIM, 'Modelling_Level':'2R', 'Thermal_Design_Power':power, 'Junction-to-Case_Thermal_Resistance': junction2Case, 'Junction-to-Board_Thermal_Resistance': junction2Case })
        else:
            print('Error: Undefined power type')
            
        return self.Components
    
    def deleteComponent(self): # 이름을 받아, 하나만 삭제할 수 있는 기능 
        self.Components = []
        print('init')
        
    def _setPcbComponents(self):
        self._TagComponents = self._Chassis.find('PCBs/PCB/Components')
        numb=0 
        sumPower=0
        for Component in self.Components:
            componentTree = ET.parse(self.componentPath)
            _TagComponent = componentTree.getroot() # 외부에서 불러온 파일이고 내부에서만 사용 
            print(Component['Reference_Designator'])
            _TagComponent.attrib['id'] = "45995-"+str(47686+numb) 
            _TagComponent.find('Identification/Reference_Designator').text = Component['Reference_Designator']
            _TagComponent.find('Geometry/Height').text = str(Component['Height']) + ' mm'
            _TagComponent.find('Geometry/Width').text = str(Component['Width']) + ' mm'
            _TagComponent.find('Geometry/Depth').text = str(Component['Depth']) + ' mm'
            _TagComponent.find('Placement/X_Location').text = str(Component['X_Location']) + ' mm'
            _TagComponent.find('Placement/Z_Location').text = str(Component['Z_Location']) + ' mm'
            _TagComponent.find('Placement/Board_Side').text = Component['Board_Side']
            _TagComponent.find('TIMs/TIM').attrib['id'] = "45995-" + str(47688+numb)
            _TagComponent.find('TIMs/TIM/Installed').text = Component['TIM']
            _TagComponent.find('TIMs/TIM/Identification/Reference_Designator').text = "TIM_" + Component['Reference_Designator']
            _TagComponent.find('TIMs/TIM/Placement/Side').text = Component['Board_Side']
            # TIM Thickness?
            if Component['Board_Side'] == 'Top':
                _TagComponent.find('TIMs/TIM/Construction/MaterialLink').text = self.MaterialDict[self.CaseInfo['Upper_Material']]
            elif Component['Board_Side'] == 'Bottom': #'BOT?' 'Bottom'?? 확인 후 변경, 예외처리 필요
                _TagComponent.find('TIMs/TIM/Construction/MaterialLink').text = self.MaterialDict[self.CaseInfo['Lower_Material']]
            
            _ComponentConstruction = _TagComponent.find('Construction')
            _TagComponent.find('Construction/Modelling_Level').text = Component['Modelling_Level']
            _TagComponent.find('Construction/MaterialLink').text = self.MaterialDict[Component['MaterialLink']]
            if Component['Modelling_Level'] == '2R':
                ET.SubElement(_ComponentConstruction, "Junction-to-Case_Thermal_Resistance")
                ET.SubElement(_ComponentConstruction, "Junction-to-Board_Thermal_Resistance")
                _TagComponent.find('Construction/Junction-to-Case_Thermal_Resistance').text = str(Component['Junction-to-Case_Thermal_Resistance']) + ' C/W'
                _TagComponent.find('Construction/Junction-to-Board_Thermal_Resistance').text = str(Component['Junction-to-Board_Thermal_Resistance']) + ' C/W'

            _TagComponent.find('Power/Thermal_Design_Power').text = str(Component['Thermal_Design_Power']) + " W"
            _TagComponent.find('Power/Calculated_Power').text = str(Component['Thermal_Design_Power']) + " W"

            self._TagComponents.insert(numb, _TagComponent)
            numb += 1
            sumPower += Component['Thermal_Design_Power']
        
        # #토탈 파워
        # self._Chassis.find('PCBs/PCB/Power/Total_Power').text = str(sumPower) + " W"
        
    # def setGrid_Controls
    def setCase(self, Upper_Height=15, Upper_Thickness=3, Upper_Material='ADC12', Lower_Height=10, Lower_Thickness=2, Lower_Material='SECC'):
        self.CaseInfo={'Upper_Height':Upper_Height, 'Upper_Thickness':Upper_Thickness, 'Upper_Material':Upper_Material, 'Lower_Height':Lower_Height, 'Lower_Thickness':Lower_Thickness, 'Lower_Material':Lower_Material}
    
    def _setCase(self):
        for i in self._Chassis.find('SolidObstructions').iter('Solid_Obstruction'):
            i.find('Geometry/Width').text = str(self.PcbInfo['Width']) + " mm"
            i.find('Geometry/Depth').text = str(self.PcbInfo['Depth']) + " mm"
            if i.find('Identification/Name').text == 'CASE_LOWER_COVER':
                i.find('Geometry/Width').text = str(self.PcbInfo['Width']) + " mm"
                i.find('Geometry/Depth').text = str(self.PcbInfo['Depth']) + " mm"
                i.find('Geometry/Height').text = str(self.CaseInfo['Lower_Thickness']) + " mm"
                i.find('Cooling/MaterialLink').text = self.MaterialDict[self.CaseInfo['Lower_Material']]
            elif i.find('Identification/Name').text == 'CASE_LOWER_SIDE':
                i.find('Geometry/Width').text = str(self.PcbInfo['Width']) + " mm"
                i.find('Geometry/Depth').text = str(self.PcbInfo['Depth']) + " mm"
                i.find('Geometry/Height').text = str(self.CaseInfo['Lower_Height']-self.CaseInfo['Lower_Thickness']) + " mm"
                i.find('Cooling/MaterialLink').text = self.MaterialDict[self.CaseInfo['Lower_Material']]
                i.find('Placement/Y_Location').text = str(500+self.CaseInfo['Lower_Thickness']) + " mm"
                i.find('Holes/Obstruction_Hole/Geometry/Width').text = str(self.PcbInfo['Width'] - 2 * self.CaseInfo['Lower_Thickness'])+ " mm"
                i.find('Holes/Obstruction_Hole/Geometry/Depth').text = str(self.PcbInfo['Depth'] - 2 * self.CaseInfo['Lower_Thickness']) + " mm"
                i.find('Holes/Obstruction_Hole/Placement/X_Location').text = str(self.CaseInfo['Lower_Thickness']) + " mm"
                i.find('Holes/Obstruction_Hole/Placement/Z_Location').text = str(self.CaseInfo['Lower_Thickness']) + " mm"
 
            elif i.find('Identification/Name').text == 'CASE_UPPER_SIDE':
                i.find('Geometry/Width').text = str(self.PcbInfo['Width']) + " mm"
                i.find('Geometry/Depth').text = str(self.PcbInfo['Depth']) + " mm"
                i.find('Geometry/Height').text = str(self.CaseInfo['Upper_Height']-self.CaseInfo['Upper_Thickness']) + " mm"
                i.find('Cooling/MaterialLink').text = self.MaterialDict[self.CaseInfo['Upper_Material']]
                i.find('Placement/Y_Location').text = str(500+self.CaseInfo['Lower_Height']+self.PcbInfo['Thickness']) + " mm"
                
                i.find('Holes/Obstruction_Hole/Geometry/Width').text = str(self.PcbInfo['Width'] - 2 * self.CaseInfo['Upper_Thickness'])+ " mm"
                i.find('Holes/Obstruction_Hole/Geometry/Depth').text = str(self.PcbInfo['Depth'] - 2 * self.CaseInfo['Upper_Thickness']) + " mm"
                i.find('Holes/Obstruction_Hole/Placement/X_Location').text = str(self.CaseInfo['Upper_Thickness']) + " mm"
                i.find('Holes/Obstruction_Hole/Placement/Z_Location').text = str(self.CaseInfo['Upper_Thickness']) + " mm"
            elif i.find('Identification/Name').text == 'CASE_UPPER_COVER':
                i.find('Geometry/Width').text = str(self.PcbInfo['Width']) + " mm"
                i.find('Geometry/Depth').text = str(self.PcbInfo['Depth']) + " mm"
                i.find('Geometry/Height').text = str(self.CaseInfo['Upper_Thickness']) + " mm"
                i.find('Placement/Y_Location').text = str(500+self.CaseInfo['Lower_Height']+self.PcbInfo['Thickness']+self.CaseInfo['Upper_Height']-self.CaseInfo['Upper_Thickness']) + " mm"
                i.find('Cooling/MaterialLink').text = self.MaterialDict[self.CaseInfo['Upper_Material']]
            else:
                print("Check, Needed.")
            
    def saveXML(self, fileName='ModifiedXML.xml'):
        self._tree.write(fileName, encoding='UTF-8', xml_declaration=True)

# %% RUN
       
# Making Instance
Board1 = SimplePCB()
Board1.Name = "Test"
print(Board1.Name)
Board1._setResultPath()

# Get Material Lists
for key, value in Board1.getMaterialList().items():
    print(key, ": ", value)

# Set Parameters    
Board1.setPcbInfo(Thickness=1.6, Width=100, Depth=90)

Layers_Thickness=[0.035, 0.07, 0.035, 0.035, 0.03, 0.07, 0.07, 0.03, 0.035, 0.035, 0.07, 0.035]
Layers_Percentage=[85, 75, 80, 90, 95, 95, 95, 95, 90, 80, 75, 85]

Board1.setLayersInfo(Layers=10)

Board1.addComponent(name="U_T_Sim", X=20, Z=50, side='Top', width=4, depth=5, height=3, material='Si(Silicon)', TIM='No', powerType='Simplified', power=1)
Board1.addComponent(name="U_T_Sim_TIM", X=40, Z=50, side='Top', width=4, depth=5, height=3, material='Si(Silicon)', TIM='Yes', powerType='Simplified', power=1)
Board1.addComponent(name="U_T_2R", X=60, Z=50, side='Top', width=4, depth=5, height=3, material='Si(Silicon)', TIM='No', powerType='2R', power=1, junction2Case = 1, junction2Board=10)
Board1.addComponent(name="U_T_2R_TIM", X=80, Z=50, side='Top', width=4, depth=5, height=3, material='Si(Silicon)', TIM='Yes', powerType='2R', power=1, junction2Case = 1, junction2Board=10)

Board1.setCase(Upper_Height=10, Upper_Thickness=5, Upper_Material='ADC12', Lower_Height=15, Lower_Thickness=3, Lower_Material='SECC')
    
Board1._setPcbInfo()
Board1._setLayersInfo()
Board1._setPcbComponents()
Board1._setCase()

Board1.saveXML()

# ChassisLink = ET_Project.find('ChassisLink')


# print(element)