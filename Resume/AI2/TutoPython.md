
# Tutoriel Python 3.x

## Introduction

- Pour ouvrir l'interprète Python, vous pouvez :
  - Trouver l'application dans le menu démarrer.
  - Utiliser la ligne de commande en tapant `idl`.
  - Utiliser IDLE, l'environnement de développement intégré pour Python.

### Commentaires

- Les commentaires en Python commencent par `#` et s'étendent jusqu'à la fin de la ligne, par exemple :
  ```python
  # Ceci est un commentaire
  ```

## Utiliser Python comme une calculatrice

### Opérations arithmétiques

- Addition : `3 + 2` donne `5`
- Soustraction : `5 - 3` donne `2`
- Multiplication : `2 * 3` donne `6`
- Division : `8 / 2` donne `4.0` la fraction n'est pas perdu 

### Division entière et Modulo

- Division entière : `7 // 2` donne `3`
- Modulo (reste de la division) : `7 % 2` donne `1`

*Attention* le plancher est toujours la valeur inférieur



### Puissance

- `2 ** 3` donne `8`, ce qui représente 2 à la puissance 3.

## Variables et Types

### Affectation de variables

- `x = 10` assigne la valeur `10` à la variable `x`.
- `x = y =z = 0` ils seront tous assigné à 0


### Types de données

- Entiers (`int`), nombres à virgule flottante (`float`), chaînes de caractères (`str`).
  ```python
  entier = 10  # int
  flottant = 10.5  # float
  chaine = "Texte"  # str
  ```

### Conversion de types

- Convertir un flottant en entier : `int(10.5)` donne `10`.
- Convertir un entier en flottant : `float(10)` donne `10.0`.
- Convertir une valeur en chaîne de caractères : `str(10)` donne `"10"`.
- int(3*3.75/1.5) donne 7
- flaot(8//5) donne 1.0

### type mélangé
- 3 * 3.75 /1.5 donne 7.5 
- 7.0 /2 donne 3.5

- Une convertion automatique en flaot 

## round
- round(6.6) = 7 ''

## Math
```python
import math
math.sqrt(4)
# 2.0
math.pow(2,3)
#8.0
```

## Chaînes de caractères

### Création et manipulation

- Les chaînes de caractères sont entourées de guillemets simples ou doubles.
  ```python
  chaine1 = "Bonjour"
  chaine2 = 'Monde'
  ```

chaine3 = "Le caractère backslash (\) est utilisé pour échapper des caractères spéciaux dans une chaîne de caractères."

chaine4 = 'Il peut également introduire des séquences spéciales, telles que \\n pour une nouvelle ligne ou \\t pour une tabulation.'

chaine = "L'apostrophe peut être incluse dans une chaîne en utilisant des guillemets doubles."

chaine = 'L\'apostrophe peut être incluse dans une chaîne en utilisant un caractère d\'échappement.'

### Triple apostrophes ou guillemets
Afin d'éviter d'utiliser le symbole antislash (backslash) pour échapper à la fin de ligne, on peut utiliser trois apostrophes ou trois guillemets.

Cette méthode conserve les espaces blancs saisis lors de l’entrée de la chaîne.
Et, comme on a vu précédemment, si on n’assigne pas à une variable, rien ne se produit.
On peut donc l’utiliser pour faire des commentaires multilignes.

```python 
chaine_multiligne = '''
Ceci est une chaîne de caractères
sur plusieurs lignes.
Elle conserve les espaces blancs
et les retours à la ligne.
'''
chaine_multiligne = """
Ceci est une autre chaîne de caractères
sur plusieurs lignes.
Elle conserve également les espaces blancs
et les retours à la ligne.
"""
```

### Concaténation et Longueur

- Concaténation : `chaine1 + " " + chaine2` donne `"Bonjour Monde"`.
- Longueur : `len(chaine1)` donne `7`.



### Accès et Slicing
- 'mot'[0] donne 'm'
- chain = 'mot' 
- Accès à un caractère : `chaine1[0]` donne `'m'`.

- chaine = 'abcdefghi'
- Slicing : `chaine1[2:4]` donne `'cd'`.
  `chaine1[0:5]` donne `'abcde'`
  `chaine1[:2]` donne `'ab'`
  `chaine1[:]` donne tout la chaine
  `chaine1[0:10000]` donne tout la chaine
  `chaine1[10:]` donne ' ' 
  `chaine1[2:1]` donne ' ' 

  `chaine1[-1]` donne `'i'`
  `chaine1[-2]` donne `'h'`
  `chaine1[-2:]` donne `'hi'`
  `chaine1[-2:]` donne tout a par les deux derniere lettre
  `chaine1[-100:]` donne tout la chaine
  `chaine1[:-100]` donne tout la chaine

### fonction
- Len(chaine)
- chaine[len(chaine) -2] donne 'h'


## Structures de données

### Listes

- Les listes sont des collections ordonnées et modifiables.
  ```python
  liste = [1, 2, 3, 4]
  liste.append(5)  # Ajoute 5 à la fin de la liste
  ```

  l = [1,2,3] + [1,2,3]
  [1,2,3 ] *2 

  Les deux listes font un reference vers le meme objet alors si on change une on changera l'autre

```python
  for i in range(2):
    l.append([])
    for j in range(5):
      l[-1].append(0)
```
### Tuples ------------------------------------------

creer un tuples
t =1,2,3


### Dictionnaires

- Les dictionnaires stockent des données sous forme de paires clé-valeur.
  ```python
  dico = {'clé': 'valeur', 'Python': 3.8}
  ```

acceder a la valeur 
d = ("prenom:'toto', 'nom: 'tata')

d["prenom"]
cle = "prenom"
d[cle]
  toto

### exercice
d = {'1':'1', '65': '2', '87': '3','211': '4','-6': '5', '0': '6'}


## Structures de contrôle

### Instructions conditionnelles

- Utilisation de `if`, `elif`, `else` pour exécuter des blocs de code conditionnellement.
  ```python
  if x > 0:
      print("x est positif")
  elif x == 0:
      print("x est zéro")
  else:
      print("x est négatif")
  ```

### Boucles

- `for` pour itérer sur les éléments d'une séquence.
- `while` pour répéter un bloc tant qu'une condition est vraie.
  ```python
  for i in range(5):
      print(i)
  ```
nbLapin = 0
n1 = 0
n2 = 0

  for i in range(18):
    print(n1)
    nbLapin = n1 + n2
    n1 = n2
    n2 = nbLapin
    n1 = n1 + 1




## Fonctions

- Définition et appel de fonctions pour réutiliser et organiser le code.
  ```python
  def ma_fonction():
      print("Bonjour Python")
  ma_fonction()  # Appelle la fonction
  ```

