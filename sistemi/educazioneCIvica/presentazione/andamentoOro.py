import matplotlib as mpl
mpl.use('TkAgg')
import matplotlib.pyplot as plt
import csv

andamentoOro = []
anni = []
data_file = open("./andamentoOro.csv")
data_reader = csv.reader(data_file, delimiter=',')
for row in data_reader:
    anni.append(int(row[0]))
    andamentoOro.append(float(row[1]))
data_file.close()
    
fig, (ax1) = plt.subplots(1, 1, figsize= (5, 5))
fig.suptitle('AndamentoOro')

ax1.plot(anni, andamentoOro, 'green', linewidth = 5)
ax1.set_xlabel('Anni')
ax1.set_ylabel('Costo dell oro negli anni (euro al grammo)')
ax1.grid()

plt.show()