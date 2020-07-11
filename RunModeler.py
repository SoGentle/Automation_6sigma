import os
import time
import subprocess

from Modeler import SimplePCB

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

Layers_Thickness=[0.035, 0.07, 0.035, 0.035, 0.03, 0.07, 0.07, 0.03, 0.035, 0.035, 0.07, 0.035]
Layers_Percentage=[85, 75, 80, 90, 95, 95, 95, 95, 90, 80, 75, 85]

Board1.setLayersInfo(Layers=12, Thickness=Layers_Thickness, Percentage=Layers_Percentage)

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
#CurrentFolder=os.path.abspath(__file__)
CurrentFolder=os.getcwd()
ResultFileFullPath=os.path.join(CurrentFolder, ResultFile)
print(ResultFileFullPath)
ETSolver='"C:\\Program Files\\6SigmaETRelease14\\6SigmaEmbeddedSolver.exe"'

BatchCommand = ETSolver + " -xmlmodel " + ResultFile + " -licenseserver 10.230.22.106 4242 -decodeSimulationResults"

print("RunSimulation")

while True:
    try:
        returend_output = subprocess.check_output(BatchCommand)
        print("DONE")
        break
    except:
        time.sleep(10)
    
print("--------------------------------")
print(returend_output)
#os.system(BatchCommand)


print("------------END--------------")