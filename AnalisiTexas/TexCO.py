import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy import fft
import math
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import warnings


np.seterr(divide='ignore')
warnings.filterwarnings("ignore", category=np.ComplexWarning)

'''

Per il Texas il metodo è differente daglin altri stati....à
sono presenti più stazioni di monitoraggio e quiindi come prima cosa 
andiamo a creare nuovi csv solo con le singole stazzioni.

Secondo questo principio:

1415 Hinton Street   ---> Texas01
250 Rim Rd           ---> Texas02
800 S Son Marcial    ---> Texas03
7421 Park Place Blvd ---> Texas04
9525 1/2 Clinton Dr  ---> Texas05
4514 1/2 Durant St   ---> Texas06
4472 Mazanec Rd      ---> Texas07
3724 North Hills Dr  ---> Texas08

'''



df_Texas01 = pd.read_csv('Texas01.csv')
df_Texas02 = pd.read_csv('Texas02.csv')
df_Texas03 = pd.read_csv('Texas03.csv')
df_Texas04 = pd.read_csv('Texas04.csv')
df_Texas05 = pd.read_csv('Texas05.csv')
df_Texas06 = pd.read_csv('Texas06.csv')
df_Texas07 = pd.read_csv('Texas07.csv')
df_Texas08 = pd.read_csv('Texas08.csv')



CO_01 = df_Texas01['CO Mean'].values
CO_02 = df_Texas02['CO Mean'].values
CO_03 = df_Texas03['CO Mean'].values
CO_04 = df_Texas04['CO Mean'].values
CO_05 = df_Texas05['CO Mean'].values
CO_06 = df_Texas06['CO Mean'].values
CO_07 = df_Texas07['CO Mean'].values
CO_08 = df_Texas08['CO Mean'].values


'''

Faccaimo i grafici

'''

'''






'''
#Texas 01
N1 = len(CO_01)
time1 = np.arange(0,N1)

#Texas 02
N2 = len(CO_02)
time2 = np.arange(0,N2)

#Texas 03
N3 = len(CO_03)
time3 = np.arange(0,N3)

#Texas 04
N4 = len(CO_04)
time4 = np.arange(0,N4)

#Texas 05
N5 = len(CO_05)
time5 = np.arange(0,N5)

#Texas 06
N6 = len(CO_06)
time6 = np.arange(0,N6)

#Texas 07
N7 = len(CO_07)
time7 = np.arange(0,N7)

#Texas 04
N8 = len(CO_08)
time8 = np.arange(0,N8)









fig, axs = plt.subplots(4, 2, sharex=False, sharey=False, layout="constrained", facecolor='aliceblue')

axs[0,0].plot(time1,  CO_01, color='steelblue', label='CO texas 01')
axs[0,0].set_xlabel("Day", size=12, color='steelblue')
axs[0,0].set_ylabel("CO mean", size=12, color='steelblue')
axs[0,0].set_title("CO Texas 01", size=17, color='red')
axs[0,0].grid(True)
axs[0,0].legend()

# Subplot [0, 1]
axs[1,0].plot(time2, CO_02, color='steelblue', label='CO texas 02')
axs[1,0].set_xlabel("Day", size=11, color='steelblue')
axs[1,0].set_ylabel("CO mean", size=11, color='steelblue')
axs[1,0].set_title("CO Texas 02", size=17, color='red')
axs[1,0].grid(True)
axs[1,0].legend()


# Subplot [1, 0]
axs[2, 0].plot(time3, CO_03, color='steelblue', label='CO texas 03')
axs[2, 0].set_xlabel("Day", size=12, color='steelblue')
axs[2, 0].set_ylabel("CO mean", size=12, color='steelblue')
axs[2, 0].set_title(" CO Texas 03", size=17, color='red')
axs[2, 0].grid(True)
axs[2, 0].legend()


# Subplot [1, 1]
axs[3, 0].plot(time4, CO_04, color='steelblue', label='CO texas 04')
axs[3, 0].set_xlabel("Day", size=12, color='steelblue')
axs[3, 0].set_ylabel("CO mean", size=12, color='steelblue')
axs[3, 0].set_title(" CO Texas 04", size=17, color='red')
axs[3, 0].grid(True)
axs[3, 0].legend()





axs[0,1].plot(time5,  CO_05, color='steelblue', label='CO texas 05')
axs[0,1].set_xlabel("Day", size=12, color='steelblue')
axs[0,1].set_ylabel("CO mean", size=12, color='steelblue')
axs[0,1].set_title("CO Texas 05", size=17, color='red')
axs[0,1].grid(True)
axs[0,1].legend()

# Subplot [0, 1]
axs[1,1].plot(time6, CO_06, color='steelblue', label='CO texas 06')
axs[1,1].set_xlabel("Day", size=12, color='steelblue')
axs[1,1].set_ylabel("CO mean", size=12, color='steelblue')
axs[1,1].set_title("CO Texas 06", size=17, color='red')
axs[1,1].grid(True)
axs[1,1].legend()


# Subplot [1, 0]
axs[2, 1].plot(time7, CO_07, color='steelblue', label='CO texas 07')
axs[2, 1].set_xlabel("Day", size=12, color='steelblue')
axs[2, 1].set_ylabel("CO mean", size=12, color='steelblue')
axs[2, 1].set_title("CO Texas 07", size=17, color='red')
axs[2, 1].grid(True)
axs[2, 1].legend()


# Subplot [1, 1]
axs[3, 1].plot(time8, CO_08, color='steelblue', label='CO texas 08 ')
axs[3, 1].set_xlabel("Day", size=12, color='steelblue')
axs[3, 1].set_ylabel("CO mean", size=12, color='steelblue')
axs[3, 1].set_title("CO Texas 08", size=17, color='red')
axs[3, 1].grid(True)
axs[3, 1].legend()

plt.show()



'''



Estraiamo i termini di fourier e le relative frequenze;
Successivamnete prendiamo il modulo quadro di questi coefficenti;
In fine per andare a fare il grafico prendiamo solo la seconda me mata dei coefficenti e delle frequenze, tanto quest'ultimo è simmetrico.


'''


tf_CO_01 = fft.fft(CO_01)
tf_CO_02 = fft.fft(CO_02)
tf_CO_03 = fft.fft(CO_03)
tf_CO_04 = fft.fft(CO_04)
tf_CO_05 = fft.fft(CO_05)
tf_CO_06 = fft.fft(CO_06)
tf_CO_07 = fft.fft(CO_07)
tf_CO_08 = fft.fft(CO_08)



#coefficenti al quadrato

qtf_CO_01 = np.abs(tf_CO_01)*np.abs(tf_CO_01)
qtf_CO_02 = np.abs(tf_CO_02)*np.abs(tf_CO_02)
qtf_CO_03 = np.abs(tf_CO_03)*np.abs(tf_CO_03)
qtf_CO_04 = np.abs(tf_CO_04)*np.abs(tf_CO_04)
qtf_CO_05 = np.abs(tf_CO_05)*np.abs(tf_CO_05)
qtf_CO_06 = np.abs(tf_CO_06)*np.abs(tf_CO_06)
qtf_CO_07 = np.abs(tf_CO_07)*np.abs(tf_CO_07)
qtf_CO_08 = np.abs(tf_CO_08)*np.abs(tf_CO_08)

#ricavo le frequenze

freq_CO_01 = fft.fftfreq(len(CO_01), 1)
freq_CO_02 = fft.fftfreq(len(CO_02), 1)
freq_CO_03 = fft.fftfreq(len(CO_03), 1)
freq_CO_04 = fft.fftfreq(len(CO_04), 1)
freq_CO_05 = fft.fftfreq(len(CO_05), 1)
freq_CO_06 = fft.fftfreq(len(CO_06), 1)
freq_CO_07 = fft.fftfreq(len(CO_07), 1)
freq_CO_08 = fft.fftfreq(len(CO_08), 1)


'''




Prendo in conciderazione solo gli la seconda meta degli array




'''

freq_CO_01 = freq_CO_01[: (len(freq_CO_01)//2)]
qtf_CO_01 = qtf_CO_01[:    (len(qtf_CO_01)//2)]
coff_CO_01 = tf_CO_01[: len(tf_CO_01)//2]

freq_CO_02 = freq_CO_02[: (len(freq_CO_02)//2)]
qtf_CO_02 = qtf_CO_02[:    (len(qtf_CO_02)//2)]
coff_CO_02 = tf_CO_02[: len(tf_CO_02)//2]

freq_CO_03 = freq_CO_03[: (len(freq_CO_03)//2)]
qtf_CO_03 = qtf_CO_03[:    (len(qtf_CO_03)//2)]
coff_CO_03 = tf_CO_03[: len(tf_CO_03)//2]

freq_CO_04 = freq_CO_04[: (len(freq_CO_04)//2)]
qtf_CO_04 = qtf_CO_04[:    (len(qtf_CO_04)//2)]
coff_CO_04 = tf_CO_04[: len(tf_CO_04)//2]

freq_CO_05 = freq_CO_05[: (len(freq_CO_05)//2)]
qtf_CO_05 = qtf_CO_05[:    (len(qtf_CO_05)//2)]
coff_CO_05 = tf_CO_05[: len(tf_CO_05)//2]

freq_CO_06 = freq_CO_06[: (len(freq_CO_06)//2)]
qtf_CO_06 = qtf_CO_06[:    (len(qtf_CO_06)//2)]
coff_CO_06 = tf_CO_06[: len(tf_CO_06)//2]

freq_CO_07 = freq_CO_07[: (len(freq_CO_07)//2)]
qtf_CO_07 = qtf_CO_07[:    (len(qtf_CO_07)//2)]
coff_CO_07 = tf_CO_07[: len(tf_CO_07)//2]

freq_CO_08 = freq_CO_08[: (len(freq_CO_08)//2)]
qtf_CO_08 = qtf_CO_08[:    (len(qtf_CO_08)//2)]
coff_CO_08 = tf_CO_08[: len(tf_CO_08)//2]


'''

Facciendo i grafici delle spettri di potenze

'''

total_CO = ([CO_01,CO_02,CO_03,CO_04,CO_05,CO_06,CO_07,CO_08])
total_time = ([time1,time2,time3,time4,time5,time6,time7,time8])
total_qtf_CO = ([ qtf_CO_01, qtf_CO_02, qtf_CO_03, qtf_CO_04,qtf_CO_05,qtf_CO_06,qtf_CO_07,qtf_CO_08 ])
total_freq_CO = ([freq_CO_01,freq_CO_02,freq_CO_03,freq_CO_04,freq_CO_05,freq_CO_06,freq_CO_07,freq_CO_08])


for i in range(0, len(total_qtf_CO) ):
    fig, axs = plt.subplots(2, 1, sharex=False, sharey=False, layout="constrained", facecolor='aliceblue')
    
    axs[0].plot(total_time[i], total_CO[i], color='royalblue', label='Adamento temporale')
    axs[0].set_title('Anadamento temporale', size=20, color='royalblue')
    axs[0].set_ylabel('CO mean', size = 15)
    axs[0].set_xlabel('Time (Day)', size = 15)
    axs[0].grid(True)
    axs[0].legend()

    axs[1].plot(total_freq_CO[i], total_qtf_CO[i], color='red', marker='', label='Spettro potenze CO')
    axs[1].set_title('Andamento in frequenze', size=20, color='red')
    axs[1].set_yscale('log')
    axs[1].set_ylabel('${|C_k|}^2$', size = 15)
    axs[1].set_xlabel('${f_{k}}$', size = 15)
    axs[1].grid(True)
    axs[1].legend()


    plt.tight_layout()
    plt.show()
    print('Analisi campionamneto di CO\n Texas:\t0',i+1,'\n')



'''


Faccio i filtri sulle frequenze


'''


maskCO_01 = abs(freq_CO_01) < 0.02
maskCO_02 = abs(freq_CO_02) < 0.02
maskCO_03 = abs(freq_CO_03) < 0.02
maskCO_04 = abs(freq_CO_04) < 0.02
maskCO_05 = abs(freq_CO_05) < 0.02
maskCO_06 = abs(freq_CO_06) < 0.02
maskCO_07 = abs(freq_CO_07) < 0.02
maskCO_08 = abs(freq_CO_08) < 0.02


'''


Frequenze selezionate...




'''



freq_CO_01 = freq_CO_01*maskCO_01
freq_CO_02 = freq_CO_02*maskCO_02
freq_CO_03 = freq_CO_03*maskCO_03
freq_CO_04 = freq_CO_04*maskCO_04
freq_CO_05 = freq_CO_05*maskCO_05
freq_CO_06 = freq_CO_06*maskCO_06
freq_CO_07 = freq_CO_07*maskCO_07
freq_CO_08 = freq_CO_08*maskCO_08






'''


Applico le maschere alle copie degli array dei coefficenti;


'''


c_maskedCO_01 = coff_CO_01*maskCO_01
c_maskedCO_02 = coff_CO_02*maskCO_02
c_maskedCO_03 = coff_CO_03*maskCO_03
c_maskedCO_04 = coff_CO_04*maskCO_04
c_maskedCO_05 = coff_CO_05*maskCO_05
c_maskedCO_06 = coff_CO_06*maskCO_06
c_maskedCO_07 = coff_CO_07*maskCO_07
c_maskedCO_08 = coff_CO_08*maskCO_08



'''


Facio l'anti-trasformata e ottengo i nuovi coefficenti;



'''

atf_CO_01 = fft.ifft(c_maskedCO_01, len(time1))
atf_CO_02 = fft.ifft(c_maskedCO_02, len(time2))
atf_CO_03 = fft.ifft(c_maskedCO_03, len(time3))
atf_CO_04 = fft.ifft(c_maskedCO_04, len(time4))
atf_CO_05 = fft.ifft(c_maskedCO_05, len(time5))
atf_CO_06 = fft.ifft(c_maskedCO_06, len(time6))
atf_CO_07 = fft.ifft(c_maskedCO_07, len(time7))
atf_CO_08 = fft.ifft(c_maskedCO_08, len(time8))

total_atf_CO = ([atf_CO_01, atf_CO_02, atf_CO_03, atf_CO_04, atf_CO_05, atf_CO_06, atf_CO_07, atf_CO_08])


atf_CO_01 = np.real(atf_CO_01)




    
for i in range(0, len(total_qtf_CO) ):
    fig, axs = plt.subplots(2, 2, sharex=False, sharey=False, layout="constrained", facecolor='aliceblue')
    
    axs[0,0].plot(total_time[i], total_CO[i], color='blue', label='CO')
    axs[0,0].set_title('Andamento Temporale', size=20, color='blue')
    axs[0,0].set_ylabel('CO mean', size=15)
    axs[0,0].set_xlabel('Time (Day)', size=15)
    axs[0,0].grid(True)
    axs[0,0].legend()
   
    axs[1,0].plot(total_freq_CO[i], total_qtf_CO[i], color='mediumvioletred', label='Spettro potenze')
    axs[1,0].set_title('Andamento in frequenze', size=20, color='mediumvioletred')
    axs[1,0].set_yscale('log')
    axs[1,0].set_ylabel('${|C_k|}^2$', size=15)
    axs[1,0].set_xlabel('${f_{k}}$', size=15)
    axs[1,0].grid(True)
    axs[1,0].legend()


    axs[1,1].plot(total_time[i], total_atf_CO[i], color='red', label='Seganle fi')
    axs[1,1].set_title('Segnale Filtrato', size=20, color='red')
    axs[1,1].set_ylabel('CO mean', size=15)
    axs[1,1].set_xlabel('Time (Day)', size=15)
    axs[1,1].grid(True)
    axs[1,1].legend()
   
    axs[0,1].plot(total_time[i], total_CO[i] , color='royalblue', alpha=0.5,label='Adamento temporale')
    axs[0,1].plot(total_time[i], total_atf_CO[i], color='red', label='Anadmento filtrato')
    axs[0,1].set_title('Origin + Filtrato', size=20, color='red')
    axs[0,1].set_ylabel('$CO mean $', size=15)
    axs[0,1].set_xlabel('$time (day)$', size=15)
    axs[0,1].grid(True)
    axs[0,1].legend()
    plt.tight_layout()
    plt.show()




freq_CO_01 = freq_CO_01*maskCO_01
freq_CO_02 = freq_CO_02*maskCO_02
freq_CO_03 = freq_CO_03*maskCO_03
freq_CO_04 = freq_CO_04*maskCO_04
freq_CO_05 = freq_CO_05*maskCO_05
freq_CO_06 = freq_CO_06*maskCO_06
freq_CO_07 = freq_CO_07*maskCO_07
freq_CO_08 = freq_CO_08*maskCO_08


#01
alpha1 = len(freq_CO_01)
final_freq_01 = np.empty(0)
for i in range (0, alpha1):
    if freq_CO_01[i] > 0.00002:
       final_freq_01 = np.append(final_freq_01,freq_CO_01[i])
       
final_freq_01 = np.round(final_freq_01,3)
final_temp_01 = 1/final_freq_01 


#02
alpha2 = len(freq_CO_02)
final_freq_02 = np.empty(0)
for i in range (0, alpha2):
    if freq_CO_02[i] > 0.00002:
       final_freq_02 = np.append(final_freq_02,freq_CO_02[i])
       
final_freq_02 = np.round(final_freq_02,3)
final_temp_02 = 1/final_freq_02



#03
alpha3 = len(freq_CO_03)
final_freq_03 = np.empty(0)
for i in range (0, alpha3):
    if freq_CO_03[i] > 0.00002:
       final_freq_03 = np.append(final_freq_03,freq_CO_03[i])
       
final_freq_03 = np.round(final_freq_03,3)
final_temp_03 = 1/final_freq_03


#04
alpha4 = len(freq_CO_04)
final_freq_04 = np.empty(0)
for i in range (0, alpha4):
    if freq_CO_04[i] > 0.00002:
       final_freq_04 = np.append(final_freq_04,freq_CO_04[i])
       
final_freq_04 = np.round(final_freq_04,3)
final_temp_04 = 1/final_freq_04



#05
alpha5 = len(freq_CO_05)
final_freq_05 = np.empty(0)
for i in range (0, alpha5):
    if freq_CO_05[i] > 0.00002:
       final_freq_05 = np.append(final_freq_05,freq_CO_05[i])
       
final_freq_05 = np.round(final_freq_05,3)
final_temp_05 = 1/final_freq_05 


#06
alpha6 = len(freq_CO_06)
final_freq_06 = np.empty(0)
for i in range (0, alpha6):
    if freq_CO_06[i] > 0.00002:
       final_freq_06 = np.append(final_freq_06,freq_CO_06[i])
       
final_freq_06 = np.round(final_freq_06,3)
final_temp_06 = 1/final_freq_06



#07
alpha7 = len(freq_CO_07)
final_freq_07 = np.empty(0)
for i in range (0, alpha7):
    if freq_CO_07[i] > 0.00002:
       final_freq_07 = np.append(final_freq_07,freq_CO_07[i])
       
final_freq_07 = np.round(final_freq_07,3)
final_temp_07 = 1/final_freq_07


#04
alpha8 = len(freq_CO_08)
final_freq_08 = np.empty(0)
for i in range (0, alpha8):
    if freq_CO_08[i] > 0.00002:
       final_freq_08 = np.append(final_freq_08,freq_CO_08[i])
       
final_freq_08 = np.round(final_freq_08,3)
final_temp_08 = 1/final_freq_08



#1
mean01 = np.mean(CO_01)
max01 = np.max(CO_01)
min01 = np.min(CO_01)
var01 = np.var(CO_01)
mf_01 = np.min(final_freq_01)
MT_01 = np.max(final_temp_01)

#2
mean02 = np.mean(CO_02)
max02 = np.max(CO_02)
min02 = np.min(CO_02)
var02 = np.var(CO_02)
mf_02 = np.min(final_freq_02)
MT_02 = np.max(final_temp_02)


#3
mean03 = np.mean(CO_03)
max03 = np.max(CO_03)
min03 = np.min(CO_03)
var03 = np.var(CO_03)
mf_03 = np.min(final_freq_03)
MT_03 = np.max(final_temp_03)

#4
mean04 = np.mean(CO_04)
max04 = np.max(CO_04)
min04 = np.min(CO_04)
var04 = np.var(CO_04)
mf_04 = np.min(final_freq_04)
MT_04 = np.max(final_temp_04)

#5
mean05 = np.mean(CO_05)
max05 = np.max(CO_05)
min05 = np.min(CO_05)
var05 = np.var(CO_05)
mf_05 = np.min(final_freq_05)
MT_05 = np.max(final_temp_05)

#6
mean06 = np.mean(CO_06)
max06 = np.max(CO_06)
min06 = np.min(CO_06)
var06 = np.var(CO_06)
mf_06 = np.min(final_freq_06)
MT_06 = np.max(final_temp_06)

#7
mean07 = np.mean(CO_07)
max07 = np.max(CO_07)
min07 = np.min(CO_07)
var07 = np.var(CO_07)
mf_07 = np.min(final_freq_07)
MT_07 = np.max(final_temp_07)

#8
mean08 = np.mean(CO_08)
max08 = np.max(CO_08)
min08 = np.min(CO_08)
var08 = np.var(CO_08)
mf_08 = np.min(final_freq_08)
MT_08 = np.max(final_temp_08)

print('\n\n\nDi seguito sono riportato un dataframe dove vengono riassunte le caretteristi piu importanti per \nogni dataset raccolto nelle varie stazioni:\n\n')

columns = ["  TEXAS_01  ", "  TEXAS_2  ", "  TEXAS_03  ", "  TEXAS_04  ", 
           "  TEXAS_05  ", "  TEXAS_06  ", "  TEXAS_07  ", "  TEXAS_08  "]
index = ["MEDIA", "VARIANZA", "MAX", "MIN", 'FREQ_MIN', 'PERIODO_MAX'  ]
data = pd.DataFrame(index=index, columns=columns)


data.loc["MEDIA"] = [mean01, mean02, mean03, mean04, mean05, mean06, mean07, mean08]
data.loc["VARIANZA"] = [var01, var02, var03, var04, var05, var06, var07, var08]
data.loc["MAX"] = [max01, max02, max03, max04, max05, max06, max07, max08]
data.loc["MIN"] = [min01, min02, min03, min04, min05, min06, min07, min08]
data.loc["FREQ_MIN"] = [mf_01, mf_02, mf_03, mf_04, mf_05, mf_06, mf_07, mf_08]
data.loc["PERIODO_MAX"] = [MT_01, MT_02, MT_03, MT_04, MT_05, MT_06, MT_07, MT_08]

data = np.round(data,3)
print(data)