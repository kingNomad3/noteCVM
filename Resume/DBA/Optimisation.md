# Optimisation de tables avec les index

- optimisation par index

- Les slaves ont les memes informations que le master et seulement le master peuvent etre modifier. Lorsque le master (serveur) est udpdate alors les slaves updates. 

![](Optimisation.m\9075242a-2d3f-2c7a-c4b5-79f3a3fa6c35.svg)

- si le master craches le systeme va choisir un slave pour etre le nouveau master  ( comm ceci sont des backup du master)

- apres un milliard de slaves le systeme devient long a cause des select, nous avons vu qu un index peut aider mais apres un millaird c'est toujours long

- lorsqu'on va chercher une table au complet l'execution est lourde, alors nous allons faire des table plus petite ceci est du 'fractionnement vertical'

![](Optimisation.m\cb9b350f-669e-356b-3f1c-957b0162370d.svg)

- au lieu d'une grosse table de users, nous pouvons avoir une petit table de user qui commence tous par ad par exemple user_ad, on appelle cela du charding

## b-tree (balanced - tree) - défaut (index)

    - balance tree, lorsqu'on fait un indez c'est b-tree par defaut

    - marche mieux lorsque nous avons enormement de valeur 


- Les index dans les bases de donnes relaton, lorsqu'on update la base de donner TOUT les index doivent etre mis a jours et recalcule. Plus la table est grosse plus sa va couter cher 

# index composer ou multiple 

- utilise des index sur plusieurs collones en meme temps

- insere les donnees de maniere differer pour les gros systemes


## Le « Full text indexing »

SELECT COUNT(*) FROM produits2 WHERE MATCH(description) AGAINST('xbox'); c'est la meme chose que :

SELECT COUNT(*) FROM produits2 WHERE description LIKE '%xbox%';

mais plus performent

----------------------

desc (nom table) - desc produit; - description de la table produit 

Select * from produits limit 0,1;  - limit a la premiere ligne 

SELECT COUNT(*) FROM produits2 WHERE description LIKE '%xbox%'; - peut commencer par n;import quoi et terminier par n'importe quoi, Le % au debut est mauvais car il va chercher tout les resultats de la table -- defeat the index

USE INDEX (nom_index) - forcer mysql a utiliser un index specifique

explain select 

recherche phonetique 



