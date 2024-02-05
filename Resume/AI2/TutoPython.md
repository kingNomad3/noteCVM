
# Tutoriel Python 3.x

## Introduction

- Pour ouvrir l'interprète Python, vous pouvez :
  - Trouver l'application dans le menu démarrer.
  - Utiliser la ligne de commande en tapant `python`.
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
- Division : `8 / 2` donne `4.0`

### Division entière et Modulo

- Division entière : `7 // 2` donne `3`
- Modulo (reste de la division) : `7 % 2` donne `1`

### Puissance

- `2 ** 3` donne `8`, ce qui représente 2 à la puissance 3.

## Variables et Types

### Affectation de variables

- `x = 10` assigne la valeur `10` à la variable `x`.

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

## Chaînes de caractères

### Création et manipulation

- Les chaînes de caractères sont entourées de guillemets simples ou doubles.
  ```python
  chaine1 = "Bonjour"
  chaine2 = 'Monde'
  ```

### Concaténation et Longueur

- Concaténation : `chaine1 + " " + chaine2` donne `"Bonjour Monde"`.
- Longueur : `len(chaine1)` donne `7`.

### Accès et Slicing

- Accès à un caractère : `chaine1[0]` donne `'B'`.
- Slicing : `chaine1[1:3]` donne `'on'`.

## Structures de données

### Listes

- Les listes sont des collections ordonnées et modifiables.
  ```python
  liste = [1, 2, 3, 4]
  liste.append(5)  # Ajoute 5 à la fin de la liste
  ```

### Dictionnaires

- Les dictionnaires stockent des données sous forme de paires clé-valeur.
  ```python
  dico = {'clé': 'valeur', 'Python': 3.8}
  ```

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

## Fonctions

- Définition et appel de fonctions pour réutiliser et organiser le code.
  ```python
  def ma_fonction():
      print("Bonjour Python")
  ma_fonction()  # Appelle la fonction
  ```

