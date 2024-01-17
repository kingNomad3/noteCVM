les transactions que nous avons rapide ne sont pas assez bonne pour les sites commex twitter(trop de tweet par min)

Alors en 2009 il y a une les base de donnes alerternative (noSQL), gerer les index le plus rapidement rapide, car tout ceci est trop rapide.

Les base de donnes ont ete fait en 1970, alors elle ne sibt oas adaote au besoin d'aujourd'hui.

Les big data: 
Les 5 “V”:
o	Volume : énorme!!
o	Variabilité : On stock mais les données ne sont pas toujours pareilles  (stockage de différente forme)
o	Véracité : Certaines données sont vraies et d’autres fausses
o	Vélocité : La vitesse à laquelle l’information entre
o	Valeur : La valeur des données, des mauvaises lecture, des fake news. Il y a tlm de donnes que les donnes ne sont pas verifiers. Ont rammasse trop de données, alors nous avont pas le temps de verifier 

- la valeur des donnes, les données des données a travers le temps, si les données n'ont plus de valeur apres deux jours alors on va pas les sauvegarder et cela va affecter le volume

- il y a enormement de donnes, sur des sites il y  a tellement de donnes qui sont rentrer les insert ne sont pas assez, a cause de la velocite des donnes

- peut d'entreprise font du big data (pas au quebec)

## NOSQL

- Il n’y a pas de définition définitive de ce que veut dire NoSQL. 
Donc il ne faut pas se fier à certains qui disent que ça veut dire : No SQL ou Not Only SQL

- no sql on ete penser en closter, plusieurs slaves (gerer les big datas)
- bcp sont open sources 
- mon enlever tout ce qui est lourds dans les transactions, reduit le stress dans la machine. Si on modifie un insert alors le resultat d'un select va prendre du temps avant de changer pas a la mili secondes 


## key value
- un immense hastable qui garde sur un dique dure,  la seul facon d'aller chercher l'info est par la cle,  la valeur peut etre n'importe quoi (image, json, video, etc) 

Un bon exemple est Amazon S3 ( de amazon), il est utilisé par spotify, Netflix, Objectif 8

- ne coute pas cher, tres utile,



## MongoDB

- permet de sauvegarder des documents JSON, nous laisse sauvegarder n'importe quoi dans la base de données,
- le probleme est qu'il n'ya pas de structures rigide, si nous fesons un typo dans une colonne, la données sera insert quand meme. 
- pas de foreign key

## Column-Family
- Extrement complex, on l'utilise lorsqu'on veut avoir une grande performance
- les tables sont fait selon les requetes par exemple je fais une recherche sur le rating the l'hotel.

## Graph

- Entités et leurs relations, par exemple les suggestions d'ami sur fb.
- se sont les relations entre les noeuds du graph

