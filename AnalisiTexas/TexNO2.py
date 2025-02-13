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



NO2_01 = df_Texas01['NO2 Mean'].values
NO2_02 = df_Texas02['NO2 Mean'].values
NO2_03 = df_Texas03['NO2 Mean'].values
NO2_04 = df_Texas04['NO2 Mean'].values
NO2_05 = df_Texas05['NO2 Mean'].values
NO2_06 = df_Texas06['NO2 Mean'].values
NO2_07 = df_Texas07['NO2 Mean'].values
NO2_08 = df_Texas08['NO2 Mean'].values


'''

Faccaimo i grafici

'''

'''






'''
#Texas 01
N1 = len(NO2_01)
time1 = np.arange(0,N1)

#Texas 02
N2 = len(NO2_02)
time2 = np.arange(0,N2)

#Texas 03
N3 = len(NO2_03)
time3 = np.arange(0,N3)

#Texas 04
N4 = len(NO2_04)
time4 = np.arange(0,N4)

#Texas 05
N5 = len(NO2_05)
time5 = np.arange(0,N5)

#Texas 06
N6 = len(NO2_06)
time6 = np.arange(0,N6)

#Texas 07
N7 = len(NO2_07)
time7 = np.arange(0,N7)

#Texas 04
N8 = len(NO2_08)
time8 = np.arange(0,N8)









fig, axs = plt.subplots(4, 2, sharex=False, sharey=False, layout="constrained", facecolor='aliceblue')

axs[0,0].plot(time1,  NO2_01, color='steelblue', label='NO2 texas 01')
axs[0,0].set_xlabel("Day", size=12, color='steelblue')
axs[0,0].set_ylabel("NO2 mean", size=12, color='steelblue')
axs[0,0].set_title("NO2 Texas 01", size=17, color='red')
axs[0,0].grid(True)
axs[0,0].legend()

# Subplot [0, 1]
axs[1,0].plot(time2, NO2_02, color='steelblue', label='NO2 texas 02')
axs[1,0].set_xlabel("Day", size=11, color='steelblue')
axs[1,0].set_ylabel("NO2 mean", size=11, color='steelblue')
axs[1,0].set_title("NO2 Texas 02", size=17, color='red')
axs[1,0].grid(True)
axs[1,0].legend()


# Subplot [1, 0]
axs[2, 0].plot(time3, NO2_03, color='steelblue', label='NO2 texas 03')
axs[2, 0].set_xlabel("Day", size=12, color='steelblue')
axs[2, 0].set_ylabel("NO2 mean", size=12, color='steelblue')
axs[2, 0].set_title(" NO2 Texas 03", size=17, color='red')
axs[2, 0].grid(True)
axs[2, 0].legend()


# Subplot [1, 1]
axs[3, 0].plot(time4, NO2_04, color='steelblue', label='NO2 texas 04')
axs[3, 0].set_xlabel("Day", size=12, color='steelblue')
axs[3, 0].set_ylabel("NO2 mean", size=12, color='steelblue')
axs[3, 0].set_title(" NO2 Texas 04", size=17, color='red')
axs[3, 0].grid(True)
axs[3, 0].legend()





axs[0,1].plot(time5,  NO2_05, color='steelblue', label='NO2 texas 05')
axs[0,1].set_xlabel("Day", size=12, color='steelblue')
axs[0,1].set_ylabel("NO2 mean", size=12, color='steelblue')
axs[0,1].set_title("NO2 Texas 05", size=17, color='red')
axs[0,1].grid(True)
axs[0,1].legend()

# Subplot [0, 1]
axs[1,1].plot(time6, NO2_06, color='steelblue', label='NO2 texas 06')
axs[1,1].set_xlabel("Day", size=12, color='steelblue')
axs[1,1].set_ylabel("NO2 mean", size=12, color='steelblue')
axs[1,1].set_title("NO2 Texas 06", size=17, color='red')
axs[1,1].grid(True)
axs[1,1].legend()


# Subplot [1, 0]
axs[2, 1].plot(time7, NO2_07, color='steelblue', label='NO2 texas 07')
axs[2, 1].set_xlabel("Day", size=12, color='steelblue')
axs[2, 1].set_ylabel("NO2 mean", size=12, color='steelblue')
axs[2, 1].set_title("NO2 Texas 07", size=17, color='red')
axs[2, 1].grid(True)
axs[2, 1].legend()


# Subplot [1, 1]
axs[3, 1].plot(time8, NO2_08, color='steelblue', label='NO2 texas 08 ')
axs[3, 1].set_xlabel("Day", size=12, color='steelblue')
axs[3, 1].set_ylabel("NO2 mean", size=12, color='steelblue')
axs[3, 1].set_title("NO2 Texas 08", size=17, color='red')
axs[3, 1].grid(True)
axs[3, 1].legend()

plt.show()



'''



Estraiamo i termini di fourier e le relative frequenze;
Successivamnete prendiamo il modulo quadro di questi coefficenti;
In fine per andare a fare il grafico prendiamo solo la seconda me mata dei coefficenti e delle frequenze, tanto quest'ultimo è simmetrico.


'''


tf_NO2_01 = fft.fft(NO2_01)
tf_NO2_02 = fft.fft(NO2_02)
tf_NO2_03 = fft.fft(NO2_03)
tf_NO2_04 = fft.fft(NO2_04)
tf_NO2_05 = fft.fft(NO2_05)
tf_NO2_06 = fft.fft(NO2_06)
tf_NO2_07 = fft.fft(NO2_07)
tf_NO2_08 = fft.fft(NO2_08)



#coefficenti al quadrato

qtf_NO2_01 = np.abs(tf_NO2_01)*np.abs(tf_NO2_01)
qtf_NO2_02 = np.abs(tf_NO2_02)*np.abs(tf_NO2_02)
qtf_NO2_03 = np.abs(tf_NO2_03)*np.abs(tf_NO2_03)
qtf_NO2_04 = np.abs(tf_NO2_04)*np.abs(tf_NO2_04)
qtf_NO2_05 = np.abs(tf_NO2_05)*np.abs(tf_NO2_05)
qtf_NO2_06 = np.abs(tf_NO2_06)*np.abs(tf_NO2_06)
qtf_NO2_07 = np.abs(tf_NO2_07)*np.abs(tf_NO2_07)
qtf_NO2_08 = np.abs(tf_NO2_08)*np.abs(tf_NO2_08)

#ricavo le frequenze

freq_NO2_01 = fft.fftfreq(len(NO2_01), 1)
freq_NO2_02 = fft.fftfreq(len(NO2_02), 1)
freq_NO2_03 = fft.fftfreq(len(NO2_03), 1)
freq_NO2_04 = fft.fftfreq(len(NO2_04), 1)
freq_NO2_05 = fft.fftfreq(len(NO2_05), 1)
freq_NO2_06 = fft.fftfreq(len(NO2_06), 1)
freq_NO2_07 = fft.fftfreq(len(NO2_07), 1)
freq_NO2_08 = fft.fftfreq(len(NO2_08), 1)


'''




Prendo in conciderazione solo gli la seconda meta degli array




'''

freq_NO2_01 = freq_NO2_01[: (len(freq_NO2_01)//2)]
qtf_NO2_01 = qtf_NO2_01[:    (len(qtf_NO2_01)//2)]
coff_NO2_01 = tf_NO2_01[: len(tf_NO2_01)//2]

freq_NO2_02 = freq_NO2_02[: (len(freq_NO2_02)//2)]
qtf_NO2_02 = qtf_NO2_02[:    (len(qtf_NO2_02)//2)]
coff_NO2_02 = tf_NO2_02[: len(tf_NO2_02)//2]

freq_NO2_03 = freq_NO2_03[: (len(freq_NO2_03)//2)]
qtf_NO2_03 = qtf_NO2_03[:    (len(qtf_NO2_03)//2)]
coff_NO2_03 = tf_NO2_03[: len(tf_NO2_03)//2]

freq_NO2_04 = freq_NO2_04[: (len(freq_NO2_04)//2)]
qtf_NO2_04 = qtf_NO2_04[:    (len(qtf_NO2_04)//2)]
coff_NO2_04 = tf_NO2_04[: len(tf_NO2_04)//2]

freq_NO2_05 = freq_NO2_05[: (len(freq_NO2_05)//2)]
qtf_NO2_05 = qtf_NO2_05[:    (len(qtf_NO2_05)//2)]
coff_NO2_05 = tf_NO2_05[: len(tf_NO2_05)//2]

freq_NO2_06 = freq_NO2_06[: (len(freq_NO2_06)//2)]
qtf_NO2_06 = qtf_NO2_06[:    (len(qtf_NO2_06)//2)]
coff_NO2_06 = tf_NO2_06[: len(tf_NO2_06)//2]

freq_NO2_07 = freq_NO2_07[: (len(freq_NO2_07)//2)]
qtf_NO2_07 = qtf_NO2_07[:    (len(qtf_NO2_07)//2)]
coff_NO2_07 = tf_NO2_07[: len(tf_NO2_07)//2]

freq_NO2_08 = freq_NO2_08[: (len(freq_NO2_08)//2)]
qtf_NO2_08 = qtf_NO2_08[:    (len(qtf_NO2_08)//2)]
coff_NO2_08 = tf_NO2_08[: len(tf_NO2_08)//2]


'''

Facciendo i grafici delle spettri di potenze

'''

total_NO2 = ([NO2_01,NO2_02,NO2_03,NO2_04,NO2_05,NO2_06,NO2_07,NO2_08])
total_time = ([time1,time2,time3,time4,time5,time6,time7,time8])
total_qtf_NO2 = ([ qtf_NO2_01, qtf_NO2_02, qtf_NO2_03, qtf_NO2_04,qtf_NO2_05,qtf_NO2_06,qtf_NO2_07,qtf_NO2_08 ])
total_freq_NO2 = ([freq_NO2_01,freq_NO2_02,freq_NO2_03,freq_NO2_04,freq_NO2_05,freq_NO2_06,freq_NO2_07,freq_NO2_08])


for i in range(0, len(total_qtf_NO2) ):
    fig, axs = plt.subplots(2, 1, sharex=False, sharey=False, layout="constrained", facecolor='aliceblue')
    
    axs[0].plot(total_time[i], total_NO2[i], color='royalblue', label='Adamento temporale')
    axs[0].set_title('Anadamento temporale', size=20, color='royalblue')
    axs[0].set_ylabel('NO2 mean', size = 15)
    axs[0].set_xlabel('Time (Day)', size = 15)
    axs[0].grid(True)
    axs[0].legend()

    axs[1].plot(total_freq_NO2[i], total_qtf_NO2[i], color='red', marker='', label='Spettro potenze NO2')
    axs[1].set_title('Andamento in frequenze', size=20, color='red')
    axs[1].set_yscale('log')
    axs[1].set_ylabel('${|C_k|}^2$', size = 15)
    axs[1].set_xlabel('${f_{k}}$', size = 15)
    axs[1].grid(True)
    axs[1].legend()


    plt.tight_layout()
    plt.show()
    print('Analisi campionamneto di NO2\n Texas:\t0',i+1,'\n')



'''


Faccio i filtri sulle frequenze


'''


maskNO2_01 = abs(freq_NO2_01) < 0.04
maskNO2_02 = abs(freq_NO2_02) < 0.04
maskNO2_03 = abs(freq_NO2_03) < 0.04
maskNO2_04 = abs(freq_NO2_04) < 0.04
maskNO2_05 = abs(freq_NO2_05) < 0.04
maskNO2_06 = abs(freq_NO2_06) < 0.04
maskNO2_07 = abs(freq_NO2_07) < 0.04
maskNO2_08 = abs(freq_NO2_08) < 0.04


'''


Frequenze selezionate...




'''



freq_NO2_01 = freq_NO2_01*maskNO2_01
freq_NO2_02 = freq_NO2_02*maskNO2_02
freq_NO2_03 = freq_NO2_03*maskNO2_03
freq_NO2_04 = freq_NO2_04*maskNO2_04
freq_NO2_05 = freq_NO2_05*maskNO2_05
freq_NO2_06 = freq_NO2_06*maskNO2_06
freq_NO2_07 = freq_NO2_07*maskNO2_07
freq_NO2_08 = freq_NO2_08*maskNO2_08






'''


Applico le maschere alle copie degli array dei coefficenti;


'''


c_maskedNO2_01 = coff_NO2_01*maskNO2_01
c_maskedNO2_02 = coff_NO2_02*maskNO2_02
c_maskedNO2_03 = coff_NO2_03*maskNO2_03
c_maskedNO2_04 = coff_NO2_04*maskNO2_04
c_maskedNO2_05 = coff_NO2_05*maskNO2_05
c_maskedNO2_06 = coff_NO2_06*maskNO2_06
c_maskedNO2_07 = coff_NO2_07*maskNO2_07
c_maskedNO2_08 = coff_NO2_08*maskNO2_08



'''


Facio l'anti-trasformata e ottengo i nuovi coefficenti;



'''

atf_NO2_01 = fft.ifft(c_maskedNO2_01, len(time1))
atf_NO2_02 = fft.ifft(c_maskedNO2_02, len(time2))
atf_NO2_03 = fft.ifft(c_maskedNO2_03, len(time3))
atf_NO2_04 = fft.ifft(c_maskedNO2_04, len(time4))
atf_NO2_05 = fft.ifft(c_maskedNO2_05, len(time5))
atf_NO2_06 = fft.ifft(c_maskedNO2_06, len(time6))
atf_NO2_07 = fft.ifft(c_maskedNO2_07, len(time7))
atf_NO2_08 = fft.ifft(c_maskedNO2_08, len(time8))

total_atf_NO2 = ([atf_NO2_01, atf_NO2_02, atf_NO2_03, atf_NO2_04, atf_NO2_05, atf_NO2_06, atf_NO2_07, atf_NO2_08])


atf_NO2_01 = np.real(atf_NO2_01)




    
for i in range(0, len(total_qtf_NO2) ):
    fig, axs = plt.subplots(2, 2, sharex=False, sharey=False, layout="constrained", facecolor='aliceblue')
    
    axs[0,0].plot(total_time[i], total_NO2[i], color='blue', label='NO2')
    axs[0,0].set_title('Andamento Temporale', size=20, color='blue')
    axs[0,0].set_ylabel('NO2 mean', size=15)
    axs[0,0].set_xlabel('Time (Day)', size=15)
    axs[0,0].grid(True)
    axs[0,0].legend()
   
    axs[1,0].plot(total_freq_NO2[i], total_qtf_NO2[i], color='mediumvioletred', label='Spettro potenze')
    axs[1,0].set_title('Andamento in frequenze', size=20, color='mediumvioletred')
    axs[1,0].set_yscale('log')
    axs[1,0].set_ylabel('${|C_k|}^2$', size=15)
    axs[1,0].set_xlabel('${f_{k}}$', size=15)
    axs[1,0].grid(True)
    axs[1,0].legend()


    axs[1,1].plot(total_time[i], total_atf_NO2[i], color='red', label='Seganle fi')
    axs[1,1].set_title('Segnale Filtrato', size=20, color='red')
    axs[1,1].set_ylabel('NO2 mean', size=15)
    axs[1,1].set_xlabel('Time (Day)', size=15)
    axs[1,1].grid(True)
    axs[1,1].legend()
   
    axs[0,1].plot(total_time[i], total_NO2[i] , color='royalblue', alpha=0.5,label='Adamento temporale')
    axs[0,1].plot(total_time[i], total_atf_NO2[i], color='red', label='Anadmento filtrato')
    axs[0,1].set_title('Origin + Filtrato', size=20, color='red')
    axs[0,1].set_ylabel('$NO2 mean $', size=15)
    axs[0,1].set_xlabel('$time (day)$', size=15)
    axs[0,1].grid(True)
    axs[0,1].legend()
    plt.tight_layout()
    plt.show()




#01
alpha1 = len(freq_NO2_01)
final_freq_01 = np.empty(0)
for i in range (0, alpha1):
    if freq_NO2_01[i] > 0.00002:
       final_freq_01 = np.append(final_freq_01,freq_NO2_01[i])
       
final_freq_01 = np.round(final_freq_01,3)
final_temp_01 = 1/final_freq_01 


#02
alpha2 = len(freq_NO2_02)
final_freq_02 = np.empty(0)
for i in range (0, alpha2):
    if freq_NO2_02[i] > 0.00002:
       final_freq_02 = np.append(final_freq_02,freq_NO2_02[i])
       
final_freq_02 = np.round(final_freq_02,3)
final_temp_02 = 1/final_freq_02



#03
alpha3 = len(freq_NO2_03)
final_freq_03 = np.empty(0)
for i in range (0, alpha3):
    if freq_NO2_03[i] > 0.00002:
       final_freq_03 = np.append(final_freq_03,freq_NO2_03[i])
       
final_freq_03 = np.round(final_freq_03,3)
final_temp_03 = 1/final_freq_03


#04
alpha4 = len(freq_NO2_04)
final_freq_04 = np.empty(0)
for i in range (0, alpha4):
    if freq_NO2_04[i] > 0.00002:
       final_freq_04 = np.append(final_freq_04,freq_NO2_04[i])
       
final_freq_04 = np.round(final_freq_04,3)
final_temp_04 = 1/final_freq_04



#05
alpha5 = len(freq_NO2_05)
final_freq_05 = np.empty(0)
for i in range (0, alpha5):
    if freq_NO2_05[i] > 0.00002:
       final_freq_05 = np.append(final_freq_05,freq_NO2_05[i])
       
final_freq_05 = np.round(final_freq_05,3)
final_temp_05 = 1/final_freq_05 


#06
alpha6 = len(freq_NO2_06)
final_freq_06 = np.empty(0)
for i in range (0, alpha6):
    if freq_NO2_06[i] > 0.00002:
       final_freq_06 = np.append(final_freq_06,freq_NO2_06[i])
       
final_freq_06 = np.round(final_freq_06,3)
final_temp_06 = 1/final_freq_06



#07
alpha7 = len(freq_NO2_07)
final_freq_07 = np.empty(0)
for i in range (0, alpha7):
    if freq_NO2_07[i] > 0.00002:
       final_freq_07 = np.append(final_freq_07,freq_NO2_07[i])
       
final_freq_07 = np.round(final_freq_07,3)
final_temp_07 = 1/final_freq_07


#04
alpha8 = len(freq_NO2_08)
final_freq_08 = np.empty(0)
for i in range (0, alpha8):
    if freq_NO2_08[i] > 0.00002:
       final_freq_08 = np.append(final_freq_08,freq_NO2_08[i])
       
final_freq_08 = np.round(final_freq_08,3)
final_temp_08 = 1/final_freq_08



#1
mean01 = np.mean(NO2_01)
max01 = np.max(NO2_01)
min01 = np.min(NO2_01)
var01 = np.var(NO2_01)
mf_01 = np.min(final_freq_01)
MT_01 = np.max(final_temp_01)

#2
mean02 = np.mean(NO2_02)
max02 = np.max(NO2_02)
min02 = np.min(NO2_02)
var02 = np.var(NO2_02)
mf_02 = np.min(final_freq_02)
MT_02 = np.max(final_temp_02)


#3
mean03 = np.mean(NO2_03)
max03 = np.max(NO2_03)
min03 = np.min(NO2_03)
var03 = np.var(NO2_03)
mf_03 = np.min(final_freq_03)
MT_03 = np.max(final_temp_03)

#4
mean04 = np.mean(NO2_04)
max04 = np.max(NO2_04)
min04 = np.min(NO2_04)
var04 = np.var(NO2_04)
mf_04 = np.min(final_freq_04)
MT_04 = np.max(final_temp_04)

#5
mean05 = np.mean(NO2_05)
max05 = np.max(NO2_05)
min05 = np.min(NO2_05)
var05 = np.var(NO2_05)
mf_05 = np.min(final_freq_05)
MT_05 = np.max(final_temp_05)

#6
mean06 = np.mean(NO2_06)
max06 = np.max(NO2_06)
min06 = np.min(NO2_06)
var06 = np.var(NO2_06)
mf_06 = np.min(final_freq_06)
MT_06 = np.max(final_temp_06)

#7
mean07 = np.mean(NO2_07)
max07 = np.max(NO2_07)
min07 = np.min(NO2_07)
var07 = np.var(NO2_07)
mf_07 = np.min(final_freq_07)
MT_07 = np.max(final_temp_07)

#8
mean08 = np.mean(NO2_08)
max08 = np.max(NO2_08)
min08 = np.min(NO2_08)
var08 = np.var(NO2_08)
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