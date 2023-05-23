# team4
Esercitazione python data intelligence experis academy

I componenti del gruppo sono 

- Bassi Stefano (Ueloiol)

- Alessandra Rispoli (Alerisp94)

- Nicola Pacella (Pach90)

- Bruno Vincenzo (Vinx9898) (leader in senso lato)

# Progetto

Il progetto prevede la costruzione di un social network dove e' possinile registrarsi, creare un post, commentare un post e aggiungere followers
Al progetto seguira' un upgrade successivo in cui sara' possibile definire i livelli di amicizia e visualizzare i post in base ai livelli di amicizia

# Struttura del codice:
Users e la calsse DataBase permettono di inserire utenti di default nella lista_utenti_oggetto tramite un ciclo for.

## lista_utenti_oggetto - 
Contiene la lista degli utenti, dove per ogni utente vengono consrvate tutte le informazioni primarie, amici e post

## la classe Utente - 
Contiene le funzioni principali accedi/registra/crea e cancella post/follow ed unfollow amici. Elementi una volta creati vengono aggiunti
alla lista_utenti_oggetto

## classe Post

## main - 
Il mai comincia con l scelta fra 3 opzioni (1 log in , 2 registrazione, 3 uscita). L'entry-point e l' exit-point avviene escusivamente da qui

- 1-log in - 

- 2 registrazione - questa opzione permette di creare un oggetto utente dove vengono registrate le prime informzioni. La lista amici e i post sono per ora liste vuote

- 3 uscita- ti permette di uscire dal programma

classe utente - crea l'utente con nome, username, password, contiene i metodi creazione

# Road map

Alla versione 1.0 del programma Astraction seguirà un upgrade che prevede la possibilità di gestire e stabilire la gerarchia delle amicizie( amici stretti, grado di parentela). In questa versione sarà possibile gestire la visione dei post nell'home-page in base alla gerarchia delle amicizie.

La data di release Astraction 2.0 è prevista per il 24/05/2023

In segutio verranno aggiunte le seguenti funzionalità che faranno riferimento ad una versione 2.1:

- reaction ai post
- ricondivisione dei post
- Indicatore di popolarità. Rendere visibile i like ricevuti, i folowers ed il numero dei post pubblicati
- Impostare un profilo business dove si potrà aggiungere un url per accedere ad eventuali shop digitali

La release della verisone 2.1 è prevista per fine settimana (25/05/2023)

In segutio verranno aggiunte le seguenti funzionalità che faranno riferimento ad una versione 2.2:

- bloccao di utenti che possono visualizzare il tuo profilo
- Inserimento di immagini nei post
- Possibilità di segnalare post offensivi
- Impostare un profilo pubblico/privato
- Inserire la possibilità di verificare il profilo (bollino blue)

La release della versione 2.2 è prevista per il 31/05/2023

# Commenti:

I commenti sono inseriti per ogni blocco di codice ad inizio blocco

I commenti descrivono in modo sintetico le mansioni svolte dai singoli blocchi

# Diagrammi di flusso

Il codice prevede un diagramma di flusso che descrive il funzionamento del codice


# Strutturazione del lavoro

1- ANALIZZARE PROBLEMA: Cercare di capire in quanti blocchi è suddivisibile il problema. (to do list)

2- NOMENCLATURA: Definire i nomi di variabili, classi, funzioni ecc. cosi da rendere confrontabile il problema.

3- COMPITI: Suddivisione dei compiti a seconda delle autopercepite capacità, gestendo in modo consono i vari blocchi.

4- RICOSTRUZIONE: Ricostruzione del codice.

5- DEBUGGING.

