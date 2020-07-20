import xml.etree.ElementTree as ET
import os

Components = []

# def getResultFile(SimulationFile):

def getResult(SimulationFile, Components):
    Folder = os.path.dirname(SimulationFile)
    File = os.path.basename(SimulationFile)
    ProjectFolder = os.path.join(Folder, File[:-4])
    ResultFolder = os.path.join(ProjectFolder, File[:-4])
    ResultFile = os.path.join(ResultFolder, 'Baseline.simulationresults')
    # print(Folder, File, ResultFile)

    tree = ET.parse(ResultFile)
    root = tree.getroot()
    for numb, Component in enumerate(Components):
        print(numb, Component['id'])
        ExtendEntity = root.find("./ExtendEntity/[@id='"+Component['id']+"']")
        Simulation_Results = ExtendEntity.find("Simulation_Results/Volume_Temperature/Maximum_Volume_Temperature").text
        # print(round(float(Simulation_Results[:-2]), 1))
        Components[numb]['JunctionTemp'] = round(float(Simulation_Results[:-2]), 1)
        if Component['Modelling_Level'] == "2R":
            CaseTemp = ExtendEntity.find("Simulation_Results/Case_Temperature").text
            Components[numb]['TopTemp'] = round(float(CaseTemp[:-2]), 1)
            BoardTemp = ExtendEntity.find("Simulation_Results/Board_Temperature").text
            Components[numb]['BottomTemp'] = round(float(BoardTemp[:-2]), 1)  
    return Components


        # ExtendEntity = root.find("./ExtendEntity/[@id='"+'45995-32002'+"']")
        # Simulation_Results = ExtendEntity.find("Simulation_Results/Volume_Temperature/Maximum_Volume_Temperature").text
        # Simulation_Results1 = ExtendEntity.find("Simulation_Results/Case_Temperature").text
        # Simulation_Results2 = ExtendEntity.find("Simulation_Results/Board_Temperature").text
        # print(round(float(Simulation_Results[:-2]), 1))
        # print(Simulation_Results1, Simulation_Results2)
    

    # print(DataDefinition)
    # for numb, Component in enumerate(Components):
        # print(root)
        # 
        # print(Component['id'])
        # print(DataDefinition.find('ExtendEntity').attrib['id']) #/[@id='+Component['id'] +']')


def addComponent(name, X=0, Z=0, side='Top', width=5, depth=5, height=2, material='Si(Silicon)', TIM='No', powerType='Simplified', power=1, junction2Case = 1, junction2Board=10):
    if powerType == 'Simplified':
        Components.append({'Reference_Designator':name, 'X_Location': X, 'Z_Location':Z, 'Board_Side':side, 'Width':width, 'Depth':depth, 'Height':height, 'MaterialLink':material, 'TIM':TIM, 'Modelling_Level':'Simplified', 'Thermal_Design_Power': power })
    elif powerType == '2R':
        Components.append({'Reference_Designator':name, 'X_Location': X, 'Z_Location':Z, 'Board_Side':side, 'Width':width, 'Depth':depth, 'Height':height, 'MaterialLink':material, 'TIM':TIM, 'Modelling_Level':'2R', 'Thermal_Design_Power':power, 'Junction-to-Case_Thermal_Resistance': junction2Case, 'Junction-to-Board_Thermal_Resistance': junction2Case })
    else:
        print('Error: Undefined power type!')

if __name__ == "__main__":
    addComponent(name="U_T_Sim", X=20, Z=50, side='Top', width=4, depth=5, height=3, material='Si(Silicon)', TIM='No', powerType='Simplified', power=1)
    addComponent(name="U_T_Sim_TIM", X=40, Z=50, side='Top', width=4, depth=5, height=3, material='Si(Silicon)', TIM='Yes', powerType='Simplified', power=1)
    addComponent(name="U_T_2R", X=60, Z=50, side='Top', width=4, depth=5, height=3, material='Si(Silicon)', TIM='No', powerType='2R', power=1, junction2Case = 1, junction2Board=10)
    addComponent(name="U_T_2R_TIM", X=80, Z=50, side='Top', width=4, depth=5, height=3, material='Si(Silicon)', TIM='Yes', powerType='2R', power=1, junction2Case = 1, junction2Board=10)
    Components[0]['id'] = "45995-"+str(32000+0)
    Components[1]['id'] = "45995-"+str(32000+1)
    Components[2]['id'] = "45995-"+str(32000+2)
    Components[3]['id'] = "45995-"+str(32000+3)
    FullPath = "/Users/sogentle/Projects/Automation_6sigma_simulation/Result.xml"
    Result = getResult(SimulationFile=FullPath, Components=Components)
    print(Result)
    for comp in Result:
        print(comp)
        print("-----------")