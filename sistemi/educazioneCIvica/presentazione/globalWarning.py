import matplotlib as mpl
mpl.use('TkAgg')
import matplotlib.pyplot as plt
import csv

aumentoTemperatura = []
emissioni = []
anni = []
data_file = open("./globalWarning.csv")
data_reader = csv.reader(data_file, delimiter=',')
for row in data_reader:
    anni.append(int(row[0]))
    aumentoTemperatura.append(float(row[1]))
    emissioni.append(float(row[2]))
data_file.close()
    
fig, (ax1, ax2, ax3) = plt.subplots(2, 1, figsize= (11, 15))
fig.suptitle('Correlazione tra aumento della temperatua terrestre media annua e l''emissioni globali')

ax1.plot(anni, aumentoTemperatura, 'red', linewidth = 5)
ax1.set_xlabel('Anni')
ax1.set_ylabel('Aumento temperatura terrestre media (°C)')
ax1.grid()

ax2.plot(anni, emissioni, 'green', linewidth = 5)
ax2.set_xlabel('Anni')
ax2.set_ylabel('Emisioni co2 in miliardi di tonnellate')
ax2.grid()

plt.show()