Définitions de base:

Classe A : De 0 à 126 pour le premier octet. C'est-à-dire que si votre adresse commence par un nombre entre 0 et 126 inclusivement, elle est de classe A. (Veuillez noter que l'adresse 127.0.0.1 est réservée pour le loopback et n'est pas considérée comme une adresse de réseau standard de classe A.)


Classe B : De 128 à 191 pour le premier octet.

Classe C : De 192 à 223 pour le premier octet.

Classe D (pour la multidiffusion) : De 224 à 239 pour le premier octet.

Classe E (réservée) : De 240 à 255 pour le premier octet.

Classe A: 0xxx xxxx (Le premier bit est 0)

Classe B: 10xx xxxx (Les deux premiers bits sont 10)

Classe C: 110x xxxx (Les trois premiers bits sont 110)

Classe D (pour multidiffusion): 1110 xxxx

Classe E (pour recherche et usage expérimental): 1111 xxxx

Classe A : Le masque par défaut est 255.0.0.0
Classe B : Le masque par défaut est 255.255.0.0
Classe C : Le masque par défaut est 255.255.255.0

- Si vous devez diviser votre réseau en sous-réseaux plus petits, ajustez le masque pour allouer plus de bits à l'identifiant de réseau. Cela réduit le nombre d'hôtes possibles dans chaque sous-réseau.

- Par exemple, si vous avez une adresse de Classe C (masque par défaut 255.255.255.0) mais que vous souhaitez créer 4 sous-réseaux, vous auriez besoin de 2 bits supplémentaires pour le sous-réseau (car 2^2 = 4). Le masque serait alors modifié comme suit:

- 255.255.255.192 (où les deux derniers bits du troisième octet sont maintenant utilisés pour le sous-réseau)

# hote
Classe A : Peut supporter plus de 16 millions d'hôtes sur un seul réseau. C'est clairement excessif pour la plupart des réseaux, y compris le vôtre.

Classe B : Peut supporter jusqu'à 65 534 hôtes sur un seul réseau. C'est encore beaucoup plus que ce dont vous avez besoin.

Classe C : Peut supporter jusqu'à 254 hôtes sur un seul réseau.

🔹 Termes de Base

Hôte: Matériel ayant au moins une carte réseau (ex. station, imprimante, routeur).

Réseau: Ensemble d'hôtes connectés. Se décline en:

LAN: Réseau local (ex. d’une entreprise).
WAN: Réseau étendu composé de plusieurs LANs.

🔹 Adresses IP (IPv4)

Composition: 32 bits (4 octets). Exemple en binaire: 11000000 10101000 00000000 00000001 qui est équivalent à 192.168.0.1 en décimal.

Classes d'Adresses Principales:

Classe A: 1-126 (1er octet). Idéal pour grands réseaux.
Classe B: 128-191 (1er octet). Pour réseaux de taille moyenne.
Classe C: 192-223 (1er octet). Conçue pour petits réseaux.

🔹 Détails des Classes

Classe A:
Structure: 0xxxxxxx . xxxxxxxx . xxxxxxxx . xxxxxxxx
Adresses disponibles: 1.0.0.1 à 126.255.255.254
Adresses privées: 10.x.x.x
Classe B:
Structure: 10xxxxxx . xxxxxxxx . xxxxxxxx . xxxxxxxx
Adresses disponibles: 128.0.0.1 à 191.255.255.254
Adresses privées: 172.16.x.x à 172.31.x.x
Classe C:
Structure: 110xxxxx . xxxxxxxx . xxxxxxxx . xxxxxxxx
Adresses disponibles: 192.0.0.1 à 223.255.255.254
Adresses privées: 192.168.x.x

🔹 Masques de Sous-réseau

Permettent de séparer les portions réseau et hôte d'une adresse.

Classe A: 255.0.0.0

Classe B: 255.255.0.0

Classe C: 255.255.255.0


Adresses non attribuables à un hôte

Adresse 0: utilisée pour représenter le réseau lui-même (ex: 10.0.0.0 en classe A).

Adresse de Broadcast: utilisée pour envoyer des messages à tous les hôtes du réseau. Pour la Classe A, ce serait x.255.255.255; 
pour la Classe B, x.x.255.255; et 
pour la Classe C, x.x.x.255.

Ici aussi on doit retirer deux adresses : 
•	D’abord l’hôte 0  (Adresse dont le dernier nombre est  = à 0)(ex : 195.0.0.0).
Aucun hôte ne peut avoir le numéro zéro, car on utilise cette notation pour désigner le réseau

•	Ensuite, l’hôte 255 (bits du  dernier octet = à 1)
Ex : 132.255.255.255
Cette adresse IP est utilisée pour la diffusion générale (broadcast) c’est –à-dire pour envoyer un message destiné à tous les hôtes du réseau

Adresse de Loopback: 127.0.0.1 utilisée pour des tests locaux sur l'hôte.

🔹 Opération ANDing

Utilisé pour déterminer si deux adresses sont sur le même réseau.

Méthode:

Effectuer un ET logique entre l'adresse source et le masque.
Répéter pour l'adresse de destination.
Si les deux résultats sont identiques, les adresses sont sur le même réseau.


Classe	
Valeur de w1	Partie affectée à ID de réseau	Partie affectée à ID de l'hôte	Nombre de réseaux disponibles	Nombre d'hôtes disponibles par réseau
A	1–126	w	x.y.z	126	16,777,214
B	128–191	w.x	y.z	16,384	65,534
C	192–223	w.x.y	z	2,097,152	254


🔹 Exemples de ANDing

Si vous avez deux adresses comme 192.59.66.200 et 192.59.66.17 avec un masque de 255.255.255.0, l'opération ANDing vous aidera à déterminer si elles sont sur le même réseau.

Pour déterminer la valeur décimale de `11111001` en binaire:

`11111001` =  
= (1 × 2^7)  
+ (1 × 2^6)  
+ (1 × 2^5)  
+ (1 × 2^4)  
+ (1 × 2^3)  
+ (0 × 2^2)  
+ (0 × 2^1)  
+ (1 × 2^0)  
= 128 + 64 + 32 + 16 + 8 + 0 + 0 + 1  
= 249


Quelle est la valeur binaire de `225` en base 10?


**Solution:**  
Pour convertir `225` en binaire:

\(225 \div 2 = 112\) reste \(1\)  
\(112 \div 2 = 56\)  reste \(0\)  
\(56 \div 2 = 28\)   reste \(0\)  
\(28 \div 2 = 14\)   reste \(0\)  
\(14 \div 2 = 7\)    reste \(0\)  
\(7 \div 2 = 3\)     reste \(1\)  
\(3 \div 2 = 1\)     reste \(1\)  
\(1 \div 2 = 0\)     reste \(1\)

Lisez les restes de bas en haut : `11100001`

Convertir 255 en binaire:

255 en base 10 est équivalent à 11111111 en base 2.
Convertir 0 en binaire:

0 en base 10 est équivalent à 00000000 en base 2.
Ainsi, en utilisant ces conversions, le masque 255.255.255.0 en décimal devient:

11111111.11111111.11111111.0000000

Table de vérité pour le ANDING
	    0(faux)	1 (vrai)
0 (faux)	0	    0
1 (vrai)	0	    1

Adresse IP de l’hôte X: 200.46.12.15
Masque: 255.255.255.0

ANDing pour l'hôte X :

200 AND 255
Chaque nombre dans sa forme binaire avec 255 donnera le même nombre. Donc, 200 reste 200.
Résultat : 200

46 AND 255
De la même façon, 46 "ET" 255 restera 46.
Résultat : 46

12 AND 255
Encore une fois, 12 "ET" 255 restera 12.
Résultat : 12

15 AND 0
Tout nombre "ET" 0 donnera toujours 0. Donc, 15 devient 0.
Résultat : 0

Adresse ANDing pour l'hôte X : 200.46.12.0

Adresse IP de l’hôte Y: 200.46.12.120
Masque: 255.255.255.0

ANDing pour l'hôte Y :

200 AND 255
Comme avant, 200 reste 200.
Résultat : 200

46 AND 255
De même, 46 reste 46.
Résultat : 46

12 AND 255
Encore une fois, 12 reste 12.
Résultat : 12

120 AND 0
120 "ET" 0 donnera 0.
Résultat : 0

Adresse ANDing pour l'hôte Y : 200.46.12.0