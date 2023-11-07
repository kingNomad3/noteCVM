# Introduction au DML
- Le DML permet la gestion et la manipulation des données stockées dans une base de données.

## Principales clauses :

- INSERT : Pour ajouter de nouvelles données.
- UPDATE : Pour modifier des données existantes.
- DELETE : Pour supprimer des données.

## INSERT
-  L'opération INSERT ajoute de nouvelles données à une table.
```sql
Exemples :
-- Création de la table employé
CREATE TABLE employe (
    id SERIAL PRIMARY KEY,
    nom VARCHAR(32) NOT NULL,
    date_embauche DATE NOT NULL DEFAULT CURRENT_DATE,
    salaire NUMERIC(5, 2)
);
```
```sql
-- Insertion de données dans la table
INSERT INTO employe VALUES (1000, 'Lebel', '2000-01-01', 20.00);
```
```sql
-- Spécification des colonnes pour l'insertion
INSERT INTO employe(id, nom, date_embauche, salaire)
VALUES (1001, 'Miron', '2000-01-02', 25.00);
```
```sql
-- Insertion partielle
INSERT INTO employe(nom) VALUES ('Dupuis');
```
```sql
-- Insertion multiple 
INSERT INTO employe(salaire, nom)
VALUES (25.00, 'Laroche'),
       (DEFAULT, 'Gravel'),
       (35.00, 'Lapierre');
```
```sql
-- Insertion basée sur une requête SELECT
INSERT INTO employe(nom, salaire)
SELECT nom, 25.00 FROM employe WHERE nom LIKE '%a%';
```

## UPDATE
- L'opération UPDATE modifie des données existantes.

```sql
Exemples :
-- Augmentation de 5% pour tous les employés
UPDATE employe
SET salaire = salaire * 1.05;
```
```sql
-- Mise en majuscule des noms et augmentation de 10$
UPDATE employe
SET nom = UPPER(nom),
salaire = salaire + 5.00
WHERE nom LIKE '%a%';
```
```sql
-- Mise à jour basée sur un critère
UPDATE employe
SET salaire = 50.00
WHERE id = 1;
```
## DELETE
- L'opération DELETE retire des données d'une table sans altérer sa structure.

```sql
Exemples :
-- Suppression basée sur un critère
DELETE FROM employe
WHERE nom LIKE '%a%';
```
```sql
-- Suppression de toutes les données de la table
DELETE FROM employe;
```

## Gestion des dépendances circulaires
- Les dépendances circulaires peuvent poser des problèmes lors de la création ou de la manipulation des données. Pour gérer ces situations, on peut désactiver temporairement les contraintes de clé étrangère et les réactiver une fois les modifications terminées.

```sql
-- Désactivation des contraintes
ALTER TABLE nom_table DISABLE TRIGGER ALL;

-- Modifications nécessaires

-- Insérer un nouvel employé
INSERT INTO employe(nom, prenom, salaire) VALUES ('Dupont', 'Jean', 2500);

-- Mettre à jour le salaire de l'employé dont l'ID est 5
UPDATE employe SET salaire = 2800 WHERE id = 5;

-- Supprimer l'employé dont l'ID est 10
DELETE FROM employe WHERE id = 10;

-- Réactivation des contraintes
ALTER TABLE nom_table ENABLE TRIGGER ALL;
```