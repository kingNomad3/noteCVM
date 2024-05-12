
# Managing SQLite Database with Python

This document outlines a Python script that manages a SQLite database, including creating tables, inserting, and querying data related to departments and employees.

## Script Overview

- **Database Connection**: Connect to a SQLite database and enable foreign key constraints.
- **Table Management**: Create and drop tables for departments and employees.
- **Data Handling**: Insert, delete, and display data.

## SQL Statements

```sql
CREATE TABLE IF NOT EXISTS departement (
    id  INT PRIMARY KEY NOT NULL,
    nom CHAR(25) NOT NULL
);

CREATE TABLE IF NOT EXISTS employe (
    id      INT NOT NULL,
    id_dept INT NOT NULL,
    nom     CHAR(25) NOT NULL,
    PRIMARY KEY(id),
    FOREIGN KEY(id_dept) REFERENCES departement(id)
);
```

## Python Functions

### Database Connection

- **Connect**:
  ```python
  def connecter(chemin):
      connexion = sqlite3.connect(chemin)
      curseur = connexion.cursor()
      curseur.execute('PRAGMA foreign_keys = 1')
      return connexion, curseur
  ```

- **Disconnect**:
  ```python
  def deconnecter(connexion, curseur):
      curseur.close()
      connexion.close()
  ```

### Table Operations

- **Create Tables**:
  ```python
  def creer_tables(curseur):
      curseur.execute(CREER_DEPARTEMENT)
      curseur.execute(CREER_EMPLOYE)
  ```

- **Drop Tables**:
  ```python
  def detruire_tables(curseur):
      curseur.execute(DROP_EMPLOYE)
      curseur.execute(DROP_DEPARTEMENT)
  ```

### Data Manipulation

- **Populate Tables**:
  ```python
  def peupler_tables(connexion, curseur):
      curseur.execute(INSERT_DEPARTEMENT, (1, 'tricot'))
      curseur.execute(INSERT_EMPLOYE, (100, 'Pierre-Paul', 1))
      curseur.execute(INSERT_EMPLOYE, (101, 'Catherine', 1))
      curseur.execute(INSERT_EMPLOYE, (102, 'Jean-Marc', 1))
      connexion.commit()
  ```

- **Remove Data**:
  ```python
  def retirer_employe(connexion, curseur, nom):
      curseur.execute(RETIRER_EMPLOYE, (nom,))
      connexion.commit()
  ```

### Displaying Data

- **Show Tables**:
  ```python
  def afficher_tables(curseur):
      print('\n*************DEPARTEMENT*************\n')
      curseur.execute(SELECT_DEPARTEMENT)
      for rangee in curseur.fetchall():
          print(rangee)
      print('\n*************EMPLOYE*************\n')
      curseur.execute(SELECT_EMPLOYE)
      for rangee in curseur.fetchall():
          print(rangee)
  ```

## Running the Script

- **Main Function**:
  ```python
  def main():
      connexion, curseur = connecter(CHEMIN_BD)
      creer_tables(curseur)
      peupler_tables(connexion, curseur)
      afficher_tables(curseur)
      deconnecter(connexion, curseur)
      return 0
  ```

This script provides a basic framework for managing a SQLite database in Python, allowing for simple operations on tables and records.

