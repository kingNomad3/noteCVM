# DQL III: Produit Cartésien et Jointures
## Introduction:
- Le concept de jointure permet de mettre en relation des informations présentes dans différentes tables. Au cœur de l’algèbre relationnel, la jointure est centrale dans SQL.

## Produit Cartésien:
- C'est un opérateur binaire qui crée toutes les combinaisons possibles des tuples provenant de deux tables.
Chaque combinaison ne fait pas nécessairement de sens, mais elle permet la mise en relation des données.

Exemple:

```sql
SELECT *
FROM employe, departement;
```

## INNER JOIN (Jointure Interne):
- Elle combine le produit cartésien et un ou plusieurs critères de sélection.
- Elle nécessite un critère de liaison, souvent une clé étrangère avec une clé primaire.
Exemple:
```sql
SELECT employe.nom, departement.nom
FROM employe 
INNER JOIN departement 
ON employe.departement_id = departement.id;
```

## LEFT OUTER JOIN (Jointure Externe Gauche):
-Cela permet d'obtenir une liste des tuples même s'ils n'ont pas de correspondance dans la table de droite.
- Les données non correspondantes de droite seront NULL.

Exemple:

```sql

SELECT employe.nom, departement.nom
FROM employe 
LEFT OUTER JOIN departement 
ON employe.departement_id = departement.id;
```

## RIGHT OUTER JOIN (Jointure Externe Droite):
- Similaire à LEFT JOIN, mais récupère les tuples sans correspondance dans la table de gauche.

Exemple:

```sql
SELECT employe.nom, departement.nom
FROM employe 
RIGHT OUTER JOIN departement 
ON employe.departement_id = departement.id;
```

## FULL OUTER JOIN (Jointure Externe Complète):
- Combine LEFT et RIGHT JOIN.
- Toutes les données sans correspondance des deux tables sont conservées.

Exemple:

```sql
SELECT employe.nom, departement.nom
FROM employe 
FULL OUTER JOIN departement 
ON employe.departement_id = departement.id;
```

## Jointures Externes Exclusives:
- Ce type de jointure retourne uniquement les données qui n'ont pas de correspondance.
Exemple (Gauche Exclusive):

```sql
SELECT employe.nom
FROM employe 
LEFT JOIN departement 
ON employe.departement_id = departement.id
WHERE departement.id IS NULL;
```
## Jointures avec la même table:
- Il est possible de joindre une table avec elle-même pour comparer deux ensembles de données de cette table.

Exemple:
```sql
SELECT a1.nom AS "Personne", a2.nom AS "Ami"
FROM amis AS a1
JOIN amis AS a2
ON a1.ami_id = a2.id;
```