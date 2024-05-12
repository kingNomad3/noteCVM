# SQLite

 - SQLite peut facilement être utilisé de manière locale.
 C’est-à-dire que la BD peut être conservée sur votre ordinateur, d'où le terme "local".
 La BD sera conservée dans un fichier.
 

 ```python 
 import sqlite3
 ```

 - Afin de créer une BD SQLite, on doit se connecter à la BD à l'aide de sqlite3.
    - Si la BD n'existe pas, elle sera créée.

```python
CHEMINBD = 'emp_dep.bd'
conn = sqlite3.connect(CHEMINBD)
```
- connexion: Un objet qui permettra de communiquer avec la BD
 - Pour exécuter des commandes SQL, on doit créer un curseur.
    - Le curseur est un objet qui permet d'exécuter des commandes SQL.
    - On peut exécuter des commandes SQL à l'aide de la méthode `execute()`.


- Un curseur permet d'exécuter des commandes sql et de récupérer le résultat de recherches.

```python
cur = conn.cursor()
cur.execute('SELECT * FROM employes')

for range in cur.fetchall():
    print(range)

```

- Notez qu'on doit aller inspecter le contenu du select avec un fetchall().
    - Chaque rangée de la table est retournée sous forme de tuple de valeurs.
    - Chaque valeur correspond à une colonne de la table.

## creation de table

```python
CREER_DEPARTEMENT = """ 
CREATE TABLE departement (
    id INT PRIMARY KEY NOT NULL,
    nom CHAR(15) NOT NULL
); """

cur.execute(CREER_DEPARTEMENT)
```
- Notez les NOT NULL
    - SQLite est très permissif…


```python
CREER_EMPLOYE = """
CREATE TABLE employe (
    id INT PRIMARY KEY NOT NULL,
    nom CHAR(15) NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (departement) REFERENCES departement(id)
); """

cur.execute(CREER_EMPLOYE)
```
- Pourquoi créer departement avant employe?
    - En SQLite, il n'y aura pas d'erreur, mais…

- Si on veut se débarrasser de ces tables, on doit appeler la commande DROP.
    
```python

DROP_EMPLOYE = "DROP TABLE IF EXISTS employe"
cur.execute(DROP_EMPLOYE)
DROP_DEPARTEMENT = "DROP TABLE IF EXISTS departement"
cur.execute(DROP_DEPARTEMENT)
```

## Binding
- Au lieu de hard-coder des valeurs dans un énoncé de DML, il est possible d’écrire des commandes qui « lieront » des valeurs à des énoncés.

```python
INSERT_DEPARTEMENT = "INSERT INTO departement (id, nom) VALUES (?, ?)"
INSERT_EMPLOYE = "INSERT INTO employe (id, nom, departement) VALUES (?, ?, ?)"
```

cur.execute(INSERT_DEPARTEMENT, (1, 'Informatique'))
cur.execute(INSERT_DEPARTEMENT, (2, 'Comptabilité'))
cur.execute(INSERT_DEPARTEMENT, (3, 'Ressources Humaines'))
cur.execute(INSERT_EMPLOYE, (4, 'Jean', 1))
cur.execute(INSERT_EMPLOYE, (5, 'Pierre', 2))
```

Lors de l’exécution, on pourra insérer des valeurs en lieu du ? et du ? en fournissant un tuple où figureront ces valeurs.
 - C’est un peu comme un chaîne formatée.

- Retirer les modifications

```python
DELETE_DEPARTEMENT = "DELETE FROM departement WHERE id = ?"
cur.execute(DELETE_DEPARTEMENT, (3,))
```

    - Note: les bindings ne sont pas nécessaires , par contre, ils permettent certaines prouesses qui seront potentiellement nécessaires.
    L'énoncé suivant aurait fait la même chose:
    'DELETE FROM employe WHERE nom = "Toto"'

- executemany(énoncé, séquence)
    - On fournit l’énoncé à exécuter et une liste de paramètres.
    - On DOIT faire du binding.


```python
INSERT_DEPARTEMENT = "INSERT INTO departement (id, nom) VALUES (?, ?)"
cur.executemany(INSERT_DEPARTEMENT, [(1, 'Informatique'), (2, 'Comptabilité'), (3, 'Ressources Humaines')])
connex.commit()
```

## Clés étrangères
- Si vous comptez utiliser des FOREIGN KEY vous devez les rendre actives

```python
connex.execute("PRAGMA foreign_keys = 1")
```
- Je vous conseille d'exécuter cette commande tout de suite après la création du curseur, comme ça vous n'oublierez pas.
    - Par contre, la contrainte échouera seulement s’il y a des données dans les tables.
- Si vous avez déjà des données, vous devrez les nettoyer avant d’activer les contraintes.

Qui appelle commit()?
    - La connexion
- C’est la connexion qui est responsable de la transaction.

- Est-ce que le commit affecte les tables?
    - DDL
        Data Definition Language
        Création, modification et destruction de table.
        Non
    - DML
        Data Manipulation Language
        Ajout, modification ou retrait de données.
        Oui
- close()
    - Lorsqu'on appelle close() sur un curseur ou une connexion, ils ne communiquent plus avec la BD et ne sont plus utilisables.
    - Lorsque __del__() est appelé sur un objet (comme lorsque le programme à terminé), close() est appelé automatiquement.
    - C'est tout de même une bonne idée de boucler les boucles.
