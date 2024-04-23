# Docstring

## Introduction
    - Le docstring est une chaîne de caractères qui est utilisée pour documenter les fonctions, les classes et les méthodes.
    - Il est utilisé pour décrire ce que fait une fonction, comment elle fonctionne et ce que l'utilisateur doit savoir pour l'utiliser.
    - Le docstring est placé juste après la signature de la fonction, de la classe ou de la méthode, et est délimité par des triples guillemets.
        ex:
        
        ```python
        def ma_fonction():
            """Ce docstring décrit ce que fait la fonction."""
            pass
        ```
    - Le docstring est une chaîne de caractères multi-lignes, ce qui signifie que vous pouvez écrire autant de lignes que vous le souhaitez.
    - Il est recommandé d'utiliser le docstring pour documenter toutes les fonctions, classes et méthodes que vous écrivez.
    - Le dostring est assiers a une variable et peut etre appeler avec la fonction help()
        ex:
        ```python
        def ma_fonction():
            """Ce docstring décrit ce que fait la fonction."""
            pass

        help(ma_fonction)
        ```
    print(f.__doc__)

# dcotruring
Les docstrings peuvent être délimités par "", '', """ """, ''' ''', mais la convention est d'utiliser """ """.
La convention est d'utiliser une ligne pour les docstrings avec un point à la fin (WORO) selon le PEP 257.


## Exemple
```python   
def ma_fonction():
    """Ce docstring décrit ce que fait la fonction."""
    pass
```

 1. one liner
 2. detaille descriptif 
 3. detail technique
  exempele
    ```python
    def ma_fonction():
        """Ce docstring décrit ce que fait la fonction.
        Cette fonction fait ceci et cela.
        Elle utilise telle et telle technique pour faire son travail.
        """
        pass
    ```
4. des exemple d'utilisation
    ```python
    def ma_fonction():
        """Ce docstring décrit ce que fait la fonction.
        Cette fonction fait ceci et cela.
        Elle utilise telle et telle technique pour faire son travail.

        Exemples d'utilisation:
        ma_fonction()  # Renvoie None
        ma_fonction(1)  # Renvoie 1
        ma_fonction(2)  # Renvoie 4
        """
        pass
    ```

## DocTest
- Les doctests sont des tests écrits dans le docstring d'une fonction, d'une classe ou d'une méthode. Comme des test unitaire (ne sont pas des test unitaire)
- Les doctests sont écrits dans le docstring d'une fonction, d'une classe ou d'une méthode.
- Les doctests sont écrits dans le docstring d'une fonction, d'une classe ou d'une méthode.

ex:
```python
    def ma_fonction(a, b):
        """Renvoie la somme de a et b.

        Exemples d'utilisation:
        >>> ma_fonction(1, 2)
        3
        >>> ma_fonction(2, 3)
        5
        >>> ma_fonction(3, 4)
        7
        """
        return a + b
``` 

# demo 
