import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from  scipy import integrate
import math
import matplotlib.pyplot as plt
import matplotlib.colors as colors



mydf = pd.read_csv('pollution_us_2013_2015.csv')




'''


Adesso selezione le colonne che davvero mi interessano cioè quelle con i valori medi degli inquinanti...


'''
correct_columns = ([4,5,8,10,15,20,25])
# Selezione delle colonne usando .iloc
new_mydf = mydf.iloc[:,correct_columns]





"""



Adesso selezioaniamo i vari stati creando 5 nuovi dataframe con i singoli stati...



"""



Data = new_mydf['Date Local']
State = new_mydf['State']
Indirizzo = new_mydf['Address']


N = len(Data)

corect_line_1 = np.empty(0)
corect_line_2 = np.empty(0)
corect_line_3 = np.empty(0)
corect_line_4 = np.empty(0)
corect_line_5 = np.empty(0)

for i in range(0, N-1):
    if  State[i] == 'Texas' and (Data[i + 1] != Data[i] or Indirizzo[i+1] != Indirizzo[i]):
        corect_line_1 = np.append(corect_line_1, i)


    elif State[i] == 'Alaska' and  ( Data[i + 1] != Data[i] or Indirizzo[i+1] != Indirizzo[i]) :
        corect_line_2 = np.append(corect_line_2, i)


    elif State[i] == 'Alabama'and (Data[i + 1] != Data[i] or Indirizzo[i+1] != Indirizzo[i]):
        corect_line_3 = np.append(corect_line_3, i)


    elif State[i] == 'Minnesota' and (Data[i + 1] != Data[i] or Indirizzo[i+1] != Indirizzo[i]):
        corect_line_4 = np.append(corect_line_4, i)


    elif State[i] == 'Oregon' and (Data[i + 1] != Data[i] or Indirizzo[i+1] != Indirizzo[i]):
        corect_line_5 = np.append(corect_line_5, i)




df_Texas = new_mydf.iloc[corect_line_1]
df_Alaska = new_mydf.iloc[corect_line_2]
df_Alabama = new_mydf.iloc[corect_line_3]
df_Minnesota = new_mydf.iloc[corect_line_4]
df_Oregon = new_mydf.iloc[corect_line_5]


df_Texas.to_csv('Texas.csv')
df_Alaska.to_csv('Alaska.csv')
df_Alabama.to_csv('Alabama.csv')
df_Minnesota.to_csv('Minnesota.csv')
df_Oregon.to_csv('Oregon.csv')


print('\nSono stati creati dei file .csv separati per ciascuno stato\nadesso è possibile eseguire uno dei seguenti file python:\n\nAlaska.py\nAlabama.py\nMinnesota.py\nOregon.py\n\nUna volta eseguiti corretamnete sarà possibile eseuire il file \n\nRiassuntoStati.py\n\nche riassumera i risultati di maggiore interesse\n')