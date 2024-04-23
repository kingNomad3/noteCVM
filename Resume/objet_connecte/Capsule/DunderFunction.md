# Méthodes Spéciales (Dunder Methods) en Python

## Méthodes de Cycle de Vie
- **`__new__`** : Appelé avant `__init__`, utilisé pour créer une nouvelle instance de la classe, notamment pour les classes immuables.
- **`__init__`** : Appelé après `__new__`, sert à initialiser l'instance de la classe.
- **`__del__`** : Appelé avant que l'instance de la classe ne soit supprimée. Son utilisation est déconseillée car le moment de son appel peut être imprévisible.

## Représentation des Objets
- **`__str__(self) -> str`** : Appelé par `print()` pour afficher l'objet de manière lisible par l'humain. Doit retourner une chaîne de caractères.
- **`__repr__(self) -> str`** : Appelé par `repr()` pour afficher l'objet. Doit retourner une chaîne de caractères qui pourrait être utilisée pour recréer l'objet (représentation plus technique).
- **`__format__(self, format_spec: str) -> str`** : Appelé par `format()` pour formater l'objet selon un spécificateur de format donné. Doit retourner une chaîne de caractères formatée.

## Opérations Mathématiques
- **`__int__(self) -> int`** : Convertit l'objet en un entier.
- **`__float__(self) -> float`** : Convertit l'objet en un flottant.
- **`__complex__(self) -> complex`** : Convertit l'objet en un complexe.
- **`__bool__(self) -> bool`** : Convertit l'objet en booléen.

## Opérations de Conteneur
- **`__eq__(self, other)`** : Définit le comportement pour l'égalité, `a == b`.
- **`__lt__(self, other)`** : Définit le comportement pour les comparaisons inférieures, `a < b`, utile pour le tri.
- **`__len__(self) -> int`** : Retourne la longueur de l'objet, utilisé par `len()`.

## Opérations sur les Séquences
- **`__iter__(self)`** : Rend l'objet itérable, utilisé par `iter()`.
- **`__next__(self)`** : Renvoie l'élément suivant de l'itérable, utilisé par `next()`. Doit lever `StopIteration` si il n'y a pas d'élément suivant.
- **`__reversed__(self)`** : Renvoie un itérable inversé de l'objet, utilisé par `reversed()`.

## Buffer Circulaire
- Concept de gestion de mémoire où, après avoir atteint la capacité maximale, les indices recommencent à zéro.
