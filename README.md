#Turtlebot Lamp Control
Turtlebot Lamp Control è il progetto che è stato sviluppato per l'esame Robot Programming e consiste nella simulazione di un robot che accende tre lampadine. 
Il progetto è stato sviluppato in ROS e ha comportato la creazione e l'utilizzo di nodi, topic, messaggi, services, parameters e una piccola simulazione in Gazebo.

Nel progetto sono stati implementati 7 nodi:
  -move turtlebot3: è il nodo che si occupa del movimento di turtlebot3.
  -contact sensor: è il nodo che si occupa del contatto con la lampadina. Questo nodo invia via topic un messaggio al nodo turtlebot control node.
  -turtlebot control node: è il nodo responsabile dell'impostazione di un parameter relativo alla lampadina toccata che verrà poi preso dal nodo check command.
  -check command: nodo che costruisce il messaggio personalizzato che verrà inviato al nodo message received.
  -message received: nodo che mostra il messaggio finale.
  -check server: è il nodo server che riceve le richieste relative allo stato della lampadina. 
  -check client: è il nodo che invia la richiesta.

Sono stati creati vari topics, un esempio è "/contact status", all'interno del quale è possibile pubblicare la stringa relativa alla lampadina rilevata.

Il messaggio personalizzato che è stato creato consiste in una stringa relativa all'accensione di una lampadina e in un booleano che rappresenta il contatto con la lampadina.

Il service prevede una stringa di comando e una stringa di risposta.
Check_client prende la stringa di comando, per esempio lampadina, lampadina_2 o lampadina_3. Check server è sempre attivo, riceve la stringa di comando e restituisce una risposta relativa allo stato delle lampadine.

I parameters sono stati utilizzati nel nodo turtlebot control node, dov'è stato impostato un parameter lampadina a cui è stato associato un valore intero 1, 2 o 3 in base alla lampadina toccata.

La simulazione in Gazebo consiste nel turtlebot che, tramite comandi da tastiera, può raggiungere le tre lampadina e attivarle ad una certa distanza, come se ci fosse un pulsante. L'accensione è stata 
realizzata spostando la lampadina in questione lungo l'asse X.
