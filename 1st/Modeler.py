#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# %% import packages
import os.path
import subprocess
import time

import xml.etree.ElementTree as ET

# %% XML Variables
Component_Simplified_XML = """
<Component id="45995-32000">
<Installed>Yes</Installed>
<Filtered>No</Filtered>
<Display_in_CFD_Progress>Auto</Display_in_CFD_Progress>
<Contributes_to_Termination_Criteria>Yes</Contributes_to_Termination_Criteria>
<Identification>
<Model>Component</Model>
<Reference_Designator>U_T_Sim_TIM</Reference_Designator>
<Type>Electrical</Type>
</Identification>
<Geometry>
<Shape>Rectangle</Shape>
<Height>3 mm</Height>
<Width>4 mm</Width>
<Depth>5 mm</Depth>
<Diameter>30 mm</Diameter>
<Heatslug_Geometry>
<Height>2.000000000000001 mm</Height>
<Depth>40 mm</Depth>
<Depth_Offset>10 mm</Depth_Offset>
</Heatslug_Geometry>
<Grid>
<Minimum_Number_Of_Cells>
<Width_Direction>5</Width_Direction>
<Depth_Direction>5</Depth_Direction>
</Minimum_Number_Of_Cells>
</Grid>
<Surface_Area>94 mm^2</Surface_Area>
</Geometry>
<Placement>
<Origin_Point>Low Centre</Origin_Point>
<Board_Side>Top</Board_Side>
<X_Location>40 mm</X_Location>
<Y_Location>0 mm</Y_Location>
<Z_Location>50 mm</Z_Location>
<Angle_To_Board>0 degrees</Angle_To_Board>
<Orientation>
<Rotation_Mechanism>Ordered</Rotation_Mechanism>
<X_Axis>0</X_Axis>
<Y_Axis>1</Y_Axis>
<Z_Axis>0</Z_Axis>
<Angle>0 degrees</Angle>
<Rotation_Order>YZX</Rotation_Order>
<Angle_1>0 degrees</Angle_1>
<Angle_2>0 degrees</Angle_2>
<Angle_3>0 degrees</Angle_3>
</Orientation>
</Placement>
<Construction>
<Modelling_Level>Simplified</Modelling_Level>
<MaterialLink>45995-47723 </MaterialLink>
<Material_Alignment>XYZ</Material_Alignment>
<Material_Normal>X</Material_Normal>
<Density>1000 kg/m^3</Density>
<Specific_Heat>1000 J/(kg K)</Specific_Heat>
<Calculated_Weight>0.13974 g</Calculated_Weight>
</Construction>
<Power>
<Power_Specification>Total Power</Power_Specification>
<Temperature_Dependent_Power_Map>No</Temperature_Dependent_Power_Map>
<Power_Map>
<Power_Map_Rows>1</Power_Map_Rows>
<Power_Map_Columns>1</Power_Map_Columns>
</Power_Map>
<Multiple_Power_Maps>
<Initial_Map_Id>0</Initial_Map_Id>
<Current_Map_Id>0</Current_Map_Id>
<Multiple_Power_Maps_Data>0
</Multiple_Power_Maps_Data>
<Map_Transitions>0
</Map_Transitions>
</Multiple_Power_Maps>
<Temperature_Dependent_Power>No</Temperature_Dependent_Power>
<Thermal_Design_Power>1 W</Thermal_Design_Power>
<Name_Plate_Power>0 W</Name_Plate_Power>
<Efficiency>0 %</Efficiency>
<Thermal_Design_Power_Temperature_Curve>20,0, 50,0 &lt;C,W&gt;</Thermal_Design_Power_Temperature_Curve>
<Thermal_Design_Power_Temperature_Multiple_Curves>
<Initial_Curve_Id>0</Initial_Curve_Id>
<Current_Curve_Id>0</Current_Curve_Id>
<Thermal_Design_Power_Temperature_Curve_Array>10,0,1000, 150,0|30,0,1000, 150,0 &lt;C,C,W&gt;</Thermal_Design_Power_Temperature_Curve_Array>
<Curve_Names>0
</Curve_Names>
<Transitions>0
</Transitions>
</Thermal_Design_Power_Temperature_Multiple_Curves>
<Power_Curve_Hysteresis>0 C</Power_Curve_Hysteresis>
<Controlling_Temperature>Component</Controlling_Temperature>
<Temperature_Dependence_Sensors/>
<Sensor_Treatment>Weighted Average</Sensor_Treatment>
<Sensor_Weights> : </Sensor_Weights>
<Operating_Power_Option>Fixed</Operating_Power_Option>
<Power_Utilisation>
<Power_Utilisation_Curve>0,0, 100,100 &lt;%,%&gt;</Power_Utilisation_Curve>
<Utilisation_Time_Dependence>Constant</Utilisation_Time_Dependence>
<Utilisation>100 %</Utilisation>
<Utilisation_Curve>0,100, 100,100 &lt;s,%&gt;</Utilisation_Curve>
</Power_Utilisation>
<Controlled_Power>
<Use_Internal_Controller>Yes</Use_Internal_Controller>
<Internal_Controller/>
<External_Controller/>
<Controller_Response>Direct</Controller_Response>
<Controller_Response_Curve>0,0, 100,100 &lt;%,%&gt;</Controller_Response_Curve>
<Response_Hysteresis>0 %</Response_Hysteresis>
</Controlled_Power>
<ForcePowerCurve>No</ForcePowerCurve>
<Calculated_Power>1 W</Calculated_Power>
</Power>
<Display_Options>
<Colour>60,60,60</Colour>
<Secondary_Colour>180,180,180</Secondary_Colour>
<Basic_Render_Style>Solid,Wireframe,Solid Outlined,Textured,Transparent,Invisible</Basic_Render_Style>
<Render_Style>Solid Outlined</Render_Style>
<Transparency>70 %</Transparency>
<Variable>Temperature</Variable>
<Show_Computational_Shape>Yes</Show_Computational_Shape>
<Data_Type>Geometry</Data_Type>
<Plot_Type>Variation Plot Smooth</Plot_Type>
<Show_Grid>No</Show_Grid>
<Target_Variable>Temperature</Target_Variable>
<Hidden>No</Hidden>
</Display_Options>
<Library_Import_Record>
<Imported_From>Standard Objects/PCB Components/Component</Imported_From>
<Version>5</Version>
</Library_Import_Record>
<SubcomponentGroups/>
<ResistorNetworkLink/>
<TIMs>
<TIM id="45995-33000">
<Installed>Yes</Installed>
<Identification>
<Model>TIM</Model>
<Reference_Designator>TIM1</Reference_Designator>
<Type>Gel</Type>
</Identification>
<Geometry>
<Size_From_Parent>Yes</Size_From_Parent>
<Shape>Rectangle</Shape>
<Width>30 mm</Width>
<Depth>30 mm</Depth>
<Diameter>30 mm</Diameter>
</Geometry>
<Placement>
<Side>Top</Side>
<Offset_1>0 mm</Offset_1>
<Offset_2>0 mm</Offset_2>
</Placement>
<Construction>
<Thermal_Specification>Conductivity</Thermal_Specification>
<Solid-Solid_Resistance>0.02 C/W</Solid-Solid_Resistance>
<Solid-Fluid_Resistance>0.02 C/W</Solid-Fluid_Resistance>
<Solid-Solid_Insulance>50 mm^2C/W</Solid-Solid_Insulance>
<Solid-Fluid_Insulance>50 mm^2C/W</Solid-Fluid_Insulance>
<Thickness>5 mm</Thickness>
<Model_Thickness>Yes</Model_Thickness>
<MaterialLink>45995-47725 </MaterialLink>
<Material_Alignment>XYZ</Material_Alignment>
<Material_Normal>X</Material_Normal>
<Electrical_Resistance>0 Ohm</Electrical_Resistance>
<Surface_Emissivity>1</Surface_Emissivity>
</Construction>
<TIMs/>
<Display_Options>
<Colour>180,180,180</Colour>
<EnableUseMaterialColour>No</EnableUseMaterialColour>
<Use_This_Colour>Yes</Use_This_Colour>
<Secondary_Colour>180,180,180</Secondary_Colour>
<Basic_Render_Style>Solid,Wireframe,Solid Outlined,Textured,Transparent,Invisible</Basic_Render_Style>
<Render_Style>Solid Outlined</Render_Style>
<Transparency>70 %</Transparency>
<Variable>Temperature</Variable>
<Show_Computational_Shape>Yes</Show_Computational_Shape>
<Data_Type>Geometry</Data_Type>
<Plot_Type>Variation Plot Smooth</Plot_Type>
<Show_Grid>No</Show_Grid>
<Target_Variable>Temperature</Target_Variable>
<Hidden>No</Hidden>
</Display_Options>
<Library_Import_Record>
<Imported_From>Standard Objects/Heatsinks/TIM</Imported_From>
<Version>1</Version>
</Library_Import_Record>
<Simulation_Results>
<Heat_Fluxes>
<ShowPolygonSides>No</ShowPolygonSides>
<ShowCuboidSides>No</ShowCuboidSides>
</Heat_Fluxes>
<Joule_Heating>0 W</Joule_Heating>
<Solar_Heating>0 W</Solar_Heating>
</Simulation_Results>
<Object_Shape_Definition>
<Shape_Type>Cuboid</Shape_Type>
<Thin_Shape>No</Thin_Shape>
<With_Holes>No</With_Holes>
</Object_Shape_Definition>
<Push_Pins/>
</TIM>
</TIMs>
<HeatsinkLink/>
<ColdPlateLink/>
<TECLink/>
<StackedComponents/>
<Sensors/>
<Vias/>
<ViaGroups/>
<Terminals/>
<ShieldingCans/>
<HTC_Boundaries/>
<PackageBuilderLink/>
<Grid_Controls/>
<Simulation_Results>
<Junction_Temperature_Curve>0,20, 100,20 &lt;s,C&gt;</Junction_Temperature_Curve>
<Case_Temperature_Curve>0,20, 100,20 &lt;s,C&gt;</Case_Temperature_Curve>
<Board_Temperature_Curve>0,20, 100,20 &lt;s,C&gt;</Board_Temperature_Curve>
<Overheat>
<Overheat>No</Overheat>
</Overheat>
<Die_Temperature>
<Number_of_Die>0</Number_of_Die>
<Maximum_Junction_Temperature_Curve>0,20, 100,20 &lt;s,C&gt;</Maximum_Junction_Temperature_Curve>
<Minimum_Junction_Temperature_Curve>0,20, 100,20 &lt;s,C&gt;</Minimum_Junction_Temperature_Curve>
<Mean_Junction_Temperature_Curve>0,20, 100,20 &lt;s,C&gt;</Mean_Junction_Temperature_Curve>
</Die_Temperature>
<Controlled_Component>
<Operating_Power>0 W</Operating_Power>
</Controlled_Component>
<Heat_Fluxes>
<ShowPolygonSides>No</ShowPolygonSides>
<ShowCuboidSides>No</ShowCuboidSides>
</Heat_Fluxes>
<Solar_Heating>0 W</Solar_Heating>
<Temperature_Dependent_Heating>0 W</Temperature_Dependent_Heating>
<Controlling_Temperature>0 C</Controlling_Temperature>
<Joule_Heating>0 W</Joule_Heating>
</Simulation_Results>
<Object_Shape_Definition>
<Shape_Type>Cuboid</Shape_Type>
<Thin_Shape>No</Thin_Shape>
<With_Holes>No</With_Holes>
</Object_Shape_Definition>
<Push_Pins/>
</Component>
"""


Layer_XML = """
<Conductor_Layer id="45995-31000">
<Installed>Yes</Installed>
<Identification>
<Name>Conductor Layer 1</Name>
</Identification>
<Placement>
<Y_Location>0 mm</Y_Location>
</Placement>
<Construction>
<Conductor_Thickness>0.035 mm</Conductor_Thickness>
<Modelling_Level>Uniform Conductivity</Modelling_Level>
<Conductor_Content_from_Image>No</Conductor_Content_from_Image>
<Conductor_Planar_Percentage>80 %</Conductor_Planar_Percentage>
<Layer_Image>
<MaterialTolerance>5 %</MaterialTolerance>
<BackgroundTolerance>5 %</BackgroundTolerance>
<MaterialRed>0</MaterialRed>
<MaterialGreen>0</MaterialGreen>
<MaterialBlue>0</MaterialBlue>
<MaterialIsConductor>Yes</MaterialIsConductor>
<BackgroundRed>255</BackgroundRed>
<BackgroundGreen>255</BackgroundGreen>
<BackgroundBlue>255</BackgroundBlue>
<BackgroundIsIgnored>No</BackgroundIsIgnored>
<Clockwise_Rotation_Angle>No Rotation</Clockwise_Rotation_Angle>
<Flip_Image_About_Vertical>No</Flip_Image_About_Vertical>
<ImageWidth>0</ImageWidth>
<ImageHeight>0</ImageHeight>
</Layer_Image>
<Map_Image_To_Grid>No</Map_Image_To_Grid>
<Conductor_Percentage_From_Image>0 %</Conductor_Percentage_From_Image>
<Different_Conductor_Material>No</Different_Conductor_Material>
<MaterialLink/>
<Material_Alignment>XYZ</Material_Alignment>
<Material_Normal>X</Material_Normal>
<Different_Dielectric_Material>No</Different_Dielectric_Material>
<DielectricMaterialLink/>
</Construction>
<Display_Options>
<Colour>39,180,44</Colour>
<Secondary_Colour>180,180,180</Secondary_Colour>
<Basic_Render_Style>Solid,Wireframe,Solid Outlined,Textured,Transparent,Invisible</Basic_Render_Style>
<Render_Style>Wireframe</Render_Style>
<Transparency>70 %</Transparency>
<Variable>Temperature</Variable>
<Show_Computational_Shape>Yes</Show_Computational_Shape>
<Data_Type>Geometry</Data_Type>
<Plot_Type>Variation Plot Smooth</Plot_Type>
<Show_Grid>No</Show_Grid>
<Target_Variable>Temperature</Target_Variable>
<Hidden>No</Hidden>
</Display_Options>
<Traces/>
<Pads/>
<Conductors/>
<Nets/>
<Substrate_Conductors/>
<Substrate_Pads/>
<Substrate_Traces/>
<Substrate_Nets/>
<Simulation_Results>
<Heat_Fluxes>
<ShowPolygonSides>No</ShowPolygonSides>
<ShowCuboidSides>No</ShowCuboidSides>
</Heat_Fluxes>
<Solar_Heating>0 W</Solar_Heating>
</Simulation_Results>
<Object_Shape_Definition>
<Shape_Type>Cuboid</Shape_Type>
<Thin_Shape>No</Thin_Shape>
<With_Holes>No</With_Holes>
</Object_Shape_Definition>
<Push_Pins/>
</Conductor_Layer>
"""
# %% Functions


# %% Modifying PCB contents
class SimplePCB():
    def __init__(self, filePath='./Default_XML.xml'):
        """
        This class is for making simplifed PCB for 6sigma.

        Parameters
        ----------
        filePath : TYPE, optional
            DESCRIPTION. The default is 'Default_XML.xml'.

        Returns
        -------
        None.

        """
        self._tree = ET.parse(filePath)
        DataDefinition = self._tree.getroot()
        
        self._ET_Project = DataDefinition.find('ET_Project')
        self._Chassis = self._ET_Project.find('ChassisLink/Chassis')
        self._name = "SimplePCB"
        self.getMaterialList()
        
        self.Components=[]
    
    @property
    def Name(self):
        return self._ET_Project.find('Identification/Name').text
    
    @Name.setter 
    def Name(self, name):
        self._ET_Project.find('Identification/Name').text = name
        print(name + ": Name is changed")

    # def setChassis(self, height=1000, width=1000, depth=1000):
    #     self._Chassis.find('Geometry/Height') = str(height) + " mm"
    #     self._Chassis.find('Geometry/Width') =  str(width) + " mm"
    #     self._Chassis.find('Geometry/Depth') =  str(depth) + " mm"

    def getMaterialList(self):
        TagMaterial = self._ET_Project.findall('Materials/Material')
        self.MaterialDict={}
        for Material in TagMaterial:
            self.MaterialDict[Material.find("Name").text] = Material.attrib['id'] + ' '
        return self.MaterialDict
    
    def _setResultPath(self, path=os.path.abspath(__file__)):
        self._ET_Project.find('SolutionControlLink/Solution_Control/Solution_Directory').text = path
    
    def setAmbientTemp(self, temperature):
        self._ET_Project.find('Environments/Environment/Temperature/Temperature').text = str(temperature) + ' C'
    
    def setPcbInfo(self, Thickness=1.6, Width=100, Depth=90):
        self.PcbInfo = {'Width':Width, 'Depth':Depth, 'Thickness': Thickness}


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

    def _setLayersInfo(self):
        self._TagConductor_Layers = self._Chassis.find('PCBs/PCB/Construction/Conductor_Layers')
        for i in range(self.LayersInfo['Layers']):
            _TagConductor_Layer = ET.fromstring(Layer_XML)

            _TagConductor_Layer.attrib['id'] = "45995-"+str(31000+i)
            _TagConductor_Layer.find('Identification/Name').text = 'Conductor Layer '+ str(1+i)
            if i == 0:
                _TagConductor_Layer.find('Placement/Y_Location').text = str(self.PcbInfo['Thickness'] - self.LayersInfo[i]['Thickness']) + ' mm'
            else:
                _TagConductor_Layer.find('Placement/Y_Location').text = '0 mm'
            _TagConductor_Layer.find('Construction/Conductor_Thickness').text = str(self.LayersInfo[i]['Thickness']) + ' mm'
            _TagConductor_Layer.find('Construction/Conductor_Planar_Percentage').text = str(self.LayersInfo[i]['Percentage']) + ' %'
            self._TagConductor_Layers.insert(i, _TagConductor_Layer)

        
    def addComponent(self, name, X=0, Z=0, side='Top', width=5, depth=5, height=2, material='Si(Silicon)', TIM='No', powerType='Simplified', power=1, junction2Case = 1, junction2Board=10, maxAvailableTemp=100):
        if powerType == 'Simplified':
            self.Components.append({'Reference_Designator':name, 'X_Location': X, 'Z_Location':Z, 'Board_Side':side, 'Width':width, 'Depth':depth, 'Height':height, 'MaterialLink':material, 'TIM':TIM, 'Modelling_Level':'Simplified', 'Thermal_Design_Power': power, 'MaxAvailableTemp':maxAvailableTemp })
        elif powerType == '2R':
            self.Components.append({'Reference_Designator':name, 'X_Location': X, 'Z_Location':Z, 'Board_Side':side, 'Width':width, 'Depth':depth, 'Height':height, 'MaterialLink':material, 'TIM':TIM, 'Modelling_Level':'2R', 'Thermal_Design_Power':power, 'Junction-to-Case_Thermal_Resistance': junction2Case, 'Junction-to-Board_Thermal_Resistance': junction2Case, 'MaxAvailableTemp':maxAvailableTemp })
        else:
            print('Error: Undefined power type!')
            
        return self.Components
    
    # 모든 소자 삭제, 이름을 받아, 하나만 삭제할 수 있는 기능있어야 할듯
    def deleteComponent(self): 
        self.Components = []
        print('Every Components was deleted')

    def _setPcbComponents(self):
        self._TagComponents = self._Chassis.find('PCBs/PCB/Components')
        # numb=0
        # sumPower=0
        for numb, Component in enumerate(self.Components):
            _TagComponent = ET.fromstring(Component_Simplified_XML)
            print(Component['Reference_Designator'] + " was added!")
            
            _TagComponent.attrib['id'] = "45995-"+str(32000+numb)
            self.Components[numb]['id'] = _TagComponent.attrib['id']
            _TagComponent.find('Identification/Reference_Designator').text = Component['Reference_Designator']
            _TagComponent.find('Geometry/Height').text = str(Component['Height']) + ' mm'
            _TagComponent.find('Geometry/Width').text = str(Component['Width']) + ' mm'
            _TagComponent.find('Geometry/Depth').text = str(Component['Depth']) + ' mm'
            _TagComponent.find('Placement/X_Location').text = str(Component['X_Location']) + ' mm'
            _TagComponent.find('Placement/Z_Location').text = str(Component['Z_Location']) + ' mm'
            _TagComponent.find('Placement/Board_Side').text = Component['Board_Side']
            _TagComponent.find('TIMs/TIM').attrib['id'] = "45995-" + str(33000+numb)
            _TagComponent.find('TIMs/TIM/Installed').text = Component['TIM']
            _TagComponent.find('TIMs/TIM/Identification/Reference_Designator').text = "TIM_" + Component['Reference_Designator']
            # _TagComponent.find('TIMs/TIM/Placement/Side').text = 'Top'
            
            if Component['Board_Side'] == 'Top':
                _TagComponent.find('TIMs/TIM/Construction/MaterialLink').text = self.MaterialDict[self.CaseInfo['Upper_Material']]
                _TagComponent.find('TIMs/TIM/Construction/Thickness').text = str(self.CaseInfo['Upper_Height'] - self.CaseInfo['Upper_Thickness'] - Component['Height']) + " mm"
            elif Component['Board_Side'] == 'Bottom': 
                _TagComponent.find('TIMs/TIM/Construction/MaterialLink').text = self.MaterialDict[self.CaseInfo['Lower_Material']]
                _TagComponent.find('TIMs/TIM/Construction/Thickness').text = str(self.CaseInfo['Lower_Height'] - self.CaseInfo['Lower_Thickness'] - Component['Height']) + " mm"
            else:
                print("Error in Component Information")

            _ComponentConstruction = _TagComponent.find('Construction')
            if Component['Modelling_Level'] == '2R':
                ET.SubElement(_ComponentConstruction, "Junction-to-Case_Thermal_Resistance")
                ET.SubElement(_ComponentConstruction, "Junction-to-Board_Thermal_Resistance")
                _TagComponent.find('Construction/Junction-to-Case_Thermal_Resistance').text = str(Component['Junction-to-Case_Thermal_Resistance']) + ' C/W'
                _TagComponent.find('Construction/Junction-to-Board_Thermal_Resistance').text = str(Component['Junction-to-Board_Thermal_Resistance']) + ' C/W'

            _TagComponent.find('Construction/Modelling_Level').text = Component['Modelling_Level']
            _TagComponent.find('Construction/MaterialLink').text = self.MaterialDict[Component['MaterialLink']]

            _TagComponent.find('Power/Thermal_Design_Power').text = str(Component['Thermal_Design_Power']) + " W"
            _TagComponent.find('Power/Calculated_Power').text = str(Component['Thermal_Design_Power']) + " W"

            self._TagComponents.insert(numb, _TagComponent)
            # numb += 1
            # sumPower += Component['Thermal_Design_Power']
        
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
            
    def saveXML(self, fileName='Result.xml'):
        self.ResultFile = fileName
        self._tree.write(fileName, encoding='UTF-8', xml_declaration=True)

    def runSim(self, fileFullPath):
        # print("Run Simulation : ", self.ResultFile)
        ETSolver='"C:\\Program Files\\6SigmaETRelease14\\6SigmaEmbeddedSolver.exe"'
        BatchCommand = ETSolver + " -xmlmodel " + fileFullPath + " -licenseserver 10.230.22.106 4242 -numproc 8 -numgenthreads 8 -restart -nozip -decodeSimulationResults"
        print(BatchCommand)
        # os.system(BatchCommand)
        while True:
            try:
                returend_output = subprocess.check_output(BatchCommand)
                print("DONE")
                break
            except:
                time.sleep(10)

# %% RUN
if __name__ == "__main__":
    # Making Instance
    Board1 = SimplePCB()
    Board1.Name = "Simplified_PCB"
    print(Board1.Name)
    Board1._setResultPath()
    
    # Get Material Lists
    for key, value in Board1.getMaterialList().items():
        print(key, ": ", value)
    
    # Set Parameters    
    Board1.setPcbInfo(Thickness=1.6, Width=100, Depth=90)
    
    Layers_Thickness=[0.035, 0.07, 0.035, 0.035]
    Layers_Percentage=[85, 75, 80, 90]
    
    Board1.setLayersInfo(Layers=4, Thickness=Layers_Thickness, Percentage=Layers_Percentage)
    
    Board1.addComponent(name="U_T_Sim", X=20, Z=50, side='Top', width=4, depth=5, height=3, material='Si(Silicon)', TIM='No', powerType='Simplified', power=1)
    Board1.addComponent(name="U_T_Sim_TIM", X=40, Z=50, side='Top', width=4, depth=5, height=3, material='Si(Silicon)', TIM='Yes', powerType='Simplified', power=1)
    Board1.addComponent(name="U_T_2R", X=60, Z=50, side='Top', width=4, depth=5, height=3, material='Si(Silicon)', TIM='No', powerType='2R', power=1, junction2Case = 1, junction2Board=10)
    Board1.addComponent(name="U_T_2R_TIM", X=80, Z=50, side='Top', width=4, depth=5, height=3, material='Si(Silicon)', TIM='Yes', powerType='2R', power=1, junction2Case = 1, junction2Board=10)
    
    Board1.setCase(Upper_Height=10, Upper_Thickness=5, Upper_Material='ADC12', Lower_Height=15, Lower_Thickness=3, Lower_Material='SECC')
        
    Board1._setPcbInfo()
    Board1._setLayersInfo()
    Board1._setPcbComponents()
    Board1._setCase()
    ResultFile='Result.xml'
    Board1.saveXML(fileName=ResultFile)
    CurrentFolder=os.getcwd()
    ResultFileFullPath=os.path.join(CurrentFolder, ResultFile)
    print(ResultFileFullPath)
    ETSolver='"C:\\Program Files\\6SigmaETRelease14\\6SigmaEmbeddedSolver.exe"'
    BatchCommand = ETSolver + " -xmlmodel " + ResultFile + " -licenseserver 10.230.22.106 4242 -decodeSimulationResults"
    
    Board1.runSim(fileFullPath=ResultFileFullPath)
