les transactions que nous avons rapide ne sont pas assez bonne pour les sites commex twitter(trop de tweet par min)

Alors en 2009 il y a une les base de donnes alerternative (noSQL), gerer les index le plus rapidement rapide, car tout ceci est trop rapide.

Les base de donnes ont ete fait en 1970, alors elle ne sibt oas adaote au besoin d'aujourd'hui.

## Les Big Data

Les Big Data sont caractérisées par les 5 "V" suivantes :

1. **Volume :** Les Big Data impliquent une quantité massive de données, énorme en volume, bien au-delà de la capacité des bases de données traditionnelles.

2. **Variabilité :** Les données dans les Big Data ne sont pas toujours uniformes. Elles peuvent prendre différentes formes, ce qui rend leur stockage et leur traitement complexes.

3. **Véracité :** Les Big Data contiennent à la fois des données vraies et fausses. La fiabilité des données peut être un défi.

4. **Vélocité :** Les Big Data sont générées et traitées à une vitesse impressionnante. Il s'agit de la rapidité à laquelle les informations sont générées et capturées.

5. **Valeur :** La valeur des données est essentielle. Cependant, il peut y avoir des problèmes liés à la qualité des données, aux fausses informations (fake news), et à la difficulté de vérifier toutes les données en raison du volume massif.

   - La valeur des données peut varier avec le temps. Si les données perdent de leur valeur après quelques jours, elles peuvent ne pas être sauvegardées, ce qui peut affecter le volume global des données.

   - Le volume massif de données peut entraîner des problèmes d'insertion et de traitement en raison de la vélocité des données.

   - Il est à noter que peu d'entreprises au Québec se lancent dans le domaine du Big Data.

## NoSQL

- Le terme NoSQL n'a pas de définition fixe, il ne faut pas se fier à l'interprétation "No SQL" ou "Not Only SQL".

- Les bases de données NoSQL sont conçues pour fonctionner en clusters, avec de multiples serveurs (slaves) pour gérer les Big Data.

- Beaucoup de bases de données NoSQL sont open source.

- NoSQL élimine les opérations lourdes dans les transactions, réduisant ainsi la pression sur les systèmes. Les modifications d'insertion peuvent prendre un certain temps avant de se refléter dans les résultats de la sélection.

## Types de Bases de Données NoSQL


### Key-Value

- Ce type de base de données fonctionne comme une immense table de hachage (hashtable) qui stocke des données sur un disque dur. Les informations sont accessibles uniquement par la clé, et la valeur peut être de n'importe quel type (image, JSON, vidéo, etc.).

- Un exemple pertinent est Amazon S3, utilisé par des entreprises comme Spotify, Netflix et Objectif 8.

- Ces bases de données sont généralement peu coûteuses et très  utiles.

**MongoDB**

MongoDB est une base de données NoSQL qui permet de stocker des documents JSON. Elle offre une grande flexibilité pour sauvegarder divers types de données. Cependant, elle présente quelques caractéristiques importantes :
 
- Le problème avec MongoDB est l'absence de structure rigide. Cela signifie que si une faute de frappe se glisse dans une colonne, les données seront insérées malgré tout.

- Contrairement aux bases de données relationnelles, MongoDB ne prend pas en charge les clés étrangères (foreign keys).


--------- 
dans mango shell

- db : dans quel base de données ous sommes 
- show dbs : tout les base de données installés sur le serveur 
use nomDataBase  : lorsque nous allons faire des select se sera dans ctete base de données comme dans mysql use data_name, si la data base n'existe pas elle sera creer lorsque nous allons inserer qqchose
db.locaux.insertOne({location: 'C4.07'})   : nom de la connection (n'existe pas, alors sera creer). Pas besoin de create un database, une table ou de declarer les type

**Column-Family**

- Les bases de données de type Column-Family sont utilisées pour atteindre de hautes performances, notamment lorsqu'il s'agit de répondre à des requêtes spécifiques. Elles sont principalement utilisées lorsque la structure des tables est optimisée pour des besoins particuliers, par exemple, pour effectuer des recherches sur la notation (rating) des hôtels.

- Ces informations complètent vos notes pour couvrir les sujets de MongoDB et des bases de données Column-Family.


Cap-collection

- va detruire la derniere données avec une nouvelle, afin de ne pas flooder le disque dure 
- dans mango db

### Graph

- Les bases de données de type graphique sont utilisées pour modéliser les relations entre entités, comme les suggestions d'amis sur Facebook. Elles se concentrent sur les liens entre les nœuds du graphique.

- Ces informations complètent vos notes pour couvrir les sujets abordés par votre enseignant en français.




