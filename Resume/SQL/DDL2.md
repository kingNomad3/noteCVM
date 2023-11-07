# 420-C42 Langages d'exploitation des bases de données
## Partie 11: DDL II - Création, modification et suppression

### 1. Objets supplémentaires:
- Les SGBD (Systèmes de Gestion de Bases de Données) autorisent la création de multiples types d'objets.

- Jusqu'ici, nous avons vu: tables, colonnes, contraintes, et types énumérés.
- Mais il existe d'autres types:
    Bases de données
    Schémas
    Types de données
    Opérateurs
    Séquences
    Vues
    Index
    Requêtes préparées
    Procédures et fonctions SQL/PLpgSQL
    Déclencheurs
    Usagers
    Groupes
    etc.
### 2. Structure hiérarchique:
- Dans des SGBD comme PostgreSQL, tous les objets sont disposés hiérarchiquement:
    database
    schema
    tous les autres objets

### 3. Objet base de données (DATABASE):
    Dans PostgreSQL, un objet "database" est un conteneur logique pour le regroupement de schémas.
    Seule une base de données peut être active par connexion.
    La base "postgres" est la base par défaut.
    Commandes pour manipuler ces objets:



```sql
CREATE DATABASE …
DROP DATABASE ...
ALTER DATABASE …
CREATE DATABASE bibliotheque;
DROP DATABASE bibliotheque;
```
- Cette commande crée une nouvelle base de données nommée "bibliotheque". Une base de données est un conteneur principal qui peut contenir des schémas, des tables et d'autres objets relatifs aux données.
- La commande DROP DATABASE supprime la base de données spécifiée, ici "bibliotheque". Attention, c'est une action irréversible.

### 4. Objet schéma (SCHEMA):
    Un schéma est un conteneur logique sous un objet "database".
    Il sert à regrouper et organiser différents objets.
    Les schémas appartiennent à un utilisateur.
    Commandes pour manipuler ces objets:
```sql
CREATE SCHEMA ...
DROP SCHEMA ...
ALTER SCHEMA ...
CREATE SCHEMA livres;
```
- Un schéma est un moyen d'organiser des objets (comme des tables) dans des conteneurs logiques au sein d'une base de données. Ici, nous créons un schéma appelé "livres" qui pourrait contenir des tables comme "auteurs", "titres", etc.

### 5. Objet séquence (SEQUENCE):
    Une séquence est un générateur de nombres.
    Elle peut être paramétrée selon différents critères.
    Les types de données SMALLSERIAL, SERIAL et BIGSERIAL utilisent une séquence pour la génération des identifiants.
    Commandes et fonctions pour manipuler ces objets:
```sql
CREATE SEQUENCE ...
DROP SEQUENCE ...
ALTER SEQUENCE ...
```
```sql
currval('sequence_name')
SELECT currval('livres_id_seq');
```
- La fonction currval retourne la dernière valeur de la séquence qui a été générée pour cette session. Si aucune valeur n'a été générée pour la session en cours, cette fonction émet une erreur.

- Cela est utile, par exemple, après avoir inséré une nouvelle ligne dans une table avec un identifiant généré automatiquement par une séquence. Vous pouvez utiliser currval pour récupérer cet identifiant pour des opérations ultérieures.

```sql
lastval()
SELECT lastval();
```
- La fonction lastval retourne la dernière valeur générée par n'importe quelle séquence dans la session en cours. Contrairement à currval, vous n'avez pas besoin de spécifier le nom de la séquence, mais cela suppose que vous avez récemment généré une valeur depuis une séquence.

- C'est utile dans des situations où vous utilisez des séquences mais que vous n'êtes pas sûr de laquelle a été utilisée en dernier.

```sql
nextval('sequence_name')
SELECT nextval('livres_id_seq');
```
- La fonction nextval incrémente la séquence et retourne la nouvelle valeur. C'est probablement la fonction la plus utilisée avec les séquences, car elle fournit un moyen d'obtenir un nouvel identifiant unique pour les inserts.

```sql
setval('sequence_name', value)
```
SELECT setval('livres_id_seq', 100);
```sql
CREATE SEQUENCE livres_id_seq;
```
- Une séquence est un générateur de nombres automatiquement incrémentés. Dans cet exemple, nous créons une séquence pour générer des identifiants uniques pour les livres. Chaque fois qu'un nouveau livre est ajouté à la base de données, cette séquence fournira un nouvel ID.

### 6. Objet vue (VIEW):
    Une vue est une "table virtuelle" représentant le résultat d'une requête.
    Elle ne stocke pas les données, mais les représente comme une table.
    Commandes pour manipuler ces objets:
```sql
CREATE [OR REPLACE] VIEW view_name AS query;
DROP VIEW view_name;
ALTER VIEW view_name ...
CREATE VIEW vue_livres AS 
SELECT titre, auteur FROM livres.livre;
```
Une vue est une table virtuelle basée sur le résultat d'une requête. Dans cet exemple, nous créons une vue qui affiche uniquement le "titre" et l'"auteur" des livres à partir de la table "livre". C'est utile pour simplifier des requêtes complexes ou pour restreindre l'accès à certaines colonnes.
### 7. Objet index (INDEX):
    Un index améliore la performance d'accès aux données.
    Un index est créé automatiquement lors de la définition d'une contrainte d'unicité ou de clé primaire.
    Commandes pour manipuler ces objets:

```sql
CREATE INDEX ...
DROP INDEX ...
ALTER INDEX ...
CREATE INDEX idx_auteur ON livres.livre(auteur);
```
Un index est une structure de données qui améliore la rapidité des opérations sur une table. Ici, nous créons un index sur la colonne "auteur" de la table "livre". Cela accélérerait considérablement les requêtes qui filtrent ou trient par auteur.

### Conclusion:
    Ce module détaille les différentes commandes DDL (Data Definition Language) pour créer, modifier et supprimer différents types d'objets dans les bases de données, y compris les bases de données elles-mêmes, les schémas, les séquences, les vues et les index. Ces outils sont essentiels pour les administrateurs de bases de données et les développeurs qui souhaitent optimiser leurs systèmes de bases de données pour une performance maximale.

