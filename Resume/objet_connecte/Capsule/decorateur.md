# Décorateurs 

@value.deleter 
@classmethode 
@staticmethod : retir le self, retir l'appel de l'objet self, on passe la classe 
@abstractclass 
@override : on peut aussi redefinir la doc string sinon il va prendre celle du parent 
@property.setter
@property.deleter
@functools.wraps

## @property: 
- Ce décorateur est utilisé pour définir des propriétés dans les classes Python. Lorsque vous utilisez @property avant une méthode, vous pouvez y accéder comme s'il s'agissait d'une propriété plutôt que d'une méthode. Il est souvent utilisé pour créer des méthodes d'accès (getters).

```python
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        self._radius = value

# Utilisation :
circle = Circle(5)
print(circle.radius)  # Appel de la méthode comme une propriété
circle.radius = 10    # Modification de la propriété à l'aide du setter
print(circle.radius)
```
## @property.setter : 
- Ce décorateur est utilisé pour définir la méthode setter d'une propriété définie à l'aide du décorateur @property. Il permet de définir le comportement lorsqu'une valeur est assignée à la propriété. Par exemple, si vous avez une propriété x définie avec @property, vous pouvez utiliser @x.setter pour définir une méthode qui sera appelée lorsque vous faites objet.x = valeur.
```python
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value <= 0:
            raise ValueError("Radius must be positive")
        self._radius = value

# Utilisation :
circle = Circle(5)
print(circle.radius)  # 5
circle.radius = 10    # Appel de la méthode setter
print(circle.radius)  # 10
circle.radius = -5    # ValueError: Radius must be positive
```


## @property.deleter : 
- Ce décorateur est utilisé pour définir la méthode de suppression d'une propriété définie à l'aide du décorateur @property. Il permet de définir le comportement lorsque la propriété est supprimée à l'aide de l'instruction del. Par exemple, si vous avez une propriété x définie avec @property, vous pouvez utiliser @x.deleter pour définir une méthode qui sera appelée lorsque vous faites del objet.x.
```python
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.deleter
    def radius(self):
        print("Deleting the radius property")
        del self._radius

# Utilisation :
circle = Circle(5)
print(circle.radius)  # 5
del circle.radius     # Appel de la méthode deleter
# Sortie : Deleting the radius property
```


## @functools.wraps : 

- Ce décorateur est utilisé pour conserver les métadonnées (telles que le nom de la fonction, la documentation, les annotations) d'une fonction définie à l'intérieur d'une autre fonction ou méthode. Lorsque vous créez un décorateur qui enveloppe une fonction existante, utiliser @functools.wraps garantit que les métadonnées de la fonction d'origine sont préservées. Cela est utile pour maintenir la lisibilité du code et garantir que les informations sur la fonction d'origine sont accessibles.
```python
import functools

def my_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("Something is happening before the function is called")
        result = func(*args, **kwargs)
        print("Something is happening after the function is called")
        return result
    return wrapper

@my_decorator
def say_hello():
    """A simple function that prints hello."""
    print("Hello!")

# Utilisation :
say_hello()
print(say_hello.__name__)         # Output: say_hello
print(say_hello.__doc__)          # Output: A simple function that prints hello.


```

## @value.deleter: 
- Ce décorateur est généralement utilisé avec le décorateur @property pour définir une méthode de suppression d'une propriété. Lorsque vous utilisez @value.deleter, vous définissez une méthode qui sera appelée lorsque vous utilisez l'instruction del pour supprimer la propriété.

```python
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.deleter
    def radius(self):
        del self._radius

# Utilisation :
circle = Circle(5)
del circle.radius  # Appel du deleter pour supprimer la propriété

```


## @classmethod: 
- Ce décorateur est utilisé pour définir des méthodes de classe en Python. Les méthodes de classe prennent un paramètre cls qui fait référence à la classe elle-même plutôt qu'à une instance de la classe. Elles peuvent être appelées soit sur la classe soit sur une instance de la classe.

```python
class Math:
    @classmethod
    def add(cls, x, y):
        return x + y

# Utilisation :
print(Math.add(5, 3))  # Appel de la méthode de classe sans instance

```


## @staticmethod: 
- Ce décorateur est utilisé pour définir des méthodes statiques en Python. Les méthodes statiques n'acceptent pas de référence à la classe ou à l'instance en tant que premier paramètre. Elles se comportent comme des fonctions ordinaires mais sont définies dans la classe à des fins d'organisation.

```python
class Math:
    @staticmethod
    def add(x, y):
        return x + y

# Utilisation :
print(Math.add(5, 3))  # Appel de la méthode statique sans instance ni classe

```

@abstractclass: Ce n'est pas un décorateur intégré à Python, mais il est couramment utilisé en conjonction avec les classes de base abstraites (ABC) du module abc. Les classes abstraites ne peuvent pas être instanciées et sont destinées à être sous-classées. Toute sous-classe d'une classe abstraite doit implémenter toutes les classes abstraites de la classe parente.

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

# Utilisation :
# Vous ne pouvez pas instancier une classe abstraite Shape directement
# Mais vous pouvez instancier une sous-classe concrète comme Circle
circle = Circle(5)
print(circle.area())

```