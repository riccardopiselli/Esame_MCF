import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy import fft
import math
import matplotlib.pyplot as plt
import matplotlib.colors as colors
from mpl_toolkits.axes_grid1.inset_locator import inset_axes

np.seterr(divide='ignore')


print('Stato: Oregon','\n', 'Inizio presa dati: 01/01/2013', '\n', 'Fine presa dati: 31/12/2015')


mydf = pd.read_csv('Oregon.csv')


"""

Per l'Oregon sono presenti i valori per una sola stazione di monitoraggio i singoli inquinati
sono stati separati e salvati in degli array
"""


NO2 = mydf['NO2 Mean'].values
SO2 = mydf['SO2 Mean'].values
CO = mydf['CO Mean'].values
O3 = mydf['O3 Mean'].values
N = len(mydf['Date Local'])
time = np.arange(0,N)


'''

Facendo un grafico del andamento temporale dei singoli inquinanti 


'''

fig, axs = plt.subplots(4, 1, layout='constrained', facecolor='aliceblue')
axs[0].plot(time,CO, color='mediumblue', label='CO andamento temporale')
axs[0].set_xlabel('Time (day)', size = 12)
axs[0].set_ylabel('CO Mean', size = 15)
axs[0].set_title('Andamneti temporali', size=20)
axs[0].legend()
axs[0].grid(True)

axs[1].plot(time,SO2, color='darkviolet',label='SO2 andamneto temporale' )
axs[1].set_xlabel('Time (day)', size = 12)
axs[1].set_ylabel('SO2 Mean', size = 15)
axs[1].legend()
axs[1].grid(True)

axs[2].plot(time,O3, color='dodgerblue',label='O3 andamneto temporale')
axs[2].set_xlabel('Time (day)', size = 12)
axs[2].set_ylabel('O3 Mean',size = 15)
axs[2].legend()
axs[2].grid(True)


axs[3].plot(time, NO2, color='navy', label='NO2 andamneto temporale')
axs[3].set_xlabel('Time (day)', size = 12)
axs[3].set_ylabel('NO2 Mean', size = 15)
axs[3].legend()
axs[3].grid(True)
plt.show()



'''



Calcolo i valori medi max e min  e altre grandezze statistiche 
durante tutto l'arco di presa dati per ogni singolo inquinante;



'''
#media
medCO = np.mean(CO)
medSO2 = np.mean(SO2)
medNO2 = np.mean(NO2)
medO3 = np.mean(O3)

#valore max e min
maxCO = np.max(CO)
minCO = np.min(CO)
maxSO2 = np.max(SO2)
minSO2 = np.min(SO2)
maxNO2 = np.max(NO2)
minNO2 = np.min(NO2)
maxO3 = np.max(O3)
minO3 = np.min(O3)

#varianza
x_CO = [medCO] * N
di_CO = x_CO - CO 
CO_quad = di_CO*di_CO
var_CO = np.sum(CO_quad)*( 1/N)

x_SO2 = [medSO2] * N
di_SO2 = x_SO2 - SO2
SO2_quad = di_SO2*di_SO2
var_SO2 = np.sum(SO2_quad)*( 1/N)

x_NO2 = [medNO2] * N
di_NO2 = x_NO2 - NO2 
NO2_quad = di_NO2*di_NO2
var_NO2 = np.sum(NO2_quad)*( 1/N)

x_O3 = [medO3] * N
di_O3 = x_O3 - O3
O3_quad = di_O3*di_O3
var_O3 = np.sum(O3_quad)*( 1/N)


print('Oregon from 2013-12-01 to 2015-12-31:')
print('\n\nLa seguente tabella raccoglie le informazioni riguardo \nal andamento  temporale degli inquinanti nello stato:\n\n')

df = pd.DataFrame({' Composto ':['CO','SO2', 'NO2', 'O3'], ' Media ':[medCO,medSO2,medNO2,medO3], 'Valori max':[maxCO,maxSO2,maxNO2,maxO3], 'Valori min':[minCO,minSO2,minNO2,minO3], 'Varianza':[var_CO,var_SO2,var_NO2,var_O3]})
print('\n', df, '\n')
df.to_csv('Data_Oregon.csv',index = False)



fig, ax = plt.subplots(facecolor='aliceblue')

t=np.array([medCO*1000,medO3*1000,medSO2,medNO2])
colors=["mediumblue","green","darkviolet","orange",]  #colors: Lista dei colori per le fette.
labels=["CO","O3","SO2","NO2"]  #labels: Lista delle etichette per le fette.
ax.pie(t, labels=labels, autopct='%1.2f%%', pctdistance=1.2, labeldistance=.6, colors= colors, shadow= True, )
ax.set_title('Percentuale Inquinanti', fontsize=24, color='darkblue', weight='bold')
plt.legend(labels, title="Legenda", bbox_to_anchor=(1.5, 0.5), fontsize=20)
plt.show()



'''



Estraiamo i termini di fourier e le relative frequenze;
Successivamnete prendiamo il modulo quadro di questi coefficenti;
In fine per andare a fare il grafico prendiamo solo la seconda me mata dei coefficenti e delle frequenze, tanto quest'ultimo è simmetrico.



'''


tf_CO = fft.fft(CO)
tf_NO2 = fft.fft(NO2)
tf_SO2 = fft.fft(SO2)
tf_O3 = fft.fft(O3)


#coefficenti al quadrato

qtf_CO = np.abs(tf_CO)*np.abs(tf_CO)
qtf_NO2 = np.abs(tf_NO2)*np.abs(tf_NO2)
qtf_SO2 = np.abs(tf_SO2)*np.abs(tf_SO2)
qtf_O3 = np.abs(tf_O3)*np.abs(tf_O3)

#ricavo le frequenze

freq_CO = fft.fftfreq(len(tf_CO), 1)
freq_SO2 = fft.fftfreq(len(tf_SO2), 1)
freq_NO2 = fft.fftfreq(len(NO2), 1)
freq_O3 = fft.fftfreq(len(O3), 1)



freq_CO = freq_CO[: (len(freq_CO)//2)]
qtf_CO = qtf_CO[:(len(qtf_CO)//2)]
coff_CO = tf_CO[: len(tf_CO)//2]

freq_O3 = freq_O3[: (len(freq_O3)//2)]
qtf_O3 = qtf_O3[:(len(qtf_O3)//2)]
coff_O3 = tf_O3[: len(tf_O3)//2]

freq_SO2 = freq_SO2[: (len(freq_SO2)//2)]
qtf_SO2 = qtf_SO2[:(len(qtf_SO2)//2)]
coff_SO2= tf_SO2[: len(tf_SO2)//2]

freq_NO2 = freq_NO2[: (len(freq_NO2)//2)]
qtf_NO2 = qtf_NO2[:    (len(qtf_NO2)//2)]
coff_NO2 = tf_NO2[: len(tf_NO2)//2]


time = time[:(len(time//2))]


m1 = np.max(qtf_CO)
m2 = np.max(qtf_NO2)
m3 = np.max(qtf_O3)
m4 = np.max(qtf_SO2)


fig, axs = plt.subplots(2, 2, sharex=False, sharey=False, layout="constrained", facecolor='aliceblue')


# Subplot [0, 0]
axs[0, 0].plot(freq_CO, qtf_CO * (1 / m1), color='mediumblue', marker='+', label='CO')
axs[0, 0].set_xlabel("Fk", size=15)
axs[0, 0].set_xlim(-0.65, 0.65)
axs[0, 0].set_ylabel("|Ck|^2", size=15)
axs[0, 0].set_title("CO normalizzato", size=13)
axs[0, 0].grid(True)
axs[0, 0].legend()

#inset to axs[0, 0]
inset_ax = inset_axes(axs[0, 0], width="40%", height="40%", loc='lower left')  
inset_ax.plot(freq_CO, qtf_CO * (1 / m1), color='mediumblue', marker='+')
inset_ax.set_xlim(-0.00, 0.04)  
inset_ax.set_ylim(  min(qtf_CO * (1 / m1)), max(qtf_CO * (1 / m1)) *0.03 )
inset_ax.grid(True)

# Subplot [0, 1]
axs[0, 1].plot(freq_NO2, qtf_NO2 * (1 / m2), color='darkviolet', marker='+', label='NO2')
axs[0, 1].set_xlabel("Fk", size=15)
axs[0, 1].set_xlim(-0.65, 0.65)
axs[0, 1].set_ylabel("|Ck|^2", size=15)
axs[0, 1].set_title("NO2 normalizzato", size=13)
axs[0, 1].grid(True)
axs[0, 1].legend()

#inset to axs[0, 1]
inset_ax = inset_axes(axs[0, 1], width="40%", height="40%", loc='lower left')  
inset_ax.plot(freq_NO2, qtf_NO2 * (1 / m2), color='darkviolet', marker='+')
inset_ax.set_xlim(-0.00, 0.04)  
inset_ax.set_ylim(min(qtf_NO2 * (1 / m2)), max(qtf_NO2 * (1 / m2))*0.03)  
inset_ax.grid(True)




# Subplot [1, 0]
axs[1, 0].plot(freq_O3, qtf_O3 * (1 / m3), color='navy', marker='+', label='03')
axs[1, 0].set_xlabel("Fk", size=15)
axs[1, 0].set_xlim(-0.65, 0.65)
axs[1, 0].set_ylabel("|Ck|^2", size=15)
axs[1, 0].set_title("O3 normalizzato", size=13)
axs[1, 0].grid(True)
axs[1, 0].legend()


#inset to axs[1, 0]
inset_ax = inset_axes(axs[1, 0], width="40%", height="40%", loc='lower left')  
inset_ax.plot(freq_O3, qtf_O3 * (1 / m3), color='navy', marker='+')
inset_ax.set_xlim(-0.00, 0.04)  
inset_ax.set_ylim(min(qtf_O3 * (1 / m3)), max(qtf_O3 * (1 / m3))*0.03)  
inset_ax.grid(True)




# Subplot [1, 1]
axs[1, 1].plot(freq_SO2, qtf_SO2 * (1 / m4), color='dodgerblue', marker='+', label='SO2')
axs[1, 1].set_xlabel("Fk", size=15)
axs[1, 1].set_xlim(-0.65, 0.65)
axs[1, 1].set_ylabel("|Ck|^2", size=15)
axs[1, 1].set_title("SO2 normalizzato", size=13)
axs[1, 1].grid(True)
axs[1, 1].legend()


#inset to axs[1, 1]
inset_ax = inset_axes(axs[1, 1], width="40%", height="40%", loc='lower left')  
inset_ax.plot(freq_NO2, qtf_SO2 * (1 / m4), color='dodgerblue', marker='+')
inset_ax.set_xlim(-0.00, 0.04)  
inset_ax.set_ylim(min(qtf_SO2 * (1 / m4)), max(qtf_SO2 * (1 / m4))*0.03)  
inset_ax.grid(True)
plt.show()



'''


Questa parte di codice permette di fare un filtro sulle frequenze desiderate;
Sono state filtarte in tutto tre volte la prima e per ottenere i dati con cui fare l'anti trasformata 
mentre le altre sono per lo studio teporale svolta succesivamnete;


'''



#filtro per frequenze piu basse
maskCO = abs(freq_CO) < 0.020
maskO3 = abs(freq_O3) < 0.020
maskSO2 = abs(freq_SO2) < 0.020
maskNO2 = abs(freq_NO2) < 0.020


#primo filtro, frequenze principali
maskCO_1 = abs(freq_CO) < 0.006
maskO3_1 = abs(freq_O3) < 0.006
maskSO2_1 = abs(freq_SO2) < 0.006
maskNO2_1 = abs(freq_NO2) < 0.006


#secondo filtro, frequnaze piu alte
maskCO_2 = abs(freq_CO) > 0.45
maskO3_2 = abs(freq_O3) > 0.45
maskSO2_2 = abs(freq_SO2) > 0.45
maskNO2_2 = abs(freq_NO2) > 0.45





'''


Frequenze selezionate...




'''


#mashera sulle frequenze piu basse selezionate
freq_CO = freq_CO*maskCO
freq_O3 = freq_O3*maskO3
freq_NO2 = freq_NO2*maskNO2
freq_SO2 = freq_SO2*maskSO2




#frequenze associate al primo filtro per lo studio temporale
freq_CO_1 = freq_CO*maskCO_1
freq_O3_1 = freq_O3*maskO3_1
freq_NO2_1 = freq_NO2*maskNO2_1
freq_SO2_1 = freq_SO2*maskSO2_1

#frequenze associate al secondo filtro per lo studio temporale
freq_CO_2 = freq_CO*maskCO_2
freq_O3_2 = freq_O3*maskO3_2
freq_NO2_2 = freq_NO2*maskNO2_2
freq_SO2_2 = freq_SO2*maskSO2_2


#print('\n','Periodi andamenti principali: ', '\n', 1/freq_O3)


'''


Applico le maschere alle copie degli array dei coefficenti;


'''


c_maskedCO = coff_CO*maskCO
c_maskedO3 = coff_O3*maskO3
c_maskedSO2 = coff_SO2*maskSO2
c_maskedNO2 = coff_NO2*maskNO2


#maschere per il primo studio andamneto temporale
c_maskedCO_1 = coff_CO*maskCO_1
c_maskedO3_1 = coff_O3*maskO3_1
c_maskedSO2_1 = coff_SO2*maskSO2_1
c_maskedNO2_1 = coff_NO2*maskNO2_1

#maschere per il secondo studio andamento temporale
c_maskedCO_2 = coff_CO*maskCO_2
c_maskedO3_2 = coff_O3*maskO3_2
c_maskedSO2_2 = coff_SO2*maskSO2_2
c_maskedNO2_2 = coff_NO2*maskNO2_2



'''


Facio l'anti-trasformata e ottengo i nuovi coefficenti;



'''


atf_CO = fft.ifft( c_maskedCO, len(time))
atf_O3 = fft.ifft( c_maskedO3, len(time))
atf_SO2 = fft.ifft( c_maskedSO2, len(time))
atf_NO2 = fft.ifft(c_maskedNO2, len(time))

atf_CO = np.real(atf_CO)
atf_NO2 = np.real(atf_NO2)
atf_O3 = np.real(atf_O3)
atf_SO2 = np.real(atf_SO2)


#nuovi coefficienti primo studio 
atf_CO_1 = fft.ifft( c_maskedCO_1, len(time))
atf_O3_1 = fft.ifft( c_maskedO3_1, len(time))
atf_SO2_1 = fft.ifft( c_maskedSO2_1, len(time))
atf_NO2_1 = fft.ifft(c_maskedNO2_1, len(time))


atf_CO_1 = np.real(atf_CO_1)
atf_NO2_1 = np.real(atf_NO2_1)
atf_O3_1 = np.real(atf_O3_1)
atf_SO2_1 = np.real(atf_SO2_1)



#nuovi coefficenti secondo studio
atf_CO_2 = fft.ifft( c_maskedCO_2, len(time))
atf_O3_2 = fft.ifft( c_maskedO3_2, len(time))
atf_SO2_2 = fft.ifft( c_maskedSO2_2, len(time))
atf_NO2_2 = fft.ifft(c_maskedNO2_2, len(time))



atf_CO_2 = np.real(atf_CO_2)
atf_NO2_2 = np.real(atf_NO2_2)
atf_O3_2 = np.real(atf_O3_2)
atf_SO2_2 = np.real(atf_SO2_2)


'''


Faccio il grafico con i nuovi coefficenti e confronto il grafico originale 
con quello ottenuto con l'anti-trasformata



'''



fig, axs = plt.subplots(4, 1, layout='constrained', facecolor='aliceblue')

axs[0].plot(time,CO, color='deepskyblue', alpha= 0.7, label='Originale (CO)')
axs[0].plot(time, atf_CO, color='navy', label='Filtrata')
axs[0].set_xlabel('Time (day)')
axs[0].set_ylabel('CO Mean')
axs[0].set_title('Ricostruzione segnale', size=20)
axs[0].grid(True)
axs[0].legend()

axs[1].plot(time,SO2, color='deepskyblue', alpha = 0.7, label='Originale (SO2)')
axs[1].plot(time, atf_SO2, color='navy', label='Filtrata')
axs[1].set_xlabel('Time (day)')
axs[1].set_ylabel('SO2 Mean')
axs[1].grid(True)
axs[1].legend()

axs[2].plot(time,O3, color='deepskyblue', alpha = 0.7, label='Originale (O3)')
axs[2].plot(time, atf_O3, color = 'navy', label='Filtrata')
axs[2].set_xlabel('Time (day)')
axs[2].set_ylabel('O3 Mean')
axs[2].grid(True)
axs[2].legend()


axs[3].plot(time, NO2, color='deepskyblue', alpha=0.7, label='Originale (NO2)')
axs[3].plot(time, atf_NO2, color='navy', label='filtrata')
axs[3].set_xlabel('Time (day)')
axs[3].set_ylabel('NO2 Mean')
axs[3].grid(True)
axs[3].legend()

plt.show()

'''


Confronto degli andamenti temporali filtrati per i periodi piccoli e lunghi;
gli array con i dati vengono moltiplicati per un fattore di normalizazione;



'''

n1 = 1 / np.max(atf_CO_1) 
n2 = 1 / np.max(atf_NO2_1)
n3 = 1 / np.max(atf_O3_1)
n4 = 1 / np.max(atf_SO2_1)




fig, axs = plt.subplots(3, 1, layout='constrained', facecolor='aliceblue')

axs[0].plot(time, n1*atf_CO_1, color='red', label=' CO Filtrata')
axs[0].plot(time, n3*atf_O3_1, color = 'navy', label='O3 Filtrata')
axs[0].grid(True)
axs[0].set_xlabel('Time (day)', size = '13')
axs[0].set_ylabel('Mean values', size='13')
axs[0].set_title('Basse frequenze', size=20)

axs[0].legend()


axs[1].plot(time, n2*atf_NO2_1, color='red', label='NO2 filtrata')
axs[1].plot(time, n3*atf_O3_1, color = 'navy', label='O3 Filtrata')
axs[1].set_xlabel('Time (day)', size = '13')
axs[1].set_ylabel('Mean values', size='13')
axs[1].grid(True)
axs[1].legend()


axs[2].plot(time, n4*atf_SO2_1, color='red', label='SO2 filtrata')
axs[2].plot(time, n3*atf_O3_1, color = 'navy', label='O3 Filtrata')
axs[2].set_xlabel('Time (day)', size = '13')
axs[2].set_ylabel('Mean values', size='13')
axs[2].grid(True)
axs[2].legend()



fig, axs = plt.subplots(3, 1, layout='constrained', facecolor='aliceblue')

axs[0].plot(time, n1*atf_CO_2, color='red', label=' CO Filtrata')
axs[0].plot(time, n3*atf_O3_2, color = 'navy', label='O3 Filtrata')
axs[0].set_xlabel('Time (day)', size = '13')
axs[0].set_ylabel('Mean values', size='13')
axs[0].set_title('Alte  frequenze', size=20)

axs[0].grid(True)
axs[0].legend()


axs[1].plot(time, n2*atf_NO2_2, color='red', label='NO2 filtrata')
axs[1].plot(time, n3*atf_O3_2, color = 'navy', label='O3 Filtrata')
axs[1].set_xlabel('Time (day)', size = '13')
axs[1].set_ylabel('Mean values', size='13')
axs[1].grid(True)
axs[1].legend()


axs[2].plot(time, n4*atf_SO2_2, color='red', label='SO2 filtrata')
axs[2].plot(time, n3*atf_O3_2, color = 'navy', label='O3 Filtrata')
axs[2].set_xlabel('Time (day)', size = '13')
axs[2].set_ylabel('Mean values', size='13')
axs[2].grid(True)
axs[2].legend()

plt.tight_layout()
plt.show()



'''


Stampiamo le frequenze selezioate dalle maschere per ogni inquinnate;



'''





alpha1 = len(freq_CO_1)


freq_CO = np.round(freq_CO,3)
freq_NO2 = np.round(freq_NO2,3)
freq_SO2 = np.round(freq_SO2,3)
freq_O3 = np.round(freq_O3,3)


xCO = pd.DataFrame({'-Frequenze CO-': freq_CO, '-Periodi CO-': np.round(1/freq_CO,3)})

for i in range (0, alpha1):
    if freq_CO[i] < 0.0002:
        xCO = xCO.drop(i)




xSO2 = pd.DataFrame({'-Frequenze SO2-': freq_SO2, '-Periodo SO2-': np.round(1/freq_SO2,3)})

for i in range (0, alpha1):
    if freq_SO2[i] < 0.0002:
        xSO2 = xSO2.drop(i)



xNO2 = pd.DataFrame({'-Frequenze NO2-': freq_NO2, '-Periodo NO2-' : np.round(1/freq_NO2,3)})

for i in range (0, alpha1):
    if freq_NO2[i] < 0.0002:
        xNO2 = xNO2.drop(i)



xO3 = pd.DataFrame({'-Frequenze O3-': freq_O3, '-Periodo O3-': np.round(1/freq_O3,3)})

for i in range (0, alpha1):
    if freq_O3[i] < 0.0002:
        xO3 = xO3.drop(i)






print('Frequenze selezioante dalle maschere: ')
print('\n CO: \n',xCO)
print('\n SO2: \n',xSO2)
print('\n NO2: \n', xNO2)
print('\n O3: \n', xO3)


'''


Faccio un Datafraem finale 


'''


dfOregon = pd.concat([xCO, xNO2, xSO2, xO3], axis=True)
dfOregon.to_csv('_oregon.csv', index=False)


print('\n\nNOTA:\nIl campionamento avviene con una frequenza di uno al giorno, cioò va specificato perche \nleggendo il valore di 0.002(1/g) per una frequneza non bisogna pensare ad una gradenzza in Hz ma di (1/1 giorno) ovvero (1/ 86400 sec)\nCome si può osservare la maggior parte delle frequenze filtrate  per la ricostruzione del segnale sono del ordine di 0.19;\nMentre le frequenze più alte che è possibile trovare non superano i 0.5(1/g)\nTuttavia va detto che tale risulatato è dato  unicamente dalla frequenza di campionamneto\ninfatti a prescindere dal segnale originale dal analisi di fuoirie la fraqunza maggiore\n che è possbile trovare non supera f_c/2 con fc pari alla frequenza di campionamento\novverouna al giorno nel nostro caso. ')

print('\n\nNELLE TABELLE LE FREQUENZE NON SONO STATE RIPORTATE IN HZ PER FARE TALE CONVERSIONE E SUFFICIENTE MOLTIPLICARE LA FREQUENZA IN (1/giorni) PER UN FATTORE 86400\n\n' )


print('\n Dataframe con tutte le frequenze scaricate \n',dfOregon)
print('\n\nIl file Oregon.py è stato eseguito correttamente è sono stati creati due file csv:\n(1)Data_Oregon.py contenete delle informazione statistiche sul set di dati \n(2)_oregon.py che raccogli le frequenze di maggior importanza per la ricostrizione del segnale')