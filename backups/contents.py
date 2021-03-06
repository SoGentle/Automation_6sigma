#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 21:10:46 2020

@author: sogentle
"""

layerXML = """
<Conductor_Layer id="45995-47675">
<Installed>Yes</Installed>
<Identification>
<Name>Conductor Layer 1</Name>
</Identification>
<Placement>
<Y_Location>1.565000000000001 mm</Y_Location>
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
compoentXML ="""
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

Base = """
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<DataDefinition label="ET Constructor" version="14.34">
<ET_Project id="45995-47666">
<Identification>
<Name>ModelV3</Name>
<Enforce_Unique_Reference_Designators>Yes</Enforce_Unique_Reference_Designators>
</Identification>
<Location>
<Latitude>0 degrees</Latitude>
<Longitude>0 degrees</Longitude>
<Altitude>0 m</Altitude>
<Model_North>0 degrees</Model_North>
<Show_Compass_North>No</Show_Compass_North>
</Location>
<Layer_Type>Chassis,PCB,Drive,Power Supply,Fan</Layer_Type>
<Custom_Installation_Status>Installed,Planned,Planned Decommission</Custom_Installation_Status>
<SolutionEnclosureLink/>
<TestChamberLink/>
<ChassisLink>
<Chassis id="45995-47667">
<Installed>Yes</Installed>
<Identification>
<Type>Server</Type>
<Model>Chassis</Model>
<Reference_Designator>CH1</Reference_Designator>
</Identification>
<Geometry>
<Height>1000 mm</Height>
<Width>1000 mm</Width>
<Depth>1000 mm</Depth>
</Geometry>
<Placement>
<Origin_Point>Low Corner</Origin_Point>
<Left_Offset>0 mm</Left_Offset>
<Front_Offset>0 mm</Front_Offset>
<X_Location>0 mm</X_Location>
<Y_Location>0 mm</Y_Location>
<Z_Location>0 mm</Z_Location>
<Orientation>
<Rotation_Mechanism>Angle and Axis</Rotation_Mechanism>
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
<Mounting_Location>
<Mount>Front</Mount>
<Depth_Offset>0 mm</Depth_Offset>
<Vertical_Mounting_Position>Bottom</Vertical_Mounting_Position>
<Vertical_Offset>0 mm</Vertical_Offset>
<Sideways_Mounting_Position>Centre</Sideways_Mounting_Position>
<Sideways_Offset>0 mm</Sideways_Offset>
<Mount_Orientation>No Rotation</Mount_Orientation>
</Mounting_Location>
<Resilience_Criteria>
<Thermal_Safety_Margin>5 C</Thermal_Safety_Margin>
</Resilience_Criteria>
<Construction>
<Total_Weight>63171.4022294118 g</Total_Weight>
</Construction>
<Display_Options>
<Colour>180,180,180</Colour>
<EnableUseMaterialColour>No</EnableUseMaterialColour>
<Use_This_Colour>Yes</Use_This_Colour>
<Secondary_Colour>180,180,180</Secondary_Colour>
<Basic_Render_Style>Solid,Wireframe,Solid Outlined,Textured,Transparent,Invisible</Basic_Render_Style>
<Render_Style>Invisible</Render_Style>
<Transparency>70 %</Transparency>
<Variable>Temperature</Variable>
<Show_Computational_Shape>No</Show_Computational_Shape>
<Data_Type>Regions</Data_Type>
<Plot_Type>Variation Plot Smooth</Plot_Type>
<Show_Grid>No</Show_Grid>
<Target_Variable>Temperature</Target_Variable>
<Hidden>No</Hidden>
</Display_Options>
<Viewing_Angle>
<Align_With_Gravity>Yes</Align_With_Gravity>
<Viewing_Angle_2D>0 degrees</Viewing_Angle_2D>
<Viewing_Axis_2D>Y</Viewing_Axis_2D>
</Viewing_Angle>
<Library_Import_Record>
<Version>0</Version>
</Library_Import_Record>
<Front>
<Chassis_Side id="45995-47668">
<Installed>Yes</Installed>
<Construction>
<Thickness>2 mm</Thickness>
<Modelling_Level>Thin</Modelling_Level>
<MaterialLink>45995-47724 </MaterialLink>
<Material_Alignment>XYZ</Material_Alignment>
<Material_Normal>X</Material_Normal>
<EnvironmentLink>45995-47732 </EnvironmentLink>
<Calculated_Weight>15720 g</Calculated_Weight>
</Construction>
<Cooling>
<Subdivide_Surfaces_For_Radiation>No</Subdivide_Surfaces_For_Radiation>
<Surface_Subdivision_Size>10 mm</Surface_Subdivision_Size>
</Cooling>
<Display_Options>
<Colour>232,229,194</Colour>
<EnableUseMaterialColour>No</EnableUseMaterialColour>
<Use_This_Colour>Yes</Use_This_Colour>
<Secondary_Colour>180,180,180</Secondary_Colour>
<Basic_Render_Style>Solid,Wireframe,Solid Outlined,Textured,Transparent,Invisible</Basic_Render_Style>
<Render_Style>Wireframe</Render_Style>
<Transparency>70 %</Transparency>
<Variable>Temperature</Variable>
<Show_Computational_Shape>No</Show_Computational_Shape>
<Data_Type>Regions</Data_Type>
<Plot_Type>Variation Plot Smooth</Plot_Type>
<Show_Grid>No</Show_Grid>
<Target_Variable>Temperature</Target_Variable>
<Hidden>No</Hidden>
</Display_Options>
<Fans/>
<Vents/>
<Vent_Openings/>
<Cable_Sockets/>
<Heatsinks/>
<PumpedSupplies/>
<PumpedReturns/>
<StreamPlot/>
<Simulation_Results>
<Heat_Fluxes>
<ShowPolygonSides>No</ShowPolygonSides>
<ShowCuboidSides>No</ShowCuboidSides>
</Heat_Fluxes>
<Heat_Flow>
<Heat_Flow_In>0 W</Heat_Flow_In>
<Heat_Flow_Out>0 W</Heat_Flow_Out>
</Heat_Flow>
<Solar_Heating>0 W</Solar_Heating>
</Simulation_Results>
<Object_Shape_Definition>
<Thin_Shape>No</Thin_Shape>
<With_Holes>Yes</With_Holes>
</Object_Shape_Definition>
<Push_Pins/>
</Chassis_Side>
</Front>
<Rear>
<Chassis_Side id="45995-47669">
<Installed>Yes</Installed>
<Construction>
<Thickness>2 mm</Thickness>
<Modelling_Level>Thin</Modelling_Level>
<MaterialLink>45995-47724 </MaterialLink>
<Material_Alignment>XYZ</Material_Alignment>
<Material_Normal>X</Material_Normal>
<EnvironmentLink>45995-47732 </EnvironmentLink>
<Calculated_Weight>15720 g</Calculated_Weight>
</Construction>
<Cooling>
<Subdivide_Surfaces_For_Radiation>No</Subdivide_Surfaces_For_Radiation>
<Surface_Subdivision_Size>10 mm</Surface_Subdivision_Size>
</Cooling>
<Display_Options>
<Colour>232,229,194</Colour>
<EnableUseMaterialColour>No</EnableUseMaterialColour>
<Use_This_Colour>Yes</Use_This_Colour>
<Secondary_Colour>180,180,180</Secondary_Colour>
<Basic_Render_Style>Solid,Wireframe,Solid Outlined,Textured,Transparent,Invisible</Basic_Render_Style>
<Render_Style>Wireframe</Render_Style>
<Transparency>70 %</Transparency>
<Variable>Temperature</Variable>
<Show_Computational_Shape>No</Show_Computational_Shape>
<Data_Type>Regions</Data_Type>
<Plot_Type>Variation Plot Smooth</Plot_Type>
<Show_Grid>No</Show_Grid>
<Target_Variable>Temperature</Target_Variable>
<Hidden>No</Hidden>
</Display_Options>
<Fans/>
<Vents/>
<Vent_Openings/>
<Cable_Sockets/>
<Heatsinks/>
<PumpedSupplies/>
<PumpedReturns/>
<StreamPlot/>
<Simulation_Results>
<Heat_Fluxes>
<ShowPolygonSides>No</ShowPolygonSides>
<ShowCuboidSides>No</ShowCuboidSides>
</Heat_Fluxes>
<Heat_Flow>
<Heat_Flow_In>0 W</Heat_Flow_In>
<Heat_Flow_Out>0 W</Heat_Flow_Out>
</Heat_Flow>
<Solar_Heating>0 W</Solar_Heating>
</Simulation_Results>
<Object_Shape_Definition>
<Thin_Shape>No</Thin_Shape>
<With_Holes>Yes</With_Holes>
</Object_Shape_Definition>
<Push_Pins/>
</Chassis_Side>
</Rear>
<Left_Side>
<Chassis_Side id="45995-47670">
<Installed>Yes</Installed>
<Construction>
<Thickness>2 mm</Thickness>
<Modelling_Level>Thin</Modelling_Level>
<MaterialLink>45995-47724 </MaterialLink>
<Material_Alignment>XYZ</Material_Alignment>
<Material_Normal>X</Material_Normal>
<EnvironmentLink>45995-47732 </EnvironmentLink>
<Calculated_Weight>15720 g</Calculated_Weight>
</Construction>
<Cooling>
<Subdivide_Surfaces_For_Radiation>No</Subdivide_Surfaces_For_Radiation>
<Surface_Subdivision_Size>10 mm</Surface_Subdivision_Size>
</Cooling>
<Display_Options>
<Colour>232,229,194</Colour>
<EnableUseMaterialColour>No</EnableUseMaterialColour>
<Use_This_Colour>Yes</Use_This_Colour>
<Secondary_Colour>180,180,180</Secondary_Colour>
<Basic_Render_Style>Solid,Wireframe,Solid Outlined,Textured,Transparent,Invisible</Basic_Render_Style>
<Render_Style>Wireframe</Render_Style>
<Transparency>70 %</Transparency>
<Variable>Temperature</Variable>
<Show_Computational_Shape>No</Show_Computational_Shape>
<Data_Type>Regions</Data_Type>
<Plot_Type>Variation Plot Smooth</Plot_Type>
<Show_Grid>No</Show_Grid>
<Target_Variable>Temperature</Target_Variable>
<Hidden>No</Hidden>
</Display_Options>
<Fans/>
<Vents/>
<Vent_Openings/>
<Cable_Sockets/>
<Heatsinks/>
<PumpedSupplies/>
<PumpedReturns/>
<StreamPlot/>
<Simulation_Results>
<Heat_Fluxes>
<ShowPolygonSides>No</ShowPolygonSides>
<ShowCuboidSides>No</ShowCuboidSides>
</Heat_Fluxes>
<Heat_Flow>
<Heat_Flow_In>0 W</Heat_Flow_In>
<Heat_Flow_Out>0 W</Heat_Flow_Out>
</Heat_Flow>
<Solar_Heating>0 W</Solar_Heating>
</Simulation_Results>
<Object_Shape_Definition>
<Thin_Shape>No</Thin_Shape>
<With_Holes>Yes</With_Holes>
</Object_Shape_Definition>
<Push_Pins/>
</Chassis_Side>
</Left_Side>
<Right_Side>
<Chassis_Side id="45995-47671">
<Installed>Yes</Installed>
<Construction>
<Thickness>2 mm</Thickness>
<Modelling_Level>Thin</Modelling_Level>
<MaterialLink>45995-47724 </MaterialLink>
<Material_Alignment>XYZ</Material_Alignment>
<Material_Normal>X</Material_Normal>
<EnvironmentLink>45995-47732 </EnvironmentLink>
<Calculated_Weight>15720 g</Calculated_Weight>
</Construction>
<Cooling>
<Subdivide_Surfaces_For_Radiation>No</Subdivide_Surfaces_For_Radiation>
<Surface_Subdivision_Size>10 mm</Surface_Subdivision_Size>
</Cooling>
<Display_Options>
<Colour>232,229,194</Colour>
<EnableUseMaterialColour>No</EnableUseMaterialColour>
<Use_This_Colour>Yes</Use_This_Colour>
<Secondary_Colour>180,180,180</Secondary_Colour>
<Basic_Render_Style>Solid,Wireframe,Solid Outlined,Textured,Transparent,Invisible</Basic_Render_Style>
<Render_Style>Wireframe</Render_Style>
<Transparency>70 %</Transparency>
<Variable>Temperature</Variable>
<Show_Computational_Shape>No</Show_Computational_Shape>
<Data_Type>Regions</Data_Type>
<Plot_Type>Variation Plot Smooth</Plot_Type>
<Show_Grid>No</Show_Grid>
<Target_Variable>Temperature</Target_Variable>
<Hidden>No</Hidden>
</Display_Options>
<Fans/>
<Vents/>
<Vent_Openings/>
<Cable_Sockets/>
<Heatsinks/>
<PumpedSupplies/>
<PumpedReturns/>
<StreamPlot/>
<Simulation_Results>
<Heat_Fluxes>
<ShowPolygonSides>No</ShowPolygonSides>
<ShowCuboidSides>No</ShowCuboidSides>
</Heat_Fluxes>
<Heat_Flow>
<Heat_Flow_In>0 W</Heat_Flow_In>
<Heat_Flow_Out>0 W</Heat_Flow_Out>
</Heat_Flow>
<Solar_Heating>0 W</Solar_Heating>
</Simulation_Results>
<Object_Shape_Definition>
<Thin_Shape>No</Thin_Shape>
<With_Holes>Yes</With_Holes>
</Object_Shape_Definition>
<Push_Pins/>
</Chassis_Side>
</Right_Side>
<Top>
<Chassis_Side id="45995-47672">
<Installed>No</Installed>
<Construction>
<Thickness>2 mm</Thickness>
<Modelling_Level>Thin</Modelling_Level>
<MaterialLink>45995-47724 </MaterialLink>
<Material_Alignment>XYZ</Material_Alignment>
<Material_Normal>X</Material_Normal>
<EnvironmentLink>45995-47732 </EnvironmentLink>
<Calculated_Weight>0 g</Calculated_Weight>
</Construction>
<Cooling>
<Subdivide_Surfaces_For_Radiation>No</Subdivide_Surfaces_For_Radiation>
<Surface_Subdivision_Size>10 mm</Surface_Subdivision_Size>
</Cooling>
<Display_Options>
<Colour>232,229,194</Colour>
<EnableUseMaterialColour>No</EnableUseMaterialColour>
<Use_This_Colour>Yes</Use_This_Colour>
<Secondary_Colour>180,180,180</Secondary_Colour>
<Basic_Render_Style>Solid,Wireframe,Solid Outlined,Textured,Transparent,Invisible</Basic_Render_Style>
<Render_Style>Wireframe</Render_Style>
<Transparency>70 %</Transparency>
<Variable>Temperature</Variable>
<Show_Computational_Shape>No</Show_Computational_Shape>
<Data_Type>Regions</Data_Type>
<Plot_Type>Variation Plot Smooth</Plot_Type>
<Show_Grid>No</Show_Grid>
<Target_Variable>Temperature</Target_Variable>
<Hidden>No</Hidden>
</Display_Options>
<Fans/>
<Vents/>
<Vent_Openings/>
<Cable_Sockets/>
<Heatsinks/>
<PumpedSupplies/>
<PumpedReturns/>
<StreamPlot/>
<Simulation_Results>
<Heat_Fluxes>
<ShowPolygonSides>No</ShowPolygonSides>
<ShowCuboidSides>No</ShowCuboidSides>
</Heat_Fluxes>
<Heat_Flow>
<Heat_Flow_In>0 W</Heat_Flow_In>
<Heat_Flow_Out>0 W</Heat_Flow_Out>
</Heat_Flow>
<Solar_Heating>0 W</Solar_Heating>
</Simulation_Results>
<Object_Shape_Definition>
<Shape_Type>Cuboid</Shape_Type>
<Thin_Shape>No</Thin_Shape>
<With_Holes>Yes</With_Holes>
</Object_Shape_Definition>
<Push_Pins/>
</Chassis_Side>
</Top>
<Bottom>
<Chassis_Side id="45995-47673">
<Installed>No</Installed>
<Construction>
<Thickness>2 mm</Thickness>
<Modelling_Level>Thin</Modelling_Level>
<MaterialLink>45995-47724 </MaterialLink>
<Material_Alignment>XYZ</Material_Alignment>
<Material_Normal>X</Material_Normal>
<EnvironmentLink>45995-47732 </EnvironmentLink>
<Calculated_Weight>0 g</Calculated_Weight>
</Construction>
<Cooling>
<Subdivide_Surfaces_For_Radiation>No</Subdivide_Surfaces_For_Radiation>
<Surface_Subdivision_Size>10 mm</Surface_Subdivision_Size>
</Cooling>
<Display_Options>
<Colour>232,229,194</Colour>
<EnableUseMaterialColour>No</EnableUseMaterialColour>
<Use_This_Colour>Yes</Use_This_Colour>
<Secondary_Colour>180,180,180</Secondary_Colour>
<Basic_Render_Style>Solid,Wireframe,Solid Outlined,Textured,Transparent,Invisible</Basic_Render_Style>
<Render_Style>Wireframe</Render_Style>
<Transparency>70 %</Transparency>
<Variable>Temperature</Variable>
<Show_Computational_Shape>No</Show_Computational_Shape>
<Data_Type>Regions</Data_Type>
<Plot_Type>Variation Plot Smooth</Plot_Type>
<Show_Grid>No</Show_Grid>
<Target_Variable>Temperature</Target_Variable>
<Hidden>No</Hidden>
</Display_Options>
<Fans/>
<Vents/>
<Vent_Openings/>
<Cable_Sockets/>
<Heatsinks/>
<PumpedSupplies/>
<PumpedReturns/>
<StreamPlot/>
<Simulation_Results>
<Heat_Fluxes>
<ShowPolygonSides>No</ShowPolygonSides>
<ShowCuboidSides>No</ShowCuboidSides>
</Heat_Fluxes>
<Heat_Flow>
<Heat_Flow_In>0 W</Heat_Flow_In>
<Heat_Flow_Out>0 W</Heat_Flow_Out>
</Heat_Flow>
<Solar_Heating>0 W</Solar_Heating>
</Simulation_Results>
<Object_Shape_Definition>
<Shape_Type>Cuboid</Shape_Type>
<Thin_Shape>No</Thin_Shape>
<With_Holes>Yes</With_Holes>
</Object_Shape_Definition>
<Push_Pins/>
</Chassis_Side>
</Bottom>
<Subchassis/>
<Subassemblies/>
<PCBs>
<PCB id="45995-47674">
<Installed>Yes</Installed>
<Identification>
<Model>PCB</Model>
<Reference_Designator>MainPCB</Reference_Designator>
</Identification>
<Geometry>
<Shape>Rectangle</Shape>
<Thickness>1.600000000000001 mm</Thickness>
<Width>100 mm</Width>
<Depth>90 mm</Depth>
<Diameter>264.000000000001 mm</Diameter>
<Surface_Area>18608 mm^2</Surface_Area>
</Geometry>
<Placement>
<Origin_Point>Low Centre</Origin_Point>
<Board_Side>Top</Board_Side>
<X_Location>500 mm</X_Location>
<Y_Location>510 mm</Y_Location>
<Height_From_Stand_Offs>No</Height_From_Stand_Offs>
<Stand_Off_Height>20 mm</Stand_Off_Height>
<Z_Location>500 mm</Z_Location>
<Centre_Offset>0 mm</Centre_Offset>
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
<Offset_1>0 mm</Offset_1>
<Offset_2>0 mm</Offset_2>
</Placement>
<Construction>
<Show_Connector>No</Show_Connector>
<Conductor_Material>45995-47715 </Conductor_Material>
<Dielectric_Material>45995-47718 </Dielectric_Material>
<Modelling_Level>3 Layer Average</Modelling_Level>
<Specified_Material/>
<Distribute_Layers>By Centre</Distribute_Layers>
<Conductor_Thickness>0.035 mm</Conductor_Thickness>
<Conductor_Planar_Percentage>80 %</Conductor_Planar_Percentage>
<Number_Of_Conductor_Layers>2</Number_Of_Conductor_Layers>
<Conductor_Layers/>
<Top_Surface_Emissivity>0.9</Top_Surface_Emissivity>
<Bottom_Surface_Emissivity>0.9</Bottom_Surface_Emissivity>
</Construction>
<Construction_Summary>
<Normal_Conductivity>0.367120124093961 W/(m K)</Normal_Conductivity>
<Planar_Conductivity>56.7684967320261 W/(m K)</Planar_Conductivity>
<Average_Density>2375.85620915033 kg/m^3</Average_Density>
<Average_Specific_Heat>796.476030656991 J/(kg K)</Average_Specific_Heat>
<Total_Conductor_Thickness>0.35 mm</Total_Conductor_Thickness>
<Calculated_Weight>34.2123294117647 g</Calculated_Weight>
<Total_Weight>34.7712894117647 g</Total_Weight>
</Construction_Summary>
<Cooling>
<Subdivide_Surfaces_For_Radiation>Yes</Subdivide_Surfaces_For_Radiation>
<Surface_Subdivision_Size>10 mm</Surface_Subdivision_Size>
</Cooling>
<Power>
<Top_Distributed_Power>0 W</Top_Distributed_Power>
<Bottom_Distributed_Power>0 W</Bottom_Distributed_Power>
<AllowPowerCurve>No</AllowPowerCurve>
<Total_Power>4 W</Total_Power>
</Power>
<Display_Options>
<Colour>39,180,44</Colour>
<Secondary_Colour>180,180,180</Secondary_Colour>
<Basic_Render_Style>Solid,Wireframe,Solid Outlined,Textured,Transparent,Invisible</Basic_Render_Style>
<Render_Style>Transparent</Render_Style>
<Transparency>70 %</Transparency>
<Variable>Temperature</Variable>
<Show_Computational_Shape>Yes</Show_Computational_Shape>
<Data_Type>Geometry</Data_Type>
<Plot_Type>Variation Plot Smooth</Plot_Type>
<Show_Grid>Yes</Show_Grid>
<Target_Variable>Regions</Target_Variable>
<Hidden>No</Hidden>
</Display_Options>
<Library_Import_Record>
<Imported_From>Standard Objects/PCB/PCB</Imported_From>
<Version>9</Version>
</Library_Import_Record>
<Connector>
<Board_Connector id="45995-47685">
<Identification>
<Type>Other</Type>
</Identification>
<Construction>
<Number_of_Connections>128</Number_of_Connections>
</Construction>
<Placement>
<Board_Edge>Back</Board_Edge>
<Reverse_Orientation>No</Reverse_Orientation>
<Centre_Offset>0 mm</Centre_Offset>
</Placement>
<Geometry>
<Length>100 mm</Length>
<Depth>10 mm</Depth>
</Geometry>
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
<Simulation_Results>
<Heat_Fluxes>
<ShowPolygonSides>No</ShowPolygonSides>
<ShowCuboidSides>No</ShowCuboidSides>
</Heat_Fluxes>
<Solar_Heating>0 W</Solar_Heating>
</Simulation_Results>
<Object_Shape_Definition>
<Thin_Shape>No</Thin_Shape>
<With_Holes>No</With_Holes>
</Object_Shape_Definition>
<Push_Pins/>
</Board_Connector>
</Connector>
<TIMs/>
<Holes/>
<Batteries/>
<Components/>
<Chip_Sockets/>
<Resistors/>
<Capacitors/>
<Inductors/>
<Heat_Spreaders/>
<Vias/>
<Heatsinks/>
<ColdPlates/>
<TECs/>
<Fans/>
<Blowers/>
<Sensors/>
<Daughter_Board_Sockets/>
<Cable_Sockets/>
<Ports/>
<Mezzanine_Cards/>
<Stand_Offs/>
<Keepouts/>
<SolidObstructions/>
<PerforatedObstructions/>
<PorousObstructions/>
<GroupObstructions/>
<FunctionalGroups/>
<ViaGroups/>
<GapPads/>
<Terminals/>
<ShieldingCans/>
<Radial_Fans/>
<Heat_Sources/>
<Grid_Controls>
<Grid_Control id="45995-47692">
<Installed>Yes</Installed>
<Identification>
<Name>Grid Control 1</Name>
</Identification>
<Geometry>
<Direction>Geometry Based</Direction>
<Size_From_Parent>Yes</Size_From_Parent>
<Size>0 mm</Size>
<Width>0 mm</Width>
<Height>0 mm</Height>
<Depth>0 mm</Depth>
</Geometry>
<Placement>
<Location>0 mm</Location>
<X_Location>0 mm</X_Location>
<Y_Location>0 mm</Y_Location>
<Z_Location>0 mm</Z_Location>
</Placement>
<Construction>
<Construction_1D>
<Extra_Grid_Type>Number Of Cells</Extra_Grid_Type>
<Line_Offset>0 mm</Line_Offset>
<Maximum_Size>101.6 mm</Maximum_Size>
<Number_Of_Cells>5</Number_Of_Cells>
<Start_Size>10 mm</Start_Size>
<Multiplier>2</Multiplier>
<Exact_Grid_Lines>No</Exact_Grid_Lines>
</Construction_1D>
<X_Construction>
<Extra_Grid_Type>Number Of Cells</Extra_Grid_Type>
<Maximum_Size>10 mm</Maximum_Size>
<Number_Of_Cells>5</Number_Of_Cells>
<Start_Size>10 mm</Start_Size>
<Multiplier>2</Multiplier>
<Exact_Grid_Lines>No</Exact_Grid_Lines>
</X_Construction>
<Y_Construction>
<Extra_Grid_Type>Number Of Cells</Extra_Grid_Type>
<Maximum_Size>10 mm</Maximum_Size>
<Number_Of_Cells>5</Number_Of_Cells>
<Start_Size>10 mm</Start_Size>
<Multiplier>2</Multiplier>
<Exact_Grid_Lines>No</Exact_Grid_Lines>
</Y_Construction>
<Z_Construction>
<Extra_Grid_Type>Number Of Cells</Extra_Grid_Type>
<Maximum_Size>10 mm</Maximum_Size>
<Number_Of_Cells>5</Number_Of_Cells>
<Start_Size>10 mm</Start_Size>
<Multiplier>2</Multiplier>
<Exact_Grid_Lines>No</Exact_Grid_Lines>
</Z_Construction>
<Geometry_Based_Construction>
<Apply_To_Solid>Yes</Apply_To_Solid>
<Maximum_Size_In_Solid>2 mm</Maximum_Size_In_Solid>
<Apply_To_Fluid>No</Apply_To_Fluid>
<Maximum_Size_In_Fluid>10 mm</Maximum_Size_In_Fluid>
<Inflate_Into_Fluid>Yes</Inflate_Into_Fluid>
<Inflation_Settings>
<Apply_To_Inside_Fluid>Yes</Apply_To_Inside_Fluid>
<Maximum_Size_In_Inside_Fluid>0.5 mm</Maximum_Size_In_Inside_Fluid>
<Extent_In_Inside_Fluid>2 mm</Extent_In_Inside_Fluid>
<Apply_To_Outside_Fluid>Yes</Apply_To_Outside_Fluid>
<Maximum_Size_In_Outside_Fluid>0.5 mm</Maximum_Size_In_Outside_Fluid>
<Extent_In_Outside_Fluid>2 mm</Extent_In_Outside_Fluid>
</Inflation_Settings>
</Geometry_Based_Construction>
</Construction>
<Display_Options>
<Auto_Colour>Yes</Auto_Colour>
<Colour>0,0,0</Colour>
<Hidden>No</Hidden>
</Display_Options>
</Grid_Control>
<Grid_Control id="45995-47693">
<Installed>Yes</Installed>
<Identification>
<Name>Grid Control 2</Name>
</Identification>
<Geometry>
<Direction>Y</Direction>
<Size_From_Parent>Yes</Size_From_Parent>
<Size>0 mm</Size>
<Width>0 mm</Width>
<Height>0 mm</Height>
<Depth>0 mm</Depth>
</Geometry>
<Placement>
<Location>0 mm</Location>
<X_Location>0 mm</X_Location>
<Y_Location>0 mm</Y_Location>
<Z_Location>0 mm</Z_Location>
</Placement>
<Construction>
<Construction_1D>
<Extra_Grid_Type>Number Of Cells</Extra_Grid_Type>
<Line_Offset>0 mm</Line_Offset>
<Maximum_Size>101.6 mm</Maximum_Size>
<Number_Of_Cells>5</Number_Of_Cells>
<Start_Size>10 mm</Start_Size>
<Multiplier>2</Multiplier>
<Exact_Grid_Lines>No</Exact_Grid_Lines>
</Construction_1D>
<X_Construction>
<Extra_Grid_Type>Number Of Cells</Extra_Grid_Type>
<Maximum_Size>10 mm</Maximum_Size>
<Number_Of_Cells>5</Number_Of_Cells>
<Start_Size>10 mm</Start_Size>
<Multiplier>2</Multiplier>
<Exact_Grid_Lines>No</Exact_Grid_Lines>
</X_Construction>
<Y_Construction>
<Extra_Grid_Type>Number Of Cells</Extra_Grid_Type>
<Maximum_Size>10 mm</Maximum_Size>
<Number_Of_Cells>5</Number_Of_Cells>
<Start_Size>10 mm</Start_Size>
<Multiplier>2</Multiplier>
<Exact_Grid_Lines>No</Exact_Grid_Lines>
</Y_Construction>
<Z_Construction>
<Extra_Grid_Type>Number Of Cells</Extra_Grid_Type>
<Maximum_Size>10 mm</Maximum_Size>
<Number_Of_Cells>5</Number_Of_Cells>
<Start_Size>10 mm</Start_Size>
<Multiplier>2</Multiplier>
<Exact_Grid_Lines>No</Exact_Grid_Lines>
</Z_Construction>
<Geometry_Based_Construction>
<Apply_To_Solid>Yes</Apply_To_Solid>
<Maximum_Size_In_Solid>10 mm</Maximum_Size_In_Solid>
<Apply_To_Fluid>No</Apply_To_Fluid>
<Maximum_Size_In_Fluid>10 mm</Maximum_Size_In_Fluid>
<Inflate_Into_Fluid>No</Inflate_Into_Fluid>
<Inflation_Settings>
<Apply_To_Inside_Fluid>Yes</Apply_To_Inside_Fluid>
<Maximum_Size_In_Inside_Fluid>10 mm</Maximum_Size_In_Inside_Fluid>
<Extent_In_Inside_Fluid>20 mm</Extent_In_Inside_Fluid>
<Apply_To_Outside_Fluid>Yes</Apply_To_Outside_Fluid>
<Maximum_Size_In_Outside_Fluid>10 mm</Maximum_Size_In_Outside_Fluid>
<Extent_In_Outside_Fluid>20 mm</Extent_In_Outside_Fluid>
</Inflation_Settings>
</Geometry_Based_Construction>
</Construction>
<Display_Options>
<Auto_Colour>Yes</Auto_Colour>
<Colour>0,0,0</Colour>
<Hidden>No</Hidden>
</Display_Options>
</Grid_Control>
</Grid_Controls>
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
<Exchange_Values/>
</PCB>
</PCBs>
<Components/>
<Batteries/>
<Fans/>
<Fan_Trays/>
<Radial_Fans/>
<Blowers/>
<Flow_Devices/>
<Pumps/>
<CoolingDucts/>
<Heatsinks/>
<ColdPlates/>
<TECs/>
<Power_Supplies/>
<Chassis_Bays/>
<Card_Bays/>
<Drive_Bays/>
<Heat_Exchangers/>
<SimplifiedEquipment/>
<Cables/>
<SolidObstructions>
<Solid_Obstruction id="45995-47694">
<Installed>Yes</Installed>
<Identification>
<Name>CASE_LOWER_COVER</Name>
<Layer_Type>Chassis</Layer_Type>
<Type>Substrate</Type>
</Identification>
<Geometry>
<Shape>Cuboid</Shape>
<Available_Sides>Front,Rear,Top,Bottom,Left,Right</Available_Sides>
<Modelling_Level>Thick</Modelling_Level>
<Collapse_Direction>Thinnest</Collapse_Direction>
<Thickness>0 mm</Thickness>
<Height>2 mm</Height>
<Width>100 mm</Width>
<Depth>90 mm</Depth>
<Diameter>20 mm</Diameter>
<Hole_Direction>Z</Hole_Direction>
<Solid/>
<Realign_Origin>No</Realign_Origin>
<Ignore_Collision_Detection>No</Ignore_Collision_Detection>
<Grid>
<Minimum_Cell_Size>0.1 mm</Minimum_Cell_Size>
<Minimum_Number_Of_Cells>
<Width_Direction>5</Width_Direction>
<Depth_Direction>5</Depth_Direction>
</Minimum_Number_Of_Cells>
</Grid>
<Surface_Area>18760 mm^2</Surface_Area>
</Geometry>
<Placement>
<Origin_Point>Low Centre</Origin_Point>
<X_Location>500 mm</X_Location>
<Y_Location>500 mm</Y_Location>
<Z_Location>500 mm</Z_Location>
<X_Origin>0 mm</X_Origin>
<Y_Origin>0 mm</Y_Origin>
<Z_Origin>0 mm</Z_Origin>
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
<Weight>0 kg</Weight>
</Construction>
<Cooling>
<Modelling_Detail>Full</Modelling_Detail>
<Heat_Conduction_Grid>Yes</Heat_Conduction_Grid>
<Heat_Option>Total Heat</Heat_Option>
<Power_Specification>Total Power</Power_Specification>
<Temperature_Dependent_Heat_Dissipation>No</Temperature_Dependent_Heat_Dissipation>
<Time_Dependent_Heat_Dissipation>No</Time_Dependent_Heat_Dissipation>
<Temperature>15.5555555555556 C</Temperature>
<Temperature_Curve>0,20, 100,20 &lt;s,C&gt;</Temperature_Curve>
<Temperature_Dependent_Power>No</Temperature_Dependent_Power>
<Heat_Dissipated>0 W</Heat_Dissipated>
<Heat_Dissipated_Curve>0,0, 100,0 &lt;s,W&gt;</Heat_Dissipated_Curve>
<Heat_Dissipated_Temperature_Curve>20,0, 50,0 &lt;C,W&gt;</Heat_Dissipated_Temperature_Curve>
<Heat_Dissipated_Temperature_Multiple_Curves>
<Initial_Curve_Id>0</Initial_Curve_Id>
<Current_Curve_Id>0</Current_Curve_Id>
<Thermal_Design_Power_Temperature_Curve_Array>10,0,1000, 150,0|30,0,1000, 150,0 &lt;C,C,W&gt;</Thermal_Design_Power_Temperature_Curve_Array>
<Curve_Names>0
</Curve_Names>
<Transitions>0
</Transitions>
</Heat_Dissipated_Temperature_Multiple_Curves>
<Heat_Dissipation_Curve_Hysteresis>0 C</Heat_Dissipation_Curve_Hysteresis>
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
<Controlling_Temperature>Solid</Controlling_Temperature>
<Temperature_Dependence_Sensors/>
<Sensor_Treatment>Weighted Average</Sensor_Treatment>
<Sensor_Weights> : </Sensor_Weights>
<User_Defined_Heat_Transfer>
<Fluid_Heat_Transfer_Option>From Solution</Fluid_Heat_Transfer_Option>
<Fluid_Heat_Transfer_Coefficient>10 W/(m^2K)</Fluid_Heat_Transfer_Coefficient>
<Solid_Heat_Transfer_Option>From Solution</Solid_Heat_Transfer_Option>
<Solid_Heat_Transfer_Coefficient>10 W/(m^2K)</Solid_Heat_Transfer_Coefficient>
</User_Defined_Heat_Transfer>
<Allow_Boundary_Cell_Reconstruction>Yes</Allow_Boundary_Cell_Reconstruction>
<Surface_Roughness>
<Roughness_Type>Whole Range</Roughness_Type>
<Roughness_Height>0 mm</Roughness_Height>
<Roughness_Length>0 mm</Roughness_Length>
<Roughness_Constant>0.5</Roughness_Constant>
</Surface_Roughness>
<Wall_Function>Standard</Wall_Function>
<Subdivide_Surfaces_For_Radiation>Yes</Subdivide_Surfaces_For_Radiation>
<Surface_Subdivision_Size>10 mm</Surface_Subdivision_Size>
<Display_in_CFD_Progress>Auto</Display_in_CFD_Progress>
<Contributes_to_Termination_Criteria>Yes</Contributes_to_Termination_Criteria>
<MaterialLink>45995-47721 </MaterialLink>
<Material_Alignment>XYZ</Material_Alignment>
<Material_Normal>X</Material_Normal>
<Calculated_Weight>141.696 g</Calculated_Weight>
</Cooling>
<Electric_Current>
<Time_Dependent_Current>No</Time_Dependent_Current>
<Current>0 mA</Current>
<Current_Curve>0,0, 100,0 &lt;s,mA&gt;</Current_Curve>
<Current_Direction>Longest</Current_Direction>
</Electric_Current>
<TIMs/>
<Heat_Sources/>
<Holes/>
<Faces/>
<Sensors/>
<ElectricalBoundaries/>
<Terminals/>
<TerminalLink/>
<Display_Options>
<Colour>180,180,180</Colour>
<EnableUseMaterialColour>Yes</EnableUseMaterialColour>
<Use_This_Colour>No</Use_This_Colour>
<Secondary_Colour>180,180,180</Secondary_Colour>
<Basic_Render_Style>Solid,Wireframe,Solid Outlined,Textured,Transparent,Invisible</Basic_Render_Style>
<Render_Style>Solid Outlined</Render_Style>
<Transparency>70 %</Transparency>
<Variable>Temperature</Variable>
<Show_Computational_Shape>Yes</Show_Computational_Shape>
<Data_Type>Geometry</Data_Type>
<Plot_Type>Variation Plot Smooth</Plot_Type>
<Show_Grid>No</Show_Grid>
<Target_Variable>Surface Temperature</Target_Variable>
<Hidden>No</Hidden>
</Display_Options>
<Grid_Controls>
<Grid_Control id="45995-47695">
<Installed>Yes</Installed>
<Identification>
<Name>Grid Control 1</Name>
</Identification>
<Geometry>
<Direction>Geometry Based</Direction>
<Size_From_Parent>Yes</Size_From_Parent>
<Size>0 mm</Size>
<Width>0 mm</Width>
<Height>0 mm</Height>
<Depth>0 mm</Depth>
</Geometry>
<Placement>
<Location>0 mm</Location>
<X_Location>0 mm</X_Location>
<Y_Location>0 mm</Y_Location>
<Z_Location>0 mm</Z_Location>
</Placement>
<Construction>
<Construction_1D>
<Extra_Grid_Type>Number Of Cells</Extra_Grid_Type>
<Line_Offset>0 mm</Line_Offset>
<Maximum_Size>101.6 mm</Maximum_Size>
<Number_Of_Cells>5</Number_Of_Cells>
<Start_Size>10 mm</Start_Size>
<Multiplier>2</Multiplier>
<Exact_Grid_Lines>No</Exact_Grid_Lines>
</Construction_1D>
<X_Construction>
<Extra_Grid_Type>Number Of Cells</Extra_Grid_Type>
<Maximum_Size>10 mm</Maximum_Size>
<Number_Of_Cells>5</Number_Of_Cells>
<Start_Size>10 mm</Start_Size>
<Multiplier>2</Multiplier>
<Exact_Grid_Lines>No</Exact_Grid_Lines>
</X_Construction>
<Y_Construction>
<Extra_Grid_Type>Number Of Cells</Extra_Grid_Type>
<Maximum_Size>10 mm</Maximum_Size>
<Number_Of_Cells>5</Number_Of_Cells>
<Start_Size>10 mm</Start_Size>
<Multiplier>2</Multiplier>
<Exact_Grid_Lines>No</Exact_Grid_Lines>
</Y_Construction>
<Z_Construction>
<Extra_Grid_Type>Number Of Cells</Extra_Grid_Type>
<Maximum_Size>10 mm</Maximum_Size>
<Number_Of_Cells>5</Number_Of_Cells>
<Start_Size>10 mm</Start_Size>
<Multiplier>2</Multiplier>
<Exact_Grid_Lines>No</Exact_Grid_Lines>
</Z_Construction>
<Geometry_Based_Construction>
<Apply_To_Solid>Yes</Apply_To_Solid>
<Maximum_Size_In_Solid>2 mm</Maximum_Size_In_Solid>
<Apply_To_Fluid>No</Apply_To_Fluid>
<Maximum_Size_In_Fluid>10 mm</Maximum_Size_In_Fluid>
<Inflate_Into_Fluid>Yes</Inflate_Into_Fluid>
<Inflation_Settings>
<Apply_To_Inside_Fluid>Yes</Apply_To_Inside_Fluid>
<Maximum_Size_In_Inside_Fluid>0.5 mm</Maximum_Size_In_Inside_Fluid>
<Extent_In_Inside_Fluid>2 mm</Extent_In_Inside_Fluid>
<Apply_To_Outside_Fluid>Yes</Apply_To_Outside_Fluid>
<Maximum_Size_In_Outside_Fluid>0.5 mm</Maximum_Size_In_Outside_Fluid>
<Extent_In_Outside_Fluid>2 mm</Extent_In_Outside_Fluid>
</Inflation_Settings>
</Geometry_Based_Construction>
</Construction>
<Display_Options>
<Auto_Colour>Yes</Auto_Colour>
<Colour>0,0,0</Colour>
<Hidden>No</Hidden>
</Display_Options>
</Grid_Control>
</Grid_Controls>
<Simulation_Results>
<Heat_Fluxes>
<ShowPolygonSides>No</ShowPolygonSides>
<ShowCuboidSides>No</ShowCuboidSides>
</Heat_Fluxes>
<Joule_Heating>0 W</Joule_Heating>
<Temperature_Dependent_Heating>0 W</Temperature_Dependent_Heating>
<Controlling_Temperature>0 C</Controlling_Temperature>
<Embedded_Heating>0 W</Embedded_Heating>
<Solar_Heating>0 W</Solar_Heating>
</Simulation_Results>
<Object_Shape_Definition>
<Shape_Type>Cuboid</Shape_Type>
<Thin_Shape>No</Thin_Shape>
<With_Holes>No</With_Holes>
</Object_Shape_Definition>
<Push_Pins/>
</Solid_Obstruction>
<Solid_Obstruction id="45995-47696">
<Installed>Yes</Installed>
<Identification>
<Name>CASE_LOWER_SIDE</Name>
<Layer_Type>Chassis</Layer_Type>
<Type>Substrate</Type>
</Identification>
<Geometry>
<Shape>Cuboid</Shape>
<Available_Sides>Top,Bottom,Side 1,Side 2,Side 3,Side 4,Hole 1 Side 1,Hole 1 Side 2,Hole 1 Side 3,Hole 1 Side 4</Available_Sides>
<Modelling_Level>Thick</Modelling_Level>
<Collapse_Direction>Thinnest</Collapse_Direction>
<Thickness>0 mm</Thickness>
<Height>8 mm</Height>
<Width>100 mm</Width>
<Depth>90 mm</Depth>
<Diameter>20 mm</Diameter>
<Hole_Direction>Y</Hole_Direction>
<Solid/>
<Realign_Origin>No</Realign_Origin>
<Ignore_Collision_Detection>No</Ignore_Collision_Detection>
<Grid>
<Minimum_Cell_Size>0.1 mm</Minimum_Cell_Size>
<Minimum_Number_Of_Cells>
<Width_Direction>5</Width_Direction>
<Depth_Direction>5</Depth_Direction>
</Minimum_Number_Of_Cells>
</Grid>
<Surface_Area>7440 mm^2</Surface_Area>
</Geometry>
<Placement>
<Origin_Point>Low Centre</Origin_Point>
<X_Location>500 mm</X_Location>
<Y_Location>502 mm</Y_Location>
<Z_Location>500 mm</Z_Location>
<X_Origin>0 mm</X_Origin>
<Y_Origin>0 mm</Y_Origin>
<Z_Origin>0 mm</Z_Origin>
<Orientation>
<Rotation_Mechanism>Ordered</Rotation_Mechanism>
<X_Axis>0</X_Axis>
<Y_Axis>1</Y_Axis>
<Z_Axis>0</Z_Axis>
<Angle>0 degrees</Angle>
<Rotation_Order>XZY</Rotation_Order>
<Angle_1>0 degrees</Angle_1>
<Angle_2>0 degrees</Angle_2>
<Angle_3>0 degrees</Angle_3>
</Orientation>
</Placement>
<Construction>
<Weight>0 kg</Weight>
</Construction>
<Cooling>
<Modelling_Detail>Full</Modelling_Detail>
<Heat_Conduction_Grid>Yes</Heat_Conduction_Grid>
<Heat_Option>Total Heat</Heat_Option>
<Power_Specification>Total Power</Power_Specification>
<Temperature_Dependent_Heat_Dissipation>No</Temperature_Dependent_Heat_Dissipation>
<Time_Dependent_Heat_Dissipation>No</Time_Dependent_Heat_Dissipation>
<Temperature>15.5555555555556 C</Temperature>
<Temperature_Curve>0,20, 100,20 &lt;s,C&gt;</Temperature_Curve>
<Temperature_Dependent_Power>No</Temperature_Dependent_Power>
<Heat_Dissipated>0 W</Heat_Dissipated>
<Heat_Dissipated_Curve>0,0, 100,0 &lt;s,W&gt;</Heat_Dissipated_Curve>
<Heat_Dissipated_Temperature_Curve>20,0, 50,0 &lt;C,W&gt;</Heat_Dissipated_Temperature_Curve>
<Heat_Dissipated_Temperature_Multiple_Curves>
<Initial_Curve_Id>0</Initial_Curve_Id>
<Current_Curve_Id>0</Current_Curve_Id>
<Thermal_Design_Power_Temperature_Curve_Array>10,0,1000, 150,0|30,0,1000, 150,0 &lt;C,C,W&gt;</Thermal_Design_Power_Temperature_Curve_Array>
<Curve_Names>0
</Curve_Names>
<Transitions>0
</Transitions>
</Heat_Dissipated_Temperature_Multiple_Curves>
<Heat_Dissipation_Curve_Hysteresis>0 C</Heat_Dissipation_Curve_Hysteresis>
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
<Controlling_Temperature>Solid</Controlling_Temperature>
<Temperature_Dependence_Sensors/>
<Sensor_Treatment>Weighted Average</Sensor_Treatment>
<Sensor_Weights> : </Sensor_Weights>
<User_Defined_Heat_Transfer>
<Fluid_Heat_Transfer_Option>From Solution</Fluid_Heat_Transfer_Option>
<Fluid_Heat_Transfer_Coefficient>10 W/(m^2K)</Fluid_Heat_Transfer_Coefficient>
<Solid_Heat_Transfer_Option>From Solution</Solid_Heat_Transfer_Option>
<Solid_Heat_Transfer_Coefficient>10 W/(m^2K)</Solid_Heat_Transfer_Coefficient>
</User_Defined_Heat_Transfer>
<Allow_Boundary_Cell_Reconstruction>Yes</Allow_Boundary_Cell_Reconstruction>
<Surface_Roughness>
<Roughness_Type>Whole Range</Roughness_Type>
<Roughness_Height>0 mm</Roughness_Height>
<Roughness_Length>0 mm</Roughness_Length>
<Roughness_Constant>0.5</Roughness_Constant>
</Surface_Roughness>
<Wall_Function>Standard</Wall_Function>
<Subdivide_Surfaces_For_Radiation>Yes</Subdivide_Surfaces_For_Radiation>
<Surface_Subdivision_Size>10 mm</Surface_Subdivision_Size>
<Display_in_CFD_Progress>Auto</Display_in_CFD_Progress>
<Contributes_to_Termination_Criteria>Yes</Contributes_to_Termination_Criteria>
<MaterialLink>45995-47721 </MaterialLink>
<Material_Alignment>XYZ</Material_Alignment>
<Material_Normal>X</Material_Normal>
<Calculated_Weight>46.854144 g</Calculated_Weight>
</Cooling>
<Electric_Current>
<Time_Dependent_Current>No</Time_Dependent_Current>
<Current>0 mA</Current>
<Current_Curve>0,0, 100,0 &lt;s,mA&gt;</Current_Curve>
<Current_Direction>Longest</Current_Direction>
</Electric_Current>
<TIMs/>
<Heat_Sources/>
<Holes>
<Obstruction_Hole id="45995-47697">
<Installed>Yes</Installed>
<Identification>
<Name>CASE_LOWER_HOLE</Name>
</Identification>
<Segment_Index>0</Segment_Index>
<Geometry>
<Shape>Rectangle</Shape>
<Available_Sides>Top,Bottom,Left,Right</Available_Sides>
<Width>96 mm</Width>
<Depth>86 mm</Depth>
<Diameter>8 mm</Diameter>
</Geometry>
<Placement>
<X_Location>2 mm</X_Location>
<Y_Location>3 mm</Y_Location>
<Z_Location>2 mm</Z_Location>
<Orientation>0 degrees</Orientation>
</Placement>
<Construction>
<Specification>Open Hole</Specification>
<Perforation_Details>
<Hole_Shape>Circular</Hole_Shape>
<Hole_Diameter>2.999999999999989 mm</Hole_Diameter>
<Hole_Size>2.999999999999989 mm</Hole_Size>
<Specify_Pitch>No</Specify_Pitch>
<Width_Pitch>2.999999999999989 mm</Width_Pitch>
<Length_Pitch>2.999999999999989 mm</Length_Pitch>
<Controllable>Yes</Controllable>
<Open_Area_Option>Fixed</Open_Area_Option>
<Open_Area>64 %</Open_Area>
<Controller_Response>Direct</Controller_Response>
<Minimum_Open_Area>64 %</Minimum_Open_Area>
<Maximum_Open_Area>64 %</Maximum_Open_Area>
<Controller_Response_Curve>0,0, 100,100 &lt;%,%&gt;</Controller_Response_Curve>
<Use_Internal_Controller>No</Use_Internal_Controller>
<Internal_PerforatedController/>
<External_PerforatedController/>
<Estimated_Open_Area>64 %</Estimated_Open_Area>
<Straighten_Flow>Yes</Straighten_Flow>
</Perforation_Details>
<Slotted_Details>
<Slot_Width>2.999999999999989 mm</Slot_Width>
<Slot_Length>2.999999999999989 mm</Slot_Length>
<Specify_Separation>No</Specify_Separation>
<Width_Separation>2.999999999999989 mm</Width_Separation>
<Length_Separation>2.999999999999989 mm</Length_Separation>
<Controllable>Yes</Controllable>
<Open_Area_Option>Fixed</Open_Area_Option>
<Open_Area>64 %</Open_Area>
<Controller_Response>Direct</Controller_Response>
<Minimum_Open_Area>64 %</Minimum_Open_Area>
<Maximum_Open_Area>64 %</Maximum_Open_Area>
<Controller_Response_Curve>0,0, 100,100 &lt;%,%&gt;</Controller_Response_Curve>
<Use_Internal_Controller>No</Use_Internal_Controller>
<Internal_SlottedController/>
<External_SlottedController/>
<Estimated_Open_Area>64 %</Estimated_Open_Area>
<Straighten_Flow>Yes</Straighten_Flow>
<Width_Directionality>Normal</Width_Directionality>
<Width_Angle>0 degrees</Width_Angle>
<Minimum_Open_Area_Width_Angle>0 degrees</Minimum_Open_Area_Width_Angle>
<Maximum_Open_Area_Width_Angle>0 degrees</Maximum_Open_Area_Width_Angle>
<Length_Directionality>Normal</Length_Directionality>
<Length_Angle>0 degrees</Length_Angle>
<Minimum_Open_Area_Length_Angle>0 degrees</Minimum_Open_Area_Length_Angle>
<Maximum_Open_Area_Length_Angle>0 degrees</Maximum_Open_Area_Length_Angle>
</Slotted_Details>
<Mesh_Details>
<Strand_Diameter>2.999999999999989 mm</Strand_Diameter>
<Specify_Separation>No</Specify_Separation>
<Width_Separation>2.999999999999989 mm</Width_Separation>
<Length_Separation>2.999999999999989 mm</Length_Separation>
<Open_Area>64 %</Open_Area>
<Estimated_Open_Area>64 %</Estimated_Open_Area>
</Mesh_Details>
</Construction>
<ResultVolumeLink/>
<Sensors/>
<Display_Options>
<Colour>180,180,180</Colour>
<EnableUseMaterialColour>No</EnableUseMaterialColour>
<Use_This_Colour>Yes</Use_This_Colour>
<Secondary_Colour>180,180,180</Secondary_Colour>
<Basic_Render_Style>Solid,Wireframe,Solid Outlined,Textured,Transparent,Invisible</Basic_Render_Style>
<Render_Style>Wireframe</Render_Style>
<Transparency>70 %</Transparency>
<Variable>Temperature</Variable>
<Show_Computational_Shape>No</Show_Computational_Shape>
<Data_Type>Regions</Data_Type>
<Plot_Type>Variation Plot Smooth</Plot_Type>
<Show_Grid>No</Show_Grid>
<Target_Variable>Temperature</Target_Variable>
<Hidden>No</Hidden>
</Display_Options>
<StreamPlot/>
<Simulation_Results>
<Through_Flow>
<Net_Flow>0 m^3/s</Net_Flow>
</Through_Flow>
<Heat_Flow>
<Positive_Heat_Flow>0 W</Positive_Heat_Flow>
<Negative_Heat_Flow>0 W</Negative_Heat_Flow>
<Net_Heat_Flow>0 W</Net_Heat_Flow>
</Heat_Flow>
<Contamination_In>
<Solved_Contaminants>0
</Solved_Contaminants>
</Contamination_In>
<Contamination_Out>
<Solved_Contaminants>0
</Solved_Contaminants>
</Contamination_Out>
</Simulation_Results>
</Obstruction_Hole>
</Holes>
<Faces/>
<Sensors/>
<ElectricalBoundaries/>
<Terminals/>
<TerminalLink/>
<Display_Options>
<Colour>180,180,180</Colour>
<EnableUseMaterialColour>Yes</EnableUseMaterialColour>
<Use_This_Colour>No</Use_This_Colour>
<Secondary_Colour>180,180,180</Secondary_Colour>
<Basic_Render_Style>Solid,Wireframe,Solid Outlined,Textured,Transparent,Invisible</Basic_Render_Style>
<Render_Style>Solid Outlined</Render_Style>
<Transparency>70 %</Transparency>
<Variable>Temperature</Variable>
<Show_Computational_Shape>Yes</Show_Computational_Shape>
<Data_Type>Geometry</Data_Type>
<Plot_Type>Variation Plot Smooth</Plot_Type>
<Show_Grid>No</Show_Grid>
<Target_Variable>Surface Temperature</Target_Variable>
<Hidden>No</Hidden>
</Display_Options>
<Grid_Controls>
<Grid_Control id="45995-47698">
<Installed>Yes</Installed>
<Identification>
<Name>Grid Control 1</Name>
</Identification>
<Geometry>
<Direction>Geometry Based</Direction>
<Size_From_Parent>Yes</Size_From_Parent>
<Size>0 mm</Size>
<Width>0 mm</Width>
<Height>0 mm</Height>
<Depth>0 mm</Depth>
</Geometry>
<Placement>
<Location>0 mm</Location>
<X_Location>0 mm</X_Location>
<Y_Location>0 mm</Y_Location>
<Z_Location>0 mm</Z_Location>
</Placement>
<Construction>
<Construction_1D>
<Extra_Grid_Type>Number Of Cells</Extra_Grid_Type>
<Line_Offset>0 mm</Line_Offset>
<Maximum_Size>101.6 mm</Maximum_Size>
<Number_Of_Cells>5</Number_Of_Cells>
<Start_Size>10 mm</Start_Size>
<Multiplier>2</Multiplier>
<Exact_Grid_Lines>No</Exact_Grid_Lines>
</Construction_1D>
<X_Construction>
<Extra_Grid_Type>Number Of Cells</Extra_Grid_Type>
<Maximum_Size>10 mm</Maximum_Size>
<Number_Of_Cells>5</Number_Of_Cells>
<Start_Size>10 mm</Start_Size>
<Multiplier>2</Multiplier>
<Exact_Grid_Lines>No</Exact_Grid_Lines>
</X_Construction>
<Y_Construction>
<Extra_Grid_Type>Number Of Cells</Extra_Grid_Type>
<Maximum_Size>10 mm</Maximum_Size>
<Number_Of_Cells>5</Number_Of_Cells>
<Start_Size>10 mm</Start_Size>
<Multiplier>2</Multiplier>
<Exact_Grid_Lines>No</Exact_Grid_Lines>
</Y_Construction>
<Z_Construction>
<Extra_Grid_Type>Number Of Cells</Extra_Grid_Type>
<Maximum_Size>10 mm</Maximum_Size>
<Number_Of_Cells>5</Number_Of_Cells>
<Start_Size>10 mm</Start_Size>
<Multiplier>2</Multiplier>
<Exact_Grid_Lines>No</Exact_Grid_Lines>
</Z_Construction>
<Geometry_Based_Construction>
<Apply_To_Solid>Yes</Apply_To_Solid>
<Maximum_Size_In_Solid>2 mm</Maximum_Size_In_Solid>
<Apply_To_Fluid>No</Apply_To_Fluid>
<Maximum_Size_In_Fluid>10 mm</Maximum_Size_In_Fluid>
<Inflate_Into_Fluid>Yes</Inflate_Into_Fluid>
<Inflation_Settings>
<Apply_To_Inside_Fluid>Yes</Apply_To_Inside_Fluid>
<Maximum_Size_In_Inside_Fluid>0.5 mm</Maximum_Size_In_Inside_Fluid>
<Extent_In_Inside_Fluid>2 mm</Extent_In_Inside_Fluid>
<Apply_To_Outside_Fluid>Yes</Apply_To_Outside_Fluid>
<Maximum_Size_In_Outside_Fluid>0.5 mm</Maximum_Size_In_Outside_Fluid>
<Extent_In_Outside_Fluid>2 mm</Extent_In_Outside_Fluid>
</Inflation_Settings>
</Geometry_Based_Construction>
</Construction>
<Display_Options>
<Auto_Colour>Yes</Auto_Colour>
<Colour>0,0,0</Colour>
<Hidden>No</Hidden>
</Display_Options>
</Grid_Control>
</Grid_Controls>
<Simulation_Results>
<Heat_Fluxes>
<ShowPolygonSides>No</ShowPolygonSides>
<ShowCuboidSides>No</ShowCuboidSides>
</Heat_Fluxes>
<Joule_Heating>0 W</Joule_Heating>
<Temperature_Dependent_Heating>0 W</Temperature_Dependent_Heating>
<Controlling_Temperature>0 C</Controlling_Temperature>
<Embedded_Heating>0 W</Embedded_Heating>
<Solar_Heating>0 W</Solar_Heating>
</Simulation_Results>
<Object_Shape_Definition>
<Shape_Type>Cuboid</Shape_Type>
<Thin_Shape>No</Thin_Shape>
<With_Holes>Yes</With_Holes>
</Object_Shape_Definition>
<Push_Pins/>
</Solid_Obstruction>
<Solid_Obstruction id="45995-47699">
<Installed>Yes</Installed>
<Identification>
<Name>CASE_UPPER_SIDE</Name>
<Layer_Type>Chassis</Layer_Type>
<Type>Substrate</Type>
</Identification>
<Geometry>
<Shape>Cuboid</Shape>
<Available_Sides>Top,Bottom,Side 1,Side 2,Side 3,Side 4,Hole 1 Side 1,Hole 1 Side 2,Hole 1 Side 3,Hole 1 Side 4</Available_Sides>
<Modelling_Level>Thick</Modelling_Level>
<Collapse_Direction>Thinnest</Collapse_Direction>
<Thickness>0 mm</Thickness>
<Height>8 mm</Height>
<Width>100 mm</Width>
<Depth>90 mm</Depth>
<Diameter>20 mm</Diameter>
<Hole_Direction>Y</Hole_Direction>
<Solid/>
<Realign_Origin>No</Realign_Origin>
<Ignore_Collision_Detection>No</Ignore_Collision_Detection>
<Grid>
<Minimum_Cell_Size>0.1 mm</Minimum_Cell_Size>
<Minimum_Number_Of_Cells>
<Width_Direction>5</Width_Direction>
<Depth_Direction>5</Depth_Direction>
</Minimum_Number_Of_Cells>
</Grid>
<Surface_Area>7440 mm^2</Surface_Area>
</Geometry>
<Placement>
<Origin_Point>Low Centre</Origin_Point>
<X_Location>500 mm</X_Location>
<Y_Location>511.6 mm</Y_Location>
<Z_Location>500 mm</Z_Location>
<X_Origin>0 mm</X_Origin>
<Y_Origin>0 mm</Y_Origin>
<Z_Origin>0 mm</Z_Origin>
<Orientation>
<Rotation_Mechanism>Ordered</Rotation_Mechanism>
<X_Axis>0</X_Axis>
<Y_Axis>1</Y_Axis>
<Z_Axis>0</Z_Axis>
<Angle>0 degrees</Angle>
<Rotation_Order>XZY</Rotation_Order>
<Angle_1>0 degrees</Angle_1>
<Angle_2>0 degrees</Angle_2>
<Angle_3>0 degrees</Angle_3>
</Orientation>
</Placement>
<Construction>
<Weight>0 kg</Weight>
</Construction>
<Cooling>
<Modelling_Detail>Full</Modelling_Detail>
<Heat_Conduction_Grid>Yes</Heat_Conduction_Grid>
<Heat_Option>Total Heat</Heat_Option>
<Power_Specification>Total Power</Power_Specification>
<Temperature_Dependent_Heat_Dissipation>No</Temperature_Dependent_Heat_Dissipation>
<Time_Dependent_Heat_Dissipation>No</Time_Dependent_Heat_Dissipation>
<Temperature>15.5555555555556 C</Temperature>
<Temperature_Curve>0,20, 100,20 &lt;s,C&gt;</Temperature_Curve>
<Temperature_Dependent_Power>No</Temperature_Dependent_Power>
<Heat_Dissipated>0 W</Heat_Dissipated>
<Heat_Dissipated_Curve>0,0, 100,0 &lt;s,W&gt;</Heat_Dissipated_Curve>
<Heat_Dissipated_Temperature_Curve>20,0, 50,0 &lt;C,W&gt;</Heat_Dissipated_Temperature_Curve>
<Heat_Dissipated_Temperature_Multiple_Curves>
<Initial_Curve_Id>0</Initial_Curve_Id>
<Current_Curve_Id>0</Current_Curve_Id>
<Thermal_Design_Power_Temperature_Curve_Array>10,0,1000, 150,0|30,0,1000, 150,0 &lt;C,C,W&gt;</Thermal_Design_Power_Temperature_Curve_Array>
<Curve_Names>0
</Curve_Names>
<Transitions>0
</Transitions>
</Heat_Dissipated_Temperature_Multiple_Curves>
<Heat_Dissipation_Curve_Hysteresis>0 C</Heat_Dissipation_Curve_Hysteresis>
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
<Controlling_Temperature>Solid</Controlling_Temperature>
<Temperature_Dependence_Sensors/>
<Sensor_Treatment>Weighted Average</Sensor_Treatment>
<Sensor_Weights> : </Sensor_Weights>
<User_Defined_Heat_Transfer>
<Fluid_Heat_Transfer_Option>From Solution</Fluid_Heat_Transfer_Option>
<Fluid_Heat_Transfer_Coefficient>10 W/(m^2K)</Fluid_Heat_Transfer_Coefficient>
<Solid_Heat_Transfer_Option>From Solution</Solid_Heat_Transfer_Option>
<Solid_Heat_Transfer_Coefficient>10 W/(m^2K)</Solid_Heat_Transfer_Coefficient>
</User_Defined_Heat_Transfer>
<Allow_Boundary_Cell_Reconstruction>Yes</Allow_Boundary_Cell_Reconstruction>
<Surface_Roughness>
<Roughness_Type>Whole Range</Roughness_Type>
<Roughness_Height>0 mm</Roughness_Height>
<Roughness_Length>0 mm</Roughness_Length>
<Roughness_Constant>0.5</Roughness_Constant>
</Surface_Roughness>
<Wall_Function>Standard</Wall_Function>
<Subdivide_Surfaces_For_Radiation>Yes</Subdivide_Surfaces_For_Radiation>
<Surface_Subdivision_Size>10 mm</Surface_Subdivision_Size>
<Display_in_CFD_Progress>Auto</Display_in_CFD_Progress>
<Contributes_to_Termination_Criteria>Yes</Contributes_to_Termination_Criteria>
<MaterialLink>45995-47709 </MaterialLink>
<Material_Alignment>XYZ</Material_Alignment>
<Material_Normal>X</Material_Normal>
<Calculated_Weight>16.802496 g</Calculated_Weight>
</Cooling>
<Electric_Current>
<Time_Dependent_Current>No</Time_Dependent_Current>
<Current>0 mA</Current>
<Current_Curve>0,0, 100,0 &lt;s,mA&gt;</Current_Curve>
<Current_Direction>Longest</Current_Direction>
</Electric_Current>
<TIMs/>
<Heat_Sources/>
<Holes>
<Obstruction_Hole id="45995-47700">
<Installed>Yes</Installed>
<Identification>
<Name>CASE_UPPER_HOLE</Name>
</Identification>
<Segment_Index>0</Segment_Index>
<Geometry>
<Shape>Rectangle</Shape>
<Available_Sides>Top,Bottom,Left,Right</Available_Sides>
<Width>96 mm</Width>
<Depth>86 mm</Depth>
<Diameter>8 mm</Diameter>
</Geometry>
<Placement>
<X_Location>2 mm</X_Location>
<Y_Location>3 mm</Y_Location>
<Z_Location>2 mm</Z_Location>
<Orientation>0 degrees</Orientation>
</Placement>
<Construction>
<Specification>Open Hole</Specification>
<Perforation_Details>
<Hole_Shape>Circular</Hole_Shape>
<Hole_Diameter>2.999999999999989 mm</Hole_Diameter>
<Hole_Size>2.999999999999989 mm</Hole_Size>
<Specify_Pitch>No</Specify_Pitch>
<Width_Pitch>2.999999999999989 mm</Width_Pitch>
<Length_Pitch>2.999999999999989 mm</Length_Pitch>
<Controllable>Yes</Controllable>
<Open_Area_Option>Fixed</Open_Area_Option>
<Open_Area>64 %</Open_Area>
<Controller_Response>Direct</Controller_Response>
<Minimum_Open_Area>64 %</Minimum_Open_Area>
<Maximum_Open_Area>64 %</Maximum_Open_Area>
<Controller_Response_Curve>0,0, 100,100 &lt;%,%&gt;</Controller_Response_Curve>
<Use_Internal_Controller>No</Use_Internal_Controller>
<Internal_PerforatedController/>
<External_PerforatedController/>
<Estimated_Open_Area>64 %</Estimated_Open_Area>
<Straighten_Flow>Yes</Straighten_Flow>
</Perforation_Details>
<Slotted_Details>
<Slot_Width>2.999999999999989 mm</Slot_Width>
<Slot_Length>2.999999999999989 mm</Slot_Length>
<Specify_Separation>No</Specify_Separation>
<Width_Separation>2.999999999999989 mm</Width_Separation>
<Length_Separation>2.999999999999989 mm</Length_Separation>
<Controllable>Yes</Controllable>
<Open_Area_Option>Fixed</Open_Area_Option>
<Open_Area>64 %</Open_Area>
<Controller_Response>Direct</Controller_Response>
<Minimum_Open_Area>64 %</Minimum_Open_Area>
<Maximum_Open_Area>64 %</Maximum_Open_Area>
<Controller_Response_Curve>0,0, 100,100 &lt;%,%&gt;</Controller_Response_Curve>
<Use_Internal_Controller>No</Use_Internal_Controller>
<Internal_SlottedController/>
<External_SlottedController/>
<Estimated_Open_Area>64 %</Estimated_Open_Area>
<Straighten_Flow>Yes</Straighten_Flow>
<Width_Directionality>Normal</Width_Directionality>
<Width_Angle>0 degrees</Width_Angle>
<Minimum_Open_Area_Width_Angle>0 degrees</Minimum_Open_Area_Width_Angle>
<Maximum_Open_Area_Width_Angle>0 degrees</Maximum_Open_Area_Width_Angle>
<Length_Directionality>Normal</Length_Directionality>
<Length_Angle>0 degrees</Length_Angle>
<Minimum_Open_Area_Length_Angle>0 degrees</Minimum_Open_Area_Length_Angle>
<Maximum_Open_Area_Length_Angle>0 degrees</Maximum_Open_Area_Length_Angle>
</Slotted_Details>
<Mesh_Details>
<Strand_Diameter>2.999999999999989 mm</Strand_Diameter>
<Specify_Separation>No</Specify_Separation>
<Width_Separation>2.999999999999989 mm</Width_Separation>
<Length_Separation>2.999999999999989 mm</Length_Separation>
<Open_Area>64 %</Open_Area>
<Estimated_Open_Area>64 %</Estimated_Open_Area>
</Mesh_Details>
</Construction>
<ResultVolumeLink/>
<Sensors/>
<Display_Options>
<Colour>180,180,180</Colour>
<EnableUseMaterialColour>No</EnableUseMaterialColour>
<Use_This_Colour>Yes</Use_This_Colour>
<Secondary_Colour>180,180,180</Secondary_Colour>
<Basic_Render_Style>Solid,Wireframe,Solid Outlined,Textured,Transparent,Invisible</Basic_Render_Style>
<Render_Style>Wireframe</Render_Style>
<Transparency>70 %</Transparency>
<Variable>Temperature</Variable>
<Show_Computational_Shape>No</Show_Computational_Shape>
<Data_Type>Regions</Data_Type>
<Plot_Type>Variation Plot Smooth</Plot_Type>
<Show_Grid>No</Show_Grid>
<Target_Variable>Temperature</Target_Variable>
<Hidden>No</Hidden>
</Display_Options>
<StreamPlot/>
<Simulation_Results>
<Through_Flow>
<Net_Flow>0 m^3/s</Net_Flow>
</Through_Flow>
<Heat_Flow>
<Positive_Heat_Flow>0 W</Positive_Heat_Flow>
<Negative_Heat_Flow>0 W</Negative_Heat_Flow>
<Net_Heat_Flow>0 W</Net_Heat_Flow>
</Heat_Flow>
<Contamination_In>
<Solved_Contaminants>0
</Solved_Contaminants>
</Contamination_In>
<Contamination_Out>
<Solved_Contaminants>0
</Solved_Contaminants>
</Contamination_Out>
</Simulation_Results>
</Obstruction_Hole>
</Holes>
<Faces/>
<Sensors/>
<ElectricalBoundaries/>
<Terminals/>
<TerminalLink/>
<Display_Options>
<Colour>180,180,180</Colour>
<EnableUseMaterialColour>Yes</EnableUseMaterialColour>
<Use_This_Colour>No</Use_This_Colour>
<Secondary_Colour>180,180,180</Secondary_Colour>
<Basic_Render_Style>Solid,Wireframe,Solid Outlined,Textured,Transparent,Invisible</Basic_Render_Style>
<Render_Style>Solid Outlined</Render_Style>
<Transparency>70 %</Transparency>
<Variable>Temperature</Variable>
<Show_Computational_Shape>Yes</Show_Computational_Shape>
<Data_Type>Geometry</Data_Type>
<Plot_Type>Variation Plot Smooth</Plot_Type>
<Show_Grid>No</Show_Grid>
<Target_Variable>Surface Temperature</Target_Variable>
<Hidden>No</Hidden>
</Display_Options>
<Grid_Controls>
<Grid_Control id="45995-47701">
<Installed>Yes</Installed>
<Identification>
<Name>Grid Control 1</Name>
</Identification>
<Geometry>
<Direction>Geometry Based</Direction>
<Size_From_Parent>Yes</Size_From_Parent>
<Size>0 mm</Size>
<Width>0 mm</Width>
<Height>0 mm</Height>
<Depth>0 mm</Depth>
</Geometry>
<Placement>
<Location>0 mm</Location>
<X_Location>0 mm</X_Location>
<Y_Location>0 mm</Y_Location>
<Z_Location>0 mm</Z_Location>
</Placement>
<Construction>
<Construction_1D>
<Extra_Grid_Type>Number Of Cells</Extra_Grid_Type>
<Line_Offset>0 mm</Line_Offset>
<Maximum_Size>101.6 mm</Maximum_Size>
<Number_Of_Cells>5</Number_Of_Cells>
<Start_Size>10 mm</Start_Size>
<Multiplier>2</Multiplier>
<Exact_Grid_Lines>No</Exact_Grid_Lines>
</Construction_1D>
<X_Construction>
<Extra_Grid_Type>Number Of Cells</Extra_Grid_Type>
<Maximum_Size>10 mm</Maximum_Size>
<Number_Of_Cells>5</Number_Of_Cells>
<Start_Size>10 mm</Start_Size>
<Multiplier>2</Multiplier>
<Exact_Grid_Lines>No</Exact_Grid_Lines>
</X_Construction>
<Y_Construction>
<Extra_Grid_Type>Number Of Cells</Extra_Grid_Type>
<Maximum_Size>10 mm</Maximum_Size>
<Number_Of_Cells>5</Number_Of_Cells>
<Start_Size>10 mm</Start_Size>
<Multiplier>2</Multiplier>
<Exact_Grid_Lines>No</Exact_Grid_Lines>
</Y_Construction>
<Z_Construction>
<Extra_Grid_Type>Number Of Cells</Extra_Grid_Type>
<Maximum_Size>10 mm</Maximum_Size>
<Number_Of_Cells>5</Number_Of_Cells>
<Start_Size>10 mm</Start_Size>
<Multiplier>2</Multiplier>
<Exact_Grid_Lines>No</Exact_Grid_Lines>
</Z_Construction>
<Geometry_Based_Construction>
<Apply_To_Solid>Yes</Apply_To_Solid>
<Maximum_Size_In_Solid>2 mm</Maximum_Size_In_Solid>
<Apply_To_Fluid>No</Apply_To_Fluid>
<Maximum_Size_In_Fluid>10 mm</Maximum_Size_In_Fluid>
<Inflate_Into_Fluid>Yes</Inflate_Into_Fluid>
<Inflation_Settings>
<Apply_To_Inside_Fluid>Yes</Apply_To_Inside_Fluid>
<Maximum_Size_In_Inside_Fluid>0.5 mm</Maximum_Size_In_Inside_Fluid>
<Extent_In_Inside_Fluid>2 mm</Extent_In_Inside_Fluid>
<Apply_To_Outside_Fluid>Yes</Apply_To_Outside_Fluid>
<Maximum_Size_In_Outside_Fluid>0.5 mm</Maximum_Size_In_Outside_Fluid>
<Extent_In_Outside_Fluid>2 mm</Extent_In_Outside_Fluid>
</Inflation_Settings>
</Geometry_Based_Construction>
</Construction>
<Display_Options>
<Auto_Colour>Yes</Auto_Colour>
<Colour>0,0,0</Colour>
<Hidden>No</Hidden>
</Display_Options>
</Grid_Control>
</Grid_Controls>
<Simulation_Results>
<Heat_Fluxes>
<ShowPolygonSides>No</ShowPolygonSides>
<ShowCuboidSides>No</ShowCuboidSides>
</Heat_Fluxes>
<Joule_Heating>0 W</Joule_Heating>
<Temperature_Dependent_Heating>0 W</Temperature_Dependent_Heating>
<Controlling_Temperature>0 C</Controlling_Temperature>
<Embedded_Heating>0 W</Embedded_Heating>
<Solar_Heating>0 W</Solar_Heating>
</Simulation_Results>
<Object_Shape_Definition>
<Shape_Type>Cuboid</Shape_Type>
<Thin_Shape>No</Thin_Shape>
<With_Holes>Yes</With_Holes>
</Object_Shape_Definition>
<Push_Pins/>
</Solid_Obstruction>
<Solid_Obstruction id="45995-47702">
<Installed>Yes</Installed>
<Identification>
<Name>CASE_UPPER_COVER</Name>
<Layer_Type>Chassis</Layer_Type>
<Type>Substrate</Type>
</Identification>
<Geometry>
<Shape>Cuboid</Shape>
<Available_Sides>Front,Rear,Top,Bottom,Left,Right</Available_Sides>
<Modelling_Level>Thick</Modelling_Level>
<Collapse_Direction>Thinnest</Collapse_Direction>
<Thickness>0 mm</Thickness>
<Height>2 mm</Height>
<Width>100 mm</Width>
<Depth>90 mm</Depth>
<Diameter>20 mm</Diameter>
<Hole_Direction>Z</Hole_Direction>
<Solid/>
<Realign_Origin>No</Realign_Origin>
<Ignore_Collision_Detection>No</Ignore_Collision_Detection>
<Grid>
<Minimum_Cell_Size>0.1 mm</Minimum_Cell_Size>
<Minimum_Number_Of_Cells>
<Width_Direction>5</Width_Direction>
<Depth_Direction>5</Depth_Direction>
</Minimum_Number_Of_Cells>
</Grid>
<Surface_Area>18760 mm^2</Surface_Area>
</Geometry>
<Placement>
<Origin_Point>Low Centre</Origin_Point>
<X_Location>500 mm</X_Location>
<Y_Location>519.6 mm</Y_Location>
<Z_Location>500 mm</Z_Location>
<X_Origin>0 mm</X_Origin>
<Y_Origin>0 mm</Y_Origin>
<Z_Origin>0 mm</Z_Origin>
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
<Weight>0 kg</Weight>
</Construction>
<Cooling>
<Modelling_Detail>Full</Modelling_Detail>
<Heat_Conduction_Grid>Yes</Heat_Conduction_Grid>
<Heat_Option>Total Heat</Heat_Option>
<Power_Specification>Total Power</Power_Specification>
<Temperature_Dependent_Heat_Dissipation>No</Temperature_Dependent_Heat_Dissipation>
<Time_Dependent_Heat_Dissipation>No</Time_Dependent_Heat_Dissipation>
<Temperature>15.5555555555556 C</Temperature>
<Temperature_Curve>0,20, 100,20 &lt;s,C&gt;</Temperature_Curve>
<Temperature_Dependent_Power>No</Temperature_Dependent_Power>
<Heat_Dissipated>0 W</Heat_Dissipated>
<Heat_Dissipated_Curve>0,0, 100,0 &lt;s,W&gt;</Heat_Dissipated_Curve>
<Heat_Dissipated_Temperature_Curve>20,0, 50,0 &lt;C,W&gt;</Heat_Dissipated_Temperature_Curve>
<Heat_Dissipated_Temperature_Multiple_Curves>
<Initial_Curve_Id>0</Initial_Curve_Id>
<Current_Curve_Id>0</Current_Curve_Id>
<Thermal_Design_Power_Temperature_Curve_Array>10,0,1000, 150,0|30,0,1000, 150,0 &lt;C,C,W&gt;</Thermal_Design_Power_Temperature_Curve_Array>
<Curve_Names>0
</Curve_Names>
<Transitions>0
</Transitions>
</Heat_Dissipated_Temperature_Multiple_Curves>
<Heat_Dissipation_Curve_Hysteresis>0 C</Heat_Dissipation_Curve_Hysteresis>
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
<Controlling_Temperature>Solid</Controlling_Temperature>
<Temperature_Dependence_Sensors/>
<Sensor_Treatment>Weighted Average</Sensor_Treatment>
<Sensor_Weights> : </Sensor_Weights>
<User_Defined_Heat_Transfer>
<Fluid_Heat_Transfer_Option>From Solution</Fluid_Heat_Transfer_Option>
<Fluid_Heat_Transfer_Coefficient>10 W/(m^2K)</Fluid_Heat_Transfer_Coefficient>
<Solid_Heat_Transfer_Option>From Solution</Solid_Heat_Transfer_Option>
<Solid_Heat_Transfer_Coefficient>10 W/(m^2K)</Solid_Heat_Transfer_Coefficient>
</User_Defined_Heat_Transfer>
<Allow_Boundary_Cell_Reconstruction>Yes</Allow_Boundary_Cell_Reconstruction>
<Surface_Roughness>
<Roughness_Type>Whole Range</Roughness_Type>
<Roughness_Height>0 mm</Roughness_Height>
<Roughness_Length>0 mm</Roughness_Length>
<Roughness_Constant>0.5</Roughness_Constant>
</Surface_Roughness>
<Wall_Function>Standard</Wall_Function>
<Subdivide_Surfaces_For_Radiation>Yes</Subdivide_Surfaces_For_Radiation>
<Surface_Subdivision_Size>10 mm</Surface_Subdivision_Size>
<Display_in_CFD_Progress>Auto</Display_in_CFD_Progress>
<Contributes_to_Termination_Criteria>Yes</Contributes_to_Termination_Criteria>
<MaterialLink>45995-47709 </MaterialLink>
<Material_Alignment>XYZ</Material_Alignment>
<Material_Normal>X</Material_Normal>
<Calculated_Weight>50.814 g</Calculated_Weight>
</Cooling>
<Electric_Current>
<Time_Dependent_Current>No</Time_Dependent_Current>
<Current>0 mA</Current>
<Current_Curve>0,0, 100,0 &lt;s,mA&gt;</Current_Curve>
<Current_Direction>Longest</Current_Direction>
</Electric_Current>
<TIMs/>
<Heat_Sources/>
<Holes/>
<Faces/>
<Sensors/>
<ElectricalBoundaries/>
<Terminals/>
<TerminalLink/>
<Display_Options>
<Colour>180,180,180</Colour>
<EnableUseMaterialColour>Yes</EnableUseMaterialColour>
<Use_This_Colour>No</Use_This_Colour>
<Secondary_Colour>180,180,180</Secondary_Colour>
<Basic_Render_Style>Solid,Wireframe,Solid Outlined,Textured,Transparent,Invisible</Basic_Render_Style>
<Render_Style>Solid Outlined</Render_Style>
<Transparency>70 %</Transparency>
<Variable>Temperature</Variable>
<Show_Computational_Shape>Yes</Show_Computational_Shape>
<Data_Type>Geometry</Data_Type>
<Plot_Type>Variation Plot Smooth</Plot_Type>
<Show_Grid>No</Show_Grid>
<Target_Variable>Surface Temperature</Target_Variable>
<Hidden>No</Hidden>
</Display_Options>
<Grid_Controls>
<Grid_Control id="45995-47703">
<Installed>Yes</Installed>
<Identification>
<Name>Grid Control 1</Name>
</Identification>
<Geometry>
<Direction>Geometry Based</Direction>
<Size_From_Parent>Yes</Size_From_Parent>
<Size>0 mm</Size>
<Width>0 mm</Width>
<Height>0 mm</Height>
<Depth>0 mm</Depth>
</Geometry>
<Placement>
<Location>0 mm</Location>
<X_Location>0 mm</X_Location>
<Y_Location>0 mm</Y_Location>
<Z_Location>0 mm</Z_Location>
</Placement>
<Construction>
<Construction_1D>
<Extra_Grid_Type>Number Of Cells</Extra_Grid_Type>
<Line_Offset>0 mm</Line_Offset>
<Maximum_Size>101.6 mm</Maximum_Size>
<Number_Of_Cells>5</Number_Of_Cells>
<Start_Size>10 mm</Start_Size>
<Multiplier>2</Multiplier>
<Exact_Grid_Lines>No</Exact_Grid_Lines>
</Construction_1D>
<X_Construction>
<Extra_Grid_Type>Number Of Cells</Extra_Grid_Type>
<Maximum_Size>10 mm</Maximum_Size>
<Number_Of_Cells>5</Number_Of_Cells>
<Start_Size>10 mm</Start_Size>
<Multiplier>2</Multiplier>
<Exact_Grid_Lines>No</Exact_Grid_Lines>
</X_Construction>
<Y_Construction>
<Extra_Grid_Type>Number Of Cells</Extra_Grid_Type>
<Maximum_Size>10 mm</Maximum_Size>
<Number_Of_Cells>5</Number_Of_Cells>
<Start_Size>10 mm</Start_Size>
<Multiplier>2</Multiplier>
<Exact_Grid_Lines>No</Exact_Grid_Lines>
</Y_Construction>
<Z_Construction>
<Extra_Grid_Type>Number Of Cells</Extra_Grid_Type>
<Maximum_Size>10 mm</Maximum_Size>
<Number_Of_Cells>5</Number_Of_Cells>
<Start_Size>10 mm</Start_Size>
<Multiplier>2</Multiplier>
<Exact_Grid_Lines>No</Exact_Grid_Lines>
</Z_Construction>
<Geometry_Based_Construction>
<Apply_To_Solid>Yes</Apply_To_Solid>
<Maximum_Size_In_Solid>2 mm</Maximum_Size_In_Solid>
<Apply_To_Fluid>No</Apply_To_Fluid>
<Maximum_Size_In_Fluid>10 mm</Maximum_Size_In_Fluid>
<Inflate_Into_Fluid>Yes</Inflate_Into_Fluid>
<Inflation_Settings>
<Apply_To_Inside_Fluid>Yes</Apply_To_Inside_Fluid>
<Maximum_Size_In_Inside_Fluid>0.5 mm</Maximum_Size_In_Inside_Fluid>
<Extent_In_Inside_Fluid>2 mm</Extent_In_Inside_Fluid>
<Apply_To_Outside_Fluid>Yes</Apply_To_Outside_Fluid>
<Maximum_Size_In_Outside_Fluid>0.5 mm</Maximum_Size_In_Outside_Fluid>
<Extent_In_Outside_Fluid>2 mm</Extent_In_Outside_Fluid>
</Inflation_Settings>
</Geometry_Based_Construction>
</Construction>
<Display_Options>
<Auto_Colour>Yes</Auto_Colour>
<Colour>0,0,0</Colour>
<Hidden>No</Hidden>
</Display_Options>
</Grid_Control>
</Grid_Controls>
<Simulation_Results>
<Heat_Fluxes>
<ShowPolygonSides>No</ShowPolygonSides>
<ShowCuboidSides>No</ShowCuboidSides>
</Heat_Fluxes>
<Joule_Heating>0 W</Joule_Heating>
<Temperature_Dependent_Heating>0 W</Temperature_Dependent_Heating>
<Controlling_Temperature>0 C</Controlling_Temperature>
<Embedded_Heating>0 W</Embedded_Heating>
<Solar_Heating>0 W</Solar_Heating>
</Simulation_Results>
<Object_Shape_Definition>
<Shape_Type>Cuboid</Shape_Type>
<Thin_Shape>No</Thin_Shape>
<With_Holes>No</With_Holes>
</Object_Shape_Definition>
<Push_Pins/>
</Solid_Obstruction>
<Solid_Obstruction id="45995-47704">
<Installed>Yes</Installed>
<Identification>
<Name>CASE_Contact</Name>
<Layer_Type>Chassis</Layer_Type>
<Type>Substrate</Type>
</Identification>
<Geometry>
<Shape>Cuboid</Shape>
<Available_Sides>Front,Rear,Top,Bottom,Left,Right</Available_Sides>
<Modelling_Level>Thick</Modelling_Level>
<Collapse_Direction>Thinnest</Collapse_Direction>
<Thickness>0 mm</Thickness>
<Height>5 mm</Height>
<Width>4 mm</Width>
<Depth>5 mm</Depth>
<Diameter>20 mm</Diameter>
<Hole_Direction>Z</Hole_Direction>
<Solid/>
<Realign_Origin>No</Realign_Origin>
<Ignore_Collision_Detection>No</Ignore_Collision_Detection>
<Grid>
<Minimum_Cell_Size>0.1 mm</Minimum_Cell_Size>
<Minimum_Number_Of_Cells>
<Width_Direction>5</Width_Direction>
<Depth_Direction>5</Depth_Direction>
</Minimum_Number_Of_Cells>
</Grid>
<Surface_Area>130 mm^2</Surface_Area>
</Geometry>
<Placement>
<Origin_Point>Low Corner</Origin_Point>
<X_Location>470 mm</X_Location>
<Y_Location>514.6 mm</Y_Location>
<Z_Location>505 mm</Z_Location>
<X_Origin>0 mm</X_Origin>
<Y_Origin>0 mm</Y_Origin>
<Z_Origin>0 mm</Z_Origin>
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
<Weight>0 kg</Weight>
</Construction>
<Cooling>
<Modelling_Detail>Full</Modelling_Detail>
<Heat_Conduction_Grid>Yes</Heat_Conduction_Grid>
<Heat_Option>Total Heat</Heat_Option>
<Power_Specification>Total Power</Power_Specification>
<Temperature_Dependent_Heat_Dissipation>No</Temperature_Dependent_Heat_Dissipation>
<Time_Dependent_Heat_Dissipation>No</Time_Dependent_Heat_Dissipation>
<Temperature>15.5555555555556 C</Temperature>
<Temperature_Curve>0,20, 100,20 &lt;s,C&gt;</Temperature_Curve>
<Temperature_Dependent_Power>No</Temperature_Dependent_Power>
<Heat_Dissipated>0 W</Heat_Dissipated>
<Heat_Dissipated_Curve>0,0, 100,0 &lt;s,W&gt;</Heat_Dissipated_Curve>
<Heat_Dissipated_Temperature_Curve>20,0, 50,0 &lt;C,W&gt;</Heat_Dissipated_Temperature_Curve>
<Heat_Dissipated_Temperature_Multiple_Curves>
<Initial_Curve_Id>0</Initial_Curve_Id>
<Current_Curve_Id>0</Current_Curve_Id>
<Thermal_Design_Power_Temperature_Curve_Array>10,0,1000, 150,0|30,0,1000, 150,0 &lt;C,C,W&gt;</Thermal_Design_Power_Temperature_Curve_Array>
<Curve_Names>0
</Curve_Names>
<Transitions>0
</Transitions>
</Heat_Dissipated_Temperature_Multiple_Curves>
<Heat_Dissipation_Curve_Hysteresis>0 C</Heat_Dissipation_Curve_Hysteresis>
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
<Controlling_Temperature>Solid</Controlling_Temperature>
<Temperature_Dependence_Sensors/>
<Sensor_Treatment>Weighted Average</Sensor_Treatment>
<Sensor_Weights> : </Sensor_Weights>
<User_Defined_Heat_Transfer>
<Fluid_Heat_Transfer_Option>From Solution</Fluid_Heat_Transfer_Option>
<Fluid_Heat_Transfer_Coefficient>10 W/(m^2K)</Fluid_Heat_Transfer_Coefficient>
<Solid_Heat_Transfer_Option>From Solution</Solid_Heat_Transfer_Option>
<Solid_Heat_Transfer_Coefficient>10 W/(m^2K)</Solid_Heat_Transfer_Coefficient>
</User_Defined_Heat_Transfer>
<Allow_Boundary_Cell_Reconstruction>Yes</Allow_Boundary_Cell_Reconstruction>
<Surface_Roughness>
<Roughness_Type>Whole Range</Roughness_Type>
<Roughness_Height>0 mm</Roughness_Height>
<Roughness_Length>0 mm</Roughness_Length>
<Roughness_Constant>0.5</Roughness_Constant>
</Surface_Roughness>
<Wall_Function>Standard</Wall_Function>
<Subdivide_Surfaces_For_Radiation>Yes</Subdivide_Surfaces_For_Radiation>
<Surface_Subdivision_Size>10 mm</Surface_Subdivision_Size>
<Display_in_CFD_Progress>Auto</Display_in_CFD_Progress>
<Contributes_to_Termination_Criteria>Yes</Contributes_to_Termination_Criteria>
<MaterialLink>45995-47709 </MaterialLink>
<Material_Alignment>XYZ</Material_Alignment>
<Material_Normal>X</Material_Normal>
<Calculated_Weight>0.2823 g</Calculated_Weight>
</Cooling>
<Electric_Current>
<Time_Dependent_Current>No</Time_Dependent_Current>
<Current>0 mA</Current>
<Current_Curve>0,0, 100,0 &lt;s,mA&gt;</Current_Curve>
<Current_Direction>Longest</Current_Direction>
</Electric_Current>
<TIMs/>
<Heat_Sources/>
<Holes/>
<Faces/>
<Sensors/>
<ElectricalBoundaries/>
<Terminals/>
<TerminalLink/>
<Display_Options>
<Colour>180,180,180</Colour>
<EnableUseMaterialColour>Yes</EnableUseMaterialColour>
<Use_This_Colour>No</Use_This_Colour>
<Secondary_Colour>180,180,180</Secondary_Colour>
<Basic_Render_Style>Solid,Wireframe,Solid Outlined,Textured,Transparent,Invisible</Basic_Render_Style>
<Render_Style>Solid Outlined</Render_Style>
<Transparency>70 %</Transparency>
<Variable>Temperature</Variable>
<Show_Computational_Shape>Yes</Show_Computational_Shape>
<Data_Type>Geometry</Data_Type>
<Plot_Type>Variation Plot Smooth</Plot_Type>
<Show_Grid>No</Show_Grid>
<Target_Variable>Surface Temperature</Target_Variable>
<Hidden>No</Hidden>
</Display_Options>
<Grid_Controls>
<Grid_Control id="45995-47705">
<Installed>Yes</Installed>
<Identification>
<Name>Grid Control 1</Name>
</Identification>
<Geometry>
<Direction>Geometry Based</Direction>
<Size_From_Parent>Yes</Size_From_Parent>
<Size>0 mm</Size>
<Width>0 mm</Width>
<Height>0 mm</Height>
<Depth>0 mm</Depth>
</Geometry>
<Placement>
<Location>0 mm</Location>
<X_Location>0 mm</X_Location>
<Y_Location>0 mm</Y_Location>
<Z_Location>0 mm</Z_Location>
</Placement>
<Construction>
<Construction_1D>
<Extra_Grid_Type>Number Of Cells</Extra_Grid_Type>
<Line_Offset>0 mm</Line_Offset>
<Maximum_Size>101.6 mm</Maximum_Size>
<Number_Of_Cells>5</Number_Of_Cells>
<Start_Size>10 mm</Start_Size>
<Multiplier>2</Multiplier>
<Exact_Grid_Lines>No</Exact_Grid_Lines>
</Construction_1D>
<X_Construction>
<Extra_Grid_Type>Number Of Cells</Extra_Grid_Type>
<Maximum_Size>10 mm</Maximum_Size>
<Number_Of_Cells>5</Number_Of_Cells>
<Start_Size>10 mm</Start_Size>
<Multiplier>2</Multiplier>
<Exact_Grid_Lines>No</Exact_Grid_Lines>
</X_Construction>
<Y_Construction>
<Extra_Grid_Type>Number Of Cells</Extra_Grid_Type>
<Maximum_Size>10 mm</Maximum_Size>
<Number_Of_Cells>5</Number_Of_Cells>
<Start_Size>10 mm</Start_Size>
<Multiplier>2</Multiplier>
<Exact_Grid_Lines>No</Exact_Grid_Lines>
</Y_Construction>
<Z_Construction>
<Extra_Grid_Type>Number Of Cells</Extra_Grid_Type>
<Maximum_Size>10 mm</Maximum_Size>
<Number_Of_Cells>5</Number_Of_Cells>
<Start_Size>10 mm</Start_Size>
<Multiplier>2</Multiplier>
<Exact_Grid_Lines>No</Exact_Grid_Lines>
</Z_Construction>
<Geometry_Based_Construction>
<Apply_To_Solid>Yes</Apply_To_Solid>
<Maximum_Size_In_Solid>2 mm</Maximum_Size_In_Solid>
<Apply_To_Fluid>No</Apply_To_Fluid>
<Maximum_Size_In_Fluid>10 mm</Maximum_Size_In_Fluid>
<Inflate_Into_Fluid>Yes</Inflate_Into_Fluid>
<Inflation_Settings>
<Apply_To_Inside_Fluid>Yes</Apply_To_Inside_Fluid>
<Maximum_Size_In_Inside_Fluid>0.5 mm</Maximum_Size_In_Inside_Fluid>
<Extent_In_Inside_Fluid>2 mm</Extent_In_Inside_Fluid>
<Apply_To_Outside_Fluid>Yes</Apply_To_Outside_Fluid>
<Maximum_Size_In_Outside_Fluid>0.5 mm</Maximum_Size_In_Outside_Fluid>
<Extent_In_Outside_Fluid>2 mm</Extent_In_Outside_Fluid>
</Inflation_Settings>
</Geometry_Based_Construction>
</Construction>
<Display_Options>
<Auto_Colour>Yes</Auto_Colour>
<Colour>0,0,0</Colour>
<Hidden>No</Hidden>
</Display_Options>
</Grid_Control>
</Grid_Controls>
<Simulation_Results>
<Heat_Fluxes>
<ShowPolygonSides>No</ShowPolygonSides>
<ShowCuboidSides>No</ShowCuboidSides>
</Heat_Fluxes>
<Joule_Heating>0 W</Joule_Heating>
<Temperature_Dependent_Heating>0 W</Temperature_Dependent_Heating>
<Controlling_Temperature>0 C</Controlling_Temperature>
<Embedded_Heating>0 W</Embedded_Heating>
<Solar_Heating>0 W</Solar_Heating>
</Simulation_Results>
<Object_Shape_Definition>
<Shape_Type>Cuboid</Shape_Type>
<Thin_Shape>No</Thin_Shape>
<With_Holes>No</With_Holes>
</Object_Shape_Definition>
<Push_Pins/>
</Solid_Obstruction>
<Solid_Obstruction id="45995-47706">
<Installed>Yes</Installed>
<Identification>
<Name>Connector</Name>
<Layer_Type>Chassis</Layer_Type>
<Type>Substrate</Type>
</Identification>
<Geometry>
<Shape>Cuboid</Shape>
<Available_Sides>Front,Rear,Top,Bottom,Left,Right</Available_Sides>
<Modelling_Level>Thick</Modelling_Level>
<Collapse_Direction>Thinnest</Collapse_Direction>
<Thickness>0 mm</Thickness>
<Height>7 mm</Height>
<Width>4 mm</Width>
<Depth>5 mm</Depth>
<Diameter>20 mm</Diameter>
<Hole_Direction>Z</Hole_Direction>
<Solid/>
<Realign_Origin>No</Realign_Origin>
<Ignore_Collision_Detection>No</Ignore_Collision_Detection>
<Grid>
<Minimum_Cell_Size>0.1 mm</Minimum_Cell_Size>
<Minimum_Number_Of_Cells>
<Width_Direction>5</Width_Direction>
<Depth_Direction>5</Depth_Direction>
</Minimum_Number_Of_Cells>
</Grid>
<Surface_Area>166 mm^2</Surface_Area>
</Geometry>
<Placement>
<Origin_Point>Low Centre</Origin_Point>
<X_Location>505 mm</X_Location>
<Y_Location>511.6 mm</Y_Location>
<Z_Location>520 mm</Z_Location>
<X_Origin>0 mm</X_Origin>
<Y_Origin>0 mm</Y_Origin>
<Z_Origin>0 mm</Z_Origin>
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
<Weight>0 kg</Weight>
</Construction>
<Cooling>
<Modelling_Detail>Full</Modelling_Detail>
<Heat_Conduction_Grid>Yes</Heat_Conduction_Grid>
<Heat_Option>Total Heat</Heat_Option>
<Power_Specification>Total Power</Power_Specification>
<Temperature_Dependent_Heat_Dissipation>No</Temperature_Dependent_Heat_Dissipation>
<Time_Dependent_Heat_Dissipation>No</Time_Dependent_Heat_Dissipation>
<Temperature>15.5555555555556 C</Temperature>
<Temperature_Curve>0,20, 100,20 &lt;s,C&gt;</Temperature_Curve>
<Temperature_Dependent_Power>No</Temperature_Dependent_Power>
<Heat_Dissipated>0 W</Heat_Dissipated>
<Heat_Dissipated_Curve>0,0, 100,0 &lt;s,W&gt;</Heat_Dissipated_Curve>
<Heat_Dissipated_Temperature_Curve>20,0, 50,0 &lt;C,W&gt;</Heat_Dissipated_Temperature_Curve>
<Heat_Dissipated_Temperature_Multiple_Curves>
<Initial_Curve_Id>0</Initial_Curve_Id>
<Current_Curve_Id>0</Current_Curve_Id>
<Thermal_Design_Power_Temperature_Curve_Array>10,0,1000, 150,0|30,0,1000, 150,0 &lt;C,C,W&gt;</Thermal_Design_Power_Temperature_Curve_Array>
<Curve_Names>0
</Curve_Names>
<Transitions>0
</Transitions>
</Heat_Dissipated_Temperature_Multiple_Curves>
<Heat_Dissipation_Curve_Hysteresis>0 C</Heat_Dissipation_Curve_Hysteresis>
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
<Controlling_Temperature>Solid</Controlling_Temperature>
<Temperature_Dependence_Sensors/>
<Sensor_Treatment>Weighted Average</Sensor_Treatment>
<Sensor_Weights> : </Sensor_Weights>
<User_Defined_Heat_Transfer>
<Fluid_Heat_Transfer_Option>From Solution</Fluid_Heat_Transfer_Option>
<Fluid_Heat_Transfer_Coefficient>10 W/(m^2K)</Fluid_Heat_Transfer_Coefficient>
<Solid_Heat_Transfer_Option>From Solution</Solid_Heat_Transfer_Option>
<Solid_Heat_Transfer_Coefficient>10 W/(m^2K)</Solid_Heat_Transfer_Coefficient>
</User_Defined_Heat_Transfer>
<Allow_Boundary_Cell_Reconstruction>Yes</Allow_Boundary_Cell_Reconstruction>
<Surface_Roughness>
<Roughness_Type>Whole Range</Roughness_Type>
<Roughness_Height>0 mm</Roughness_Height>
<Roughness_Length>0 mm</Roughness_Length>
<Roughness_Constant>0.5</Roughness_Constant>
</Surface_Roughness>
<Wall_Function>Standard</Wall_Function>
<Subdivide_Surfaces_For_Radiation>Yes</Subdivide_Surfaces_For_Radiation>
<Surface_Subdivision_Size>10 mm</Surface_Subdivision_Size>
<Display_in_CFD_Progress>Auto</Display_in_CFD_Progress>
<Contributes_to_Termination_Criteria>Yes</Contributes_to_Termination_Criteria>
<MaterialLink>45995-47719 </MaterialLink>
<Material_Alignment>XYZ</Material_Alignment>
<Material_Normal>X</Material_Normal>
<Calculated_Weight>0.182 g</Calculated_Weight>
</Cooling>
<Electric_Current>
<Time_Dependent_Current>No</Time_Dependent_Current>
<Current>0 mA</Current>
<Current_Curve>0,0, 100,0 &lt;s,mA&gt;</Current_Curve>
<Current_Direction>Longest</Current_Direction>
</Electric_Current>
<TIMs/>
<Heat_Sources/>
<Holes/>
<Faces/>
<Sensors/>
<ElectricalBoundaries/>
<Terminals/>
<TerminalLink/>
<Display_Options>
<Colour>180,180,180</Colour>
<EnableUseMaterialColour>Yes</EnableUseMaterialColour>
<Use_This_Colour>No</Use_This_Colour>
<Secondary_Colour>180,180,180</Secondary_Colour>
<Basic_Render_Style>Solid,Wireframe,Solid Outlined,Textured,Transparent,Invisible</Basic_Render_Style>
<Render_Style>Solid Outlined</Render_Style>
<Transparency>70 %</Transparency>
<Variable>Temperature</Variable>
<Show_Computational_Shape>Yes</Show_Computational_Shape>
<Data_Type>Geometry</Data_Type>
<Plot_Type>Variation Plot Smooth</Plot_Type>
<Show_Grid>No</Show_Grid>
<Target_Variable>Surface Temperature</Target_Variable>
<Hidden>No</Hidden>
</Display_Options>
<Grid_Controls>
<Grid_Control id="45995-47707">
<Installed>Yes</Installed>
<Identification>
<Name>Grid Control 1</Name>
</Identification>
<Geometry>
<Direction>Geometry Based</Direction>
<Size_From_Parent>Yes</Size_From_Parent>
<Size>0 mm</Size>
<Width>0 mm</Width>
<Height>0 mm</Height>
<Depth>0 mm</Depth>
</Geometry>
<Placement>
<Location>0 mm</Location>
<X_Location>0 mm</X_Location>
<Y_Location>0 mm</Y_Location>
<Z_Location>0 mm</Z_Location>
</Placement>
<Construction>
<Construction_1D>
<Extra_Grid_Type>Number Of Cells</Extra_Grid_Type>
<Line_Offset>0 mm</Line_Offset>
<Maximum_Size>101.6 mm</Maximum_Size>
<Number_Of_Cells>5</Number_Of_Cells>
<Start_Size>10 mm</Start_Size>
<Multiplier>2</Multiplier>
<Exact_Grid_Lines>No</Exact_Grid_Lines>
</Construction_1D>
<X_Construction>
<Extra_Grid_Type>Number Of Cells</Extra_Grid_Type>
<Maximum_Size>10 mm</Maximum_Size>
<Number_Of_Cells>5</Number_Of_Cells>
<Start_Size>10 mm</Start_Size>
<Multiplier>2</Multiplier>
<Exact_Grid_Lines>No</Exact_Grid_Lines>
</X_Construction>
<Y_Construction>
<Extra_Grid_Type>Number Of Cells</Extra_Grid_Type>
<Maximum_Size>10 mm</Maximum_Size>
<Number_Of_Cells>5</Number_Of_Cells>
<Start_Size>10 mm</Start_Size>
<Multiplier>2</Multiplier>
<Exact_Grid_Lines>No</Exact_Grid_Lines>
</Y_Construction>
<Z_Construction>
<Extra_Grid_Type>Number Of Cells</Extra_Grid_Type>
<Maximum_Size>10 mm</Maximum_Size>
<Number_Of_Cells>5</Number_Of_Cells>
<Start_Size>10 mm</Start_Size>
<Multiplier>2</Multiplier>
<Exact_Grid_Lines>No</Exact_Grid_Lines>
</Z_Construction>
<Geometry_Based_Construction>
<Apply_To_Solid>Yes</Apply_To_Solid>
<Maximum_Size_In_Solid>2 mm</Maximum_Size_In_Solid>
<Apply_To_Fluid>No</Apply_To_Fluid>
<Maximum_Size_In_Fluid>10 mm</Maximum_Size_In_Fluid>
<Inflate_Into_Fluid>Yes</Inflate_Into_Fluid>
<Inflation_Settings>
<Apply_To_Inside_Fluid>Yes</Apply_To_Inside_Fluid>
<Maximum_Size_In_Inside_Fluid>0.5 mm</Maximum_Size_In_Inside_Fluid>
<Extent_In_Inside_Fluid>2 mm</Extent_In_Inside_Fluid>
<Apply_To_Outside_Fluid>Yes</Apply_To_Outside_Fluid>
<Maximum_Size_In_Outside_Fluid>0.5 mm</Maximum_Size_In_Outside_Fluid>
<Extent_In_Outside_Fluid>2 mm</Extent_In_Outside_Fluid>
</Inflation_Settings>
</Geometry_Based_Construction>
</Construction>
<Display_Options>
<Auto_Colour>Yes</Auto_Colour>
<Colour>0,0,0</Colour>
<Hidden>No</Hidden>
</Display_Options>
</Grid_Control>
</Grid_Controls>
<Simulation_Results>
<Heat_Fluxes>
<ShowPolygonSides>No</ShowPolygonSides>
<ShowCuboidSides>No</ShowCuboidSides>
</Heat_Fluxes>
<Joule_Heating>0 W</Joule_Heating>
<Temperature_Dependent_Heating>0 W</Temperature_Dependent_Heating>
<Controlling_Temperature>0 C</Controlling_Temperature>
<Embedded_Heating>0 W</Embedded_Heating>
<Solar_Heating>0 W</Solar_Heating>
</Simulation_Results>
<Object_Shape_Definition>
<Shape_Type>Cuboid</Shape_Type>
<Thin_Shape>No</Thin_Shape>
<With_Holes>No</With_Holes>
</Object_Shape_Definition>
<Push_Pins/>
</Solid_Obstruction>
</SolidObstructions>
<PerforatedObstructions/>
<PorousObstructions/>
<GroupObstructions/>
<Sensors/>
<Controllers/>
<EquipmentLink/>
<ChassisLink/>
<ResultVolumes/>
<ResultFaces/>
<Heat_Sources/>
<Grid_Controls>
<Grid_Control id="45995-47708">
<Installed>Yes</Installed>
<Identification>
<Name>Grid Control - Chassis</Name>
</Identification>
<Geometry>
<Direction>3D</Direction>
<Size_From_Parent>No</Size_From_Parent>
<Size>1000 mm</Size>
<Width>300 mm</Width>
<Height>300 mm</Height>
<Depth>300 mm</Depth>
</Geometry>
<Placement>
<Location>0 mm</Location>
<X_Location>350 mm</X_Location>
<Y_Location>350 mm</Y_Location>
<Z_Location>350 mm</Z_Location>
</Placement>
<Construction>
<Construction_1D>
<Extra_Grid_Type>Number Of Cells</Extra_Grid_Type>
<Line_Offset>0 mm</Line_Offset>
<Maximum_Size>101.6 mm</Maximum_Size>
<Number_Of_Cells>5</Number_Of_Cells>
<Start_Size>10 mm</Start_Size>
<Multiplier>2</Multiplier>
<Exact_Grid_Lines>No</Exact_Grid_Lines>
</Construction_1D>
<X_Construction>
<Extra_Grid_Type>Maximum Size</Extra_Grid_Type>
<Maximum_Size>5 mm</Maximum_Size>
<Number_Of_Cells>5</Number_Of_Cells>
<Start_Size>10 mm</Start_Size>
<Multiplier>2</Multiplier>
<Exact_Grid_Lines>No</Exact_Grid_Lines>
</X_Construction>
<Y_Construction>
<Extra_Grid_Type>Maximum Size</Extra_Grid_Type>
<Maximum_Size>5 mm</Maximum_Size>
<Number_Of_Cells>5</Number_Of_Cells>
<Start_Size>10 mm</Start_Size>
<Multiplier>2</Multiplier>
<Exact_Grid_Lines>No</Exact_Grid_Lines>
</Y_Construction>
<Z_Construction>
<Extra_Grid_Type>Maximum Size</Extra_Grid_Type>
<Maximum_Size>5 mm</Maximum_Size>
<Number_Of_Cells>5</Number_Of_Cells>
<Start_Size>10 mm</Start_Size>
<Multiplier>2</Multiplier>
<Exact_Grid_Lines>No</Exact_Grid_Lines>
</Z_Construction>
<Geometry_Based_Construction>
<Apply_To_Solid>Yes</Apply_To_Solid>
<Maximum_Size_In_Solid>10 mm</Maximum_Size_In_Solid>
<Apply_To_Fluid>No</Apply_To_Fluid>
<Maximum_Size_In_Fluid>10 mm</Maximum_Size_In_Fluid>
<Inflate_Into_Fluid>No</Inflate_Into_Fluid>
<Inflation_Settings>
<Apply_To_Inside_Fluid>Yes</Apply_To_Inside_Fluid>
<Maximum_Size_In_Inside_Fluid>10 mm</Maximum_Size_In_Inside_Fluid>
<Extent_In_Inside_Fluid>20 mm</Extent_In_Inside_Fluid>
<Apply_To_Outside_Fluid>Yes</Apply_To_Outside_Fluid>
<Maximum_Size_In_Outside_Fluid>10 mm</Maximum_Size_In_Outside_Fluid>
<Extent_In_Outside_Fluid>20 mm</Extent_In_Outside_Fluid>
</Inflation_Settings>
</Geometry_Based_Construction>
</Construction>
<Display_Options>
<Auto_Colour>Yes</Auto_Colour>
<Colour>0,0,0</Colour>
<Hidden>Yes</Hidden>
</Display_Options>
</Grid_Control>
</Grid_Controls>
<Simulation_Results>
<Heat_Flow>
<Heat_Flow_In>0 W</Heat_Flow_In>
<Heat_Flow_Out>0 W</Heat_Flow_Out>
</Heat_Flow>
</Simulation_Results>
<Exchange_Values/>
</Chassis>
</ChassisLink>
<Materials>
<Material id="45995-47709">
<Name>ADC12</Name>
<Conductivity>
<Type>Isotropic</Type>
<Option>Constant</Option>
<Value>92 W/(m K)</Value>
<Conductivity_Temperature_Curve>0,0.0261, 200,0.0261 &lt;C,W/(m K)&gt;</Conductivity_Temperature_Curve>
<Normal>1 W/(m K)</Normal>
<Planar>1 W/(m K)</Planar>
<K1>1 W/(m K)</K1>
<K2>1 W/(m K)</K2>
<K3>1 W/(m K)</K3>
</Conductivity>
<Density>
<Option>Constant</Option>
<Value>2823 kg/m^3</Value>
</Density>
<Specific_Heat>
<Option>Constant</Option>
<Value>963 J/(kg K)</Value>
<Specific_Heat_Temperature_Curve>0,1005, 200,1005 &lt;C,J/(kg K)&gt;</Specific_Heat_Temperature_Curve>
</Specific_Heat>
<Heat_Radiation_Properties>
<Transparent_To_Heat_Radiation>No</Transparent_To_Heat_Radiation>
<Surface_Emissivity>
<Value>0.18</Value>
</Surface_Emissivity>
</Heat_Radiation_Properties>
<Solar_Radiation_Properties>
<Solar_Reflectance>
<Value>0</Value>
</Solar_Reflectance>
<Transparent_To_Solar_Radiation>No</Transparent_To_Solar_Radiation>
<Use_Reference_Values>Yes</Use_Reference_Values>
<Solar_Absorptance>
<Value>0</Value>
</Solar_Absorptance>
<Reference_Thickness>
<Value>1000 mm</Value>
</Reference_Thickness>
<Solar_Attenuation_Coefficient>
<Value>0 1/m</Value>
</Solar_Attenuation_Coefficient>
</Solar_Radiation_Properties>
<Electrical_Conductivity>
<Option>Constant</Option>
<Value>0 S/m</Value>
<Electrical_Conductivity_Temperature_Curve>0,0, 100,0 &lt;C,S/m&gt;</Electrical_Conductivity_Temperature_Curve>
<Max_Value>10000000000 S/m</Max_Value>
</Electrical_Conductivity>
<Display_Options>
<Choose_Custom_Colour>No</Choose_Custom_Colour>
<Colour>255,255,255</Colour>
</Display_Options>
</Material>
<Material id="45995-47710">
<Name>ADC12_Coated</Name>
<Conductivity>
<Type>Isotropic</Type>
<Option>Constant</Option>
<Value>92 W/(m K)</Value>
<Conductivity_Temperature_Curve>0,0.0261, 200,0.0261 &lt;C,W/(m K)&gt;</Conductivity_Temperature_Curve>
<Normal>1 W/(m K)</Normal>
<Planar>1 W/(m K)</Planar>
<K1>1 W/(m K)</K1>
<K2>1 W/(m K)</K2>
<K3>1 W/(m K)</K3>
</Conductivity>
<Density>
<Option>Constant</Option>
<Value>2823 kg/m^3</Value>
</Density>
<Specific_Heat>
<Option>Constant</Option>
<Value>963 J/(kg K)</Value>
<Specific_Heat_Temperature_Curve>0,1005, 200,1005 &lt;C,J/(kg K)&gt;</Specific_Heat_Temperature_Curve>
</Specific_Heat>
<Heat_Radiation_Properties>
<Transparent_To_Heat_Radiation>No</Transparent_To_Heat_Radiation>
<Surface_Emissivity>
<Value>0.9</Value>
</Surface_Emissivity>
</Heat_Radiation_Properties>
<Solar_Radiation_Properties>
<Solar_Reflectance>
<Value>0</Value>
</Solar_Reflectance>
<Transparent_To_Solar_Radiation>No</Transparent_To_Solar_Radiation>
<Use_Reference_Values>Yes</Use_Reference_Values>
<Solar_Absorptance>
<Value>0</Value>
</Solar_Absorptance>
<Reference_Thickness>
<Value>1000 mm</Value>
</Reference_Thickness>
<Solar_Attenuation_Coefficient>
<Value>0 1/m</Value>
</Solar_Attenuation_Coefficient>
</Solar_Radiation_Properties>
<Electrical_Conductivity>
<Option>Constant</Option>
<Value>0 S/m</Value>
<Electrical_Conductivity_Temperature_Curve>0,0, 100,0 &lt;C,S/m&gt;</Electrical_Conductivity_Temperature_Curve>
<Max_Value>10000000000 S/m</Max_Value>
</Electrical_Conductivity>
<Display_Options>
<Choose_Custom_Colour>No</Choose_Custom_Colour>
<Colour>255,255,255</Colour>
</Display_Options>
</Material>
<Material id="45995-47711">
<Name>AL6061-O</Name>
<Conductivity>
<Type>Isotropic</Type>
<Option>Constant</Option>
<Value>180 W/(m K)</Value>
<Conductivity_Temperature_Curve>0,0.0261, 200,0.0261 &lt;C,W/(m K)&gt;</Conductivity_Temperature_Curve>
<Normal>1 W/(m K)</Normal>
<Planar>1 W/(m K)</Planar>
<K1>1 W/(m K)</K1>
<K2>1 W/(m K)</K2>
<K3>1 W/(m K)</K3>
</Conductivity>
<Density>
<Option>Constant</Option>
<Value>2700 kg/m^3</Value>
</Density>
<Specific_Heat>
<Option>Constant</Option>
<Value>896 J/(kg K)</Value>
<Specific_Heat_Temperature_Curve>0,1005, 200,1005 &lt;C,J/(kg K)&gt;</Specific_Heat_Temperature_Curve>
</Specific_Heat>
<Heat_Radiation_Properties>
<Transparent_To_Heat_Radiation>No</Transparent_To_Heat_Radiation>
<Surface_Emissivity>
<Value>0.1</Value>
</Surface_Emissivity>
</Heat_Radiation_Properties>
<Solar_Radiation_Properties>
<Solar_Reflectance>
<Value>0</Value>
</Solar_Reflectance>
<Transparent_To_Solar_Radiation>No</Transparent_To_Solar_Radiation>
<Use_Reference_Values>Yes</Use_Reference_Values>
<Solar_Absorptance>
<Value>0</Value>
</Solar_Absorptance>
<Reference_Thickness>
<Value>1000 mm</Value>
</Reference_Thickness>
<Solar_Attenuation_Coefficient>
<Value>0 1/m</Value>
</Solar_Attenuation_Coefficient>
</Solar_Radiation_Properties>
<Electrical_Conductivity>
<Option>Constant</Option>
<Value>0 S/m</Value>
<Electrical_Conductivity_Temperature_Curve>0,0, 100,0 &lt;C,S/m&gt;</Electrical_Conductivity_Temperature_Curve>
<Max_Value>10000000000 S/m</Max_Value>
</Electrical_Conductivity>
<Display_Options>
<Choose_Custom_Colour>No</Choose_Custom_Colour>
<Colour>255,255,255</Colour>
</Display_Options>
</Material>
<Material id="45995-47712">
<Name>AL6061-O_Coated</Name>
<Conductivity>
<Type>Isotropic</Type>
<Option>Constant</Option>
<Value>180 W/(m K)</Value>
<Conductivity_Temperature_Curve>0,0.0261, 200,0.0261 &lt;C,W/(m K)&gt;</Conductivity_Temperature_Curve>
<Normal>1 W/(m K)</Normal>
<Planar>1 W/(m K)</Planar>
<K1>1 W/(m K)</K1>
<K2>1 W/(m K)</K2>
<K3>1 W/(m K)</K3>
</Conductivity>
<Density>
<Option>Constant</Option>
<Value>2700 kg/m^3</Value>
</Density>
<Specific_Heat>
<Option>Constant</Option>
<Value>896 J/(kg K)</Value>
<Specific_Heat_Temperature_Curve>0,1005, 200,1005 &lt;C,J/(kg K)&gt;</Specific_Heat_Temperature_Curve>
</Specific_Heat>
<Heat_Radiation_Properties>
<Transparent_To_Heat_Radiation>No</Transparent_To_Heat_Radiation>
<Surface_Emissivity>
<Value>0.9</Value>
</Surface_Emissivity>
</Heat_Radiation_Properties>
<Solar_Radiation_Properties>
<Solar_Reflectance>
<Value>0</Value>
</Solar_Reflectance>
<Transparent_To_Solar_Radiation>No</Transparent_To_Solar_Radiation>
<Use_Reference_Values>Yes</Use_Reference_Values>
<Solar_Absorptance>
<Value>0</Value>
</Solar_Absorptance>
<Reference_Thickness>
<Value>1000 mm</Value>
</Reference_Thickness>
<Solar_Attenuation_Coefficient>
<Value>0 1/m</Value>
</Solar_Attenuation_Coefficient>
</Solar_Radiation_Properties>
<Electrical_Conductivity>
<Option>Constant</Option>
<Value>0 S/m</Value>
<Electrical_Conductivity_Temperature_Curve>0,0, 100,0 &lt;C,S/m&gt;</Electrical_Conductivity_Temperature_Curve>
<Max_Value>10000000000 S/m</Max_Value>
</Electrical_Conductivity>
<Display_Options>
<Choose_Custom_Colour>No</Choose_Custom_Colour>
<Colour>255,255,255</Colour>
</Display_Options>
</Material>
<Material id="45995-47713">
<Name>ALDC</Name>
<Conductivity>
<Type>Isotropic</Type>
<Option>Constant</Option>
<Value>109 W/(m K)</Value>
<Conductivity_Temperature_Curve>0,0.0261, 200,0.0261 &lt;C,W/(m K)&gt;</Conductivity_Temperature_Curve>
<Normal>1 W/(m K)</Normal>
<Planar>1 W/(m K)</Planar>
<K1>1 W/(m K)</K1>
<K2>1 W/(m K)</K2>
<K3>1 W/(m K)</K3>
</Conductivity>
<Density>
<Option>Constant</Option>
<Value>2750 kg/m^3</Value>
</Density>
<Specific_Heat>
<Option>Constant</Option>
<Value>960 J/(kg K)</Value>
<Specific_Heat_Temperature_Curve>0,1005, 200,1005 &lt;C,J/(kg K)&gt;</Specific_Heat_Temperature_Curve>
</Specific_Heat>
<Heat_Radiation_Properties>
<Transparent_To_Heat_Radiation>No</Transparent_To_Heat_Radiation>
<Surface_Emissivity>
<Value>0.18</Value>
</Surface_Emissivity>
</Heat_Radiation_Properties>
<Solar_Radiation_Properties>
<Solar_Reflectance>
<Value>0</Value>
</Solar_Reflectance>
<Transparent_To_Solar_Radiation>No</Transparent_To_Solar_Radiation>
<Use_Reference_Values>Yes</Use_Reference_Values>
<Solar_Absorptance>
<Value>0</Value>
</Solar_Absorptance>
<Reference_Thickness>
<Value>1000 mm</Value>
</Reference_Thickness>
<Solar_Attenuation_Coefficient>
<Value>0 1/m</Value>
</Solar_Attenuation_Coefficient>
</Solar_Radiation_Properties>
<Electrical_Conductivity>
<Option>Constant</Option>
<Value>0 S/m</Value>
<Electrical_Conductivity_Temperature_Curve>0,0, 100,0 &lt;C,S/m&gt;</Electrical_Conductivity_Temperature_Curve>
<Max_Value>10000000000 S/m</Max_Value>
</Electrical_Conductivity>
<Display_Options>
<Choose_Custom_Colour>No</Choose_Custom_Colour>
<Colour>255,255,255</Colour>
</Display_Options>
</Material>
<Material id="45995-47714">
<Name>Copper, Pure</Name>
<Conductivity>
<Type>Isotropic</Type>
<Option>Constant</Option>
<Value>386 W/(m K)</Value>
<Conductivity_Temperature_Curve>0,386, 200,386 &lt;C,W/(m K)&gt;</Conductivity_Temperature_Curve>
<Normal>1 W/(m K)</Normal>
<Planar>1 W/(m K)</Planar>
<K1>1 W/(m K)</K1>
<K2>1 W/(m K)</K2>
<K3>1 W/(m K)</K3>
</Conductivity>
<Density>
<Option>Constant</Option>
<Value>8950 kg/m^3</Value>
</Density>
<Specific_Heat>
<Option>Constant</Option>
<Value>380 J/(kg K)</Value>
<Specific_Heat_Temperature_Curve>0,380, 200,380 &lt;C,J/(kg K)&gt;</Specific_Heat_Temperature_Curve>
</Specific_Heat>
<Heat_Radiation_Properties>
<Transparent_To_Heat_Radiation>No</Transparent_To_Heat_Radiation>
<Surface_Emissivity>
<Value>0.92</Value>
</Surface_Emissivity>
</Heat_Radiation_Properties>
<Solar_Radiation_Properties>
<Solar_Reflectance>
<Value>0</Value>
</Solar_Reflectance>
<Transparent_To_Solar_Radiation>No</Transparent_To_Solar_Radiation>
<Use_Reference_Values>Yes</Use_Reference_Values>
<Solar_Absorptance>
<Value>0</Value>
</Solar_Absorptance>
<Reference_Thickness>
<Value>1000 mm</Value>
</Reference_Thickness>
<Solar_Attenuation_Coefficient>
<Value>0 1/m</Value>
</Solar_Attenuation_Coefficient>
</Solar_Radiation_Properties>
<Electrical_Conductivity>
<Option>Constant</Option>
<Value>59500000 S/m</Value>
<Electrical_Conductivity_Temperature_Curve>0,0, 100,0 &lt;C,S/m&gt;</Electrical_Conductivity_Temperature_Curve>
<Max_Value>10000000000 S/m</Max_Value>
</Electrical_Conductivity>
<Display_Options>
<Choose_Custom_Colour>No</Choose_Custom_Colour>
<Colour>255,255,255</Colour>
</Display_Options>
</Material>
<Material id="45995-47715">
<Name>CU</Name>
<Conductivity>
<Type>Isotropic</Type>
<Option>Constant</Option>
<Value>386 W/(m K)</Value>
<Conductivity_Temperature_Curve>0,0.0261, 200,0.0261 &lt;C,W/(m K)&gt;</Conductivity_Temperature_Curve>
<Normal>1 W/(m K)</Normal>
<Planar>1 W/(m K)</Planar>
<K1>1 W/(m K)</K1>
<K2>1 W/(m K)</K2>
<K3>1 W/(m K)</K3>
</Conductivity>
<Density>
<Option>Constant</Option>
<Value>8940 kg/m^3</Value>
</Density>
<Specific_Heat>
<Option>Constant</Option>
<Value>386 J/(kg K)</Value>
<Specific_Heat_Temperature_Curve>0,1005, 200,1005 &lt;C,J/(kg K)&gt;</Specific_Heat_Temperature_Curve>
</Specific_Heat>
<Heat_Radiation_Properties>
<Transparent_To_Heat_Radiation>No</Transparent_To_Heat_Radiation>
<Surface_Emissivity>
<Value>0.8</Value>
</Surface_Emissivity>
</Heat_Radiation_Properties>
<Solar_Radiation_Properties>
<Solar_Reflectance>
<Value>0</Value>
</Solar_Reflectance>
<Transparent_To_Solar_Radiation>No</Transparent_To_Solar_Radiation>
<Use_Reference_Values>Yes</Use_Reference_Values>
<Solar_Absorptance>
<Value>0</Value>
</Solar_Absorptance>
<Reference_Thickness>
<Value>1000 mm</Value>
</Reference_Thickness>
<Solar_Attenuation_Coefficient>
<Value>0 1/m</Value>
</Solar_Attenuation_Coefficient>
</Solar_Radiation_Properties>
<Electrical_Conductivity>
<Option>Constant</Option>
<Value>0 S/m</Value>
<Electrical_Conductivity_Temperature_Curve>0,0, 100,0 &lt;C,S/m&gt;</Electrical_Conductivity_Temperature_Curve>
<Max_Value>10000000000 S/m</Max_Value>
</Electrical_Conductivity>
<Display_Options>
<Choose_Custom_Colour>No</Choose_Custom_Colour>
<Colour>255,255,255</Colour>
</Display_Options>
</Material>
<Material id="45995-47716">
<Name>EPOXY</Name>
<Conductivity>
<Type>Isotropic</Type>
<Option>Constant</Option>
<Value>1 W/(m K)</Value>
<Conductivity_Temperature_Curve>0,0.0261, 200,0.0261 &lt;C,W/(m K)&gt;</Conductivity_Temperature_Curve>
<Normal>1 W/(m K)</Normal>
<Planar>1 W/(m K)</Planar>
<K1>1 W/(m K)</K1>
<K2>1 W/(m K)</K2>
<K3>1 W/(m K)</K3>
</Conductivity>
<Density>
<Option>Constant</Option>
<Value>670 kg/m^3</Value>
</Density>
<Specific_Heat>
<Option>Constant</Option>
<Value>1000 J/(kg K)</Value>
<Specific_Heat_Temperature_Curve>0,1005, 200,1005 &lt;C,J/(kg K)&gt;</Specific_Heat_Temperature_Curve>
</Specific_Heat>
<Heat_Radiation_Properties>
<Transparent_To_Heat_Radiation>No</Transparent_To_Heat_Radiation>
<Surface_Emissivity>
<Value>0.8</Value>
</Surface_Emissivity>
</Heat_Radiation_Properties>
<Solar_Radiation_Properties>
<Solar_Reflectance>
<Value>0</Value>
</Solar_Reflectance>
<Transparent_To_Solar_Radiation>No</Transparent_To_Solar_Radiation>
<Use_Reference_Values>Yes</Use_Reference_Values>
<Solar_Absorptance>
<Value>0</Value>
</Solar_Absorptance>
<Reference_Thickness>
<Value>1000 mm</Value>
</Reference_Thickness>
<Solar_Attenuation_Coefficient>
<Value>0 1/m</Value>
</Solar_Attenuation_Coefficient>
</Solar_Radiation_Properties>
<Electrical_Conductivity>
<Option>Constant</Option>
<Value>0 S/m</Value>
<Electrical_Conductivity_Temperature_Curve>0,0, 100,0 &lt;C,S/m&gt;</Electrical_Conductivity_Temperature_Curve>
<Max_Value>10000000000 S/m</Max_Value>
</Electrical_Conductivity>
<Display_Options>
<Choose_Custom_Colour>No</Choose_Custom_Colour>
<Colour>255,255,255</Colour>
</Display_Options>
</Material>
<Material id="45995-47717">
<Name>FR4</Name>
<Conductivity>
<Type>Isotropic</Type>
<Option>Constant</Option>
<Value>0.3 W/(m K)</Value>
<Conductivity_Temperature_Curve>-17.7777777777778,0.3, 93.3333333333333,0.3 &lt;C,W/(m K)&gt;</Conductivity_Temperature_Curve>
<Normal>1 W/(m K)</Normal>
<Planar>1 W/(m K)</Planar>
<K1>1 W/(m K)</K1>
<K2>1 W/(m K)</K2>
<K3>1 W/(m K)</K3>
</Conductivity>
<Density>
<Option>Constant</Option>
<Value>1200 kg/m^3</Value>
</Density>
<Specific_Heat>
<Option>Constant</Option>
<Value>880 J/(kg K)</Value>
<Specific_Heat_Temperature_Curve>0,880, 200,880 &lt;C,J/(kg K)&gt;</Specific_Heat_Temperature_Curve>
</Specific_Heat>
<Heat_Radiation_Properties>
<Transparent_To_Heat_Radiation>No</Transparent_To_Heat_Radiation>
<Surface_Emissivity>
<Value>0.92</Value>
</Surface_Emissivity>
</Heat_Radiation_Properties>
<Solar_Radiation_Properties>
<Solar_Reflectance>
<Value>0</Value>
</Solar_Reflectance>
<Transparent_To_Solar_Radiation>No</Transparent_To_Solar_Radiation>
<Use_Reference_Values>Yes</Use_Reference_Values>
<Solar_Absorptance>
<Value>0</Value>
</Solar_Absorptance>
<Reference_Thickness>
<Value>1000 mm</Value>
</Reference_Thickness>
<Solar_Attenuation_Coefficient>
<Value>0 1/m</Value>
</Solar_Attenuation_Coefficient>
</Solar_Radiation_Properties>
<Electrical_Conductivity>
<Option>Constant</Option>
<Value>0 S/m</Value>
<Electrical_Conductivity_Temperature_Curve>0,0, 100,0 &lt;C,S/m&gt;</Electrical_Conductivity_Temperature_Curve>
<Max_Value>10000000000 S/m</Max_Value>
</Electrical_Conductivity>
<Display_Options>
<Choose_Custom_Colour>No</Choose_Custom_Colour>
<Colour>255,255,255</Colour>
</Display_Options>
</Material>
<Material id="45995-47718">
<Name>FR4_DB</Name>
<Conductivity>
<Type>Isotropic</Type>
<Option>Constant</Option>
<Value>0.3 W/(m K)</Value>
<Conductivity_Temperature_Curve>0,0.0261, 200,0.0261 &lt;C,W/(m K)&gt;</Conductivity_Temperature_Curve>
<Normal>1 W/(m K)</Normal>
<Planar>1 W/(m K)</Planar>
<K1>1 W/(m K)</K1>
<K2>1 W/(m K)</K2>
<K3>1 W/(m K)</K3>
</Conductivity>
<Density>
<Option>Constant</Option>
<Value>1250 kg/m^3</Value>
</Density>
<Specific_Heat>
<Option>Constant</Option>
<Value>1300 J/(kg K)</Value>
<Specific_Heat_Temperature_Curve>0,1005, 200,1005 &lt;C,J/(kg K)&gt;</Specific_Heat_Temperature_Curve>
</Specific_Heat>
<Heat_Radiation_Properties>
<Transparent_To_Heat_Radiation>No</Transparent_To_Heat_Radiation>
<Surface_Emissivity>
<Value>0.8</Value>
</Surface_Emissivity>
</Heat_Radiation_Properties>
<Solar_Radiation_Properties>
<Solar_Reflectance>
<Value>0</Value>
</Solar_Reflectance>
<Transparent_To_Solar_Radiation>No</Transparent_To_Solar_Radiation>
<Use_Reference_Values>Yes</Use_Reference_Values>
<Solar_Absorptance>
<Value>0</Value>
</Solar_Absorptance>
<Reference_Thickness>
<Value>1000 mm</Value>
</Reference_Thickness>
<Solar_Attenuation_Coefficient>
<Value>0 1/m</Value>
</Solar_Attenuation_Coefficient>
</Solar_Radiation_Properties>
<Electrical_Conductivity>
<Option>Constant</Option>
<Value>0 S/m</Value>
<Electrical_Conductivity_Temperature_Curve>0,0, 100,0 &lt;C,S/m&gt;</Electrical_Conductivity_Temperature_Curve>
<Max_Value>10000000000 S/m</Max_Value>
</Electrical_Conductivity>
<Display_Options>
<Choose_Custom_Colour>No</Choose_Custom_Colour>
<Colour>255,255,255</Colour>
</Display_Options>
</Material>
<Material id="45995-47719">
<Name>PBT</Name>
<Conductivity>
<Type>Isotropic</Type>
<Option>Constant</Option>
<Value>0.18 W/(m K)</Value>
<Conductivity_Temperature_Curve>0,0.0261, 200,0.0261 &lt;C,W/(m K)&gt;</Conductivity_Temperature_Curve>
<Normal>1 W/(m K)</Normal>
<Planar>1 W/(m K)</Planar>
<K1>1 W/(m K)</K1>
<K2>1 W/(m K)</K2>
<K3>1 W/(m K)</K3>
</Conductivity>
<Density>
<Option>Constant</Option>
<Value>1300 kg/m^3</Value>
</Density>
<Specific_Heat>
<Option>Constant</Option>
<Value>1200 J/(kg K)</Value>
<Specific_Heat_Temperature_Curve>0,1005, 200,1005 &lt;C,J/(kg K)&gt;</Specific_Heat_Temperature_Curve>
</Specific_Heat>
<Heat_Radiation_Properties>
<Transparent_To_Heat_Radiation>No</Transparent_To_Heat_Radiation>
<Surface_Emissivity>
<Value>0.8</Value>
</Surface_Emissivity>
</Heat_Radiation_Properties>
<Solar_Radiation_Properties>
<Solar_Reflectance>
<Value>0</Value>
</Solar_Reflectance>
<Transparent_To_Solar_Radiation>No</Transparent_To_Solar_Radiation>
<Use_Reference_Values>Yes</Use_Reference_Values>
<Solar_Absorptance>
<Value>0</Value>
</Solar_Absorptance>
<Reference_Thickness>
<Value>1000 mm</Value>
</Reference_Thickness>
<Solar_Attenuation_Coefficient>
<Value>0 1/m</Value>
</Solar_Attenuation_Coefficient>
</Solar_Radiation_Properties>
<Electrical_Conductivity>
<Option>Constant</Option>
<Value>0 S/m</Value>
<Electrical_Conductivity_Temperature_Curve>0,0, 100,0 &lt;C,S/m&gt;</Electrical_Conductivity_Temperature_Curve>
<Max_Value>10000000000 S/m</Max_Value>
</Electrical_Conductivity>
<Display_Options>
<Choose_Custom_Colour>No</Choose_Custom_Colour>
<Colour>255,255,255</Colour>
</Display_Options>
</Material>
<Material id="45995-47720">
<Name>PBT-PET-GF30</Name>
<Conductivity>
<Type>Isotropic</Type>
<Option>Constant</Option>
<Value>0.271 W/(m K)</Value>
<Conductivity_Temperature_Curve>0,0.0261, 200,0.0261 &lt;C,W/(m K)&gt;</Conductivity_Temperature_Curve>
<Normal>1 W/(m K)</Normal>
<Planar>1 W/(m K)</Planar>
<K1>1 W/(m K)</K1>
<K2>1 W/(m K)</K2>
<K3>1 W/(m K)</K3>
</Conductivity>
<Density>
<Option>Constant</Option>
<Value>1460 kg/m^3</Value>
</Density>
<Specific_Heat>
<Option>Constant</Option>
<Value>1200 J/(kg K)</Value>
<Specific_Heat_Temperature_Curve>0,1005, 200,1005 &lt;C,J/(kg K)&gt;</Specific_Heat_Temperature_Curve>
</Specific_Heat>
<Heat_Radiation_Properties>
<Transparent_To_Heat_Radiation>No</Transparent_To_Heat_Radiation>
<Surface_Emissivity>
<Value>0.8</Value>
</Surface_Emissivity>
</Heat_Radiation_Properties>
<Solar_Radiation_Properties>
<Solar_Reflectance>
<Value>0</Value>
</Solar_Reflectance>
<Transparent_To_Solar_Radiation>No</Transparent_To_Solar_Radiation>
<Use_Reference_Values>Yes</Use_Reference_Values>
<Solar_Absorptance>
<Value>0</Value>
</Solar_Absorptance>
<Reference_Thickness>
<Value>1000 mm</Value>
</Reference_Thickness>
<Solar_Attenuation_Coefficient>
<Value>0 1/m</Value>
</Solar_Attenuation_Coefficient>
</Solar_Radiation_Properties>
<Electrical_Conductivity>
<Option>Constant</Option>
<Value>0 S/m</Value>
<Electrical_Conductivity_Temperature_Curve>0,0, 100,0 &lt;C,S/m&gt;</Electrical_Conductivity_Temperature_Curve>
<Max_Value>10000000000 S/m</Max_Value>
</Electrical_Conductivity>
<Display_Options>
<Choose_Custom_Colour>No</Choose_Custom_Colour>
<Colour>255,255,255</Colour>
</Display_Options>
</Material>
<Material id="45995-47721">
<Name>SECC</Name>
<Conductivity>
<Type>Isotropic</Type>
<Option>Constant</Option>
<Value>60.2 W/(m K)</Value>
<Conductivity_Temperature_Curve>0,0.0261, 200,0.0261 &lt;C,W/(m K)&gt;</Conductivity_Temperature_Curve>
<Normal>1 W/(m K)</Normal>
<Planar>1 W/(m K)</Planar>
<K1>1 W/(m K)</K1>
<K2>1 W/(m K)</K2>
<K3>1 W/(m K)</K3>
</Conductivity>
<Density>
<Option>Constant</Option>
<Value>7872 kg/m^3</Value>
</Density>
<Specific_Heat>
<Option>Constant</Option>
<Value>519 J/(kg K)</Value>
<Specific_Heat_Temperature_Curve>0,1005, 200,1005 &lt;C,J/(kg K)&gt;</Specific_Heat_Temperature_Curve>
</Specific_Heat>
<Heat_Radiation_Properties>
<Transparent_To_Heat_Radiation>No</Transparent_To_Heat_Radiation>
<Surface_Emissivity>
<Value>0.28</Value>
</Surface_Emissivity>
</Heat_Radiation_Properties>
<Solar_Radiation_Properties>
<Solar_Reflectance>
<Value>0</Value>
</Solar_Reflectance>
<Transparent_To_Solar_Radiation>No</Transparent_To_Solar_Radiation>
<Use_Reference_Values>Yes</Use_Reference_Values>
<Solar_Absorptance>
<Value>0</Value>
</Solar_Absorptance>
<Reference_Thickness>
<Value>1000 mm</Value>
</Reference_Thickness>
<Solar_Attenuation_Coefficient>
<Value>0 1/m</Value>
</Solar_Attenuation_Coefficient>
</Solar_Radiation_Properties>
<Electrical_Conductivity>
<Option>Constant</Option>
<Value>0 S/m</Value>
<Electrical_Conductivity_Temperature_Curve>0,0, 100,0 &lt;C,S/m&gt;</Electrical_Conductivity_Temperature_Curve>
<Max_Value>10000000000 S/m</Max_Value>
</Electrical_Conductivity>
<Display_Options>
<Choose_Custom_Colour>No</Choose_Custom_Colour>
<Colour>255,255,255</Colour>
</Display_Options>
</Material>
<Material id="45995-47722">
<Name>SECC_Coated</Name>
<Conductivity>
<Type>Isotropic</Type>
<Option>Constant</Option>
<Value>60.2 W/(m K)</Value>
<Conductivity_Temperature_Curve>0,0.0261, 200,0.0261 &lt;C,W/(m K)&gt;</Conductivity_Temperature_Curve>
<Normal>1 W/(m K)</Normal>
<Planar>1 W/(m K)</Planar>
<K1>1 W/(m K)</K1>
<K2>1 W/(m K)</K2>
<K3>1 W/(m K)</K3>
</Conductivity>
<Density>
<Option>Constant</Option>
<Value>7872 kg/m^3</Value>
</Density>
<Specific_Heat>
<Option>Constant</Option>
<Value>519 J/(kg K)</Value>
<Specific_Heat_Temperature_Curve>0,1005, 200,1005 &lt;C,J/(kg K)&gt;</Specific_Heat_Temperature_Curve>
</Specific_Heat>
<Heat_Radiation_Properties>
<Transparent_To_Heat_Radiation>No</Transparent_To_Heat_Radiation>
<Surface_Emissivity>
<Value>0.9</Value>
</Surface_Emissivity>
</Heat_Radiation_Properties>
<Solar_Radiation_Properties>
<Solar_Reflectance>
<Value>0</Value>
</Solar_Reflectance>
<Transparent_To_Solar_Radiation>No</Transparent_To_Solar_Radiation>
<Use_Reference_Values>Yes</Use_Reference_Values>
<Solar_Absorptance>
<Value>0</Value>
</Solar_Absorptance>
<Reference_Thickness>
<Value>1000 mm</Value>
</Reference_Thickness>
<Solar_Attenuation_Coefficient>
<Value>0 1/m</Value>
</Solar_Attenuation_Coefficient>
</Solar_Radiation_Properties>
<Electrical_Conductivity>
<Option>Constant</Option>
<Value>0 S/m</Value>
<Electrical_Conductivity_Temperature_Curve>0,0, 100,0 &lt;C,S/m&gt;</Electrical_Conductivity_Temperature_Curve>
<Max_Value>10000000000 S/m</Max_Value>
</Electrical_Conductivity>
<Display_Options>
<Choose_Custom_Colour>No</Choose_Custom_Colour>
<Colour>255,255,255</Colour>
</Display_Options>
</Material>
<Material id="45995-47723">
<Name>Si(Silicon)</Name>
<Conductivity>
<Type>Isotropic</Type>
<Option>Constant</Option>
<Value>124 W/(m K)</Value>
<Conductivity_Temperature_Curve>0,0.0261, 200,0.0261 &lt;C,W/(m K)&gt;</Conductivity_Temperature_Curve>
<Normal>1 W/(m K)</Normal>
<Planar>1 W/(m K)</Planar>
<K1>1 W/(m K)</K1>
<K2>1 W/(m K)</K2>
<K3>1 W/(m K)</K3>
</Conductivity>
<Density>
<Option>Constant</Option>
<Value>2329 kg/m^3</Value>
</Density>
<Specific_Heat>
<Option>Constant</Option>
<Value>702 J/(kg K)</Value>
<Specific_Heat_Temperature_Curve>0,1005, 200,1005 &lt;C,J/(kg K)&gt;</Specific_Heat_Temperature_Curve>
</Specific_Heat>
<Heat_Radiation_Properties>
<Transparent_To_Heat_Radiation>No</Transparent_To_Heat_Radiation>
<Surface_Emissivity>
<Value>0.8</Value>
</Surface_Emissivity>
</Heat_Radiation_Properties>
<Solar_Radiation_Properties>
<Solar_Reflectance>
<Value>0</Value>
</Solar_Reflectance>
<Transparent_To_Solar_Radiation>No</Transparent_To_Solar_Radiation>
<Use_Reference_Values>Yes</Use_Reference_Values>
<Solar_Absorptance>
<Value>0</Value>
</Solar_Absorptance>
<Reference_Thickness>
<Value>1000 mm</Value>
</Reference_Thickness>
<Solar_Attenuation_Coefficient>
<Value>0 1/m</Value>
</Solar_Attenuation_Coefficient>
</Solar_Radiation_Properties>
<Electrical_Conductivity>
<Option>Constant</Option>
<Value>0 S/m</Value>
<Electrical_Conductivity_Temperature_Curve>0,0, 100,0 &lt;C,S/m&gt;</Electrical_Conductivity_Temperature_Curve>
<Max_Value>10000000000 S/m</Max_Value>
</Electrical_Conductivity>
<Display_Options>
<Choose_Custom_Colour>No</Choose_Custom_Colour>
<Colour>255,255,255</Colour>
</Display_Options>
</Material>
<Material id="45995-47724">
<Name>Steel, Mild</Name>
<Conductivity>
<Type>Isotropic</Type>
<Option>Constant</Option>
<Value>63 W/(m K)</Value>
<Conductivity_Temperature_Curve>0,63, 200,63 &lt;C,W/(m K)&gt;</Conductivity_Temperature_Curve>
<Normal>1 W/(m K)</Normal>
<Planar>1 W/(m K)</Planar>
<K1>1 W/(m K)</K1>
<K2>1 W/(m K)</K2>
<K3>1 W/(m K)</K3>
</Conductivity>
<Density>
<Option>Constant</Option>
<Value>7860 kg/m^3</Value>
</Density>
<Specific_Heat>
<Option>Constant</Option>
<Value>420 J/(kg K)</Value>
<Specific_Heat_Temperature_Curve>0,420, 200,420 &lt;C,J/(kg K)&gt;</Specific_Heat_Temperature_Curve>
</Specific_Heat>
<Heat_Radiation_Properties>
<Transparent_To_Heat_Radiation>No</Transparent_To_Heat_Radiation>
<Surface_Emissivity>
<Value>0.92</Value>
</Surface_Emissivity>
</Heat_Radiation_Properties>
<Solar_Radiation_Properties>
<Solar_Reflectance>
<Value>0</Value>
</Solar_Reflectance>
<Transparent_To_Solar_Radiation>No</Transparent_To_Solar_Radiation>
<Use_Reference_Values>Yes</Use_Reference_Values>
<Solar_Absorptance>
<Value>0</Value>
</Solar_Absorptance>
<Reference_Thickness>
<Value>1 m</Value>
</Reference_Thickness>
<Solar_Attenuation_Coefficient>
<Value>0 1/m</Value>
</Solar_Attenuation_Coefficient>
</Solar_Radiation_Properties>
<Electrical_Conductivity>
<Option>Constant</Option>
<Value>5560000 S/m</Value>
<Electrical_Conductivity_Temperature_Curve>0,0, 100,0 &lt;C,S/m&gt;</Electrical_Conductivity_Temperature_Curve>
<Max_Value>10000000000 S/m</Max_Value>
</Electrical_Conductivity>
<Display_Options>
<Choose_Custom_Colour>No</Choose_Custom_Colour>
<Colour>255,255,255</Colour>
</Display_Options>
</Material>
<Material id="45995-47725">
<Name>Thermal-Pad</Name>
<Conductivity>
<Type>Isotropic</Type>
<Option>Constant</Option>
<Value>1.5 W/(m K)</Value>
<Conductivity_Temperature_Curve>0,0.0261, 200,0.0261 &lt;C,W/(m K)&gt;</Conductivity_Temperature_Curve>
<Normal>1 W/(m K)</Normal>
<Planar>1 W/(m K)</Planar>
<K1>1 W/(m K)</K1>
<K2>1 W/(m K)</K2>
<K3>1 W/(m K)</K3>
</Conductivity>
<Density>
<Option>Constant</Option>
<Value>2100 kg/m^3</Value>
</Density>
<Specific_Heat>
<Option>Constant</Option>
<Value>1000 J/(kg K)</Value>
<Specific_Heat_Temperature_Curve>0,1005, 200,1005 &lt;C,J/(kg K)&gt;</Specific_Heat_Temperature_Curve>
</Specific_Heat>
<Heat_Radiation_Properties>
<Transparent_To_Heat_Radiation>No</Transparent_To_Heat_Radiation>
<Surface_Emissivity>
<Value>0.8</Value>
</Surface_Emissivity>
</Heat_Radiation_Properties>
<Solar_Radiation_Properties>
<Solar_Reflectance>
<Value>0</Value>
</Solar_Reflectance>
<Transparent_To_Solar_Radiation>No</Transparent_To_Solar_Radiation>
<Use_Reference_Values>Yes</Use_Reference_Values>
<Solar_Absorptance>
<Value>0</Value>
</Solar_Absorptance>
<Reference_Thickness>
<Value>1000 mm</Value>
</Reference_Thickness>
<Solar_Attenuation_Coefficient>
<Value>0 1/m</Value>
</Solar_Attenuation_Coefficient>
</Solar_Radiation_Properties>
<Electrical_Conductivity>
<Option>Constant</Option>
<Value>0 S/m</Value>
<Electrical_Conductivity_Temperature_Curve>0,0, 100,0 &lt;C,S/m&gt;</Electrical_Conductivity_Temperature_Curve>
<Max_Value>10000000000 S/m</Max_Value>
</Electrical_Conductivity>
<Display_Options>
<Choose_Custom_Colour>No</Choose_Custom_Colour>
<Colour>255,255,255</Colour>
</Display_Options>
</Material>
</Materials>
<Fluids/>
<Contaminants/>
<Generic_Scalars/>
<SuppressedErrors/>
<ShortcutCameras/>
<Created_in>6SigmaET</Created_in>
<Last_Modified_in>6SigmaET</Last_Modified_in>
<Continuous_Error_Checking>Yes</Continuous_Error_Checking>
<Model_Store_Record>
<Revision_Number>0</Revision_Number>
<Upload_Date>00/00/0000</Upload_Date>
<Upload_Time>09:00:00</Upload_Time>
<Download_Date>00/00/0000</Download_Date>
<Download_Time>09:00:00</Download_Time>
<Last_Saved_Date>00/00/0000</Last_Saved_Date>
<Last_Saved_Time>09:00:00</Last_Saved_Time>
</Model_Store_Record>
<PACDataList/>
<LegendBounds>
<LegendBound id="45995-47726">
<Name>Radiation Surface Heat Flux</Name>
<Bound_Type>Full</Bound_Type>
<Upper_Bound>1</Upper_Bound>
<Lower_Bound>0</Lower_Bound>
</LegendBound>
<LegendBound id="45995-47727">
<Name>Temperature</Name>
<Bound_Type>Full</Bound_Type>
<Upper_Bound>1</Upper_Bound>
<Lower_Bound>0</Lower_Bound>
</LegendBound>
<LegendBound id="45995-47728">
<Name>Surface Radiation</Name>
<Bound_Type>Full</Bound_Type>
<Upper_Bound>1</Upper_Bound>
<Lower_Bound>0</Lower_Bound>
</LegendBound>
<LegendBound id="45995-47729">
<Name>X Heat Flux</Name>
<Bound_Type>Full</Bound_Type>
<Upper_Bound>1</Upper_Bound>
<Lower_Bound>0</Lower_Bound>
</LegendBound>
</LegendBounds>
<LegendScalings/>
<SurfaceTempOptionsLink>
<Surface_Temperature_Options id="45995-47730">
<Surface_Temperature_Outlined>Yes</Surface_Temperature_Outlined>
<Surface_Temperature_Edge_Threshold>10 degrees</Surface_Temperature_Edge_Threshold>
<Surface_Temperature_Refinement_Factor>4</Surface_Temperature_Refinement_Factor>
<Caching_Surface_Temperature>No</Caching_Surface_Temperature>
</Surface_Temperature_Options>
</SurfaceTempOptionsLink>
<Activate_Cooling_Module>Yes</Activate_Cooling_Module>
<Project_Fluid>
<Fluid id="45995-47731">
<Name>Air</Name>
<Density>
<Altitude_Based>No</Altitude_Based>
<Option>Ideal Gas</Option>
<Value>1.19 kg/m^3</Value>
<Pressure_Altitude_Curve>-250,104365, 0,101325, 250,98357.6, 500,95461.2, 750,92634.6, 1000,89876.2, 1500,84559.6, 2000,79501.4, 2500,74691.7, 3000,70121.1, 3500,65780.3, 4000,61660.4, 5000,54048.2, 6000,47217.6, 7000,41105.2, 8000,35651.6, 9000,30800.7, 10000,26499.9 &lt;m,Pa&gt;</Pressure_Altitude_Curve>
<Density_Reference_Temperature>23 C</Density_Reference_Temperature>
<Calculated_Density>0 kg/m^3</Calculated_Density>
</Density>
<Laminar_Viscosity>
<Option>Constant</Option>
<Value>0.0000184 kg/ms</Value>
<Laminar_Viscosity_Temperature_Curve>0,1.84e-05, 200,1.84e-05 &lt;C,kg/ms&gt;</Laminar_Viscosity_Temperature_Curve>
</Laminar_Viscosity>
<Conductivity>
<Option>Constant</Option>
<Value>0.0260305 W/(m K)</Value>
<Conductivity_Temperature_Curve>0,0.0261, 200,0.0261 &lt;C,W/(m K)&gt;</Conductivity_Temperature_Curve>
</Conductivity>
<Specific_Heat>
<Option>Constant</Option>
<Value>1003.62 J/(kg K)</Value>
<Specific_Heat_Temperature_Curve>0,1005, 200,1005 &lt;C,J/(kg K)&gt;</Specific_Heat_Temperature_Curve>
</Specific_Heat>
<Expansivity>
<Value>0.0033333 1/C</Value>
</Expansivity>
<Molecular_Weight>
<Value>28.9664 kg/kmol</Value>
</Molecular_Weight>
<Reference_Pressure>
<Value>101325 Pa</Value>
</Reference_Pressure>
</Fluid>
</Project_Fluid>
<Environments>
<Environment id="45995-47732">
<Identification>
<Name>Default Environment</Name>
</Identification>
<Temperature>
<Time_Dependent_Specification>No</Time_Dependent_Specification>
<Option>Constant</Option>
<Temperature>75 C</Temperature>
<Temperature_Curve>0,20, 100,20 &lt;s,C&gt;</Temperature_Curve>
<Heat_Load_Value>0 W/m^2</Heat_Load_Value>
<Heat_Load_Curve>0,0, 100,0 &lt;s,W/m^2&gt;</Heat_Load_Curve>
<Total_Heat_Load_Value>0 W</Total_Heat_Load_Value>
<Total_Heat_Load_Curve>0,0, 100,0 &lt;s,W&gt;</Total_Heat_Load_Curve>
<External_Heat_Transfer>
<Option>From Environment</Option>
<Heat_Transfer_Coefficient>10 W/(m^2K)</Heat_Transfer_Coefficient>
<HTC_Curve>0,10, 100,10 &lt;s,W/(m^2K)&gt;</HTC_Curve>
<Heat_Radiation>
<Active>Yes</Active>
<Radiant_Temperature_Option>Use Temperature Value</Radiant_Temperature_Option>
<Radiant_Temperature>20 C</Radiant_Temperature>
<Radiant_Temperature_Curve>0,20, 100,20 &lt;s,C&gt;</Radiant_Temperature_Curve>
<Emissivity>1</Emissivity>
</Heat_Radiation>
<Solar_Radiation>
<Active>Yes</Active>
</Solar_Radiation>
</External_Heat_Transfer>
</Temperature>
<Velocity>
<Velocity_Specification>Uniform</Velocity_Specification>
<X_Velocity>
<X_Velocity>0 m/s</X_Velocity>
</X_Velocity>
<Y_Velocity>
<Y_Velocity>0 m/s</Y_Velocity>
</Y_Velocity>
<Z_Velocity>
<Z_Velocity>0 m/s</Z_Velocity>
</Z_Velocity>
<Wind_Profile>
<Direction>S</Direction>
<Azimuth>0 degrees</Azimuth>
<Height_Variation>None</Height_Variation>
<Wind_Speed>1 m/s</Wind_Speed>
<Reference_Height>10 m</Reference_Height>
<Roughness_Length>0.1 m</Roughness_Length>
<Wind_Profile>0,0, 0.1,0.131, 0.2,0.262, 0.5,0.435, 1,0.565, 2,0.696, 5,0.869, 10,1, 20,1.131, 35,1.236, 50,1.304 &lt;m,m/s&gt;</Wind_Profile>
</Wind_Profile>
</Velocity>
<Pressure>
<Pressure>0 Pa</Pressure>
</Pressure>
<Relative_Humidity>
<Relative_Humidity>0 %</Relative_Humidity>
</Relative_Humidity>
<Contaminants>
<Environmental_Contaminants/>
<Concentrations> : </Concentrations>
</Contaminants>
<Generic_Scalars>
<Environmental_Generic_Scalars/>
<Constant_Values> : </Constant_Values>
</Generic_Scalars>
</Environment>
</Environments>
<SolutionControlLink>
<Solution_Control id="45995-47733">
<Solution_Directory>\\sh-nas\KHKIM\Works_2020\Mobis\Test_Model_v3\Test_Model_v3/Baseline</Solution_Directory>
<Solution_Scheme>
<Solution_Type>Flow and Temperature</Solution_Type>
<Freeze_Flow>No</Freeze_Flow>
<Use_Mixed_Precision>No</Use_Mixed_Precision>
<Main_Matrix_Precision>Double</Main_Matrix_Precision>
</Solution_Scheme>
<Initialisation_Control>
<Regenerate_Grid_and_Regions>Auto</Regenerate_Grid_and_Regions>
<Reuse_Radiation_Data_On_Restart>Yes</Reuse_Radiation_Data_On_Restart>
</Initialisation_Control>
<Transient>
<Time_Varying>No</Time_Varying>
<Definition>
<Time_Grid_Type>Uniform</Time_Grid_Type>
<Total_Simulation_Time>1 s</Total_Simulation_Time>
<Time_Step>1 s</Time_Step>
<Time_Grid>0 &lt;s&gt;</Time_Grid>
<Variable_Time_Grid>
<Time_Grid_Ranges/>
</Variable_Time_Grid>
<Transient_Termination_Criterion>
<Stop_At_Defined_Temperature>No</Stop_At_Defined_Temperature>
<Sensor_Or_Component/>
<Transient_Stop_Temperature>40 C</Transient_Stop_Temperature>
</Transient_Termination_Criterion>
<Time_Step_Number_of_Iterations>100</Time_Step_Number_of_Iterations>
<Time_Step_Monitor_Interval>10</Time_Step_Monitor_Interval>
<Flow_Field_Output_Specification>Interval</Flow_Field_Output_Specification>
<Flow_Field_Output_Interval>1 s</Flow_Field_Output_Interval>
<Flow_Field_Output_Times>0 &lt;s&gt;</Flow_Field_Output_Times>
<Object_Results_Output_Specification>Same As Flow Field</Object_Results_Output_Specification>
<Object_Results_Output_Interval>1 s</Object_Results_Output_Interval>
<Object_Results_Output_Times>0 &lt;s&gt;</Object_Results_Output_Times>
<Surface_Heat_Transfer>No</Surface_Heat_Transfer>
<Equipment_Thermal_Inertia>No</Equipment_Thermal_Inertia>
<ACU_Response_Time>60 s</ACU_Response_Time>
<Initialise_Variables_From>Constant Fields</Initialise_Variables_From>
</Definition>
</Transient>
<Iterations>
<Number_of_Iterations>200</Number_of_Iterations>
<Monitor_Interval>1</Monitor_Interval>
</Iterations>
<Turbulence>
<Model>Standard KE</Model>
<Value>0.01 kg/ms</Value>
<LVEL_Wall_Function>Standard</LVEL_Wall_Function>
<KE_Wall_Function>Standard</KE_Wall_Function>
<Inlet_Turbulence>Yes</Inlet_Turbulence>
<Specification_Type>Auto</Specification_Type>
<Inlet_Energy_Intensity>5 %</Inlet_Energy_Intensity>
<Inlet_Turbulent_Viscosity>0.01 kg/ms</Inlet_Turbulent_Viscosity>
<Inlet_Length_Scale_Coefficient>0.1</Inlet_Length_Scale_Coefficient>
<Face_Resistance_Turbulence>No</Face_Resistance_Turbulence>
<Set_Face_Resistance_Flow_To_Laminar>No</Set_Face_Resistance_Flow_To_Laminar>
<Volume_Resistance_Turbulence>No</Volume_Resistance_Turbulence>
<Set_Volume_Resistance_Flow_To_Laminar>No</Set_Volume_Resistance_Flow_To_Laminar>
<Turbulent_Viscosity_Upper_Bound>10000000000 kg/ms</Turbulent_Viscosity_Upper_Bound>
<Allow_Turbulence_Generation_By_Buoyancy>No</Allow_Turbulence_Generation_By_Buoyancy>
<C3EP>1</C3EP>
<Store_Turbulent_Viscosity>No</Store_Turbulent_Viscosity>
<Store_Turbulence_Generation>No</Store_Turbulence_Generation>
<Store_Y_Plus>No</Store_Y_Plus>
</Turbulence>
<Gravity>
<Active>Yes</Active>
<Definition>
<Gx>0 m/s^2</Gx>
<Gy>-9.81 m/s^2</Gy>
<Gz>0 m/s^2</Gz>
<Reference_Temperature_Option>Auto</Reference_Temperature_Option>
<Reference_Temperature>20 C</Reference_Temperature>
<Boundary_Modification>No</Boundary_Modification>
</Definition>
</Gravity>
<Fluid_Treatment>
<Allow_Ideal_Gases>Yes</Allow_Ideal_Gases>
</Fluid_Treatment>
<Flow_Objects>
<Allowed_Blockage>50 %</Allowed_Blockage>
<Maximum_Temperature_Threshold>100 %</Maximum_Temperature_Threshold>
<Flows_Overwrite_Blanking_Plates>Yes</Flows_Overwrite_Blanking_Plates>
<Use_Accelerated_Velocity>Yes</Use_Accelerated_Velocity>
<Use_Consistent_Momentum>No</Use_Consistent_Momentum>
<Use_Fix_Resistance_Coefficient>No</Use_Fix_Resistance_Coefficient>
<Allow_Momentum_Diffusion_across_Resistance>Yes</Allow_Momentum_Diffusion_across_Resistance>
<Allow_Pressure_Driven_Excess_Flow>Yes</Allow_Pressure_Driven_Excess_Flow>
<Excess_Flow_Correlation>0,0, 1000,0.44 &lt;1/m^2,&gt;</Excess_Flow_Correlation>
<Off_Equipment_Excess_Flow_Factor>1.25</Off_Equipment_Excess_Flow_Factor>
<Adjust_Coefficients_For_Pressure>Yes</Adjust_Coefficients_For_Pressure>
<Fan_Curve_Reference_Density>1.19 kg/m^3</Fan_Curve_Reference_Density>
<Fan_Inlet_Pressure_Type>Total Pressure</Fan_Inlet_Pressure_Type>
<Axial_Fan_Outlet_Pressure_Treatment>Maximum</Axial_Fan_Outlet_Pressure_Treatment>
<Fan_Outlet_Maximum_Pressure_Threshold>90 %</Fan_Outlet_Maximum_Pressure_Threshold>
<Adjust_Coefficients_For_Calibration>No</Adjust_Coefficients_For_Calibration>
<Straighten_Reversed_Grille_Flows>Yes</Straighten_Reversed_Grille_Flows>
<Flow_Network_Relaxation>0.5</Flow_Network_Relaxation>
<Flow_Network_Resistance_Relaxation>0.5</Flow_Network_Resistance_Relaxation>
</Flow_Objects>
<Solid_Objects>
<Record_Thermal_Data>Yes</Record_Thermal_Data>
<Allow_User_Defined_Heat_Transfer>No</Allow_User_Defined_Heat_Transfer>
<Allow_Temperature_Dependent_Power>No</Allow_Temperature_Dependent_Power>
<Use_Thin_Solid_Heat_Flux_Relaxation>No</Use_Thin_Solid_Heat_Flux_Relaxation>
<Thin_Solid_Heat_Flux_Relaxation>0.1</Thin_Solid_Heat_Flux_Relaxation>
<Allow_Surface_Roughness>No</Allow_Surface_Roughness>
<Allow_Wall_Function_Specification>No</Allow_Wall_Function_Specification>
<Allow_Surface_Area_Adjustment>No</Allow_Surface_Area_Adjustment>
<Allow_Object_Based_Boundary_Cell_Reconstruction>No</Allow_Object_Based_Boundary_Cell_Reconstruction>
<Allow_Motion>No</Allow_Motion>
<Anisotropic_Correction>
<Apply_Anisotropic_Correction>Detailed</Apply_Anisotropic_Correction>
<Use_Anisotropic_Correction_Relaxation>No</Use_Anisotropic_Correction_Relaxation>
<Anisotropic_Correction_Relaxation>0.1</Anisotropic_Correction_Relaxation>
</Anisotropic_Correction>
<Convective_HTC>
<Output_convective_HTC>No</Output_convective_HTC>
<Free_Stream_Temperature>Auto</Free_Stream_Temperature>
<Free_Stream_Temperature_Value>20 C</Free_Stream_Temperature_Value>
</Convective_HTC>
</Solid_Objects>
<Hybrid_Cells>
<Allow>No</Allow>
<Ignore_Hybrid_Cells>No</Ignore_Hybrid_Cells>
<Split_Face_Generation_Option>Split Any Faces</Split_Face_Generation_Option>
<Maximum_Open_Area_Fraction>2</Maximum_Open_Area_Fraction>
<Maximum_Cell_Expansion_Ratio>5</Maximum_Cell_Expansion_Ratio>
<Use_Hybrid_Cell_Regions>Yes</Use_Hybrid_Cell_Regions>
<Eliminate_Tiny_Gaps>No</Eliminate_Tiny_Gaps>
<Adjust_Flow_Boundaries>No</Adjust_Flow_Boundaries>
<Adjust_Resistance_Boundaries>Yes</Adjust_Resistance_Boundaries>
<Adjust_Friction>Yes</Adjust_Friction>
<Validate_Cells>Yes</Validate_Cells>
<Minimum_Open_Area_Fraction>0.0001</Minimum_Open_Area_Fraction>
<Cell_Tolerance>0.0005</Cell_Tolerance>
<Wall_Distance_Tolerance>0.01</Wall_Distance_Tolerance>
<Minimum_Wall_Distance_Fraction>0.1</Minimum_Wall_Distance_Fraction>
<Smooth_Wall_Distance>Yes</Smooth_Wall_Distance>
<Use_Average_Mass_Flux>No</Use_Average_Mass_Flux>
<Merge_Tiny_Cells>No</Merge_Tiny_Cells>
<Merging_Criterion>0.1</Merging_Criterion>
</Hybrid_Cells>
<Solar_Radiation>
<Active>No</Active>
<Use_Calculator>No</Use_Calculator>
<Intensity>200 W/m^2</Intensity>
<Direction>
<Ix>0</Ix>
<Iy>-1</Iy>
<Iz>0</Iz>
</Direction>
<Ignore_Reflected_Radiation>Yes</Ignore_Reflected_Radiation>
<Sky_Radiation>
<Allow_Sky_Radiation>No</Allow_Sky_Radiation>
<Sky_Temperature>20 C</Sky_Temperature>
</Sky_Radiation>
<Face_Subdivision>16</Face_Subdivision>
<Max_Number_of_Iterations>50</Max_Number_of_Iterations>
<Simulation_Results>
<Heat_Dissipated>0 W</Heat_Dissipated>
</Simulation_Results>
<Detailed_Solar_Intensity>
<Start_Date>01/01/2010</Start_Date>
<End_Date>31/12/2010</End_Date>
<Start_Time>09:00:00</Start_Time>
<End_Time>09:00:00</End_Time>
<Interval>60 min</Interval>
<Cloudiness>0</Cloudiness>
<Moisture>0.0045 kg/kg</Moisture>
<Visibility>50 km</Visibility>
<Chosen_Index/>
</Detailed_Solar_Intensity>
</Solar_Radiation>
<Heat_Radiation>
<Active>Yes</Active>
<Modelling_Level>Full</Modelling_Level>
<Heat_Radiation_Method>Hemisphere</Heat_Radiation_Method>
<View_Factor>
<Object_Polygon_Subdivision>6</Object_Polygon_Subdivision>
<Hemisphere_Base_Size>100</Hemisphere_Base_Size>
<Surface_Refinement_Level>2</Surface_Refinement_Level>
<Outline_Mismatch_Threshold>25 %</Outline_Mismatch_Threshold>
<Use_View_Factor_Adjustment>No</Use_View_Factor_Adjustment>
<Minimum_Area_Threshold>0.1 %</Minimum_Area_Threshold>
<Number_Of_Rays_Per_Triangle>51200</Number_Of_Rays_Per_Triangle>
<Use_GPU>No</Use_GPU>
<Use_Geometrical_Outlines>No</Use_Geometrical_Outlines>
</View_Factor>
<Allow_Surface_Subdivision>Yes</Allow_Surface_Subdivision>
<Store_Surface_Radiation>Yes</Store_Surface_Radiation>
</Heat_Radiation>
<Joule_Heating>
<Active>No</Active>
<Solve_For_Electric_Potential>Yes</Solve_For_Electric_Potential>
<Use_Gradient_Reconstruction>Yes</Use_Gradient_Reconstruction>
<Allow_Solution_To_Continue>Yes</Allow_Solution_To_Continue>
<Use_Region_Solution>Yes</Use_Region_Solution>
<Use_MPI>Yes</Use_MPI>
<Linear_Solver>CR</Linear_Solver>
<Iteration_Control>
<Solution_Interval>1</Solution_Interval>
<Termination_Criterion>0.0001</Termination_Criterion>
<Number_Of_Iterations>1000</Number_Of_Iterations>
<Inner_Iteration_Control>
<Termination_Criterion>0.001</Termination_Criterion>
<Number_Of_Iterations>1000</Number_Of_Iterations>
</Inner_Iteration_Control>
</Iteration_Control>
<Save_Solution_Region_Geometries>No</Save_Solution_Region_Geometries>
</Joule_Heating>
<Contamination_Control>
<Active>No</Active>
</Contamination_Control>
<Development_Control>
<Active>No</Active>
<Write_Variable_Min_Max_Values>No</Write_Variable_Min_Max_Values>
<Calculate_Wall_Distance_Field>No</Calculate_Wall_Distance_Field>
<Parallel_Solver_Emulator>No</Parallel_Solver_Emulator>
<Precision>Single</Precision>
<Number_Of_Partitions>1</Number_Of_Partitions>
<AMG_Coupling_Level>0</AMG_Coupling_Level>
<Save_Solution_Geometries>No</Save_Solution_Geometries>
<Heat_Radiation_Auxiliary_Options>
<Allow_Surface_Outline_Display>No</Allow_Surface_Outline_Display>
</Heat_Radiation_Auxiliary_Options>
</Development_Control>
<Generic_Scalar_Control>
<Active>No</Active>
</Generic_Scalar_Control>
<Mass_Balance>
<Check>Yes</Check>
<Allow_Imbalance_For_Time_Dependent_Flows>Yes</Allow_Imbalance_For_Time_Dependent_Flows>
<Global_Criterion>0.0001</Global_Criterion>
<Local_Criterion>0.00001</Local_Criterion>
</Mass_Balance>
<Device_Relaxation>
<Pressure_Relaxation>
<Adjust>Yes</Adjust>
<Mode>Automatic</Mode>
<Linear_Relaxation>1</Linear_Relaxation>
</Pressure_Relaxation>
<Flow_Rate_Relaxation>
<Adjust_Flow_Rate_Relaxation>No</Adjust_Flow_Rate_Relaxation>
<Flow_Rate_Linear_Relaxation>0.1</Flow_Rate_Linear_Relaxation>
</Flow_Rate_Relaxation>
</Device_Relaxation>
<Additional_Analysis>
<Run_Additional_Analysis_On_Cancel>No</Run_Additional_Analysis_On_Cancel>
<Effectiveness_Indices>
<Active>No</Active>
<Iteration_Control>
<Termination_Criterion>0.0001</Termination_Criterion>
<Number_Of_Iterations>10</Number_Of_Iterations>
<Inner_Iteration_Control>
<Termination_Criterion>0.01</Termination_Criterion>
<Number_Of_Iterations>100</Number_Of_Iterations>
</Inner_Iteration_Control>
</Iteration_Control>
</Effectiveness_Indices>
<ACU_Zones_of_Influence>
<Active>No</Active>
</ACU_Zones_of_Influence>
<Thermal_Comfort>
<Active>No</Active>
<Show_Auxiliary_Variables>No</Show_Auxiliary_Variables>
<Calculation_Parameters>
<Metabolic_Rate>58.15 W/m^2</Metabolic_Rate>
<External_Work>0 W/m^2</External_Work>
<Clothing_Thermal_Resistance>1 Clo</Clothing_Thermal_Resistance>
<Water_Vapour_Pressure>1400 Pa</Water_Vapour_Pressure>
<Above_Floor_Level>1.8 m</Above_Floor_Level>
</Calculation_Parameters>
<Simulation_Results>
<ADPI>0 %</ADPI>
</Simulation_Results>
</Thermal_Comfort>
<Humidity_Calculation>
<Active>No</Active>
<Iteration_Control>
<Termination_Criterion>0.00001</Termination_Criterion>
<Number_Of_Iterations>100</Number_Of_Iterations>
<Inner_Iteration_Control>
<Termination_Criterion>0.01</Termination_Criterion>
<Number_Of_Iterations>10</Number_Of_Iterations>
</Inner_Iteration_Control>
</Iteration_Control>
</Humidity_Calculation>
<Exergy_Loss>
<Active>No</Active>
<Exergy_Reference_Temperature>20 C</Exergy_Reference_Temperature>
<Exergy_Reference_Pressure>101330 Pa</Exergy_Reference_Pressure>
</Exergy_Loss>
</Additional_Analysis>
<Multiple_Solution_Regions>
<Remove_Passive_Regions>No</Remove_Passive_Regions>
<Use_Multiple_Reference_Temperatures>No</Use_Multiple_Reference_Temperatures>
<Stagnant_Cell_Adjustment>No</Stagnant_Cell_Adjustment>
<Store_Region_Geometry>No</Store_Region_Geometry>
<Write_Region_Summary>No</Write_Region_Summary>
</Multiple_Solution_Regions>
<Error_Fields>
<Store_Error_Fields>No</Store_Error_Fields>
</Error_Fields>
<Boundary_Attributes>
<Check_Boundary_Attributes>No</Check_Boundary_Attributes>
</Boundary_Attributes>
<Termination_Control>
<Termination_Strategy>Residuals Only</Termination_Strategy>
<Residual_Termination_Criteria>
<Termination_Factor>
<Value>1</Value>
<Use_Reference_Values>Yes</Use_Reference_Values>
<Use_Solid_Cell_Correction>No</Use_Solid_Cell_Correction>
<Use_Cell_Flux>Yes</Use_Cell_Flux>
</Termination_Factor>
<Ignored_Variables>
<Ignore_Temperature>No</Ignore_Temperature>
<Ignore_X_Velocity>No</Ignore_X_Velocity>
<Ignore_Y_Velocity>No</Ignore_Y_Velocity>
<Ignore_Z_Velocity>No</Ignore_Z_Velocity>
<Ignore_Pressure>No</Ignore_Pressure>
<Ignore_KE>No</Ignore_KE>
<Ignore_EP>No</Ignore_EP>
</Ignored_Variables>
</Residual_Termination_Criteria>
<Monitor_Termination_Criteria>
<Use_Sensors>Yes</Use_Sensors>
<Select_Additional_Monitors>By Object Type</Select_Additional_Monitors>
<Monitor_Objects>
<Use_Vent_Openings>Yes</Use_Vent_Openings>
<Use_Fans>Yes</Use_Fans>
<Use_ACUs>Yes</Use_ACUs>
<Use_Rows>Yes</Use_Rows>
<Use_Pumped_Returns>Yes</Use_Pumped_Returns>
<Use_Components>Yes</Use_Components>
<Use_IT_Equipment>Yes</Use_IT_Equipment>
<Use_Card_Enclosures>Yes</Use_Card_Enclosures>
</Monitor_Objects>
<Monitor_Data_Type>
<Use_Flow_Rates>Yes</Use_Flow_Rates>
<Use_Temperatures>Yes</Use_Temperatures>
</Monitor_Data_Type>
<Termination_Parameters>
<Number_of_Iterations_Analysed>20</Number_of_Iterations_Analysed>
<Gradient_Tolerance>0.003</Gradient_Tolerance>
<Maximum_RMS>0.00005</Maximum_RMS>
<Termination_Factor_Threshold>10</Termination_Factor_Threshold>
</Termination_Parameters>
</Monitor_Termination_Criteria>
</Termination_Control>
<Grid>
<Grid_Type>Unstructured</Grid_Type>
<Unstructured_Grid_Control>
<Level_Generation>Refine From Max Size</Level_Generation>
<Use_First_Level_2x2x2>Yes</Use_First_Level_2x2x2>
<First_Level_Coarsening_Limit>5 %</First_Level_Coarsening_Limit>
<Two_Dimensional_Grid>No</Two_Dimensional_Grid>
<Two_Dimensional_Grid_Direction>X-Y</Two_Dimensional_Grid_Direction>
<Single_Level_Grid>No</Single_Level_Grid>
<Limit_Refinement_Ratio>Yes</Limit_Refinement_Ratio>
<Refinement_Ratio_Limit>1</Refinement_Ratio_Limit>
<Use_Extrusion>Yes</Use_Extrusion>
<Eliminate_Dummy_Cells>Yes</Eliminate_Dummy_Cells>
<Gap_Refinement>Yes</Gap_Refinement>
<Push_Cells_To_Lower_Levels>No</Push_Cells_To_Lower_Levels>
<Store_Grid_Connectivity>Yes</Store_Grid_Connectivity>
<Grid_Plane_Display>
<X_Location>500 mm</X_Location>
<Y_Location>500 mm</Y_Location>
<Z_Location>500 mm</Z_Location>
<Height_Off_Floor>0 m</Height_Off_Floor>
<Grid_Level>Multilevel</Grid_Level>
</Grid_Plane_Display>
</Unstructured_Grid_Control>
<Cell_size_definition>Limited</Cell_size_definition>
<Grid_Rules_Definition_File>ET/Small Models.csv</Grid_Rules_Definition_File>
<Number_in_X>5</Number_in_X>
<Number_in_Y>5</Number_in_Y>
<Number_in_Z>5</Number_in_Z>
<Uniform>No</Uniform>
<Limit_Maximum_Cell_Size>Yes</Limit_Maximum_Cell_Size>
<Ignore_Top_Level_Grid_Rule>Yes</Ignore_Top_Level_Grid_Rule>
<Max_size_in_X>20 mm</Max_size_in_X>
<Max_size_in_Y>20 mm</Max_size_in_Y>
<Max_size_in_Z>20 mm</Max_size_in_Z>
<Cell_Count_Target>1000000000</Cell_Count_Target>
<X-Z_Cell_Size>0.1 m</X-Z_Cell_Size>
<Y_Cell_Size>0.1 m</Y_Cell_Size>
<Minimum_Gap_Size>0.01 mm</Minimum_Gap_Size>
<Enable_Heat_Conduction_Gridding>Yes</Enable_Heat_Conduction_Gridding>
<Use_Advanced_Grid_Controls>Yes</Use_Advanced_Grid_Controls>
<Use_Inflation>Yes</Use_Inflation>
<Apply_Smoothing>No</Apply_Smoothing>
<Aspect_Ratio_Limit>5</Aspect_Ratio_Limit>
<Expansion_Ratio_Limit>2</Expansion_Ratio_Limit>
<Mounting_Rail_Simplification>No</Mounting_Rail_Simplification>
<Grid_Summary>
<Grid_Cell_Count>743 741 (Finest grid 153 x 145 x 151)</Grid_Cell_Count>
<Grid_Cell_Count_Simple>743 741</Grid_Cell_Count_Simple>
<Auto_.40.Unlimited.41._Cell_Count>743 741</Auto_.40.Unlimited.41._Cell_Count>
<Cells_Added_In_Gaps>0</Cells_Added_In_Gaps>
<Dummy_Cells_Eliminated>0</Dummy_Cells_Eliminated>
<Available_Grid_Levels>Multilevel,Level 0,Level 1,Level 2,Level 3,Level 4,Level 5,Level 6,Level 7</Available_Grid_Levels>
<Percentage_Of_Unlimited>100.00 %</Percentage_Of_Unlimited>
<Number_Of_Levels>8
<Cells_At_Level_0>9514</Cells_At_Level_0>
<Cells_At_Level_1>64265</Cells_At_Level_1>
<Cells_At_Level_2>118183</Cells_At_Level_2>
<Cells_At_Level_3>58076</Cells_At_Level_3>
<Cells_At_Level_4>50321</Cells_At_Level_4>
<Cells_At_Level_5>288987</Cells_At_Level_5>
<Cells_At_Level_6>7362</Cells_At_Level_6>
<Cells_At_Level_7>147033</Cells_At_Level_7>
</Number_Of_Levels>
<Grid_Size_in_X>0</Grid_Size_in_X>
<Grid_Size_in_Y>0</Grid_Size_in_Y>
<Grid_Size_in_Z>0</Grid_Size_in_Z>
<Largest_Cells>
<Largest_X>0.02 @ 0.468, 0, 0 m</Largest_X>
<Largest_Y>0.0198667 @ 0, 0.488133, 0 m</Largest_Y>
<Largest_Z>0.019619 @ 0, 0, 0.35 m</Largest_Z>
</Largest_Cells>
<Smallest_Cells>
<Smallest_X>0.0005 @ 0.4745, 0.498, 0.448095 m</Smallest_X>
<Smallest_Y>3.5e-05 @ 0.4495, 0.51, 0.4545 m</Smallest_Y>
<Smallest_Z>0.0005 @ 0.458, 0.35, 0.517 m</Smallest_Z>
</Smallest_Cells>
<Maximum_Aspect_Ratio>57.1429 (X/Y) @ 0.45, 0.51, 0.4545 m</Maximum_Aspect_Ratio>
<Maximum_Expansion_Ratio>14.5714 (Y) @ 0.44975, 0.510035, 0.45475 m</Maximum_Expansion_Ratio>
<Maximum_Refinement_Ratio>1 (X) @ 0.35, 0.354933, 0.340278 m</Maximum_Refinement_Ratio>
</Grid_Summary>
</Grid>
<Miscellaneous>
<Use_Potential_Flow_Solver>No</Use_Potential_Flow_Solver>
<Use_Region_Solvers>No</Use_Region_Solvers>
<Use_Double_Precision>No</Use_Double_Precision>
<Linear_Solver>CR</Linear_Solver>
<Reorder_Region_Cell_Indices>No</Reorder_Region_Cell_Indices>
<Potential_Flow_Solver_Control>
<Iteration_Control>
<Termination_Criterion>0.001</Termination_Criterion>
<Number_Of_Iterations>1000</Number_Of_Iterations>
<Inner_Iteration_Control>
<Termination_Criterion>0.01</Termination_Criterion>
<Number_Of_Iterations>100</Number_Of_Iterations>
</Inner_Iteration_Control>
</Iteration_Control>
</Potential_Flow_Solver_Control>
<Use_Double_Precision_Thermal_Solver>Yes</Use_Double_Precision_Thermal_Solver>
<Use_Face_Velocity_Solver>No</Use_Face_Velocity_Solver>
<Use_Cell_Momentum_Convection>Yes</Use_Cell_Momentum_Convection>
<Use_Gradient_Reconstruction_Scheme>No</Use_Gradient_Reconstruction_Scheme>
<Pressure_Correction_Coefficients>Convection Only</Pressure_Correction_Coefficients>
<Store_Computational_Geometry>Yes</Store_Computational_Geometry>
<Combine_Cell_Computational_Geometry>Yes</Combine_Cell_Computational_Geometry>
<Simplify_Computational_Geometry>Yes</Simplify_Computational_Geometry>
<Multilevel_Computational_Geometry>Yes</Multilevel_Computational_Geometry>
<Delete_Temporary_Solver_Files>Yes</Delete_Temporary_Solver_Files>
<Binary_Output>Yes</Binary_Output>
<Save_Profiling_Info>No</Save_Profiling_Info>
<Ignore_Top_AMG_Coarse_Level>Yes</Ignore_Top_AMG_Coarse_Level>
<Use_Edge_Blocking_Info>No</Use_Edge_Blocking_Info>
<Exclude_Blocked_Momentum_Cells>No</Exclude_Blocked_Momentum_Cells>
<Store_Cell_Momentum_Fields>Yes</Store_Cell_Momentum_Fields>
</Miscellaneous>
<Parallel_Control>
<Delete_Distributed_Data>Yes</Delete_Distributed_Data>
<Apply_AMG_Extension>Yes</Apply_AMG_Extension>
<Coupling_Level>0</Coupling_Level>
<Domain_Decomposition>
<Direction>Auto</Direction>
<Area_to_Load_Balance_Weighting>1</Area_to_Load_Balance_Weighting>
<Use_Edge_Weighted_Partitioning>No</Use_Edge_Weighted_Partitioning>
<Use_Coarse_Graph_For_Partitioning>Yes</Use_Coarse_Graph_For_Partitioning>
<Extend_Communication_Buffers>Yes</Extend_Communication_Buffers>
</Domain_Decomposition>
</Parallel_Control>
<Thermal_Resistor_Network>
<Use_Network_For_2R_Components>Yes</Use_Network_For_2R_Components>
<Limit_External_Resistance>No</Limit_External_Resistance>
<External_Resistance_Limiting_Factor>0.01</External_Resistance_Limiting_Factor>
<Use_Single_Limiting_Value>No</Use_Single_Limiting_Value>
<Use_False_Time_Relaxation>No</Use_False_Time_Relaxation>
<Link_To_Linear_Solver>No</Link_To_Linear_Solver>
<Maximum_Number_Of_Local_Iterations>10</Maximum_Number_Of_Local_Iterations>
<Local_Residual_Reduction_Factor>0.5</Local_Residual_Reduction_Factor>
<Compact_Component_Generator>
<Solver_Type>GDHN</Solver_Type>
<Weight_Factor>0.5</Weight_Factor>
<Resistor_Initial_Value>10</Resistor_Initial_Value>
<Maximum_Resistor_Bound>100000</Maximum_Resistor_Bound>
<Minimum_Resistor_Bound>0.00001</Minimum_Resistor_Bound>
<Resistor_Perturbation_Factor>0.0001</Resistor_Perturbation_Factor>
<Convergence_Criterion>1e-07</Convergence_Criterion>
<Maximum_Number_Of_Iterations>1000</Maximum_Number_Of_Iterations>
<Output_interval>1</Output_interval>
</Compact_Component_Generator>
</Thermal_Resistor_Network>
<Variables>
<Initial_Values_From_Open_Boundaries>Yes</Initial_Values_From_Open_Boundaries>
<Temperature>
<Variable_Name>Temperature</Variable_Name>
<Initial_Value_Option>Auto</Initial_Value_Option>
<Initial_Value>20 C</Initial_Value>
<Stop_Residual_Sum>0.0004</Stop_Residual_Sum>
<False_Time_Step>10000</False_Time_Step>
<Outer_Linear_Relaxation>1</Outer_Linear_Relaxation>
<Maximum_Bound>10000000000</Maximum_Bound>
<Minimum_Bound>-10000000000</Minimum_Bound>
<Maximum_Inner_Iterations>50</Maximum_Inner_Iterations>
<Structured_Linear_Solver>AMG</Structured_Linear_Solver>
<Unstructured_Linear_Solver>AMG</Unstructured_Linear_Solver>
<Structured_AMG_Control>
<AMG_Type>Flexible V Cycle</AMG_Type>
<Maximum_Number_of_Levels>10</Maximum_Number_of_Levels>
<Maximum_Number_of_Relaxations>5</Maximum_Number_of_Relaxations>
<Maximum_Number_of_Iterations>1000</Maximum_Number_of_Iterations>
<Agglomeration_Type>Level Grid</Agglomeration_Type>
<Prolongation_Relaxation_Type>Linear</Prolongation_Relaxation_Type>
<Inertia_Relaxation>0.1</Inertia_Relaxation>
<Prolongation_Relaxation>0.8</Prolongation_Relaxation>
<Residual_Reduction>0.15</Residual_Reduction>
</Structured_AMG_Control>
<Unstructured_AMG_Control>
<AMG_Type>Flexible V Cycle</AMG_Type>
<Maximum_Number_of_Levels>10</Maximum_Number_of_Levels>
<Maximum_Number_of_Relaxations>5</Maximum_Number_of_Relaxations>
<Maximum_Number_of_Iterations>1000</Maximum_Number_of_Iterations>
<Agglomeration_Type>Level Grid</Agglomeration_Type>
<Prolongation_Relaxation_Type>Linear</Prolongation_Relaxation_Type>
<Inertia_Relaxation>0.1</Inertia_Relaxation>
<Prolongation_Relaxation>0.9</Prolongation_Relaxation>
<Residual_Reduction>0.15</Residual_Reduction>
<Exclude_Fix_Value_Cells>No</Exclude_Fix_Value_Cells>
</Unstructured_AMG_Control>
<Use_Gradient_Reconstruction>No</Use_Gradient_Reconstruction>
<Convection_Scheme>FOU</Convection_Scheme>
<Field_Precision>Double</Field_Precision>
<Use_Initial_Relaxation_Control>No</Use_Initial_Relaxation_Control>
<Number_Of_Initial_Iterations>10</Number_Of_Initial_Iterations>
<Initial_False_Time_Step>10</Initial_False_Time_Step>
</Temperature>
<KE>
<Variable_Name>KE</Variable_Name>
<Initial_Value>0.001 m2/s2</Initial_Value>
<Stop_Residual_Sum>0.001</Stop_Residual_Sum>
<False_Time_Step>0.1</False_Time_Step>
<Outer_Linear_Relaxation>1</Outer_Linear_Relaxation>
<Maximum_Bound>10000000000</Maximum_Bound>
<Minimum_Bound>1e-10</Minimum_Bound>
<Maximum_Inner_Iterations>2</Maximum_Inner_Iterations>
<Linear_Solver>CR</Linear_Solver>
<AMG_Control>
<AMG_Type>Flexible V Cycle</AMG_Type>
<Maximum_Number_of_Levels>10</Maximum_Number_of_Levels>
<Maximum_Number_of_Relaxations>5</Maximum_Number_of_Relaxations>
<Maximum_Number_of_Iterations>1000</Maximum_Number_of_Iterations>
<Prolongation_Relaxation>0.9</Prolongation_Relaxation>
<Residual_Reduction>0.15</Residual_Reduction>
</AMG_Control>
<Use_Gradient_Reconstruction>No</Use_Gradient_Reconstruction>
<Convection_Scheme>FOU</Convection_Scheme>
</KE>
<EP>
<Variable_Name>EP</Variable_Name>
<Initial_Value>0.01 m2/s3</Initial_Value>
<Stop_Residual_Sum>0.001</Stop_Residual_Sum>
<False_Time_Step>0.1</False_Time_Step>
<Outer_Linear_Relaxation>1</Outer_Linear_Relaxation>
<Maximum_Bound>10000000000</Maximum_Bound>
<Minimum_Bound>1e-10</Minimum_Bound>
<Maximum_Inner_Iterations>2</Maximum_Inner_Iterations>
<Linear_Solver>CR</Linear_Solver>
<AMG_Control>
<AMG_Type>Flexible V Cycle</AMG_Type>
<Maximum_Number_of_Levels>10</Maximum_Number_of_Levels>
<Maximum_Number_of_Relaxations>5</Maximum_Number_of_Relaxations>
<Maximum_Number_of_Iterations>1000</Maximum_Number_of_Iterations>
<Prolongation_Relaxation>0.9</Prolongation_Relaxation>
<Residual_Reduction>0.15</Residual_Reduction>
</AMG_Control>
<Use_Gradient_Reconstruction>No</Use_Gradient_Reconstruction>
<Convection_Scheme>FOU</Convection_Scheme>
</EP>
<X_Velocity>
<Variable_Name>X Velocity</Variable_Name>
<Initial_Value>0 m/s</Initial_Value>
<Stop_Residual_Sum>0.001</Stop_Residual_Sum>
<False_Time_Step>0.1</False_Time_Step>
<Outer_Linear_Relaxation>1</Outer_Linear_Relaxation>
<Maximum_Bound>50</Maximum_Bound>
<Minimum_Bound>-50</Minimum_Bound>
<Maximum_Inner_Iterations>2</Maximum_Inner_Iterations>
<Linear_Solver>CR</Linear_Solver>
<AMG_Control>
<AMG_Type>Flexible V Cycle</AMG_Type>
<Maximum_Number_of_Levels>10</Maximum_Number_of_Levels>
<Maximum_Number_of_Relaxations>5</Maximum_Number_of_Relaxations>
<Maximum_Number_of_Iterations>1000</Maximum_Number_of_Iterations>
<Prolongation_Relaxation>0.9</Prolongation_Relaxation>
<Residual_Reduction>0.15</Residual_Reduction>
</AMG_Control>
<Use_Gradient_Reconstruction>No</Use_Gradient_Reconstruction>
<Convection_Scheme>FOU</Convection_Scheme>
</X_Velocity>
<Y_Velocity>
<Variable_Name>Y Velocity</Variable_Name>
<Initial_Value>0 m/s</Initial_Value>
<Stop_Residual_Sum>0.001</Stop_Residual_Sum>
<False_Time_Step>0.1</False_Time_Step>
<Outer_Linear_Relaxation>1</Outer_Linear_Relaxation>
<Maximum_Bound>50</Maximum_Bound>
<Minimum_Bound>-50</Minimum_Bound>
<Maximum_Inner_Iterations>2</Maximum_Inner_Iterations>
<Linear_Solver>CR</Linear_Solver>
<AMG_Control>
<AMG_Type>Flexible V Cycle</AMG_Type>
<Maximum_Number_of_Levels>10</Maximum_Number_of_Levels>
<Maximum_Number_of_Relaxations>5</Maximum_Number_of_Relaxations>
<Maximum_Number_of_Iterations>1000</Maximum_Number_of_Iterations>
<Prolongation_Relaxation>0.9</Prolongation_Relaxation>
<Residual_Reduction>0.15</Residual_Reduction>
</AMG_Control>
<Use_Gradient_Reconstruction>No</Use_Gradient_Reconstruction>
<Convection_Scheme>FOU</Convection_Scheme>
</Y_Velocity>
<Z_Velocity>
<Variable_Name>Z Velocity</Variable_Name>
<Initial_Value>0 m/s</Initial_Value>
<Stop_Residual_Sum>0.001</Stop_Residual_Sum>
<False_Time_Step>0.1</False_Time_Step>
<Outer_Linear_Relaxation>1</Outer_Linear_Relaxation>
<Maximum_Bound>50</Maximum_Bound>
<Minimum_Bound>-50</Minimum_Bound>
<Maximum_Inner_Iterations>2</Maximum_Inner_Iterations>
<Linear_Solver>CR</Linear_Solver>
<AMG_Control>
<AMG_Type>Flexible V Cycle</AMG_Type>
<Maximum_Number_of_Levels>10</Maximum_Number_of_Levels>
<Maximum_Number_of_Relaxations>5</Maximum_Number_of_Relaxations>
<Maximum_Number_of_Iterations>1000</Maximum_Number_of_Iterations>
<Prolongation_Relaxation>0.9</Prolongation_Relaxation>
<Residual_Reduction>0.15</Residual_Reduction>
</AMG_Control>
<Use_Gradient_Reconstruction>No</Use_Gradient_Reconstruction>
<Convection_Scheme>FOU</Convection_Scheme>
</Z_Velocity>
<Pressure>
<Variable_Name>Pressure</Variable_Name>
<Initial_Value>0 Pa</Initial_Value>
<Stop_Residual_Sum>0.001</Stop_Residual_Sum>
<False_Time_Step>10000000000</False_Time_Step>
<Outer_Linear_Relaxation>0.75</Outer_Linear_Relaxation>
<Maximum_Bound>10000000000</Maximum_Bound>
<Minimum_Bound>-10000000000</Minimum_Bound>
<Maximum_Inner_Iterations>50</Maximum_Inner_Iterations>
<Linear_Solver>CR</Linear_Solver>
<AMG_Control>
<AMG_Type>Flexible V Cycle</AMG_Type>
<Maximum_Number_of_Levels>10</Maximum_Number_of_Levels>
<Maximum_Number_of_Relaxations>5</Maximum_Number_of_Relaxations>
<Maximum_Number_of_Iterations>1000</Maximum_Number_of_Iterations>
<Prolongation_Relaxation>0.9</Prolongation_Relaxation>
<Residual_Reduction>0.15</Residual_Reduction>
</AMG_Control>
<Use_Gradient_Reconstruction>No</Use_Gradient_Reconstruction>
<Field_Precision>Single</Field_Precision>
</Pressure>
<Humidity>
<Variable_Name>Humidity</Variable_Name>
<Initial_Value>0 kg/kg</Initial_Value>
<Stop_Residual_Sum>0.001</Stop_Residual_Sum>
<False_Time_Step>10</False_Time_Step>
<Outer_Linear_Relaxation>1</Outer_Linear_Relaxation>
<Maximum_Bound>10000000000</Maximum_Bound>
<Minimum_Bound>0</Minimum_Bound>
<Maximum_Inner_Iterations>10</Maximum_Inner_Iterations>
<Linear_Solver>CR</Linear_Solver>
<AMG_Control>
<AMG_Type>Flexible V Cycle</AMG_Type>
<Maximum_Number_of_Levels>10</Maximum_Number_of_Levels>
<Maximum_Number_of_Relaxations>5</Maximum_Number_of_Relaxations>
<Maximum_Number_of_Iterations>1000</Maximum_Number_of_Iterations>
<Prolongation_Relaxation>0.9</Prolongation_Relaxation>
<Residual_Reduction>0.15</Residual_Reduction>
</AMG_Control>
<Use_Gradient_Reconstruction>No</Use_Gradient_Reconstruction>
<Convection_Scheme>FOU</Convection_Scheme>
</Humidity>
<Contamination>
<Variable_Name>Contamination</Variable_Name>
<Initial_Value>0 %</Initial_Value>
<Stop_Residual_Sum>0.001</Stop_Residual_Sum>
<False_Time_Step>10</False_Time_Step>
<Outer_Linear_Relaxation>1</Outer_Linear_Relaxation>
<Maximum_Bound>10000000000</Maximum_Bound>
<Minimum_Bound>1e-10</Minimum_Bound>
<Maximum_Inner_Iterations>10</Maximum_Inner_Iterations>
<Linear_Solver>CR</Linear_Solver>
<AMG_Control>
<AMG_Type>Flexible V Cycle</AMG_Type>
<Maximum_Number_of_Levels>10</Maximum_Number_of_Levels>
<Maximum_Number_of_Relaxations>5</Maximum_Number_of_Relaxations>
<Maximum_Number_of_Iterations>1000</Maximum_Number_of_Iterations>
<Prolongation_Relaxation>0.9</Prolongation_Relaxation>
<Residual_Reduction>0.15</Residual_Reduction>
</AMG_Control>
<Use_Gradient_Reconstruction>No</Use_Gradient_Reconstruction>
<Convection_Scheme>FOU</Convection_Scheme>
</Contamination>
<Generic_Scalar>
<Variable_Name>Generic Scalar</Variable_Name>
<Initial_Value>0</Initial_Value>
<Stop_Residual_Sum>0.001</Stop_Residual_Sum>
<False_Time_Step>10</False_Time_Step>
<Outer_Linear_Relaxation>1</Outer_Linear_Relaxation>
<Maximum_Bound>10000000000</Maximum_Bound>
<Minimum_Bound>0</Minimum_Bound>
<Maximum_Inner_Iterations>10</Maximum_Inner_Iterations>
<Linear_Solver>CR</Linear_Solver>
<AMG_Control>
<AMG_Type>Flexible V Cycle</AMG_Type>
<Maximum_Number_of_Levels>10</Maximum_Number_of_Levels>
<Maximum_Number_of_Relaxations>5</Maximum_Number_of_Relaxations>
<Maximum_Number_of_Iterations>1000</Maximum_Number_of_Iterations>
<Prolongation_Relaxation>0.9</Prolongation_Relaxation>
<Residual_Reduction>0.15</Residual_Reduction>
</AMG_Control>
<Use_Gradient_Reconstruction>No</Use_Gradient_Reconstruction>
<Convection_Scheme>FOU</Convection_Scheme>
</Generic_Scalar>
</Variables>
<Generic_Scalars>
<Settings>
<Number_Of_Generic_Scalars>0
</Number_Of_Generic_Scalars>
</Settings>
</Generic_Scalars>
<Auxiliary_Variables>
<Store_Total_Pressure>No</Store_Total_Pressure>
<Store_Density>No</Store_Density>
<Store_Heat_Fluxes>Yes</Store_Heat_Fluxes>
<Store_Laminar_Viscosity>No</Store_Laminar_Viscosity>
<Store_Conductivity>No</Store_Conductivity>
<Store_Specific_Heat>No</Store_Specific_Heat>
</Auxiliary_Variables>
<Zoom_In_Volume>
<X_Location>0</X_Location>
<Y_Location>0</Y_Location>
<Z_Location>0</Z_Location>
<X_Size>0</X_Size>
<Y_Size>0</Y_Size>
<Z_Size>0</Z_Size>
<Zoom_In_Control>
<Modelling_Detail>Room Level</Modelling_Detail>
<Apply_Cell_Count_Target_to>Whole Room</Apply_Cell_Count_Target_to>
</Zoom_In_Control>
</Zoom_In_Volume>
<Stored_Simulation_Results>
<Store_for_Inflows>No</Store_for_Inflows>
<Store_for_Outflows>No</Store_for_Outflows>
<Store_for_Holes>No</Store_for_Holes>
<Solution_Summary>No</Solution_Summary>
</Stored_Simulation_Results>
<External_Format_Output>
<VTK>No</VTK>
<VTM>No</VTM>
<Include_All_Data>No</Include_All_Data>
</External_Format_Output>
<Reference_Data>
<Velocity>1 m/s</Velocity>
<Density>1 kg/m^3</Density>
<Pressure>0 Pa</Pressure>
</Reference_Data>
<Simulation_Results>
<Model_Status>-1</Model_Status>
<Steady_State_Solution_Available>No</Steady_State_Solution_Available>
<Transient_Results>No</Transient_Results>
<Transient_Simulation_Results>No</Transient_Simulation_Results>
<Available_Variables>Temperature,Velocity,X Velocity,Y Velocity,Z Velocity,Pressure,KE,EP</Available_Variables>
<Available_Vector_Variables>Velocity</Available_Vector_Variables>
<Available_Flow_Solution_Regions>1</Available_Flow_Solution_Regions>
<HasSolvedContaminants>No</HasSolvedContaminants>
<Parallel_Solution>No</Parallel_Solution>
<Grid_Generation_Time>0 s</Grid_Generation_Time>
<Overall_CFD_Generation_Time>0 s</Overall_CFD_Generation_Time>
<Radiation_View_Factor_Time>0 s</Radiation_View_Factor_Time>
<Radiation_Absorption_Factor_Time>0 s</Radiation_Absorption_Factor_Time>
<Joule_Heating_Time>0 s</Joule_Heating_Time>
<Last_Solver_Run_Time>0 s</Last_Solver_Run_Time>
<Cumulative_Solver_Time>0 s</Cumulative_Solver_Time>
<Last_Solver_Run_Number_Of_Iterations/>
<Cumulative_Number_Of_Iterations/>
<Last_Solver_Run_Number_Of_Time_Steps/>
<Cumulative_Number_Of_Time_Steps/>
<Number_Of_Processes/>
<Parallel_Data_Decomposition_Time>0 s</Parallel_Data_Decomposition_Time>
<Parallel_Data_Reassembly_Time>0 s</Parallel_Data_Reassembly_Time>
<Update_From_CFD_Solution_Time>0 s</Update_From_CFD_Solution_Time>
</Simulation_Results>
<Run_Configurations/>
<Zones_Of_Influence>
<Type>Air Cooling Unit</Type>
<Source_ACUs/>
<Sink_Cabinets/>
</Zones_Of_Influence>
<SolverExchange_Control>
<Active>No</Active>
<Extend_Results>No</Extend_Results>
<Advanced_Controls>No</Advanced_Controls>
<Mode>FileParser</Mode>
<FileParser_Properties>
<Exchange_Format>CSV</Exchange_Format>
<File_Mode>Default</File_Mode>
<Sync_Mode>Each Iteration</Sync_Mode>
<Limit_input_file_try_attempts>Yes</Limit_input_file_try_attempts>
<Input_file_try_attempts>1000</Input_file_try_attempts>
</FileParser_Properties>
<User-Defined_DLL_Properties>
<Linux_Support>No</Linux_Support>
<Event_Handler/>
</User-Defined_DLL_Properties>
</SolverExchange_Control>
</Solution_Control>
</SolutionControlLink>
<StreamlineOptionsLink>
<Streamline_Options id="45995-47734">
<Construction>
<Number_of_Frames>24</Number_of_Frames>
<Particle_Synchronisation>0.3</Particle_Synchronisation>
<Reset_Particles>No</Reset_Particles>
<Apply_Smoothing>Yes</Apply_Smoothing>
</Construction>
<Geometry>
<Ribbon_Width>0.5</Ribbon_Width>
<Texture_Length>0.5</Texture_Length>
<Texture_Spacing>0.5</Texture_Spacing>
</Geometry>
<Display_Options>
<Ribbon_Transparency>0</Ribbon_Transparency>
</Display_Options>
</Streamline_Options>
</StreamlineOptionsLink>
<ResultPlaneOptionsLink>
<Result_Plane_Options id="45995-47735">
<Animation_Options>
<Number_of_Frames>24</Number_of_Frames>
</Animation_Options>
<Standard_Plots>
<Update_All>Yes</Update_All>
<Show_Grid>No</Show_Grid>
<Plot_Type>Variation Plot Smooth</Plot_Type>
</Standard_Plots>
</Result_Plane_Options>
</ResultPlaneOptionsLink>
<TransientOptionsLink>
<Transient_Options id="45995-47736">
<Time_step_dependent>No</Time_step_dependent>
<Frames_per_output>5</Frames_per_output>
<Frames_per_second>5</Frames_per_second>
</Transient_Options>
</TransientOptionsLink>
<GIFOptionsLink>
<GIF_Options id="45995-47737">
<Frames_per_second>10</Frames_per_second>
<Dither>No</Dither>
</GIF_Options>
</GIFOptionsLink>
<SpinOptionsLink>
<Spin_Options id="45995-47738">
<Spin_Model>No</Spin_Model>
<Spin_Direction>Clockwise</Spin_Direction>
<Frames_per_Revolution>360</Frames_per_Revolution>
</Spin_Options>
</SpinOptionsLink>
<MovieOptionsLink>
<Movie_Options id="45995-47739">
<Frames_per_second>30</Frames_per_second>
<Quality>90</Quality>
</Movie_Options>
</MovieOptionsLink>
<ImageOptionsLink/>
<GeneralAnimationOptionsLink>
<General_Animation_Options id="45995-47740">
<Maximum_Animation_Speed_.40.FPS.41.>100</Maximum_Animation_Speed_.40.FPS.41.>
</General_Animation_Options>
</GeneralAnimationOptionsLink>
<Result_Planes/>
<Profile_Plots/>
<Profile_Plot_Collections/>
<Result_Volumes/>
<Push_Pins/>
<MaxMins/>
<Flow_Solution_Regions/>
<Fogs/>
<Cameras/>
<Walkthroughs/>
<Solids/>
<PressureDatumLink/>
<UserDefinedDLLList/>
<LatticeBoltzmannControlLink>
<Lattice_Boltzmann_Control id="45995-47741">
<Number_Of_Iterations>1000</Number_Of_Iterations>
<Flow_Field_Output_Interval>10</Flow_Field_Output_Interval>
<Relaxation_Time>1</Relaxation_Time>
<Lattice_Spacing>1 mm</Lattice_Spacing>
</Lattice_Boltzmann_Control>
</LatticeBoltzmannControlLink>
<CAD_Planes/>
<Exchange_Sets/>
<ControllerViews/>
</ET_Project>
</DataDefinition>
"""