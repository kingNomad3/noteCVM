
# Managing SQLite Database with Python Using Classes

This document outlines a Python script that manages a SQLite database using a class-based approach, facilitating the creation, insertion, deletion, and querying of data related to departments and employees.

## Script Overview

- **Database Setup**: Establishes database connections and enables foreign key constraints.
- **Class-Based Architecture**: Implements database operations within a class to maintain clean and manageable code.

## Class: `DAO` (Data Access Object)

### Constructor

- **Purpose**: Initialize the database connection parameters.
  ```python
  def __init__(self, chemin):
      self.chemin = chemin
  ```

### Connection Management

- **Connect**:
  ```python
  def connecter(self):
      self.connexion = sqlite3.connect(self.chemin)
      self.curseur = self.connexion.cursor()
      self.curseur.execute(ALLUMER_CLES_ETRANGERES)
  ```

- **Disconnect**:
  ```python
  def deconnecter(self):
      self.curseur.close()
      self.connexion.close()
  ```

### Table Management

- **Create Tables**:
  ```python
  def creer_tables(self):
      self.curseur.execute(CREER_DEPARTEMENT)
      self.curseur.execute(CREER_EMPLOYE)
  ```

- **Drop Tables**:
  ```python
  def detruire_tables(self):
      self.curseur.execute(DROP_EMPLOYE)
      self.curseur.execute(DROP_DEPARTEMENT)
  ```

### Data Manipulation

- **Populate Tables**:
  ```python
  def peupler_tables(self):
      self.curseur.execute(INSERT_DEPARTEMENT, (1, 'tricot'))
      self.curseur.execute(INSERT_EMPLOYE, (100, 'Pierre-Paul', 1))
      self.curseur.execute(INSERT_EMPLOYE, (101, 'Catherine', 1))
      self.curseur.execute(INSERT_EMPLOYE, (102, 'Jean-Marc', 1))
      self.connexion.commit()
  ```

- **Insert Multiple Employees**:
  ```python
  def inserer_plusieurs_employes(self, liste_employes):
      self.curseur.executemany(INSERT_EMPLOYE, liste_employes)
      self.connexion.commit()
  ```

- **Remove Data**:
  ```python
  def retirer_employe(self, nom):
      self.curseur.execute(RETIRER_EMPLOYE, (nom,))
      self.connexion.commit()
  ```

### Display Data

- **Show Tables**:
  ```python
  def afficher_tables(self):
      print('\n*************DEPARTEMENT*************\n')
      self.curseur.execute(SELECT_DEPARTEMENT)
      for rangee in self.curseur.fetchall():
          print(rangee)
          
      print('\n*************EMPLOYE*************\n')
      self.curseur.execute(SELECT_EMPLOYE)
      for rangee in self.curseur.fetchall():
          print(rangee)
  ```

## Main Execution Function

- **Demonstrates** how to use the `DAO` class for database operations.
  ```python
  def main():
      bd = DAO(CHEMIN_BD)
      bd.connecter()
      bd.creer_tables()
      bd.peupler_tables()
      bd.afficher_tables()
      bd.deconnecter()
      return 0
  ```

This class-based approach makes the database handling code more organized and modular, simplifying maintenance and enhancing readability.
