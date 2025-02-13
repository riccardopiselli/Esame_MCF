# Esame_MCF
Il  documento in allegato  contiene un elaborato svolto per l'esame di "metodi computazionali per la fisica".
Il compito da svolgere è l' analisi di una dataset, contenete i campionamenti di alcuni inquinanti atmosferici misurati da stazioni dislocate negli usa.
La raccolta dati copre un intervallo di tempo che va dal gennaio 2013 fino a dicembre 2015, e per ogni stato americano sono presenti più stazioni di riferimento.

Durante l'analisi dei dati, è emersa una problematica iniziale, le richieste prevedevano:

-  uno studio dell'evoluzione temporale dei vari inquinanti all'interno di uno stesso Stato;
-  un'analisi dei dati raccolti dalle diverse stazioni di monitoraggio per ciascuno Stato;
-  un confronto dello stesso inquinante tra i vari Stati ed eventualmente tra le diverse stazioni.

La problematica riscontrata consiste nel fatto che, per una certa parte degli Stati, è disponibile il dataset di una sola stazione di monitoraggio.
Per garantire un'analisi più iteressante, è stato deciso di selezionare quattro Stati con una sola stazione di monitoraggio e un ulteriore Stato (il Texas), caratterizzato dal maggior numero  in assoluto di stazioni disponibili (otto). Questa scelta consente di effettuare uno studio comparativo tra le diverse stazioni di uno stesso Stato.


Il file è stato condiviso privo di tutti i csv necessari, poiche pensato per essere condiviso solo con il dataset originario e progressivamnete ricavare gli altri file csv 
solo quando necessario, questo onde evitare un appesantimento, evitabile, del file.


## DESCRIZZIONE CONTENUTO FILE E ORDINE APERTURA##

1) La prima cosa da fare e aprire la directory Stati; digitando **ls** è possibile notare come essa contenga il file **pollution_us_13_15.csv** che raccogli il dataset completo e dei file .py
2) Succesivamente va mandato in secuzione il file **AndamentiStati.py** che analizza il file .csv e ne scrive altri del tipo **NomedelloStato.csv**
3) Ogni file python 'legge' il file .csv decodificato con lo stesso nome dello stato.
4) Una volta che i file:
   - **Alaska.py**
   - **Oregon.py**
   - **Minnesota.py**
   - **Alabama.py**
   - **Texas.py**
   - **TexCO.py**
   - **TexSO2.py**
   - **TexNO2.py**
   - **TexO3.py**
  
sono stati mandati in esecuzione ed eseguiti correttamnete è possibile usare il file **RiassuntoStati.py**
che raccogli tutti i risultati precedenti.

5) La Cartella Stati contiene anche il file **Texas.py** in fase di esecuzione  legge il csv originario e crea a sua volta altri csv per i campionamneti in basse al inquinante.
   Il focus su questo Stato è stato fatto protrio per cogliere le eventuali differenze al interno di una stessa area geografica e per
   lo stesso inquinante nelle diverse stazioni.

7) Adesso è possibile eseguire liberamente uno dei file **TexCO.py** **TexNO2.py**  **TexSO2.py** **TexO3.py**. che leggono i csv per i ripettivi inquinanti.
8) Per la directory inquinanti non vi è un ordine preferenziale in cui eseguire i file.py 

## Considerazioni ##

Lo studio studio dei dati campionanti è stato fatto con le trasformate di fuorie.
Come da richiesta sono state selezioante solo le freqienza più basse (armoniche di periodo maggiore) per la ricostruzione del segnale.
Tuttavia il codice per  maschere sulle frequenze è stato fatto in modo tale che l'utente pottesse modificarne il 'taglio' delle frequenze liberamnete.
Alla fine di ogni studio sono stampati dei dataframe che riportano i risulatati che posso qundi essere osservati facilmente.



