from converter import *
from loader import *
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

time,data = take_time(readSMCFile("../Control-6DOF-simulator-robot/smc_files/OTAV.HN1.IU.20_a.smc").get('data'))
print(max(data))
plt.plot(time,data, "r-")
#plt.axis([0,1,2,3])
plt.title("Aceleración en eje X gráfico de simulación")
plt.xlabel("segundos")
plt.ylabel("centímetros")
plt.show()

time,data = take_time(readSMCFile("../Control-6DOF-simulator-robot/smc_files/OTAV.HN1.IU.20_d.smc").get('data'))
print(max(data))
plt.plot(time,data, "r-")
#plt.axis([0,1,2,3])
plt.title("Desplazamiento en eje X gráfico de simulación")
plt.xlabel("segundos")
plt.ylabel("mm")
plt.show()

time,data = take_time(readSMCFile("../Control-6DOF-simulator-robot/smc_files/OTAV.HN2.IU.20_d.smc").get('data'))
print(max(data))
plt.plot(time,data, "r-")
#plt.axis([0,1,2,3])
plt.title("Desplazamiento en eje Y gráfico de simulación")
plt.xlabel("segundos")
plt.ylabel("desplazamiento mm")
plt.show()

time,data = take_time(readSMCFile("../Control-6DOF-simulator-robot/smc_files/OTAV.HN2.IU.20_a.smc").get('data'))
print(max(data))
plt.plot(time,data, "r-")
#plt.axis([0,1,2,3])
plt.title("Aceleración en eje Y gráfico de simulación")
plt.xlabel("segundos")
plt.ylabel("centímetros")
plt.show()

time,data = take_time(readSMCFile("../Control-6DOF-simulator-robot/smc_files/OTAV.HNZ.IU.20_d.smc").get('data'))
print(max(data))
plt.plot(time,data, "r-")
#plt.axis([0,1,2,3])
plt.title("Desplazamiento en eje Z gráfico de simulación")
plt.xlabel("segundos")
plt.ylabel("desplazamiento mm")
plt.show()

time,data = take_time(readSMCFile("../Control-6DOF-simulator-robot/smc_files/OTAV.HNZ.IU.20_a.smc").get('data'))
print(max(data))
plt.plot(time,data, "r-")
#plt.axis([0,1,2,3])
plt.title("Aceleración en eje Z gráfico de simulación")
plt.xlabel("segundos")
plt.ylabel("centímetros")
plt.show()

