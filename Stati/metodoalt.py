import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from  scipy import integrate
import math
import matplotlib.pyplot as plt
import matplotlib.colors as colors

mydf = pd.read_csv('pollution_us_2013_2015.csv')


'''



Etraggo  le cose che mi interessano le le organizzo in array....



'''




Data = mydf['Date Local']
Stato = mydf['State']
Indirizzo = mydf['Address']
coM = mydf['CO Mean']
so2M = mydf['SO2 Mean']
o3M = mydf['O3 Mean']
time = np.arange(0,len(Data))







'''



Creo un array vuoto dove verranno messi gli indici delle righe che selezionerò



'''


corect_line = np.empty(0)
corect_line = np.append(corect_line,0)


'''



Ciclo for che riempe l'arrai introdotto sopra...



'''


for i in range(0, len(Data)-1):
   if ( Data[i + 1] != Data[i] or Indirizzo[i+1] != Indirizzo[i]) and (Stato[i] == 'Minnesota' or Stato[i] == 'Alabama' or Stato[i] == 'Oregon' or  Stato[i]=='Texas' or Stato[i] == 'Alaska'):
     corect_line = np.append(corect_line, i + 1)
   else:
      a = 1 



'''


Adesso seleziono le righe che voglio del mio dataframe...


'''


# Selezionare le righe specifiche
new_mydf = mydf.iloc[corect_line]
print("\nRighe selezionate:")
print(new_mydf['Date Local'],'\n',len(new_mydf))





'''


Adesso selezione le colonne che davvero mi interessano cioè quelle con i valori medi degli inquinanti...


'''
correct_columns = ([1,2,3,4,5,6,7,8,10,15,20,25])
# Selezione delle colonne usando .iloc
new_new_mydf = new_mydf.iloc[:,correct_columns]
print('colonne selezionate','\n',new_new_mydf.columns)





final_df = new_new_mydf


'''



estraggo i le cose che mi interessano le le organizzo in array....



'''
Data1 = final_df['Date Local']
Stato1 = final_df['State']
Indirizzo1 = final_df['Address']
COMean = final_df['CO Mean']
SO2Mean = final_df['SO2 Mean']
O3Mean = final_df['O3 Mean']
NO2mean = final_df['NO2 Mean']
time = np.arange(0,len(Data1))


'''

Faccio il grafico

'''


fig, axs = plt.subplots(4, 1, layout='constrained')
axs[0].plot(time,COMean, color='red')
axs[0].set_xlabel('Time (day)')
axs[0].set_ylabel('CO Mean')
axs[0].grid(True)

axs[1].plot(time,SO2Mean, color='forestgreen')
axs[1].set_xlabel('Time (day)')
axs[1].set_ylabel('SO2 Mean')
axs[1].grid(True)

axs[2].plot(time,O3Mean, color='dodgerblue')
axs[2].set_xlabel('Time (day)')
axs[2].set_ylabel('O3 Mean')
axs[2].grid(True)


axs[3].plot(time, NO2mean, color='orange')
axs[3].set_xlabel('Time (day)')
axs[3].set_ylabel('NO2 Mean')
axs[3].grid(True)
plt.show()







final_df.to_csv('nuova_semplificata.csv')
