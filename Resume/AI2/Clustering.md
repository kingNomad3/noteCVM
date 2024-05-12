# Clustering

Une des tâches classiques de l'IA est le partitionnement de données (data clustering).
Applications:
- Imagerie médicale: Différencier des tissus
- Génétique: Identifier des familles de gènes
- Commerce électronique: Grouper des achats potentiels pour un client.
- Suggestions
- Analyse de réseaux sociaux: Reconnaître des "communautés" d'utilisateurs.

# Partitionnement

Le partitionnement de données se fait sur un ensemble de données représentées sous la forme de points dans un espace n-dimensionnel.
Notre analyse des cooccurrences de mots dans un texte génère de tels points.

## Partitionnement/Clustering

L'idée derrière le clustering (partitionnement) est que l'on cherche à regrouper nos données afin que certaines d'entre elles appartiennent à un premier "cluster" (partition), d'autres, à un deuxième cluster, et ainsi de suite.

Afin de visualiser la situation de manière graphique, limitons notre espace à deux dimensions.
On peut extrapoler les concepts qui suivront à un espace n-dimensionnel comme nous l'avons fait en classe.
i.e., Pythagore sur 2 dimensions, ensuite sur 3 dimensions, etc.

![Example Image](/Resume/AI2/Image/Image1.png)

Il existe plusieurs types de partitionnement de données.
Nous verrons le partitionnement de données à l'aide de centroïdes.
Les centroïdes sont les barycentres géométriques des partitions (clusters).

## Clustering: Centroïdes

### Centroïde
Le centroïde, barycentre, ou centre de gravité, est le point sur lequel peut se maintenir en équilibre un système.
Pensez à un mobile de bébé ou bien tenir un cabaret de cafétéria en équilibre sur son doigt.

#### Comment trouve-t-on ce point?

En physique, on calcule le barycentre en additionnant les coordonnées des points, que l’on majore à l’aide des poids relatifs (proportionnels) de chaque objet dans le système.
En géométrie, barycentre et centroïde sont des synonymes.

Pour les points A, B, et C, possédant les poids respectifs a, b, et c, le barycentre G est fourni par la relation suivante:

$$
G = \frac{a}{a+b+c} A + \frac{b}{a+b+c} B + \frac{c}{a+b+c} C
$$



S'il y a "n" points (A) et ils ont tous le même poids, disons "m", la formule devient:

$$
G = \frac{m}{mn} A_1 + \frac{m}{mn} A_2 + \ldots + \frac{m}{mn} A_n
$$
$$
G = \frac{1}{n} (A_1 + A_2 + \ldots + A_n)
$$
$$
G = \frac{1}{n} \sum_{i=1}^{n} A_i
$$


Cette formule peut être réécrite comme suit:

$$
G = \frac{1}{n} \sum_{i=1}^{n} A_i
$$


Une moyenne! Le centroïde est donc le point moyen du cluster lorsque tous les points ont le même poids.

#### Utilisation de l'algorithme du k-means

- **INIT**: On crée k centroïdes aléatoirement. Chaque point va dans le cluster du centroïde le plus proche.
- **TANT QUE nombre de migrations > 0**: On calcule les nouveaux centroïdes des k clusters. Chaque point va dans le cluster du centroïde le plus proche. On compte le nombre de migrations.

### Note Historique

Jusqu'à présent dans ce cours, on s'arrêtait plus ou moins à la phase init avec k = 1 (1-mean). On fournissait un centroïde, c'est-à-dire le mot pour lequel on cherche des mots similaires. On retournait les mots qui lui étaient le plus proches, comme dans la phase INIT, sans boucler.

Maintenant, on fournit plusieurs centroïdes, et on considère TOUS les mots, sans exclusion.

Il est important de noter que les centroïdes se déplacent, mais les mots (leurs coordonnées) ne se déplacent jamais. C’est simplement que leur appartenance à un groupe peut changer, comme une ville conquise lors d’une guerre. Elle ne se déplace pas, mais elle change d’allégeance nationale.


# Clustering avec 5 Centroïdes

Supposons que nous voulons effectuer un partitionnement avec cinq centroïdes. Pour chaque mot de notre vocabulaire, nous déterminons le centroïde le plus proche. Le mot est alors considéré comme faisant partie de la "nation" du centroïde le plus proche et n'appartient pas aux quatre autres nations.

## Attribution des Mots

Une fois tous les mots (villes) assignés à un cluster (nation), chaque mot contribue avec son poids et ses coordonnées au calcul déterminant la position de la nouvelle "capitale nationale" (centroïde).

## Calcul de Position d'un Centroïde

La position d’un centroïde est calculée en prenant la moyenne des coordonnées des mots (villes) dans son cluster (nation). L'algorithme est considéré comme terminé lorsque les mots ne changent plus de groupe.

## Initialisation des Centroïdes

La partie la plus délicate de l'algorithme est son initialisation :
- Utilisation de mots comme centroïdes ?
- Sélection aléatoire de mots ?
- Création de points dans l'espace qui ne correspondent pas à des mots réels ?

## Convergence de l'Algorithme

Quelle que soit la méthode initiale choisie pour déterminer les centroïdes, une fois que les points sont regroupés en clusters stables, l'algorithme a terminé son exécution et est dit avoir convergé. En théorie, les points regroupés partagent certaines propriétés, et il est possible de tirer des conclusions sur ces propriétés.

## Position des Centroïdes

Il est important de noter que les coordonnées des centroïdes peuvent et vont souvent tomber "entre" les mots. Cela indique qu'il faut utiliser des nombres flottants pour ces calculs.

## Ressources Complémentaires

Pour une visualisation interactive de l'algorithme de k-means, consultez [ce lien](http://www.naftaliharris.com/blog/visualizing-k-means-clustering/) (disponible en anglais).

