# DQL I
### DQL I SELECT
- La clause SELECT est la seule du DQL, souvent mise dans le groupe DML.
- Elle retourne soit une erreur ou un résultat sous forme d'une table.
- Elle peut être utilisée sans la clause FROM, dans ce cas, elle retourne un seul tuple.
sql
C
```sql
Exemples : 
SELECT 0; 
SELECT 'Bonjour'; 
SELECT '2000-01-01'; 
SELECT 2 * 3, 3 * 2; 
SELECT 'Hello' || ' world'; 
SELECT DATE('2000-01-01') + '1';
```
### DQL I FROM
- La clause FROM spécifie la table où se trouvent les informations.
- Sans FROM, une requête SELECT retourne un seul tuple.
- Avec FROM, le nombre de lignes retournées est égal au nombre de tuples dans la table.

```sql
Exemples :
SELECT * FROM employe;
SELECT nom, prenom, salaire FROM employe;
```

### DQL I alias
- L'alias est un titre alternatif pour une colonne du résultat.
- Il est recommandé d'utiliser le mot réservé AS.
```sql
Exemple : SELECT salaire AS Salaire_Annuel, ROUND(salaire * 1.10, 2) AS "Salaire_Après_Augmentation" FROM employe;
SELECT salaire AS Salaire, ROUND(salaire * 1.10, 2) "Nouveau salaire" FROM employe;
```
### DQL I WHERE
- La clause WHERE filtre les résultats selon une condition spécifiée.
- Elle utilise des opérateurs de comparaison (e.g., =, <>, <, <=) et logiques (e.g., AND, OR).
```sql
SELECT * FROM employe WHERE salaire >= 25;
SELECT * FROM employe WHERE nom = 'Dupuis';
SELECT nom, prenom FROM employe WHERE date_embauche < '2002-01-01';
```
### DQL I SELECT DISTINCT
- La clause DISTINCT élimine les doublons dans les résultats.
```sql
Exemple : SELECT DISTINCT departement FROM employe;
```
### DQL I opérateurs et fonctions
- Les opérateurs et fonctions pour manipuler les données dans les requêtes.
```sql
Exemples :
Opérateurs de comparaison: SELECT nom FROM employe WHERE age >= 30;
Opérateurs mathématiques: SELECT ROUND(salaire/12) AS "Salaire Mensuel" FROM employe;
Fonctions trigonométriques: SELECT SIN(angle) AS resultat_sin FROM angles;
```

### DQL I LIKE

- L’opérateur LIKE (ou ~~) retourne vrai si la chaîne de caractères correspond au patron donné. 
- L'opérateur LIKE permet de filtrer les résultats selon un motif spécifié.
```sql
Exemple : SELECT nom FROM livres WHERE titre LIKE 'Harry%';
 SELECT 'Gaston' LIKE 'Gaston'; 
```

### DQL I expressions régulières

- Les expressions régulières permettent de rechercher, filtrer ou remplacer des chaînes selon des motifs complexes.
```sql
Exemple 1: 
SELECT nom FROM employe WHERE prenom ~ '^J.*';
-- Trouve les prénoms qui commencent par la lettre 'J'.

Exemple 2:
SELECT email FROM utilisateurs WHERE email ~ '^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$';
-- Valide la structure des adresses e-mail.

Exemple 3:
SELECT commentaire FROM feedback WHERE commentaire !~ '.*[0-9].*';
-- Sélectionne les commentaires sans chiffres.

Exemple 4:
SELECT nom FROM employe WHERE prenom ~* '^j.*';
-- Trouve les prénoms qui commencent par la lettre 'j', insensible à la casse grâce à `~*`.

Exemple 5:
SELECT rue FROM adresses WHERE rue ~ '^[0-9]+ .*';
-- Trouve les noms de rues qui commencent par un numéro de maison.
```

DQL I opérateurs et fonctions liés aux dates et aux heures

- current_date (retourne la date courante)
- date_part (extrait une partie d'une date)

- Opérateurs et fonctions pour travailler avec des dates et des heures.
```sql
Exemple : SELECT nom, current_date FROM employe;
```




DQL I valeurs nulles

La manipulation de la valeur nulle est délicate en SQL.
Exemple : SELECT nom, date_fin_contrat FROM employe WHERE date_fin_contrat IS NULL;


### DQL I ORDER BY

- L'ordre dans lequel les lignes sont retournées peut dépendre de nombreux facteurs.
- L’ordre de sortie d’une requête est arbitraire sans ORDER BY.
```sql
Exemple : SELECT nom, prenom FROM employe ORDER BY nom DESC;
 SELECT nom, prenom, departement FROM employe ORDER BY nom;
```
### DQL I LIMIT & OFFSET

- Les clause LIMIT et OFFSET vous permettent de produire un sous-ensemble du résultat de la requête.
- Ces clauses permettent de limiter le nombre de résultats retournés et de spécifier à partir de quel enregistrement commencer.
```sql
Exemple : SELECT titre FROM livres ORDER BY date_publication DESC LIMIT 5 OFFSET 10;
```

### DQL I CASE
- L’expression CASE permet d’obtenir un résultat différent selon plusieurs conditions.
```sql
Exemple :
  SELECT prenom, 
  CASE 
     WHEN age < 20 THEN 'Jeune'
     WHEN age BETWEEN 20 AND 60 THEN 'Adulte'
     ELSE 'Senior'
  END AS categorie_age
  FROM employe;
  
    SELECT nom,
    CASE 
    WHEN genre = 'f' THEN 'Femme'
    ELSE 'Pas normal'
    END
    FROM employe;
 ``` 

### DQL I requêtes imbriquées
- Une requête peut être imbriquée dans une autre pour former des requêtes complexes.
```sql
Exemple :
sql
Copy code
  SELECT prenom, nom 
  FROM employe 
  WHERE departement = 
     (SELECT departement FROM managers WHERE nom = 'Dupont');
```

### DQL I combinaisons de requêtes

- Les requêtes peuvent être combinées à l'aide des opérateurs UNION, INTERSECT, et EXCEPT.
```sql
Exemples :
SELECT nom FROM employe UNION SELECT prenom FROM employe;
UNION: SELECT ville FROM clients UNION SELECT ville FROM fournisseurs;
INTERSECT: SELECT nom FROM vendeurs INTERSECT SELECT nom FROM acheteurs;
EXCEPT: SELECT nom FROM employes EXCEPT SELECT nom FROM managers;
```

### DQL I opérateurs de comparaison et opérateurs logiques
- Permettent de comparer des valeurs.
```sql
Opérateurs de comparaisons: =, <>, <, <=, >, >=
Opérateurs logiques: AND, OR, NOT
```sql
### DQL I opérateur BETWEEN
- Simplifie une expression utilisant un intervalle.
```sql
Exemple: 
SELECT nom FROM employe WHERE salaire BETWEEN 10.00 AND 20.00;
```
### DQL I opérateurs sur les listes
- Il existe des opérateurs pour analyser des listes: ANY, ALL, IN
```sql
Exemples:
... WHERE xyz >= ANY(VALUES (12), (5), (74));
SELECT nom FROM employe WHERE departement IN ('ventes', 'r&d');
```

### DQL I valeurs nulles
- Gestion et considération des valeurs nulles en SQL.
```sql
Exemple:
SELECT 'bob' = NULL; -- retourne NULL
SELECT NULL = NULL; -- retourne NULL
```
### DQL I formatage (entrée et sortie)
- Convertit un type de données en une chaîne de caractères et vice versa.
```sql
Exemple:
to_char (un nombre, une date, une heure)
to_number (vers un nombre)
to_date (vers une date)
```
### DQL I conversion de types
- SQL est un langage typé fort, nécessitant parfois des conversions de type.
```sql
Exemple:
SELECT ROUND(CAST('0.75' AS NUMERIC));
```
```sql
Exercice 1.1.
Faites afficher la liste de tous les employés de la table employe
SELECT * 
	FROM employe

Exercice 1.2.
Faites afficher le nom, le prénom et le département des employés de la table employe. 
SELECT nom,prenom, departement 
	FROM employe

Exercice 1.3.
Inverser l’ordre d’affichage des résultats du numéro précédent: on veut avoir les colonnes dans
l’ordre suivant : département, prénom et nom. 
SELECT departement, nom,prenom 
	FROM employe

Exercice 1.4.
Faites afficher la liste des employés (nom et prénom) qui travaillent dans le département des
ventes. 
SELECT nom, prenom 
	FROM employe 
		WHERE departement = 'ventes'
		
Exercice 1.5.
Faites afficher la liste des employés dont le salaire horaire est supérieur à 20.00$. On veut voir
seulement le nom et le prénom des employés ainsi que leur salaire. Les entêtes de colonnes seront
respectivement Nom de l’employé, Prénom de l’employé et Salaire de l’employé (où chacun
des titres respecte les espaces ainsi que les majuscules et minuscules). 
SELECT nom,prenom,salaire 
	FROM employe
	WHERE salaire > 20;
	
Exercice 1.6.	
Faites afficher la liste des employés (nom, prénom, département et salaire) qui travaillent dans les
départements des ventes et dont le salaire est supérieur à 20.00$. 
SELECT nom,prenom,salaire 
	FROM employe
	WHERE salaire > 20 AND departement = 'ventes';
	
Exercice 1.7.
Faites afficher la liste de tous les employés travaillant dans le département de R&D ainsi que tous
les employés résidant à Montréal qui gagne au moins 25.00$. 
SELECT nom,prenom,salaire 
	FROM employe
	WHERE salaire > 20 AND departement = 'r&d' AND ville = 'Montréal';
SELECT nom, prenom, salaire
    FROM employe
    WHERE departement = 'r&d' OR (ville = 'Montréal' AND salaire > 25.0);

Exercice 1.8.
Faites afficher la liste des employés (nom, prénom et ville) habitant à Laval et à Longueuil. On
désire deux versions de cette solution : d’abord en n’utilisant pas l’opérateur IN et ensuite en
l’utilisant.
SELECT nom, prenom,ville
	FROM employe
	WHERE ville = 'laval' OR ville = 'Longueuil'
SELECT nom, prenom, ville 
	FROM employe 
	WHERE ville IN ('Laval','Longueuil');
	
Exercice 1.9.
Faites afficher la liste des employés (nom, prénom et département) dont le superviseur est 111. 
SELECT nom, prenom, ville 
	FROM employe 
	WHERE superviseur= '111'
	
	
Exercice 1.10.
Faites afficher la liste des employés (le nom, le prénom et le salaire seulement) dont le salaire
horaire est entre 20.00$ et 30.00$ inclusivement. On désire deux versions de cette solution :
d’abord sans l’usage de l’opérateur BETWEEN et ensuite avec son utilisation. 
SELECT nom, prenom, salaire 
	FROM employe 
	WHERE salaire <= 30 AND salaire >=20;
SELECT nom, prenom, salaire
    FROM employe
    WHERE salaire BETWEEN 20.0 AND 30.0;
	
Exercice 1.11.
Est-ce que l’opérateur BETWEEN est inclusif ou exclusif? Autrement dit, est-ce que les bornes
spécifiées sont incluses dans le résultat de la requête? Tentez d’ajuster les deux sous requêtes
précédentes pour rendre les bornes exclusives. 
L'opérateur BETWEEN est inclusif, 
ce qui signifie que les bornes spécifiées sont 
incluses dans le résultat de la requête. Lorsque vous utilisez l'opérateur BETWEEN pour filtrer 
des données dans une requête SQL, les valeurs qui sont égales ou supérieures à la 
borne inférieure et égales ou inférieures à la borne supérieure sont incluses dans le résultat.
SELECT nom, prenom, salaire
    FROM employe
    WHERE salaire > 20.0 AND salaire < 30.0;
	
Exercice 1.12.
Croyez-vous qu’il soit possible d’utiliser l’opérateur BETWEEN si on désire l’appliquer sur des
chaînes de caractères. On vous demande d’afficher la liste des employés (le nom et le prénom
seulement) dont le nom est inclus entre Lebel et Tremblay inclusivement. 
SELECT nom, prenom
    FROM employe
    WHERE nom BETWEEN 'Lebel' AND 'Tremblay';	

Exercice 1.13.
Faites afficher la liste de tous les noms de famille. On désire deux versions de cette liste. D’abord,
on veut une liste représentant toutes les occurrences de nom (même s’il y a des doublons).
Ensuite, on désire avoir une liste sans occurrence (sans doublon). 
SELECT nom, prenom 
	FROM employe
SELECT DISTINCT nom
    FROM employe;

Exercice 1.14.
Faites afficher le nombre 1. 
SELECT 1

Exercice 1.15.
Faites afficher la liste de tous les employés (nom et prénom) avec la mention employé dans une
troisième colonne.
SELECT nom, prenom, 'employé'
    FROM employe;

Exercice 1.16.
On désire connaître l’impact d’une hausse salariale de 5%. Afficher le nom, le prénom, le salaire,
le montant de la hausse de 5% sur les salaires et finalement, le salaire incluant la hausse. 
SELECT nom, prenom, salaire, salaire *0.5, salaire *1.05 
	FROM employe
	
	
Exercice 1.17.
On désire la liste des employés (nom, prénom et département) qui ne travaillent pas dans les
départements des ventes et aux achats. On vous demande d’utiliser l’opérateur IN.	
SELECT nom, prenom, departement 
	FROM employe
	WHERE departement NOT IN ('ventes', 'achats');
	
	
Exercice 1.19.
On désire la liste des employés (nom, prénom et salaire) qui ont un salaire entre 20.00$
inclusivement et 30.00$ exclusivement. On désire deux versions de cette solution. La première
n’utilisant pas l’opérateur BETWEEN et la seconde l’utilisant. 
SELECT nom, prenom, salaire
	FROM employe
	WHERE salaire >= 20.0 AND salaire < 30.0;
SELECT nom, prenom, salaire
    FROM employe
    WHERE salaire BETWEEN 20.0 AND 30.0 AND salaire <> 30.0;
	
Exercice 1.20.
En respectant le format du modèle suivant, écrire la requête permettant d’afficher le prénom, le
nom et le département de chaque employé. Attention, la solution ne possède qu’une seule
colonne. (l’opérateur || permet la concaténation des chaînes de caractères) 	
SELECT prenom || ' ' || nom || ' travail dans le département : ' || departement || '.' 
            AS "Les employés et leur département"
    FROM employe;	
```
