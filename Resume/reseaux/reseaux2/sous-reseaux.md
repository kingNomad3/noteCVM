## Les sous-réseaux 

### 1. Création de sous-réseaux
- Adresse principale: **200.211.102.0 (classe C)**
- But: Créer **4 sous-réseaux**.

( formule :    2b=nb de sous-réseaux, où b = nb de bits à mettre à 1 du côté de l'hôte)

#### a) Calcul du masque de sous-réseaux
- Masque standard (classe C): `255.255.255.0`
- Besoin de 2 bits supplémentaires pour créer 4 sous-réseaux (`2^2 = 4`)
- Masque modifié (dernier octet en binaire) : 255.255.255.11000000
- Masque modifié: `255.255.255.192`

#### b) Adresses des sous-réseaux

256 / 4 = 64     (ou bien : 256 – 192 = 64)

- Sous-réseaux:
  - `200.211.102.0`                 200.211.102.00000000
  - `200.211.102.64`                200.211.102.01000000
  - `200.211.102.128`               200.211.102.10000000
  - `200.211.102.192`               200.211.102.11000000
                                        reseaux   | hote

#### c) Plages d'adresses IP disponibles
- 1er sous-réseau: `200.211.102.1` à `200.211.102.62`
- 2ème sous-réseau: `200.211.102.65` à `200.211.102.126`
- 3ème sous-réseau: `200.211.102.129` à `200.211.102.190`
- 4ème sous-réseau: `200.211.102.193` à `200.211.102.254`

### 2. Utilisation du masque

#### Exemple 1: hôtes sur le même sous-réseau
- Source: `200.211.102.10`
- Destination: `200.211.102.16`
- Résultat ANDing:
  - **Source:** `200.211.102.0`
  - **Destination:** `200.211.102.0`
- Les hôtes sont sur **le même sous-réseau**.

#### Exemple 2: hôtes sur différents sous-réseaux
- Source: `200.211.102.10`
- Destination: `200.211.102.198`
- Résultat ANDing:
  - **Source:** `200.211.102.0`
  - **Destination:** `200.211.102.192`
- Les hôtes sont sur **deux sous-réseaux différents**.

Exemple 2: hôtes sur deux sous-réseaux différents
Hôtes considérés:
Source: 200.211.102.10
Destination: 200.211.102.198
Masque de sous-réseau utilisé:
255.255.255.192
Lorsque vous faites l'opération AND en utilisant le masque de sous-réseau, vous gardez la partie réseau inchangée et mettez la partie hôte à zéro.

Projet ANDING (en décimal):
Source: 200.211.102.10 avec Masque: 255.255.255.192
Pour obtenir l'adresse réseau (ID réseau):

Prenez chaque octet de l'adresse IP et faites un AND avec l'octet correspondant du masque.
Résultat:

Pour le premier octet: 200 AND 255 = 200
Pour le deuxième octet: 211 AND 255 = 211
Pour le troisième octet: 102 AND 255 = 102
Pour le quatrième octet: 10 AND 192 = 0
=> ID réseau: 200.211.102.0

Destination: 200.211.102.198 avec Masque: 255.255.255.192
Résultat:

Pour le premier octet: 200 AND 255 = 200
Pour le deuxième octet: 211 AND 255 = 211
Pour le troisième octet: 102 AND 255 = 102
Pour le quatrième octet: 198 AND 192 = 192
=> ID réseau: 200.211.102.192

Comparaison:
L'adresse réseau dérivée de l'adresse source est 200.211.102.0, tandis que l'adresse réseau dérivée de l'adresse de destination est 200.211.102.192.

Ces deux adresses réseau sont différentes, ce qui signifie que les adresses source et destination se trouvent dans deux sous-réseaux différents.

## Travail

### 1) Soit la classe d'adresses 200.200.100.0. On a besoin de créer au moins 12 sous-réseaux.

Nous avons commencé avec un masque de 255.255.255.0 qui, en binaire, est représenté par 11111111.11111111.11111111.00000000. Puisque nous avons besoin de 12 sous-réseaux, nous avons besoin de suffisamment de bits pour représenter ces sous-réseaux.

Pour trouver combien de bits sont nécessaires pour représenter un certain nombre de sous-réseaux, nous pouvons utiliser la formule : 
2"x >=12

x = 4 car 2"4 = 16 est le plus petit qui est >=12

a) **Le nombre de bits nécessaire pour identifier les réseaux :** 
   - 4 bits

b) **Le nombre de sous-réseaux possibles:** 
   - 16 sous-réseaux

c) **Le nombre de bits du masque :** 
   - 28 bits

   Le masque initial est de 24 bits (255.255.255.0). Ajoutons 4 bits pour les sous-réseaux : 24 + 4 = 28 bits
   8+8+8+4

d) **Le masque, en notation décimale pointée:** 
   - 255.255.255.240
   on prend le 4 bit et on rajouter 4 fois le 1 alors, 1111 et on remplie avec des 0 (8 bit en tout)
   Le nouveau masque en binaire est 11111111.11111111.11111111.11110000.

Cela se traduit en décimal par : 255.255.255.240

Réponse: 255.255.255.240

e) **Le nombre de bits pour les hôtes:** 
   - 4 bits

   Total de bits pour les adresses IP = 32 bits. En enlevant les bits du masque (28), cela donne : 32 - 28 = 4 bits

f) **Le nombre d’hôtes possibles par sous-réseau :** 
   - 14 hôtes
2 
x
 −2 (on retire 2 pour l'adresse réseau et l'adresse broadcast). Pour 4 bits, cela donne : 
2"4 −2=16−2=14
pour les bon 256 -240 = 16 et - 2 = 14


g) **Les identifiants des dix premiers sous-réseaux :** 



| Réseau | Identifiant réseau  | Plages d’adresses des hôtes        |
|--------|---------------------|-----------------------------------|
| 1      | 200.200.100.0       | 200.200.100.1 à 200.200.100.14    |
| 2      | 200.200.100.16      | 200.200.100.17 à 200.200.100.30   |
| 3      | 200.200.100.32      | 200.200.100.33 à 200.200.100.46   |
| 4      | 200.200.100.48      | 200.200.100.49 à 200.200.100.62   |
| 5      | 200.200.100.64      | 200.200.100.65 à 200.200.100.78   |
| 6      | 200.200.100.80      | 200.200.100.81 à 200.200.100.94   |
| 7      | 200.200.100.96      | 200.200.100.97 à 200.200.100.110  |
| 8      | 200.200.100.112     | 200.200.100.113 à 200.200.100.126 |
| 9      | 200.200.100.128     | 200.200.100.129 à 200.200.100.142 |
| 10     | 200.200.100.144     | 200.200.100.145 à 200.200.100.158 |

on enleve 2 reseaux   

Note: Les identifiants des réseaux augmentent par incréments de 16 (ou 2^4) car nous utilisons 4 bits pour les sous-réseaux. Les plages d'adresses des hôtes sont déduites du fait que nous avons 14 hôtes possibles par sous-réseau (comme calculé précédemment).

1.	Masque initial :
L'adresse donnée est de la classe C : 200.200.100.0. Les adresses de classe C ont un masque standard de 255.255.255.0, ce qui, en notation binaire, se traduit par 11111111.11111111.11111111.00000000.
Si nous comptons le nombre total de bits 1, cela donne : 8 bits (pour le premier octet) + 8 bits (pour le deuxième octet) + 8 bits (pour le troisième octet) = 24 bits. Donc, le masque initial a 24 bits.
2.	Pourquoi ajoutons-nous 4 bits au masque ?
Nous souhaitons diviser le réseau en sous-réseaux. Pour ce faire, nous convertissons certains des bits hôtes (les bits 0 du masque original) en bits de sous-réseau.
Dans cet exemple, nous avons besoin de 12 sous-réseaux. Le plus petit nombre de bits qui peut représenter 12 (ou plus) sous-réseaux est 4 bits (car 2^4 = 16). C'est pourquoi nous ajoutons 4 bits au masque original.


2f 256 -248 = 8 pour faire le f