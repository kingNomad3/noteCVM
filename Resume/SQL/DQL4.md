# Partie 10: DQL IV - Requêtes corrélées et autres opérateurs ensemblistes
## DQL IV requête non corrélée:
- Les requêtes imbriquées non corrélées n'ont pas de lien direct entre la requête interne et externe.
- Elles sont souvent utilisées pour obtenir de l'information qui sera ensuite injectée dans la requête externe.
Exemple:

Identifier le département des ventes:

```sql
SELECT * FROM employe 
WHERE departement = (SELECT id FROM departement WHERE nom = 'Ventes');
```
- Si la requête interne retourne l'identifiant 5 pour le département des ventes:

```sql
SELECT * FROM employe WHERE departement = 5;
```
## DQL IV requête corrélée:
- Une requête corrélée est une requête imbriquée qui se sert de l'information de la requête externe.
- Elle est exécutée pour chaque ligne de la requête externe.

Exemples:
a. Trouver les employés supervisés par le chef de leur département:

```sql
SELECT nom, prenom
FROM employe
WHERE superviseur = 
(SELECT departement.superviseur FROM departement WHERE departement.id = employe.departement);
```
b. Employés avec le salaire le plus bas dans leur département:

``` sql
SELECT nom, prenom
FROM employe AS emp
WHERE salaire = 
(SELECT MIN(es.salaire) FROM employe AS es WHERE es.departement = emp.departement);
```
c. Employés ayant au moins le salaire moyen de leur département et étant minoritaires par genre:

```sql
SELECT nom, prenom
FROM employe AS emp
WHERE salaire >= 
(SELECT AVG(es.salaire) FROM employe AS es WHERE es.departement = emp.departement)
AND genre = 
(SELECT eg.genre FROM employe AS eg WHERE eg.departement = emp.departement GROUP BY eg.genre ORDER BY COUNT(*) ASC LIMIT 1);
```
## DQL IV opérateurs ensemblistes:
- IN vérifie si une valeur appartient à une liste.
- ANY vérifie si une condition est vraie pour au moins une valeur d'une liste.
- ALL vérifie si une condition est vraie pour toutes les valeurs d'une liste.
- EXISTS vérifie s'il existe au moins une valeur correspondante.

Equivalences logiques:
```sql
a IN (x1, x2, x3) équivaut à a = x1 OR a = x2 OR a = x3.
a > ANY(x1, x2, x3) équivaut à a > x1 OR a > x2 OR a > x3.
a > ALL(x1, x2, x3) équivaut à a > x1 AND a > x2 AND a > x3.
EXISTS({ensemble}) équivaut à COUNT(*{ensemble}) > 0.
Exemples:
a. Employés ayant un salaire supérieur à au moins un employé dont le nom commence par B:
```
```sql
SELECT nom, prenom
FROM employe
WHERE salaire > ANY( 
SELECT salaire FROM employe WHERE nom LIKE 'B%');
```
b. Employés ayant un salaire supérieur ou égal à tous les employés du département des ventes:

```sql
SELECT nom, prenom
FROM employe
WHERE salaire >= ALL( 
SELECT salaire FROM employe WHERE departement = (SELECT id FROM departement WHERE nom = 'Ventes'));
```
c. Départements ayant au moins un employé embauché après juin 2002:

```sql
SELECT nom
FROM departement AS dep
WHERE EXISTS( 
SELECT nas FROM employe AS emp WHERE date_embauche > '2002-06-01' AND emp.departement
```