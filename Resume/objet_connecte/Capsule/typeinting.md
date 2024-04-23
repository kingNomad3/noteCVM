# Annotations de Type en Python

La raison pk on a des types dans les codes comme int ou string, c'est un moyen d'aider les developpeur a deboger nos code
par exemple le code attendait un int mais un string lui a ete donner

### Annotations de Type Basiques
- Objectif : Les annotations de type aident les développeurs à déboguer le code en spécifiant les types attendus.

from types import NoneType
None est comme true or false est un NoneType, n'est pas un type None est une instance de NoneType et NonType est un type


### Variables Dunder Intégrées
- defaults : Contient les valeurs par défaut des arguments de fonction.
- annotations : Stocke les annotations de type.
- NoneType : Importé depuis types, None est une instance de NoneType. Contrairement à None, qui n'est pas un type, NoneType est un type.
```python
from types import NoneType

def check_type(value):
    if isinstance(value, NoneType):
        print("La variable est de type None.")
    else:
        print("La variable n'est pas de type None.")

# Exemples d'utilisation
check_type(None)  # Affiche: La variable est de type None.
check_type(10)    # Affiche: La variable n'est pas de type None.
check_type("hello")  # Affiche: La variable n'est pas de type None.
```

### Annotations de Type (Python 3.9+) :
- L'argument values de la fonction scan_moy est annoté avec le type List[float], ce qui signifie qu'il s'attend à recevoir une liste de nombres à virgule flottante en entrée.

```python
#<3.9
nl: List[int] = [1, 2, 3]
n2: Tuple[int, str, float] = (1, "allo", 3.14)
n3: Dict[int, str] = {1: "allo"}

def scan_moy(values: List[float]) -> Tuple[float, float]:
    # ...
```

### Annotation de Type pour une Variable 
### Annotation de Type pour les Paramètres de Fonction 
### Annotation de Type de Retour de Fonction 
- La variable vit est annotée avec le type float.
- Le type de retour de la fonction my_function est annoté avec le type None.
-  Les paramètres vit et v2 de la fonction my_function sont annotés avec les types int et str respectivement.
```python
vit: float = Allo()
    hint

def(vit:int,v2:str='') -> None:
```

###  Annotation de type Any : permet de définir un paramètre pouvant être de n'importe quel type
- En assignant différentes valeurs à a, nous démontrons sa polyvalence pour contenir des valeurs de types variés, y compris des entiers, des flottants, des instances d'objets et des chaînes de caractères.
```python
from typing import Any

a: Any = 1  # La variable a peut être de type int
a = 3.14    # Maintenant, la variable a peut être de type float
a = Tower() # La variable a peut être une instance de la classe Tower
a = "allo"  # La variable a peut être une chaîne de caractères
```

### Annotation de type Union : permet de spécifier que le type peut être soit un int, soit un float
- Nous utilisons l'annotation de type Union[int, float] pour indiquer que la variable nombre peut être soit un entier, soit un flottant.
- En attribuant des valeurs à nombre, nous démontrons sa capacité à être de l'un ou l'autre type spécifié dans l'union, en l'occurrence un entier puis un flottant.
```python
# < 3.10
from typing import Union

nombre: Union[int, float] = 3  # La variable nombre peut être soit un entier, soit un flottant

nombre = 3.14  # Maintenant, la variable nombre est un flottant
```

### Annotation de types d'Union et types optionnels (à partir de Python 3.10)
- Nous utilisons l'annotation de type Union[int, float] pour indiquer que la variable nombre peut être soit un entier, soit un flottant.
- Nous utilisons également l'annotation de type Optional[int] pour indiquer que la variable value peut être soit un entier, soit None, ce qui signifie qu'elle est optionnelle.
# 3.10
```python
from typing import Union, Optional

nombre: Union[int, float] = 3  # La variable nombre peut être soit un entier, soit un flottant
value: Optional[int] = None  # La variable value peut être soit un entier, soit None (c'est-à-dire optionnel)

```
### Annotation de type Callable : permet de définir des types de fonctions
- Nous utilisons l'annotation de type Callable[[int, float], complex] pour indiquer que la variable task est une fonction prenant un entier et un flottant en entrée et renvoyant un complexe en sortie.
- Nous utilisons la fonction callable() pour vérifier si la fonction f est appelable.
```python
from typing import Callable

def f(i: int, r: float) -> complex:
    # Corps de la fonction
    pass

task: Callable[[int, float], complex] = f  # La variable task est annotée comme une fonction prenant un int et un float en entrée et renvoyant un complexe en sortie

is_callable = callable(f)  # La fonction callable() vérifie si f est appelable (c'est-à-dire si f est une fonction)

```


# Annotation de type Iterable : spécifie que la fonction accepte un itérable contenant des entiers ou des flottants

```python
from typing import Iterable

def show(values: Iterable[int | float]):
    # Parcourt tous les éléments de l'itérable
    for v in values:
        # Affiche la valeur actuelle diminuée de 3
        print(v - 3)
```

### Alias de type : spécifie un alias pour un type de données spécifique
- Nous utilisons l'alias de type DataQty pour spécifier une liste pouvant contenir des entiers ou des flottants.
- Les variables qt1 et qt2 sont annotées comme des listes de type DataQty, ce qui signifie qu'elles peuvent contenir des entiers ou des flottants.
```python
# 1
#aliace de type
Data qty = list[int|float]

qt1: list[int|float] = [1,2,3]
qt2:     = [3,5]
```

### Types Littéraux (Python 3.8+)
- Objectif : Définit des variables avec une valeur littérale spécifique.
- Nous utilisons l'annotation de type Literal['red', 'green', 'blue'] pour spécifier que la variable var ne peut contenir que les valeurs littérales 'red', 'green' ou 'blue'.
```python
from typing import Literal

var: Literal['red', 'green', 'blue'] = 'red'  # La variable var est annotée pour contenir seulement les valeurs 'red', 'green' ou 'blue'
```

### Déclarations Anticipées (Python 3.7)
-  Résout les dépendances circulaires entre les classes ou les fonctions.
Exemple :
```python
# Déclarations Anticipées (Python 3.7+)
# Résout les dépendances circulaires entre les classes ou les fonctions.

# Exemple avec une classe Tower qui référence une autre instance de Tower dans sa méthode compare
class Tower:
    def compare(other: 'Tower') -> bool:
        ...

# En utilisant la syntaxe 'Tower' entre guillemets simples, nous permettons au compilateur de comprendre que Tower sera défini plus tard.

# Exemple avec des fonctions qui se référencent mutuellement
class A:
    def f() -> 'B':
        ...

class B:
    def g() -> None:
        ...

# Dans cet exemple, la méthode f de la classe A retourne une instance de la classe B, mais la classe B est définie après la classe A.
# En utilisant la syntaxe 'B', nous indiquons au compilateur que B sera défini plus tard.

# Nouveauté dans les futures versions de Python
from __future__ import annotations

# Avec cette importation, les annotations de type ne nécessitent plus les guillemets simples pour les références anticipées.

# Exemple :
class A:
    def f() -> B:
        ...

class B:
    def g() -> A:
        ...

# Dans cet exemple, nous n'avons plus besoin des guillemets simples autour de B dans la méthode f de A car nous avons importé __future__.annotations.


```




### Vérification de Type dans les Importations Conditionnelles
- Objectif : Permet les importations conditionnelles à des fins de vérification de type.
```python
# Vérification de Type dans les Importations Conditionnelles

# Permet les importations conditionnelles à des fins de vérification de type.

# Exemple :

# Dans le fichier a.py
from typing import TYPE_CHECKING

# Si nous sommes en train de vérifier le type, nous importons la classe B depuis le fichier b.py
if TYPE_CHECKING:
    from b import B

# Définition de la classe A
class A:
    def f() -> B:
        ...

# Dans ce fichier, nous importons la classe B depuis le fichier b.py uniquement à des fins de vérification de type.
# Cela permet d'éviter les importations cycliques tout en fournissant des annotations de type correctes.

# Dans le fichier b.py
from typing import TYPE_CHECKING

# Si nous sommes en train de vérifier le type, nous importons la classe A depuis le fichier a.py
if TYPE_CHECKING:
    from a import A

# Définition de la classe B
class B:
    def f(v: 'B') -> 'A':
        return v

# Comme dans le fichier a.py, nous importons la classe A depuis le fichier a.py uniquement à des fins de vérification de type.

# Cette technique permet de résoudre les problèmes d'importations cycliques tout en fournissant des annotations de type précises.



```


### Note Personnelle : Typage Avancé
- Dans Python, le typage avancé offre des fonctionnalités supplémentaires pour définir des types plus spécifiques et complexes. Voici quelques concepts de typage avancé :
## NewType
- Permet de créer de nouveaux types basés sur des types existants pour améliorer la lisibilité et la maintenabilité du code.
- Utile pour créer des alias de types avec des noms plus explicites.
```python
from typing import NewType

UserID = NewType('UserID', int)
```

## TypeVar
- Utilisé pour définir des variables de type générique et pour annoter des fonctions avec des types génériques.
- Permet d'exprimer des contraintes entre les types et d'assurer la cohérence du typage.
```python
from typing import TypeVar

T = TypeVar('T')
```

## Annonated
- Permet d'ajouter des métadonnées ou des annotations aux variables et aux fonctions.
- Utile pour fournir des informations supplémentaires sur les types ou les données.
```python
from typing import Annotated

age: Annotated[int, "Age of the person"]
```

## Generic
- Utilisé pour définir des classes ou des fonctions génériques pouvant fonctionner avec différents types de données.
- Permet de créer des structures de données flexibles et réutilisables.
```python
from typing import Generic, TypeVar, Iterable

T = TypeVar('T')

class Stack(Generic[T]):
    def __init__(self):
        self.items: list[T] = []

    def push(self, item: T):
        self.items.append(item)

    def pop(self) -> T:
        return self.items.pop()

    def is_empty(self) -> bool:
        return len(self.items) == 0
```




