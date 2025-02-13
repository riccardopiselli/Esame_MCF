import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from  scipy import integrate
import math
import matplotlib.pyplot as plt
import matplotlib.colors as colors


Data_Oregon_scaricato = pd.read_csv('Data_Oregon.csv') 
Data_Alaska_scaricato = pd.read_csv('Data_Alaska.csv') 
Data_Minnesota_scaricato = pd.read_csv('Data_Minnesota.csv') 
Data_Alabama_scaricato = pd.read_csv('Data_Alabama.csv') 


print('\n\nLe seguenti tabelle contengono delle informazioni rigurdo \nal andamento  temporale degli inquinanti nei vari stati\n\n')
print('Alaska  from 2014-07-01 to 2015-12-31: \n \n',Data_Alaska_scaricato,'\n')
print('Alabama from 2013-12-01 to 2015-12-31: \n \n ',Data_Alabama_scaricato,'\n')
print('Oregon: from 2013-01-01 to 2015-12-31:\n \n',Data_Oregon_scaricato,'\n')
print('Minnesota from 2014-05-02 to 2015-12-31 : \n \n',Data_Minnesota_scaricato,'\n')
print('\n \n \n')


Completo_alaska_scaricato = pd.read_csv('_alaska.csv')
Completo_oregon_scaricato = pd.read_csv('_oregon.csv')
Completo_alabama_scaricato = pd.read_csv('_alabama.csv')
Completo_minnesota_scaricato = pd.read_csv('_minnesota.csv')


print('\n La tabelle succesiva racolglie le frequenze (1/1 giorno), con relativi periodi (giorni), filtrate \n dalle maschere per tutti gli stati: \n')


print('\nAlaska: \n',Completo_alaska_scaricato,'\n')
print('\nAlabama: \n',Completo_alabama_scaricato,'\n')
print('\nOregon: \n',Completo_oregon_scaricato,'\n')
print('\nMinnesota: \n',Completo_minnesota_scaricato,'\n')
