# commande utilisé



- desc (nom table) - desc produit; - description de la table produit 

- Select * from produits limit 0,1;  - limit a la premiere ligne 

- SELECT COUNT(*) FROM produits2 WHERE description LIKE '%xbox%'; 
    - peut commencer par n;import quoi et terminier par n'importe quoi, Le % au debut est mauvais car il va chercher tout les resultats de la table -- defeat the index

- USE INDEX (nom_index) - forcer mysql a utiliser un index specifique

- explain select 


- CREATE DATABASE cvm_db CHARACTER SET utf8 COLLATE utf8_general_ci; 

    - collate: touche au orderby groupe by
    - _ci permet de mettre tout mes recherches sont case insesitive, veut dire aussi ei
    - general: pour les mots comme coeur genereleent coeur le e est coller au o 

- show databases; - montre la base de données sur le serveur

- CREATE USER cvm_user@'localhost' identified by 'AAAaaa111';
        - @localhost :  de ou on se connect, 
        - alors si CREATE USER cvm_user@'10.57.57.14' identified by 'AAAaaa111'; on peut lui donner des droits spécifique
        - CREATE USER cvm_user@'%' identified by 'AAAaaa111'; de n'importe quel addresse ip, se connectant d'ailleurs
        - CREATE USER cvm_user identified by 'AAAaaa111'; all

- GRANT ALL ON cvm_db.* TO cvm_user@'localhost';
    - donne tout les droits a cette usager pour tout les tables

- GRANT SELECT ON cvm_db.users TO CVM_user@'%'
    - donne juste select comme droit a cette table 

- use cvm_db;
    - a partir de maintenant tout ce que je fais est dans cette base de donnnées la 

    CREATE TABLE users (
	id INT NOT NULL AUTO_INCREMENT - increment est serial 
    
C:\Program Files\MySQL\MySQL Server 8.0\bin\mysqldumb.exe


.\mysqldump.exe --no-tablespaces -uroot -p cvm_db > backup.sql
);


```MySQL
SELECT email FROM users WHERE id > 0 limit 0,1; # limit(offset,count) tu te tasses de combien et tu en prend combien 
# si limit 10,10, on va a la 1element et on donne les 11 prochain

use cvm_db;

CREATE TABLE users (
	id INT NOT NULL AUTO_INCREMENT, # auto_increment is serial
    status ENUM("pending","inactive","active") DEFAULT "pending",
    email VARCHAR(255) NOT NULL,
    PRIMARY KEY pk_users(id),
    UNIQUE INDEX uk_users_email(email)
) engine=InnoDB; #plus tot on a mis not case senstive ici on pourrait le remettre case sensitive



show databases;

CREATE DATABASE cvm_db CHARACTER SET utf8 COLLATE utf8_general_ci;

CREATE USER cvm_user@'localhost' identified by 'AAAaaa111';

GRANT ALL ON cvm_db.* TO cvm_user@'localhost';
GRANT SELECT ON cvm_db.users TO CVM_user@'%';


```