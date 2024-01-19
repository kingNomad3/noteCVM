# neo4 (graph)

commande cmd pour demarrer Neo4J (on doit etre dans le dossier neo4j):
.\bin\neo4j console
http://localhost:7474/browser/

username neo4j

- cypher (nom du language des base de données graph) 
- ( C'est nous qui décidons de la relation des variables, ex: Plus Grand Que, c'est en json)

"Montréal" Plus Grand Que  "Laval" Plus Grand Que  "Blainville"
		Plus Grand Que  "St-Eustache"

>> MATCH  (L) -[: Plus Grand Que ]-> (V)
trouve moi un noeud, qui a une relation plus grand que, avec un autre noeud
>> WHERE L.nom = 'Laval'
>> RETURN v.nom
(L ou v, c'est comme une rangée dans une table)
==================
>> MATCH  (L) <-[: Plus Grand Que ]- (V)
inverse de : trouve moi un noeud, qui a une relation plus grand que, avec un autre noeud
(sens de la flèche change)
>> WHERE L.nom = 'Laval'
>> RETURN v.nom
===================
ex:
MATCH (f) -[:AMI_AVEC]->(a)
WHERE f.nom - 'Fred'
RETURN a.nom

ex:
MATCH (f) -[:AMI_AVEC]->(a)-[:AMI_AVEC]->(b)
WHERE f.nom - 'Fred'
RETURN a.nom



(création d'un nouveau noeud, on peux avoir des noeuds de différents types)
-- label (type de noeud)
create (:person {name : 'John', title : "dev", year : ' 2023'})
create (:person {name : 'Joe', title : "dev", year : ' 2022'})
create (:person {name : 'Jack', title : "dev", year : ' 2021'})

Match(a) : trouve moi un a comme select * from a etant un variable
return a

Match (a:person)  
return a

#relation
Match (a:person),(b:person)
WHERE b.name = 'John' and b.nom = 'Jack'
CREATE (a)- [:FRIENDS_SINCE { year : 2010}] ->(b)
## ou, ce sont facon de la faire
Match (a:person {name: 'John'}),(b:person {name: 'Jack'})
CREATE (a)- [:FRIENDS_SINCE { year : 2010}] ->(b)

Match (a:person {name: 'John'}),(b:person {name: 'Joe'})
CREATE (a)- [:FRIENDS_SINCE { year : 2010}] ->(b)

- lors de la creation, il nous faut un sense. Une direction est obligatoire.


## index
CREATE index_person FOR (p:person) ON (p.name) : je veux tout les variable de type person et je veux sur le name 

<> :different de 

Match (a:person)  
return a.name <> 'joe'
RETURN a.name
ORDER BY a.name

#trouve oi tout les noeuds qui ne sont oas joe et qui a une relation avec b
Match (a:person)  - [:FRIENDS_SINCE] -() # va dans les deux sense
Match (a:person)  - [:FRIENDs_SINCE] - (b)
return a.name <> 'joe'
RETURN a.name
ORDER BY a.name

MATCH (a: person) -[]-> (b), (c)-[]->(a) # une realtion peu importe 
RETURN b

#trouve moi tout les noeuds qui n'ont aucune relation
MATCH(n) 
WHERE NOT(()-[]->(n))
RETURN n

#suprimer un noeuds
MATCH(n) 
WHERE NOT(()-[]->(n))
DELETE n

#suprimer une relation 
MATCH(n) - [r:TEST]->(m)
WHERE NOT(()-[]->(n))
DELETE n

# ne peut pas suprimer le noeuds car il y a plein de relation alors la cmd ci-haut ne marche pas
#SUPRRIMER LE NOEUDS ET TOUT CES RELATIONS
MATCH(n) - [r:TEST]->(m)
WHERE NOT(()-[]->(n))
DETACH DELETE n


#SUPRRIMER SLM LES RELATIONS
MATCH(n) - [r:TEST]->(m)
DETACH DELETE R


#UPDATE jack est devenue jane et est mtn en dba 
MATCH(n:personn {name : 'Jack'})
SET n.name = 'Jane', n.title = 'dba'

# trouve moi la cle primarie qui est egal a 1
MATCH (n:personn)
WHERE elementId(n) = 1
return n

#aggregation
-- equivalent sql: SELECT avg(year) from person where year > 0  GROUP BY title
MATCH(n)
WHERE n.year > 0
RETURN n.title, avg(n.year)

#having
MATCH(n)
WHERE n.year > 0
WITH n.title as title, avg(n.year) as y
WHERE y > 2000
RETURN title, y
