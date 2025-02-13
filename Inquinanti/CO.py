import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy import fft
import math
import matplotlib.pyplot as plt
import matplotlib.colors as colors
from mpl_toolkits.axes_grid1.inset_locator import inset_axes
import os



np.seterr(divide='ignore')



'''

Estraggo i file dal csv presente nella altra directory e salvo di degli array solo 
i dati relativi al inquinante che mi interessa.


'''

directory_path = '/home/riccardo-piselli/metodicf/Esame/Stati/' 

Oregon_file_name = "Oregon.csv"  
Alabama_file_name = "Alabama.csv"  
Alaska_file_name = "Alaska.csv"  
Minnesota_file_name = "Oregon.csv"  





Oregon_file_path = os.path.join(directory_path, Oregon_file_name)
Minnesota_file_path = os.path.join(directory_path, Minnesota_file_name)
Alaska_file_path = os.path.join(directory_path, Alaska_file_name)
Alabama_file_path = os.path.join(directory_path, Alabama_file_name)



'''


Creo dei dataFrame con i file scaricati e seleziono solo l'inquinnate che mi serve


'''

oregon_mydf = pd.read_csv(Oregon_file_path)
minnesota_mydf = pd.read_csv(Minnesota_file_path)
alabama_mydf = pd.read_csv(Alabama_file_path)
alaska_mydf = pd.read_csv(Alaska_file_path)


CO_Oregon = oregon_mydf['CO Mean'].values
CO_Alabama = alabama_mydf['CO Mean'].values
CO_Alaska = alaska_mydf['CO Mean'].values
CO_Minnesota = minnesota_mydf['CO Mean'].values

N1 = np.arange(0, len(CO_Oregon))
N2 = np.arange(0, len(CO_Alabama))
N3 = np.arange(0, len(CO_Alaska))
N4 = np.arange(0, len(CO_Minnesota))

'''


Faccio il grafi dello stesso inquinnate in stati diversi


'''




fig, axs = plt.subplots(2, 2, sharex=False, sharey=False, layout="constrained", facecolor='aliceblue')


# Subplot [0, 0]
axs[0, 0].plot(N1, CO_Oregon , color='mediumblue', label='CO')
axs[0, 0].set_xlabel("Day", size=15)
axs[0, 0].set_ylabel("CO mean", size=15)
axs[0, 0].set_title("CO Oregon", size=13)
axs[0, 0].grid(True)
axs[0, 0].legend()

# Subplot [0, 1]
axs[0, 1].plot(N2, CO_Alabama, color='darkviolet', label='NO2')
axs[0, 1].set_xlabel("DAy", size=15)
axs[0, 1].set_ylabel("CO mean", size=15)
axs[0, 1].set_title("CO Alabama", size=13)
axs[0, 1].grid(True)
axs[0, 1].legend()


# Subplot [1, 0]
axs[1, 0].plot(N3, CO_Alaska, color='navy', label='03')
axs[1, 0].set_xlabel("Day", size=15)
axs[1, 0].set_ylabel("CO mean", size=15)
axs[1, 0].set_title("CO Alaska", size=13)
axs[1, 0].grid(True)
axs[1, 0].legend()




# Subplot [1, 1]
axs[1, 1].plot(N4, CO_Minnesota, color='dodgerblue', label='SO2')
axs[1, 1].set_xlabel("DAY", size=15)
axs[1, 1].set_ylabel("CO MEAN", size=15)
axs[1, 1].set_title("CO Minnesota", size=13)
axs[1, 1].grid(True)
axs[1, 1].legend()


plt.show()


'''


Scarcico i file contenenti delle informazioni statistiche 
rigurdo al evoluzione temporale del Inquinante nei vari stati


'''


myDF_Oregon = pd.read_csv(os.path.join(directory_path, 'Data_Oregon.csv'))
myDF_Alaska = pd.read_csv(os.path.join(directory_path, 'Data_Alabama.csv'))
myDF_Alabama = pd.read_csv(os.path.join(directory_path, 'Data_Alaska.csv'))
myDF_Minnesota = pd.read_csv(os.path.join(directory_path, 'Data_Minnesota.csv'))

print('\n\nQuesti Dataframe hanno delle informazioni statistiche riguardo al evoluzione temporale\ndel Inquinante, tipo media e varianza ')

print('\nOregon:\n',myDF_Oregon.loc[0])
print('\nAlaska:\n',myDF_Alabama.loc[0])
print('\nAlabama:\n',myDF_Alaska.loc[0])
print('\nMinnesota:\n',myDF_Minnesota.loc[0])

freq_mydf_Oregon = pd.read_csv(os.path.join(directory_path, '_oregon.csv'))
freq_mydf_Alabama = pd.read_csv(os.path.join(directory_path, '_alabama.csv'))
freq_mydf_Alaska = pd.read_csv(os.path.join(directory_path, '_alaska.csv'))
freq_mydf_Minnesota = pd.read_csv(os.path.join(directory_path, '_minnesota.csv'))


print('\n\nDi seguito sono riportant i dataframe relatvi alla frequenze \nprincipali e i relativi periodi del inquinnate.')

print('\nOregon:\n', freq_mydf_Oregon[['-Frequenze CO-','-Periodi CO-']])
print('\nAlabama:\n', freq_mydf_Alabama[['-Frequenze CO-','-Periodi CO-']])
print('\nAlaska:\n', freq_mydf_Alaska[['-Frequenze CO-','-Periodi CO-']])
print('\nMinnesota:\n', freq_mydf_Minnesota[['-Frequenze CO-','-Periodi CO-']])


