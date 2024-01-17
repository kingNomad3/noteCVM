
# Les Transactions

## ACID

Les transactions en bases de données doivent respecter les propriétés ACID, ce qui signifie :

- **Atomique :** Une transaction est soit effectuée complètement (commit), soit elle est annulée complètement (rollback).
- **Coherante :** Une transaction doit mettre la base de données dans un état cohérent. Soit tout est fait, soit rien n'est fait lorsqu'on fait commit.
- **Isolée :** Pendant l'exécution d'une transaction, elle doit être isolée des autres transactions.
- **Durable :** Une fois qu'une transaction est validée (commit), ses modifications doivent persister même en cas de panne du système.

Lorsque vous êtes en mode super utilisateur, c'est généralement appelé "root" dans MySQL.

# Moteur de table MEMORY

L'engine MEMORY permet de sauvegarder en mémoire vive les données, ce qui signifie que les données sont perdues si l'ordinateur est éteint. Il est utilisé pour stocker temporairement de l'information.

# MyISAM

Le moteur MyISAM présente les caractéristiques suivantes :

- Il ne respecte pas les propriétés ACID, ce qui signifie qu'il n'y a pas de transactions.
- Il utilise un verrouillage au niveau de la table (table-lock), ce qui signifie qu'une modification ne peut pas être effectuée tant qu'une autre n'est pas terminée.
- Il ne prend pas en charge les clés étrangères (foreign keys).
- Cependant, il est plus léger en termes de ressources et est apprécié pour sa simplicité.

# InnoDB

Le moteur InnoDB, en revanche, respecte les propriétés ACID, ce qui signifie qu'il prend en charge les transactions. Il utilise un verrouillage au niveau de la ligne (row-lock), ce qui permet à plusieurs transactions de travailler simultanément sur des parties différentes de la table sans se bloquer mutuellement. Cependant, il peut y avoir des situations de deadlock où deux transactions se verrouillent mutuellement.

-----------------

La commande `SHOW DATABASES;` permet de voir la liste des bases de données sur le serveur MySQL.

# MySQL - Introduction

## La Gestion des Usagers

Les droits d’un usager sur une base de données peuvent varier dépendamment de l’endroit (machine) où il se connecte.

Par exemple :

```sql
CREATE USER 'usr_facturation'@'localhost' IDENTIFIED BY 'xyz_pwd';
GRANT ALL ON ma_bd_facturation.* TO 'usr_facturation'@'localhost';
```

## Les Engins de Tables de MySQL

Voici une liste des engins de tables les plus populaires :

### InnoDB

- Engin par défaut de MySQL.
- Supporte les transactions (donc les clés étrangères également).
- Row-lock.

### MyISAM

- Table-lock.
- Jusqu’à tout récemment, c’était l’engin par défaut de MySQL.
- Ne supporte pas les transactions, ni les clés étrangères.
- Peut, dans certains cas, être plus rapide si la table est intense au niveau des SELECT.

### MEMORY

- Table dont le contenu est gardé en mémoire uniquement.
- Comme toutes les données sont en mémoire (incluant les index), c’est extrêmement rapide. Il faut cependant faire attention. Si le serveur plante ou se ferme, les données seront perdues.

## Certaines Clauses et Particularités de MySQL

### LIMIT

Afin de limiter les résultats d’une requête, la clause LIMIT est utilisée.

Exemple :

```sql
SELECT id, name FROM users ORDER BY name LIMIT 10, 20;
```

Ceci retourne les résultats à partir de la ligne #11 jusqu’à la ligne #30 (inclusivement).

### AUTO_INCREMENT

Il n’est pas nécessaire de faire des séquences comme avec Oracle (version inférieure à 12c).

Exemple :

```sql
CREATE TABLE users (
  id INT NOT NULL AUTO_INCREMENT,
  ...
  PRIMARY KEY pk_users(id)
) ENGINE = InnoDB;
```

### FULLTEXT SEARCH

La recherche en texte intégral permet de rechercher des mots dans un texte. Vous pouvez créer un index FULLTEXT pour améliorer les performances de recherche.

Exemple :

```sql
CREATE TABLE products (
  id INT NOT NULL AUTO_INCREMENT,
  description TEXT,
  PRIMARY KEY pk_products (id),
  FULLTEXT idx_prod_desc (description)
) ENGINE = InnoDB;

SELECT * FROM products WHERE MATCH(description) AGAINST("table rouge");
```

### Syntaxe

- Création d’une base de données :

```sql
CREATE {DATABASE | SCHEMA } xyz_db CHARACTER SET = utf8;
```

- Création d’un usager :

```sql
CREATE USER 'foo'@'192.168.0.1' IDENTIFIED BY 'pwd';
```

- Assignation de droits d’un usager à une base de données :

```sql
GRANT SELECT, INSERT ON xyz_db.* TO 'foo'@'192.168.0.1';
```

Suppression de droits d’un usager sur une base de données :

```sql
REVOKE INSERT ON xyz_db.* TO 'foo'@'192.168.0.1';
```

# prof
```sql
show databases;

CREATE DATABASE cvm_db CHARACTER SET utf8 COLLATE utf8_general_ci;

CREATE USER cvm_user@'localhost' identified by 'AAAaaa111';
CREATE USER cvm_user@'%' identified by 'AAAaaa111';

GRANT ALL ON cvm_db.* TO cvm_user@'localhost';
GRANT SELECT ON cvm_db.users TO cvm_user@'%';

mysqldump.exe --no-tablespaces -uroot -p cvm_db > backup.sql

-- LIMIT (offset, count)
SELECT email FROM users WHERE id > 0 LIMIT 80,5;

use cvm_db;

CREATE TABLE users (
  id INT NOT NULL AUTO_INCREMENT,
  status ENUM("pending", "inactive", "active") DEFAULT "pending",
  email VARCHAR(100) NOT NULL,
  PRIMARY KEY pk_users(id),
  UNIQUE INDEX uk_users_email(email)
) engine=innoDB ;

CREATE unique INDEX sadf on users(email);
```