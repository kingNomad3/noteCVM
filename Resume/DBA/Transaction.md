# Les transactions
## ACID 
- atomique:  soit elle est faite "commit" soit elle n`est oas fait "roll back"
- Cehorant: sois tout est fait sois rien est fait lorsqu`on fait commit
- Isoler: pendant ta transaction
- durable : si le systeme s'eteint la transaction est enore la 


Lorsqu'on est en super utilisateur c'est root dans MySql

# Engin de table memory

engine= memory : sauvegarde memory lorsque l'ordinateur se ferme,  c'est en memoire vive 

- permet de garder de l'information temporairement 

# MyIsom

- No ACID
- est l'encettre des innoDb, il n'ya pas de transactions
- table lock: ne peut pas faire une modification lorsqu'une autre n'est pas terminer, verouille la table au cmomplet
- pas de foreing key

- Par contre plus leger a rouler 
- la simplicité est son point fort 

# innoDB

- ACID 
- row lock: lock l'index 
- dead lock : 2 row lock attend une information que l'autre lock a verouiller



-----------------
show databases; - montre la base de données sur le serveur
