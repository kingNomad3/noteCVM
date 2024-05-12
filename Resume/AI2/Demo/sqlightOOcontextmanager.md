
# SQLite Database Management with Context Managers in Python

This document explains a Python script for managing a SQLite database, utilizing a class with context management capabilities to handle database connections.

## Importing Modules

- `sqlite3`: For database operations.
- `traceback`: For handling and tracing back exceptions (if needed).

```python
import sqlite3
from traceback import print_tb
```

## Database Schema Definitions

- **Departement** and **Employe** tables with foreign key constraints:

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

## Class Definition: `DAO` (Data Access Object)

### Constructor and Context Management

- The class initializes with a database path and includes `__enter__` and `__exit__` methods for context management, automating the setup and teardown processes:

```python
class DAO():
    def __init__(self, chemin):
        self.chemin = chemin

    def __enter__(self):
        self.connecter()
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.deconnecter()
        if exc_type is not None:
            print(f'Une exception de type {exc_type} a été soulevée.')
            print(exc_value)
            print_tb(exc_traceback)
```

### Database Operations

- **Connection and Disconnection**:
  ```python
  def connecter(self):
      self.connexion = sqlite3.connect(self.chemin)
      self.curseur = self.connexion.cursor()
      self.curseur.execute(ALLUMER_CLES_ETRANGERES)

  def deconnecter(self):
      self.curseur.close()
      self.connexion.close()
  ```

- **Create and Drop Tables**:
  ```python
  def creer_tables(self):
      self.curseur.execute(CREER_DEPARTEMENT)
      self.curseur.execute(CREER_EMPLOYE)

  def detruire_tables(self):
      self.curseur.execute(DROP_EMPLOYE)
      self.curseur.execute(DROP_DEPARTEMENT)
  ```

- **Data Manipulation**:
  ```python
  def peupler_tables(self):
      self.curseur.execute(INSERT_DEPARTEMENT, (1, 'tricot'))
      self.curseur.execute(INSERT_EMPLOYE, (100, 'Pierre-Paul', 1))
      self.curseur.execute(INSERT_EMPLOYE, (101, 'Catherine', 1))
      self.curseur.execute(INSERT_EMPLOYE, (102, 'Jean-Marc', 1))
      self.connexion.commit()
  ```

### Display Data

- **Print Table Data**:
  ```python
  def afficher_tables(self):
      print('
*************DEPARTEMENT*************
')
      self.curseur.execute(SELECT_DEPARTEMENT)
      for rangee in self.curseur.fetchall():
          print(rangee)
      print('
*************EMPLOYE*************
')
      self.curseur.execute(SELECT_EMPLOYE)
      for rangee in self.curseur.fetchall():
          print(rangee)
  ```

## Usage

- Example usage within a context manager to ensure proper resource management:

```python
def main():
    with DAO('emp_dept.db') as bd:
        bd.creer_tables()
        bd.peupler_tables()
        bd.afficher_tables()
    return 0
```

This script is designed to make database management tasks straightforward and error-free by leveraging Python's context management protocol.
