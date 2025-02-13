import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy import fft
import math
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import os




np.seterr(divide='ignore')




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


directory_path = '/home/riccardo-piselli/metodicf/Esame/Stati/' 
Texas_file_name = "Texas.csv"  
Texas_file_path = os.path.join(directory_path, Texas_file_name)
mydf = pd.read_csv(Texas_file_path)


correct_line_Texas01 = np.empty(0)
correct_line_Texas02 = np.empty(0)
correct_line_Texas03 = np.empty(0)
correct_line_Texas04 = np.empty(0)
correct_line_Texas05 = np.empty(0)
correct_line_Texas06 = np.empty(0)
correct_line_Texas07 = np.empty(0)
correct_line_Texas08 = np.empty(0)


N = len(mydf['Date Local'])
Address = mydf['Address']

for i in range(0,N-1):
    if Address[i] == '1415 Hinton Street':
       correct_line_Texas01 = np.append(correct_line_Texas01, i)
    
    elif Address[i] == '250 Rim Rd':
        correct_line_Texas02 = np.append(correct_line_Texas02, i)
    
    elif Address[i] == '800 S San Marcial Street' :
        correct_line_Texas03 = np.append(correct_line_Texas03, i)

  
    elif Address[i] == '7421 Park Place Blvd':
        correct_line_Texas04 = np.append(correct_line_Texas04, i)

    elif Address[i] == '9525 1/2 Clinton Dr':
        correct_line_Texas05 = np.append(correct_line_Texas05, i)

    elif Address[i] == '4514 1/2 Durant St':
        correct_line_Texas06 = np.append(correct_line_Texas06, i)
    
    elif Address[i] == '4472 Mazanec Rd':
        correct_line_Texas07 = np.append(correct_line_Texas07, i)
    
    elif Address[i] == '3724 North Hills Dr':
        correct_line_Texas08 = np.append(correct_line_Texas08, i)



df_Texas01 = mydf.iloc[correct_line_Texas01]
df_Texas02 = mydf.iloc[correct_line_Texas02]
df_Texas03 = mydf.iloc[correct_line_Texas03]
df_Texas04 = mydf.iloc[correct_line_Texas04]
df_Texas05 = mydf.iloc[correct_line_Texas05]
df_Texas06 = mydf.iloc[correct_line_Texas06]
df_Texas07 = mydf.iloc[correct_line_Texas07]
df_Texas08 = mydf.iloc[correct_line_Texas08]

'''



Salvo i risulatati dei miei dataframe in dei file csv... 



'''



df_Texas01.to_csv('Texas01.csv')
df_Texas02.to_csv('Texas02.csv')
df_Texas03.to_csv('Texas03.csv')
df_Texas04.to_csv('Texas04.csv')
df_Texas05.to_csv('Texas05.csv')
df_Texas06.to_csv('Texas06.csv')
df_Texas07.to_csv('Texas07.csv')
df_Texas08.to_csv('Texas08.csv')

'''

Adesso faccio i grafici...
Iniziamo estraendo le colonne che mi interessano dai vari Dataframe

'''


SO2_01 = df_Texas01['SO2 Mean'].values
SO2_02 = df_Texas02['SO2 Mean'].values
SO2_03 = df_Texas03['SO2 Mean'].values
SO2_04 = df_Texas04['SO2 Mean'].values
SO2_05 = df_Texas05['SO2 Mean'].values
SO2_06 = df_Texas06['SO2 Mean'].values
SO2_07 = df_Texas07['SO2 Mean'].values
SO2_08 = df_Texas08['SO2 Mean'].values

NO2_01 = df_Texas01['NO2 Mean'].values
NO2_02 = df_Texas02['NO2 Mean'].values
NO2_03 = df_Texas03['NO2 Mean'].values
NO2_04 = df_Texas04['NO2 Mean'].values
NO2_05 = df_Texas05['NO2 Mean'].values
NO2_06 = df_Texas06['NO2 Mean'].values
NO2_07 = df_Texas07['NO2 Mean'].values
NO2_08 = df_Texas08['NO2 Mean'].values

O3_01 = df_Texas01['O3 Mean'].values
O3_02 = df_Texas02['O3 Mean'].values
O3_03 = df_Texas03['O3 Mean'].values
O3_04 = df_Texas04['O3 Mean'].values
O3_05 = df_Texas05['O3 Mean'].values
O3_06 = df_Texas06['O3 Mean'].values
O3_07 = df_Texas07['O3 Mean'].values
O3_08 = df_Texas08['O3 Mean'].values

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
#Texas 01
N1 = len(SO2_01)
time1 = np.arange(0,N1)

#Texas 02
N2 = len(SO2_02)
time2 = np.arange(0,N2)

#Texas 03
N3 = len(SO2_03)
time3 = np.arange(0,N3)

#Texas 04
N4 = len(SO2_04)
time4 = np.arange(0,N4)

#Texas 05
N5 = len(SO2_05)
time5 = np.arange(0,N5)

#Texas 06
N6 = len(SO2_06)
time6 = np.arange(0,N6)

#Texas 07
N7 = len(SO2_07)
time7 = np.arange(0,N7)

#Texas 04
N8 = len(SO2_08)
time8 = np.arange(0,N8)



fig, axs = plt.subplots(4, 2, sharex=False, sharey=False, layout="constrained", facecolor='aliceblue')

axs[0,0].plot(time1,  CO_01, color='steelblue', label='Co texas 01')
axs[0,0].set_xlabel("Day", size=12, color='steelblue')
axs[0,0].set_ylabel("CO mean", size=12, color='steelblue')
axs[0,0].set_title("Texas 01", size=17, color='red')
axs[0,0].grid(True)
axs[0,0].legend()

# Subplot [0, 1]
axs[1,0].plot(time2, CO_02, color='steelblue', label='CO texas 02')
axs[1,0].set_xlabel("Day", size=11, color='steelblue')
axs[1,0].set_ylabel("CO mean", size=11, color='steelblue')
axs[1,0].set_title("Texas 02", size=17, color='steelblue')
axs[1,0].grid(True)
axs[1,0].legend()


# Subplot [1, 0]
axs[2, 0].plot(time3, CO_03, color='steelblue', label='CO texas 03')
axs[2, 0].set_xlabel("Day", size=12, color='steelblue')
axs[2, 0].set_ylabel("CO mean", size=12, color='steelblue')
axs[2, 0].set_title("Texas 03", size=17, color='red')
axs[2, 0].grid(True)
axs[2, 0].legend()


# Subplot [1, 1]
axs[3, 0].plot(time4, CO_04, color='steelblue', label='CO texas 04')
axs[3, 0].set_xlabel("Day", size=12, color='steelblue')
axs[3, 0].set_ylabel("CO mean", size=12, color='steelblue')
axs[3, 0].set_title("Texas 04", size=17, color='red')
axs[3, 0].grid(True)
axs[3, 0].legend()


axs[0,1].plot(time5,  CO_05, color='steelblue', label='Co texas 05')
axs[0,1].set_xlabel("Day", size=12, color='steelblue')
axs[0,1].set_ylabel("CO mean", size=12, color='steelblue')
axs[0,1].set_title("Co Texas 05", size=17, color='red')
axs[0,1].grid(True)
axs[0,1].legend()

# Subplot [0, 1]
axs[1,1].plot(time6, CO_06, color='steelblue', label='CO texas 06')
axs[1,1].set_xlabel("Day", size=12, color='steelblue')
axs[1,1].set_ylabel("CO mean", size=12, color='steelblue')
axs[1,1].set_title("Co Texas 06", size=17, color='red')
axs[1,1].grid(True)
axs[1,1].legend()


# Subplot [1, 0]
axs[2, 1].plot(time7, CO_07, color='steelblue', label='CO texas 07')
axs[2, 1].set_xlabel("Day", size=12, color='steelblue')
axs[2, 1].set_ylabel("CO mean", size=12, color='steelblue')
axs[2, 1].set_title("Co Texas 07", size=17, color='red')
axs[2, 1].grid(True)
axs[2, 1].legend()


# Subplot [1, 1]
axs[3, 1].plot(time8, CO_08, color='steelblue', label='CO texas 08 ')
axs[3, 1].set_xlabel("Day", size=12, color='steelblue')
axs[3, 1].set_ylabel("CO mean", size=12, color='steelblue')
axs[3, 1].set_title("Co Texas 08", size=17, color='red')
axs[3, 1].grid(True)
axs[3, 1].legend()

plt.close()






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

plt.close()

fig, axs = plt.subplots(4, 2, sharex=False, sharey=False, layout="constrained", facecolor='aliceblue')

axs[0,0].plot(time1,  SO2_01, color='steelblue', label='SO2 texas 01')
axs[0,0].set_xlabel("Day", size=12, color='steelblue')
axs[0,0].set_ylabel("SO2 mean", size=12, color='steelblue')
axs[0,0].set_title("SO2 Texas 01", size=17, color='red')
axs[0,0].grid(True)
axs[0,0].legend()

# Subplot [0, 1]
axs[1,0].plot(time2, SO2_02, color='steelblue', label='SO2 texas 02')
axs[1,0].set_xlabel("Day", size=11, color='steelblue')
axs[1,0].set_ylabel("SO2 mean", size=11, color='steelblue')
axs[1,0].set_title("SO2 Texas 02", size=17, color='red')
axs[1,0].grid(True)
axs[1,0].legend()


# Subplot [1, 0]
axs[2, 0].plot(time3, SO2_03, color='steelblue', label='SO2 texas 03')
axs[2, 0].set_xlabel("Day", size=12, color='steelblue')
axs[2, 0].set_ylabel("SO2 mean", size=12, color='steelblue')
axs[2, 0].set_title(" SO2 Texas 03", size=17, color='red')
axs[2, 0].grid(True)
axs[2, 0].legend()


# Subplot [1, 1]
axs[3, 0].plot(time4, SO2_04, color='steelblue', label='SO2 texas 04')
axs[3, 0].set_xlabel("Day", size=12, color='steelblue')
axs[3, 0].set_ylabel("SO2 mean", size=12, color='steelblue')
axs[3, 0].set_title(" SO2 Texas 04", size=17, color='red')
axs[3, 0].grid(True)
axs[3, 0].legend()





axs[0,1].plot(time5,  SO2_05, color='steelblue', label='SO2 texas 05')
axs[0,1].set_xlabel("Day", size=12, color='steelblue')
axs[0,1].set_ylabel("SO2 mean", size=12, color='steelblue')
axs[0,1].set_title("SO2 Texas 05", size=17, color='red')
axs[0,1].grid(True)
axs[0,1].legend()

# Subplot [0, 1]
axs[1,1].plot(time6, SO2_06, color='steelblue', label='SO2 texas 06')
axs[1,1].set_xlabel("Day", size=12, color='steelblue')
axs[1,1].set_ylabel("SO2 mean", size=12, color='steelblue')
axs[1,1].set_title("SO2 Texas 06", size=17, color='red')
axs[1,1].grid(True)
axs[1,1].legend()


# Subplot [1, 0]
axs[2, 1].plot(time7, SO2_07, color='steelblue', label='SO2 texas 07')
axs[2, 1].set_xlabel("Day", size=12, color='steelblue')
axs[2, 1].set_ylabel("SO2 mean", size=12, color='steelblue')
axs[2, 1].set_title("SO2 Texas 07", size=17, color='red')
axs[2, 1].grid(True)
axs[2, 1].legend()


# Subplot [1, 1]
axs[3, 1].plot(time8, SO2_08, color='steelblue', label='SO2 texas 08 ')
axs[3, 1].set_xlabel("Day", size=12, color='steelblue')
axs[3, 1].set_ylabel("SO2 mean", size=12, color='steelblue')
axs[3, 1].set_title("SO2 Texas 08", size=17, color='red')
axs[3, 1].grid(True)
axs[3, 1].legend()


plt.close()


fig, axs = plt.subplots(4, 2, sharex=False, sharey=False, layout="constrained", facecolor='aliceblue')

axs[0,0].plot(time1,  O3_01, color='steelblue', label='O3 texas 01')
axs[0,0].set_xlabel("Day", size=12, color='steelblue')
axs[0,0].set_ylabel("O3 mean", size=12, color='steelblue')
axs[0,0].set_title("O3 Texas 01", size=17, color='red')
axs[0,0].grid(True)
axs[0,0].legend()

# Subplot [0, 1]
axs[1,0].plot(time2, O3_02, color='steelblue', label='O3 texas 02')
axs[1,0].set_xlabel("Day", size=11, color='steelblue')
axs[1,0].set_ylabel("O3 mean", size=11, color='steelblue')
axs[1,0].set_title("O3 Texas 02", size=17, color='red')
axs[1,0].grid(True)
axs[1,0].legend()


# Subplot [1, 0]
axs[2, 0].plot(time3, O3_03, color='steelblue', label='O3 texas 03')
axs[2, 0].set_xlabel("Day", size=12, color='steelblue')
axs[2, 0].set_ylabel("O3 mean", size=12, color='steelblue')
axs[2, 0].set_title(" O3 Texas 03", size=17, color='red')
axs[2, 0].grid(True)
axs[2, 0].legend()


# Subplot [1, 1]
axs[3, 0].plot(time4, O3_04, color='steelblue', label='O3 texas 04')
axs[3, 0].set_xlabel("Day", size=12, color='steelblue')
axs[3, 0].set_ylabel("O3 mean", size=12, color='steelblue')
axs[3, 0].set_title(" O3 Texas 04", size=17, color='red')
axs[3, 0].grid(True)
axs[3, 0].legend()





axs[0,1].plot(time5,  O3_05, color='steelblue', label='O3 texas 05')
axs[0,1].set_xlabel("Day", size=12, color='steelblue')
axs[0,1].set_ylabel("O3 mean", size=12, color='steelblue')
axs[0,1].set_title("O3 Texas 05", size=17, color='red')
axs[0,1].grid(True)
axs[0,1].legend()

# Subplot [0, 1]
axs[1,1].plot(time6, O3_06, color='steelblue', label='O3 texas 06')
axs[1,1].set_xlabel("Day", size=12, color='steelblue')
axs[1,1].set_ylabel("O3 mean", size=12, color='steelblue')
axs[1,1].set_title("O3 Texas 06", size=17, color='red')
axs[1,1].grid(True)
axs[1,1].legend()


# Subplot [1, 0]
axs[2, 1].plot(time7, O3_07, color='steelblue', label='O3 texas 07')
axs[2, 1].set_xlabel("Day", size=12, color='steelblue')
axs[2, 1].set_ylabel("O3 mean", size=12, color='steelblue')
axs[2, 1].set_title("O3 Texas 07", size=17, color='red')
axs[2, 1].grid(True)
axs[2, 1].legend()


# Subplot [1, 1]
axs[3, 1].plot(time8, O3_08, color='steelblue', label='O3 texas 08 ')
axs[3, 1].set_xlabel("Day", size=12, color='steelblue')
axs[3, 1].set_ylabel("O3 mean", size=12, color='steelblue')
axs[3, 1].set_title("O3 Texas 08", size=17, color='red')
axs[3, 1].grid(True)
axs[3, 1].legend()

plt.close()


'''


'''
Estraiamo i termini di fourier e le relative frequenze;
Successivamnete prendiamo il modulo quadro di questi coefficenti;
In fine per andare a fare il grafico prendiamo solo la seconda me mata dei coefficenti e delle frequenze, tanto quest'ultimo è simmetrico.
'''

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


'''

total_NO2 = ([NO2_01,NO2_02,NO2_03,NO2_04,NO2_05,NO2_06,NO2_07,NO2_08])
total_time = ([time1,time2,time3,time4,time5,time6,time7,time8])
total_qtf_NO2 = ([ qtf_NO2_01, qtf_NO2_02, qtf_NO2_03, qtf_NO2_04,qtf_NO2_05,qtf_NO2_06,qtf_NO2_07,qtf_NO2_08 ])
total_freq_NO2 = ([freq_NO2_01,freq_NO2_02,freq_NO2_03,freq_NO2_04,freq_NO2_05,freq_NO2_06,freq_NO2_07,freq_NO2_08])


for i in range(0, len(total_qtf_NO2) ):
    fig, axs = plt.subplots(2, 1, sharex=False, sharey=False, layout="constrained", facecolor='aliceblue')
    
    axs[0].plot(total_time[i], total_NO2[i], color='royalblue', label='Adamento temporale')
    axs[0].set_title('Anadamento temporale', size=15, color='royalblue')
    axs[0].set_ylabel('NO2 mean')
    axs[0].set_xlabel('Time (Day)')
    axs[0].grid(True)
    axs[0].legend()

    axs[1].plot(total_freq_NO2[i], total_qtf_NO2[i], color='red', marker='v', label='Spettro potenze NO2')
    axs[1].set_title('Andamento in frequenze', size=15, color='red')
    axs[1].set_yscale('log')
    axs[1].set_ylabel('${|C_k|}^2$')
    axs[1].set_xlabel('${f_{k}}$')
    axs[1].grid(True)
    axs[1].legend()
    plt.tight_layout()
    plt.close()




'''




'''


maskNO2_01 = abs(freq_NO2_01) < 0.06
maskNO2_02 = abs(freq_NO2_02) < 0.05
maskNO2_03 = abs(freq_NO2_03) < 0.05
maskNO2_04 = abs(freq_NO2_04) < 0.05
maskNO2_05 = abs(freq_NO2_05) < 0.05
maskNO2_06 = abs(freq_NO2_06) < 0.05
maskNO2_07 = abs(freq_NO2_07) < 0.05
maskNO2_08 = abs(freq_NO2_08) < 0.05


'''






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
    axs[0,0].set_title('Andamento Temporale', size=15, color='blue')
    axs[0,0].set_ylabel('NO2 mean')
    axs[0,0].set_xlabel('Time (Day)')
    axs[0,0].grid(True)
    axs[0,0].legend()
   
    axs[1,0].plot(total_freq_NO2[i], total_qtf_NO2[i], color='darkviolet', label='Spettro potenze')
    axs[1,0].set_title('Andamento in frequenze', size=15, color='darkviolet')
    axs[1,0].set_yscale('log')
    axs[1,0].set_ylabel('${|C_k|}^2$')
    axs[1,0].set_xlabel('${f_{k}}$')
    axs[1,0].grid(True)
    axs[1,0].legend()


    axs[1,1].plot(total_time[i], total_atf_NO2[i], color='red', label='Seganle fi')
    axs[1,1].set_title('Segnale filtrato', size=15, color='red')
    axs[1,1].set_ylabel('NO2 mean')
    axs[1,1].set_xlabel('Time (Day)')
    axs[1,1].grid(True)
    axs[1,1].legend()
   
    axs[0,1].plot(total_time[i], total_NO2[i] , color='royalblue', alpha=0.5,label='Adamento temporale')
    axs[0,1].plot(total_time[i], total_atf_NO2[i], color='red', label='Anadmento filtrato')
    axs[0,1].set_title('Confronto segnale originale e filtrato', size=15, color='red')
    axs[0,1].set_ylabel('$NO2 mean $')
    axs[0,1].set_xlabel('$time (day)$')
    axs[0,1].grid(True)
    axs[0,1].legend()
    plt.show()

'''