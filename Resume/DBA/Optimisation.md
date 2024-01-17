# Optimisation de tables avec les index


## Les catégories d’index les plus utilisées

- optimisation par index

- Les slaves ont les memes informations que le master et seulement le master peuvent etre modifier. Lorsque le master (serveur) est udpdate alors les slaves updates. 

![](Optimisation.m\9075242a-2d3f-2c7a-c4b5-79f3a3fa6c35.svg)

- si le master craches le systeme va choisir un slave pour etre le nouveau master  ( comm ceci sont des backup du master)

- apres un milliard de slaves le systeme devient long a cause des select, nous avons vu qu un index peut aider mais apres un millaird c'est toujours long

- lorsqu'on va chercher une table au complet l'execution est lourde, alors nous allons faire des table plus petite ceci est du 'fractionnement vertical'

![](Optimisation.m\cb9b350f-669e-356b-3f1c-957b0162370d.svg)

- au lieu d'une grosse table de users, nous pouvons avoir une petit table de user qui commence tous par ad par exemple user_ad, on appelle cela du charding


- **B-tree (balanced-tree) - Par Défaut**
  - Le type d'index le plus populaire est le B-tree, qui est également l'index par défaut. Il est appelé "arbre équilibré" parce que les feuilles de l'arbre sont toujours au même niveau. Cependant, les blocs d'index peuvent contenir un nombre variable de valeurs et de l'espace inutilisé.

  - Par exemple, si nous exécutons la requête : `SELECT * FROM USERS WHERE AGE = 21`, l'index permettra de localiser la ligne dans la table qui correspond à la requête.

  - Vous pouvez créer un index B-tree avec la commande : `CREATE INDEX idx_city ON USERS (city);`

## Index Unique

- Les index uniques doivent être créés sur des colonnes où chaque valeur ne peut apparaître qu'une seule fois.

- Voici quelques exemples de bonnes candidatures pour des index uniques : adresse e-mail, numéro d'assurance sociale, nom d'utilisateur.

- Vous pouvez créer un index unique avec la commande : `CREATE UNIQUE INDEX idx_username ON USERS(username);`

## Index à Colonne Simple

- Les index à colonne simple doivent être utilisés lorsque l'utilisateur effectue une requête de filtrage sur une seule colonne.

- Par exemple : `SELECT * FROM users WHERE birth_date > TO_DATE('1990', 'YYYY');`

## Index à Colonnes Multiples (Index Composite)

- Les index à colonnes multiples, également appelés index composites, sont extrêmement utiles lorsqu'une requête implique plusieurs colonnes.

- Un exemple valable d'index composite est (province, ville, rue).
  - Exemple de requêtes utilisant cet index :
    - `WHERE province = …`
    - `WHERE province = … AND ville = …`
    - `WHERE province = … AND ville = … AND rue = …`
  
- Exemple où l'index ne sera pas utilisé :
  - `WHERE ville = … AND rue = …`
  - `WHERE ville = …`
  - `WHERE rue = …`

- La requête suivante n'utiliserait pas l'index (province, ville, rue) :
  `SELECT * FROM users WHERE ville = ‘montreal’ AND rue = ‘Sanguinet’`


## Le « Full Text Indexing »

- Utiliser le "Full Text Indexing" permet d'indexer chaque mot dans un texte. Cela peut grandement améliorer les performances, mais peut être plus long à maintenir pour la base de données.

- Pour créer un index "Full Text" en MYSQL :

`CREATE FULLTEXT INDEX idx_produits_desc ON produits2(description);`

- Une requête utilisant le "Full Text Indexing" peut être beaucoup plus performante qu'une requête utilisant LIKE avec des % au début et à la fin du mot recherché.

- Par exemple :

`SELECT COUNT(*) FROM produits2 WHERE MATCH(description) AGAINST('xbox');`

- Ceci est dramatiquement plus performant que cette requête :

`SELECT COUNT(*) FROM produits2 WHERE description LIKE '%xbox%';`

## Autres Commandes Utiles

- Utilisez `DESC (nom_table)` pour obtenir la description de la structure d'une table, par exemple : `DESC produit` donne la description de la table "produit".

- Limitez le nombre de résultats d'une requête avec `SELECT * FROM produits LIMIT 0,1` pour obtenir seulement la première ligne.

- Évitez d'utiliser `%` au début d'une chaîne dans une requête LIKE, car cela peut entraîner une recherche inefficace en recherchant tous les résultats de la table.

- Pour forcer MySQL à utiliser un index spécifique, utilisez `USE INDEX (nom_index)`.

- Utilisez `EXPLAIN SELECT` pour analyser et optimiser les performances de vos requêtes.

- Il existe également des techniques de recherche phonétique pour améliorer la recherche de mots similaires.



