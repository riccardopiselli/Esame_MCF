# Esame_MCF
Il  documento allegato  contiene un elaborato svolto per l'esame di "metodi computazionali per la fisica".
Il compito da svolgere è l' analisi di una dataset, contenete i campionamenti di alcuni inquinanti atmosferici misurati da stazioni dislocate negli usa.
La raccolta dati copre un intervallo di tempo che va dal gennaio 2013 fino a dicembre 2015, e per ogni stato americano sono presenti più stazioni di riferimento.

Durante l'analisi dei dati, è emersa una problematica iniziale. Le richieste prevedevano:

-  uno studio dell'evoluzione temporale dei vari inquinanti all'interno di uno stesso Stato;
-  un'analisi dei dati raccolti dalle diverse stazioni di monitoraggio per ciascuno Stato;
-  un confronto dello stesso inquinante tra i vari Stati ed eventualmente tra le diverse stazioni.

La problematica riscontrata consiste nel fatto che, per la maggior parte degli Stati, è disponibile il dataset di una sola stazione di monitoraggio.
Per garantire un'analisi più iteressante, è stato deciso di selezionare quattro Stati con una sola stazione di monitoraggio e un ulteriore Stato (il Texas), caratterizzato dal maggior numero  in assoluto di stazioni disponibili (otto). Questa scelta consente di effettuare uno studio comparativo tra le diverse stazioni di uno stesso Stato.

## DESCRIZZIONE CONTENUTO FILE E ORDINE APERTURA FILE ##

1) La prima cosa da fare e aprire la directory Stati; facendo **ls** è possibile vedere che essa contiene il file **pollution_us_13_15.csv** che raccogli il dataset completo e dei file .py
2) Succesivamente va mandato in secuzione il file **AndamentiStati.py** che analizza il file .csv e ne scrive altri del tipo **NomedelloStato.csv**
3) Ogni file python 'legge' il file .csv decodificato con lo stesso nome dello stato.
4) Una volta che i file:
   - **Alaska.py**
   - **Oregon.py**
   - **Minnesota.py**
   - **Alabama.py**

sono stati mandati in esecuzione ed eseguiti correttamnete è possibile runnare il file **RiassuntoStati.py**
che raccogli tutti i risultati precedenti.

5) La cartella Texas contiene una studio simile a quello fatto per i stati precedenti, ma a causa del maggiore numero stazioni è stata dedicata una cartella specifica solo a questo studio, il primo file da mandare in esecuzione è **Texas.py**
che prede i dati dal csv di riferimento e li divide per le diverse stazioni; una volta eseguito il file è possibile digitando il comando **ls** visualizzare la lista nuovi file .csv

6) Adesso è possibile eseguire liberamente uno dei file **TexCO.py** **TexNO2.py**  **TexSO2.py** **TexO3.py**.
7) Per la directory inquinanti non vi è un ordine preferenziale in cui eseguire i file .py

## Considerazioni ##

Lo studio studio dei dati campionanti è stato fatto con le trasformate di fuorie.
Come da richiesta sono state selezioante solo le freqienza più basse (armoniche di periodo maggiore) per la ricostruzione del segnale.
Tuttavia il codice per  maschere sulle frequenze è stato fatto in modo tale che l'utente pottesse modificarne il 'taglio'.
Alla fine di ogni studio sono stampati dei dataframe che riportano i risulatati.



