#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 22:02:59 2020

@author: sogentle
"""


Component_Simplified_XML = """
<Component id="45995-47687">
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
<TIM id="45995-47688">
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

Component_2R_XML = """
<Component id="45995-47690">
<Installed>Yes</Installed>
<Filtered>No</Filtered>
<Display_in_CFD_Progress>Auto</Display_in_CFD_Progress>
<Contributes_to_Termination_Criteria>Yes</Contributes_to_Termination_Criteria>
<Identification>
<Model>Component</Model>
<Reference_Designator>U_T_2R_TIM</Reference_Designator>
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
<X_Location>80 mm</X_Location>
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
<Modelling_Level>2R</Modelling_Level>
<MaterialLink>45995-47723 </MaterialLink>
<Material_Alignment>XYZ</Material_Alignment>
<Material_Normal>X</Material_Normal>
<Junction-to-Case_Thermal_Resistance>1 C/W</Junction-to-Case_Thermal_Resistance>
<Junction-to-Board_Thermal_Resistance>10 C/W</Junction-to-Board_Thermal_Resistance>
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
<TIM id="45995-47691">
<Installed>Yes</Installed>
<Identification>
<Model>TIM</Model>
<Reference_Designator>TIM3</Reference_Designator>
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
<MaterialLink>45995-47709 </MaterialLink>
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
<Conductor_Layer id="45995-47675">
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