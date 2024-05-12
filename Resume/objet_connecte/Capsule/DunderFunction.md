# Méthodes Spéciales (Dunder Methods) en Python

## Méthodes de Cycle de Vie
- **`__new__`** : Appelé avant `__init__`, utilisé pour créer une nouvelle instance de la classe, notamment pour les classes immuables.
- **`__init__`** : Appelé après `__new__`, sert à initialiser l'instance de la classe.
- **`__del__`** : Appelé avant que l'instance de la classe ne soit supprimée. Son utilisation est déconseillée car le moment de son appel peut être imprévisible.

```python
class MyClass:
    def __new__(cls, *args, **kwargs):
        print("__new__ called")
        return super().__new__(cls)

    def __init__(self, value):
        print("__init__ called")
        self.value = value

    def __del__(self):
        print("__del__ called")

# Utilisation :
obj = MyClass(10)
# Sortie :
# __new__ called
# __init__ called

del obj
# Sortie :
# __del__ called
```


## Représentation des Objets
- **`__str__(self) -> str`** : Appelé par `print()` pour afficher l'objet de manière lisible par l'humain. Doit retourner une chaîne de caractères.
- **`__repr__(self) -> str`** : Appelé par `repr()` pour afficher l'objet. Doit retourner une chaîne de caractères qui pourrait être utilisée pour recréer l'objet (représentation plus technique).
- **`__format__(self, format_spec: str) -> str`** : Appelé par `format()` pour formater l'objet selon un spécificateur de format donné. Doit retourner une chaîne de caractères formatée.

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Point({self.x}, {self.y})"

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

# Utilisation :
p = Point(3, 4)
print(str(p))   # Output: Point(3, 4)
print(repr(p))  # Output: Point(3, 4)
```

## Opérations Mathématiques
- **`__int__(self) -> int`** : Convertit l'objet en un entier.
- **`__float__(self) -> float`** : Convertit l'objet en un flottant.
- **`__complex__(self) -> complex`** : Convertit l'objet en un complexe.
- **`__bool__(self) -> bool`** : Convertit l'objet en booléen.
    
```python
class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __int__(self):
        return int(self.real)

    def __float__(self):
        return float(self.real)

    def __complex__(self):
        return complex(self.real, self.imaginary)

    def __bool__(self):
        return self.real != 0 or self.imaginary != 0

# Utilisation :
num = ComplexNumber(3, 4)

print(int(num))     # Output: 3
print(float(num))   # Output: 3.0
print(complex(num)) # Output: (3+4j)
print(bool(num))    # Output: True
```

## Opérations de Conteneur
- **`__eq__(self, other)`** : Définit le comportement pour l'égalité, `a == b`.
- **`__lt__(self, other)`** : Définit le comportement pour les comparaisons inférieures, `a < b`, utile pour le tri.
- **`__len__(self) -> int`** : Retourne la longueur de l'objet, utilisé par `len()`.

```python
class MyList:
    def __init__(self, data):
        self.data = data

    def __len__(self):
        return len(self.data)

    def __eq__(self, other):
        return self.data == other.data

    def __lt__(self, other):
        return len(self.data) < len(other.data)

# Utilisation :
list1 = MyList([1, 2, 3])
list2 = MyList([4, 5, 6])
list3 = MyList([1, 2, 3])

print(len(list1))    # Output: 3
print(list1 == list2) # Output: False
print(list1 == list3) # Output: True
print(list1 < list2)  # Output: True
``` 

## Opérations sur les Séquences
- **`__iter__(self)`** : Rend l'objet itérable, utilisé par `iter()`.
- **`__next__(self)`** : Renvoie l'élément suivant de l'itérable, utilisé par `next()`. Doit lever `StopIteration` si il n'y a pas d'élément suivant.
- **`__reversed__(self)`** : Renvoie un itérable inversé de l'objet, utilisé par `reversed()`.

```python
class MySequence:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.data):
            result = self.data[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration

    def __reversed__(self):
        return reversed(self.data)

# Utilisation :
seq = MySequence([1, 2, 3, 4, 5])

# Utilisation de __iter__ et __next__
for item in seq:
    print(item, end=" ")  # Output: 1 2 3 4 5

# Utilisation de __reversed__
reversed_seq = reversed(seq)
print(list(reversed_seq))  # Output: [5, 4, 3, 2, 1]
```

__getitem__
def __init__(self,values):
def__getitem__(self,value):
return self.__values[value+1]. 

a= A([1,2,3])
print(a=1)

#print true, false false

## Buffer Circulaire
- Concept de gestion de mémoire où, après avoir atteint la capacité maximale, les indices recommencent à zéro.
```python
from collections import deque

class CircularBuffer:
    def __init__(self, capacity):
        self.buffer = deque(maxlen=capacity)

    def append(self, item):
        self.buffer.append(item)

    def get_buffer(self):
        return list(self.buffer)

# Utilisation :
buffer = CircularBuffer(5)

buffer.append(1)
buffer.append(2)
buffer.append(3)
buffer.append(4)
buffer.append(5)

print(buffer.get_buffer())  # Output: [1, 2, 3, 4, 5]

buffer.append(6)
buffer.append(7)

print(buffer.get_buffer())  # Output: [3, 4, 5, 6, 7]
```
