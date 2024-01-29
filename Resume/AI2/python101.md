import re
# ceci est un commentaire
x =2 # commentarie
x = y = z = 5



• Exercices
(-b +/- math.sqrt(b**2 - 4*a*c)) / (2 * a)
ou
a= -5.6
b = 31.1
c= 9-2
-b+(b**2 -4*a*c)**(1/2))/(2a)

1. 4x2 + 17x - 1 = 0, x = ?
(-17+math.sqrt(17**2-4*4*-1))/2*4
0.9284983931459578

2. -5.6x2 + 31.1x + 9 = 2, x = ?
(-31.1 + math.sqrt(31.1**2 - 4*-5.6*7)) / (2 * -5.6)
-0.21663021121832812

3. 8x2-1265.789x = 0, x = ?

4. L'aire d'un cercle ayant pour diamètre 3.64m
(indice, utilisez math.pi)
    - import math 
    - y = 4*math.pi * (x/2)**2
5. L'aire extérieur d’un prisme rectangulaire aux
dimensions suivantes: 4.5cm, 7cm, 12.75cm.

largeur = 7
longueyr = 4.5
hauteur = 12.75

2(longueur*largeur) +2* (longueur*hauteur) + 2*(largeur * hauteur)

6. Volume d'un tipi ayant un rayon de 2.176 m et
une hauteur de 3.5m.
(math.pi *2.176**2 *3.5)/3
17.35459345261132

# Chaine
    - sois guillemet simple ou double 

'je suis "stupide" '


• Exercices
1. Trouvez comment inverser une chaîne.

>>> text = "allo" [::-1]
>>> print(text)
2. Si on a des variables dont on veut insérer les
valeurs dans une chaîne formatée, python
nous permet de le faire, comment?

>>> test = 'une valeur de %s'
>>> x = ' une string %s avec '
>>> y = "valeur"
>>> x % test % y
' une string une valeur de valeur avec '
>>> 

3. Comment isoleriez-vous la chaîne « les » à
partir de la chaîne « Allo les amis ! »?
