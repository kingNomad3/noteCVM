# DQL II: Fonctions d’agrégation et regroupement
1. Introduction:

SQL propose plusieurs fonctions d’agrégation pour synthétiser un ensemble de données.
2. Fonctions d’agrégation de base:
- Ces fonctions permettent de résumer les données. Par exemple:
* COUNT(*): Compte toutes les lignes, y compris les nulls.
* SUM(colonne): Somme toutes les valeurs d'une colonne.
* AVG(colonne): Moyenne des valeurs non nulles d'une colonne.
* MIN(colonne) & MAX(colonne): Retourne respectivement les valeurs minimum et maximum.

*Exemple:*  
```sql
SELECT COUNT(*), MIN(salaire), MAX(salaire), AVG(salaire)
FROM employe WHERE departement = 'Ventes';
```
3. GROUP BY:
- Permet de regrouper les résultats par une ou plusieurs colonnes.
*Exemple:*  
```sql
SELECT departement, COUNT(*) AS "Nombre d'Employés"
FROM employe WHERE departement IS NOT NULL
GROUP BY departement;
```
4. Exemples de regroupement incorrect:
- Lors de l'utilisation de GROUP BY, il est essentiel de ne pas combiner des fonctions d'agrégation avec des données d'enregistrement individuelles sans regrouper ces colonnes de données.

5. HAVING:
- Utilisé pour filtrer les groupes après leur création.
- Fonctionne de manière similaire à la clause WHERE mais pour les groupes.

*Exemple:*  
```sql
SELECT departement, COUNT(*) AS "Nombre d'Employés"
FROM employe
GROUP BY departement
HAVING COUNT(*) > 5;
```
6. Ordre d'évaluation des clauses:
- C'est l'ordre dans lequel SQL évalue les différentes clauses : FROM, WHERE, GROUP BY, HAVING, SELECT, DISTINCT, ORDER BY, et LIMIT/OFFSET.

7. Défis avec WHERE et HAVING:
- L'utilisation des clauses WHERE et HAVING peut parfois prêter à confusion. Il faut se rappeler:
* WHERE filtre les enregistrements individuels.
* HAVING filtre les groupes.

*Scénario & Solution:*  
Supposons que vous voulez le nombre d'employés dans des départements avec des salaires >= 30 et vous n'êtes intéressé que par les départements avec > 5 employés. La solution serait:
```sql
SELECT departement, COUNT(*) 
FROM employe 
WHERE salaire >= 30 
AND departement IN (SELECT departement FROM employe GROUP BY departement HAVING COUNT(*) > 5) 
GROUP BY departement;
```