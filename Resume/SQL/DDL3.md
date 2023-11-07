# 420-C42 Langages d'exploitation des bases de données
## Partie 12: DDL III - Création, modification et suppression
### 1. Résolution d'une instruction:
 Chaque requête envoyée à un serveur SGBD subit plusieurs étapes:

#### Normalisation:
    1. retrait des espaces, commentaires, normalisation des mots-clés, identifiants, etc.
    2. Analyse Lexicale: segmentation de la requête en unités lexicales.
    3. Analyse Syntaxique: construction de l'arbre syntaxique de la requête.
    4. Analyse Sémantique: validation du sens de la requête (existence des objets, cohérence des types, droits, etc.)
    5. Définition d'un plan d'exécution: ordre des opérations, estimation des coûts, utilisation des index, etc.
    6. Optimisation du plan d'exécution: sélection d'un plan optimal basé sur divers critères.
    7. Exécution: lancement du plan d'exécution optimal.
    8. Retour du résultat: formatage et transmission du résultat.

### 2. Requête préparée (PREPARE):
    Les requêtes préparées optimisent l'exécution de requêtes récurrentes en préparant leur structure. Une fois la requête préparée créée, elle peut être exécutée plusieurs fois avec des paramètres différents.

```sql
PREPARE ...
EXECUTE ...
DEALLOCATE ...
```

### 3. Procédure SQL:
    Les procédures SQL sont des ensembles d'instructions SQL qui peuvent être exécutés. Contrairement aux fonctions, les procédures ne retournent pas de valeurs. Elles sont utiles pour automatiser et centraliser des séquences d'opérations.

```sql
CREATE OR REPLACE PROCEDURE ...
CALL ...
```
### 4. Fonction SQL:
    Les fonctions SQL sont similaires aux procédures, mais elles retournent une valeur. Elles peuvent être appelées depuis d'autres requêtes SQL.

```sql
CREATE OR REPLACE FUNCTION ...
SELECT ...
```
### 5. Autres objets:
    Il existe de nombreux autres objets en SQL, comme les déclencheurs (triggers) ou des extensions des fonctions et procédures. Pour exploiter pleinement la puissance d'un SGBD comme PostgreSQL, il est essentiel de se familiariser avec tous ces objets.

### Conclusion:
    Cette partie a couvert la manière dont les requêtes sont traitées et exécutées par les SGBD, ainsi que les avantages et utilisations des requêtes préparées, des procédures et des fonctions SQL. L'utilisation efficace de ces objets peut grandement améliorer les performances et la modularité d'une base de données.