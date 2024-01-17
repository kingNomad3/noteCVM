
# Commandes Utilisées

## DESC (Description de la table)

- Pour afficher la description d'une table, utilisez : 
  ```sql
  DESC nom_de_la_table;
  ```
  Cela affiche la structure de la table spécifiée.

## SELECT avec LIMIT

- Pour sélectionner uniquement la première ligne d'une table, utilisez : 
  ```sql
  SELECT * FROM nom_de_la_table LIMIT 0, 1;
  ```
  Cela limite les résultats à la première ligne de la table.

## SELECT COUNT(*) avec LIKE

- Pour compter le nombre de lignes où une colonne contient un certain motif (par exemple, '%xbox%'), utilisez : 
  ```sql
  SELECT COUNT(*) FROM nom_de_la_table WHERE colonne LIKE '%xbox%';
  ```
  Veillez à éviter le '%' au début, car il entraînerait une recherche de tous les résultats de la table, contournant l'index.

## USE INDEX (Forcer l'utilisation d'un index spécifique)

- Pour forcer MySQL à utiliser un index spécifique dans une requête, utilisez : 
  ```sql
  USE INDEX (nom_de_l_index);
  ```
  Cela indique à MySQL d'utiliser l'index spécifié pour la requête.

## EXPLAIN SELECT

- Pour obtenir des informations sur la façon dont MySQL exécute une requête SELECT, utilisez : 
  ```sql
  EXPLAIN SELECT colonnes FROM nom_de_la_table WHERE conditions;
  ```
  Cela vous fournira des détails sur l'exécution de la requête.

## CREATE DATABASE cvm_db CHARACTER SET utf8 COLLATE utf8_general_ci; 

- Pour créer une base de données avec un jeu de caractères et une collation spécifiques, utilisez : 
  ```sql
  CREATE DATABASE cvm_db CHARACTER SET utf8 COLLATE utf8_general_ci;
  ```
  - `collate`: touche au `ORDER BY` et `GROUP BY`
  - `_ci` permet de rendre toutes les recherches insensibles à la casse, ce qui signifie aussi `ei`
  - `general`: pour des mots comme "coeur", généralement "coeur" avec le "e" collé au "o"
  - charset utf8: L'option CHARACTER SET utf8 définit le jeu de caractères à UTF-8, qui est un encodage de caractères prenant en charge un large éventail de caractères, y compris les caractères internationaux.

## show databases;

- Pour afficher les bases de données disponibles sur le serveur, utilisez : 
  ```sql
  show databases;
  ```

## CREATE USER cvm_user@'localhost' identified by 'AAAaaa111';

- Pour créer un utilisateur MySQL avec un mot de passe, utilisez : 
  ```sql
  CREATE USER cvm_user@'localhost' IDENTIFIED BY 'AAAaaa111';
  ```
  - `@localhost`: pour définir de quel emplacement se connecter
  - Vous pouvez spécifier des droits spécifiques en modifiant l'adresse IP ou en utilisant '%' pour n'importe quelle adresse IP.

## GRANT ALL ON cvm_db.* TO cvm_user@'localhost';

- Pour accorder tous les droits à un utilisateur sur toutes les tables d'une base de données, utilisez : 
  ```sql
  GRANT ALL ON cvm_db.* TO cvm_user@'localhost';
  ```

## GRANT SELECT ON cvm_db.users TO cvm_user@'%'

- Pour accorder uniquement le droit SELECT à un utilisateur sur une table spécifique, utilisez : 
  ```sql
  GRANT SELECT ON cvm_db.users TO cvm_user@'%';
  ```

## use cvm_db;

- Pour sélectionner une base de données spécifique à utiliser dans vos requêtes, utilisez : 
  ```sql
  USE cvm_db;
  ```
  À partir de ce point, toutes les opérations seront effectuées dans cette base de données.

## CREATE TABLE users (
	id INT NOT NULL AUTO_INCREMENT, -- Auto_increment est l'équivalent de SERIAL
    status ENUM("pending", "inactive", "active") DEFAULT "pending",
    email VARCHAR(255) NOT NULL,
    PRIMARY KEY (id),
    UNIQUE INDEX uk_users_email(email)
) ENGINE=InnoDB;

- Pour créer une table avec des colonnes, utilisez : 
  ```sql
  CREATE TABLE users (
    id INT NOT NULL AUTO_INCREMENT, -- Auto_increment est l'équivalent de SERIAL
    status ENUM("pending", "inactive", "active") DEFAULT "pending",
    email VARCHAR(255) NOT NULL,
    PRIMARY KEY (id),
    UNIQUE INDEX uk_users_email(email)
  ) ENGINE=InnoDB;
  ```
  - `ENGINE=InnoDB`: spécifie le moteur de table InnoDB.

## mysqldump.exe (pour créer une copie de sauvegarde)

- Pour créer une copie de sauvegarde de la base de données, utilisez la commande `mysqldump.exe`. Par exemple : 
  ```shell
  C:\Program Files\MySQL\MySQL Server 8.0in\mysqldump.exe
  --no-tablespaces -uroot -p cvm_db > backup.sql
  ```
  Cette commande crée un fichier de sauvegarde appelé `backup.sql` de la base de données `cvm_db`.

## SELECT avec LIMIT (Offset et Count)

- Pour sélectionner des lignes avec un décalage (offset) et un nombre spécifiés (count), utilisez la clause `LIMIT`. Par exemple :
  ```sql
  SELECT email FROM users WHERE id > 0 LIMIT 0, 1;
  ```
  - `LIMIT 0, 1` signifie que vous commencez à la première ligne et prenez une ligne.

## Création de tables avec AUTO_INCREMENT

- Lorsque vous créez une table avec une colonne `id` utilisant `INT NOT NULL AUTO_INCREMENT`, cela signifie que la colonne `id` sera auto-incrémentée, agissant comme une séquence.
  ```sql
  CREATE TABLE users (
    id INT NOT NULL AUTO_INCREMENT,
    -- Autres colonnes ici
    PRIMARY KEY (id)
  ) ENGINE=InnoDB;
  ```
  Cela permet à chaque nouvelle ligne d'obtenir un ID unique généré automatiquement.

```
