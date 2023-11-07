# Partie 6: DDL I (Création, modification, et suppression - table et type énuméré)
## DDL (Langage de définition de données)
- Définition: Permet de définir la structure de la base de données.
- DDL (Data Definition Language)

### Clauses principales:
- Le DDL permet de définir la structure de la base de données.
- CREATE : création d’objets.
- ALTER : modification d’objets.
- DROP : suppression d’objets.
- Et d'autres clauses secondaires comme RENAME, TRUNCATE TABLE, et COMMENT.
```sql
- CREATE : Utilisé pour créer un nouvel objet dans la base de données.
CREATE TABLE Employes (
    ID SERIAL PRIMARY KEY,
    Nom VARCHAR(100) NOT NULL,
    Prenom VARCHAR(100) NOT NULL,
    Email VARCHAR(255) UNIQUE NOT NULL,
    DateNaissance DATE,
    Departement VARCHAR(50)
);
```sql
- ALTER : Modifie un objet existant.
```sql
ALTER TABLE Employes ADD COLUMN Adresse VARCHAR(255);
ALTER TABLE Employes ALTER COLUMN Departement TYPE VARCHAR(100);
```sql
- DROP : Supprime un objet.
```
DROP TABLE IF EXISTS Employes;
```
### Types de Données et Contraintes
- Types énumérés : Pour définir un ensemble fixe de valeurs constantes.
```sql
CREATE TYPE JourSemaine AS ENUM ('Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi');
CREATE TABLE Planning (
    ID SERIAL PRIMARY KEY,
    Jour JourSemaine NOT NULL,
    Activite VARCHAR(255) NOT NULL
);
```
### Contrainte CHECK : Assure que les données répondent à une condition spécifique.
```sql
CREATE TABLE Salaries (
    ID SERIAL PRIMARY KEY,
    Nom VARCHAR(100) NOT NULL,
    Salaire DECIMAL CHECK (Salaire >= 0)
);
```
### Contrainte de clé étrangère : Établit un lien entre les données de deux tables.
```sql
CREATE TABLE Departements (
    ID SERIAL PRIMARY KEY,
    NomDepartement VARCHAR(100) NOT NULL
);

CREATE TABLE Employes (
    ID SERIAL PRIMARY KEY,
    Nom VARCHAR(100) NOT NULL,
    DepartementID INTEGER REFERENCES Departements(ID)
);
```
### Valeur par défaut (DEFAULT) : Attribue une valeur par défaut lors de la création d'une entrée.
```sql
CREATE TABLE Commandes (
    ID SERIAL PRIMARY KEY,
    DateCommande DATE DEFAULT CURRENT_DATE,
    Produit VARCHAR(100) NOT NULL
);
```

