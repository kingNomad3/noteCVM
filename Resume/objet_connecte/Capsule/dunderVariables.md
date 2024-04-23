# Dunder variable

- ce sont des variables que python contient qui stock de l'information en pausant des questions (tu es quoi?).

__name__ =  : c'est une variable disponible dans les fichiers, fonction et method  E
__doc__ = : c'est la que le docString est contenut  E
__file__ = : donne le nom du fichier ou l'element se trouve 
__dict__ = : possede l'infractruture de l'objet, relier a la classe lui meme, objet instance (tres important) E
__default__ = : slm pour les methodes et fonctions, c'est fait pour les callables, c'est un dictionnaire dans lequel ou nous avons les arugmenet et la valeur par defaut (ex: toto = 0) appartient a l'objet 
__kwdefault__ = :
__closure__ = : 
__class__ = : E


```python
"""doc test"""

class test:
    def __init__(self):
        """dosstring init """
        self.value = 0

    def test(self):
        """dostring test test """


print(Test.__doc__)
print(Test.test.__doc__)
t = Test()
print(t.__doc__) 
```

## Variables Dunder en Python

Les variables Dunder, également connues sous le nom de méthodes magiques ou spéciales, sont des variables prédéfinies en Python qui fournissent des fonctionnalités spécifiques. Elles sont encadrées par deux tirets bas (\_\_) et servent à diverses fins, telles que l'inspection, la personnalisation et la surcharge d'opérateurs.

### Variables Dunder Courantes :

1. __name__:
Utilisation: Disponible dans les modules, les fonctions et les classes.
But: Représente le nom du module ou de la fonction actuelle. Lorsqu'un fichier Python est exécuté directement, son __name__ est défini sur '__main__'.

```python 
# Exemple d'utilisation de __name__ dans un module

# main.py
def main():
    print("Ceci est le module principal.")

if __name__ == "__main__":
    main() # Affiche "Ceci est le module principal."
```

2. `__doc__`: 
   - **Utilisation**: Disponible dans les modules, les fonctions et les classes.
   - **But**: Contient la docstring associée au module, à la fonction ou à la classe. Les docstrings fournissent une documentation pour les éléments de code.

```python
# Exemple d'utilisation de __doc__ dans une fonction

def greet(name):
    """Fonction pour saluer une personne."""
    print(f"Bonjour, {name}!")

print(greet.__doc__) # Affiche "Fonction pour saluer une personne."
```

3. `__file__`: 
   - **Utilisation**: Disponible dans les modules.
   - **But**: Renvoie le chemin du fichier où le module est défini.

```python 
# Exemple d'utilisation de __file__ dans un module

import os

print("Chemin du fichier actuel:", os.path.abspath(__file__)) # Affiche "Chemin absolue du fichier actuel: /chemin/vers/le/fichier.py"
```

4. `__dict__`: 
   - **Utilisation**: Disponible dans les classes et les instances.
   - **But**: Contient l'espace de noms de l'objet, y compris ses attributs et ses méthodes. Essentiel pour l'inspection et l'accès dynamique aux attributs.

```python
# Exemple d'utilisation de __dict__ dans une classe

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person1 = Person("Alice", 30)
print(person1.__dict__) # Affiche "{'name': 'Alice', 'age': 30}"
```

5. `__defaults__`: 
   - **Utilisation**: Disponible dans les fonctions et les méthodes.
   - **But**: Stocke les valeurs par défaut des arguments pour les objets appelables. Utile pour manipuler les fonctions avec des paramètres optionnels.


# Exemple d'utilisation de __defaults__ dans une fonction

```python
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

print(greet.__defaults__) # Affiche "('Hello',)" car 'Hello' est la valeur par défaut de l'argument 'greeting'
```

6. `__kwdefaults__`: 
   - **Utilisation**: Disponible dans les fonctions et les méthodes.
   - **But**: Stocke les valeurs par défaut des arguments de mot-clé pour les objets appelables.

```python
# Exemple d'utilisation de __kwdefaults__ dans une fonction

def greet(name, greeting="Hello", *, punctuation="!"):
    print(f"{greeting}, {name}{punctuation}")

print(greet.__kwdefaults__) # Affiche "{'punctuation': '!'}" car '!' est la valeur par défaut de l'argument de mot-clé 'punctuation'
```


7. `__closure__`: 
   - **Utilisation**: Généralement utilisé dans les fonctions définies à l'intérieur d'autres fonctions (fonctions imbriquées).
   - **But**: Contient les variables locales de l'environnement englobant (enclosing) dans lequel la fonction a été définie. 

```python
# Exemple d'utilisation de __closure__ dans une fonction imbriquée

def outer_function(x):
    y = 10
    def inner_function():
        return x + y
    return inner_function

closure = outer_function(5).__closure__
if closure:
    print("Variables dans le __closure__ de inner_function:", [cell.cell_contents for cell in closure]) # Afficche "Variables dans le __closure__ de inner_function: [5, 10]"
else:
    print("Pas de __closure__.")
```

8. `__class__`: 
   - **Utilisation**: Disponible dans les instances.
   - **But**: Référence à la classe à partir de laquelle l'instance a été créée. Utile pour accéder aux attributs de classe à partir d'une instance.

```python
# Exemple d'utilisation de __class__ dans une instance

class Dog:
    def bark(self):
        print("Woof!")

dog = Dog()
print(dog.__class__)  # Affiche <class '__main__.Dog'> car dog est une instance de la classe Dog

```