# Gestionale per Ristorante con Python
Un semplice gestionale per ristoranti scritto in Python che consente di gestire prenotazioni e include una funzionalità di blacklist per clienti indesiderati. 
Questo progetto è ideale per piccoli ristoranti che desiderano un sistema base per organizzare le prenotazioni e monitorare i clienti problematici.

## Funzionalità principali
Blacklist: Aggiungi i clienti indesiderati a una blacklist per evitare che possano effettuare nuove prenotazioni.
Prenotazioni: Gestione delle prenotazioni coperti disponibili al giorno.
Controllo dei coperti: Verifica in tempo reale quanti coperti sono ancora disponibili per una data specifica.
Interfaccia a riga di comando: Semplice interfaccia testuale per facilitare l'uso da parte del personale del ristorante.

## Requisiti
Python 3.x
Libreria sqlite3 per il database delle prenotazioni e blacklist

## Installazione

1 - Clona il repository sul tuo computer:
git clone https://github.com/Bebbo123/Gestionale_Ristorante.git

2 - Entra nella cartella del progetto:

cd Gestionale_Ristorante

3 - Installa le dipendenze richieste (anche se sqlite3 e datetime fanno già parte della libreria standard Python):

pip install sqlite3 datetime

4- Esegui il programma:

python main.py

## Uso
Dopo aver avviato il gestionale, potrai:

- Aggiungere un cliente alla blacklist
- Verificare i coperti disponibili in una data specifica
- Aggiungere prenotazioni
- Visualizzare e gestire le prenotazioni esistenti

## Possibili miglioramenti
Aggiungere un'interfaccia grafica (GUI) per facilitare l'utilizzo da parte del personale.
Implementare un sistema di notifiche via email per confermare o ricordare le prenotazioni.
Integrare la gestione di tavoli multipli e turni del ristorante.
Creare una reportistica settimanale per monitorare le prenotazioni.

