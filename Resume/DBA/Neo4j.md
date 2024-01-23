
# Neo4j (Graph Database)

## Commande CMD pour démarrer Neo4J
- Dans le dossier Neo4j, exécuter : `.in
eo4j console`.
- Accès via : http://localhost:7474/browser/.
- Nom d'utilisateur : `neo4j`.

## Cypher: Langage des Bases de Données Graph
- Cypher est le langage de requête pour les bases de données graph.
- Les utilisateurs définissent les relations entre les variables, par exemple, 'Plus Grand Que'.

### Exemples de Requêtes Cypher
- Requête pour trouver une relation spécifique :
  - `MATCH (L) -[: Plus Grand Que ]-> (V)` où L a une relation 'Plus Grand Que' avec V.
  - `WHERE L.nom = 'Laval'` et `RETURN v.nom` pour filtrer et retourner les résultats.
- Inversion de la relation :
  - `MATCH (L) <-[: Plus Grand Que ]- (V)` où V a une relation 'Plus Grand Que' avec L.
  (sens de la flèche change)
>> WHERE L.nom = 'Laval'
>> RETURN v.nom

#### Autres Exemples
- Trouver les amis de Fred :
  - `MATCH (f) -[:AMI_AVEC]->(a) WHERE f.nom = 'Fred' RETURN a.nom`.
- Chaîne d'amis :
  - `MATCH (f) -[:AMI_AVEC]->(a)-[:AMI_AVEC]->(b) WHERE f.nom = 'Fred' RETURN a.nom`.

### Création de Noeuds et Relations
- Créer des noeuds de différents types :
  - `create (:person {name: 'John', title: "dev", year: '2023'})`.
  - `create (:person {name: 'Joe', title: "dev", year: '2022'})`.
  - `create (:person {name: 'Jack', title: "dev", year: '2021'})`.
- Relations entre noeuds :
  - `Match (a:person),(b:person) WHERE b.name = 'John' and b.nom = 'Jack' CREATE (a)-[:FRIENDS_SINCE { year: 2010}]->(b)`.
  - ou
  - `Match (a:person {name: 'John'}),(b:person {name: 'Jack'}) CREATE (a)- [:FRIENDS_SINCE { year : 2010}] ->(b)`
  - `Match (a:person {name: 'John'}),(b:person {name: 'Joe'}) CREATE (a)- [:FRIENDS_SINCE { year : 2010}] ->(b)`
  
  - lors de la creation, il nous faut un sense. Une direction est obligatoire.

### Indexation et Requêtes Avancées
- Création d'un index :
  - `CREATE index_person FOR (p:person) ON (p.name)`. :je veux tout les variable de type person et je veux sur le name 
- Requêtes avec conditions :
  - `Match (a:person) WHERE a.name <> 'Joe' RETURN a.name ORDER BY a.name`.
    - <> :different de 

# trouve oi tout les noeuds qui ne sont oas joe et qui a une relation avec b
  Match (a:person)  - [:FRIENDS_SINCE] -() # va dans les deux sense
  Match (a:person)  - [:FRIENDs_SINCE] - (ba)
  return a.name <> 'joe'
  RETURN a.name
  ORDER BY a.name

MATCH (a: person) -[]-> (b), (c)-[]->(a) # une realtion peu importe 
RETURN b

#trouve moi tout les noeuds qui n'ont aucune relation
MATCH(n) 
WHERE NOT(()-[]->(n))
RETURN n


### Suppression et Mise à Jour
- Supprimer des noeuds et relations :
  - `MATCH(n) WHERE NOT(()-[]->(n)) DETACH DELETE n`.
- suprimer une relation 
  - `MATCH(n) - [r:TEST]->(m) WHERE NOT(()-[]->(n)) DELETE n`
- Mise à jour de noeuds :
  - `MATCH(n:person {name: 'Jack'}) SET n.name = 'Jane', n.title = 'dba'`.

# trouve moi la cle primarie qui est egal a 1
MATCH (n:personn)
WHERE elementId(n) = 1
return n  

### Agrégation et Filtrage
- Exemple d'agrégation :
  - `MATCH(n) WHERE n.year > 0 RETURN n.title, avg(n.year)`.
  - equivalent sql: SELECT avg(year) from person where year > 0  GROUP BY title
- Filtrage avec 'HAVING' :
  - `MATCH(n) WHERE n.year > 0 WITH n.title as title, avg(n.year) as y WHERE y > 2000 RETURN title, y`.
