# Tests Unitaires en Python

- Les tests unitaires sont une pratique essentielle dans le développement logiciel qui consiste à vérifier le bon fonctionnement des parties individuelles (unités) d'un programme. En Python, le module unittest fournit un ensemble d'outils pour écrire et exécuter des tests unitaires.

## Écriture de Tests Unitaires avec unittest :

```python
#Importation du Module :
import unitest

# Création d'une Classe de Test :
#Les tests unitaires sont écrits sous forme de méthodes dans des classes de test. Chaque méthode de test doit commencer par le préfixe test_.
class TestMyCode(unittest.TestCase):
    def test_addition(self):
        # Écrire le test pour la fonction d'addition
        pass

# Utilisation des Méthodes d'Assertion :
# Les méthodes d'assertion sont utilisées pour vérifier si les résultats attendus correspondent aux résultats réels de l'exécution du code testé.
# Voici quelques-unes des méthodes d'assertion les plus couramment utilisées :
# assertEqual(a, b): Vérifie si a est égal à b.
# assertTrue(x): Vérifie si x est vrai.
# assertFalse(x): Vérifie si x est faux.
# assertRaises(exception, callable, *args, **kwargs): Vérifie si l'appel à callable(*args, **kwargs) lève une exception de type exception.""""

class TestMyCode(unittest.TestCase):
    def test_addition(self):
        result = addition(3, 5)
        self.assertEqual(result, 8)

# Exécution des Tests :
# Pour exécuter les tests, utilisez la fonction unittest.main().
if __name__ == '__main__':
    unittest.main()
```

- Dans cet exemple, le test vérifie si l'addition de 3 et 5 donne 8. Si tous les tests réussissent, aucune sortie ne sera affichée. Sinon, des messages d'échec seront affichés pour les tests qui ont échoué.
```python
import unittest

def addition(a, b):
    return a + b

class TestAddition(unittest.TestCase):
    def test_addition(self):
        result = addition(3, 5)
        self.assertEqual(result, 8)

if __name__ == '__main__':
    unittest.main()
```

### autre exemples
```python
class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Division by zero is not allowed.")
        return a / b


import unittest

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_addition(self):
        self.assertEqual(self.calc.add(3, 5), 8)

    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(8, 4), 4)

    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(2, 3), 6)

    def test_division(self):
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertRaises(ValueError, self.calc.divide, 10, 0)

if __name__ == '__main__':
    unittest.main()
```
- Nous avons défini une classe TestCalculator qui hérite de unittest.TestCase.
- Nous avons utilisé la méthode setUp() pour instancier un objet Calculator avant chaque test.
- Nous avons écrit quatre méthodes de test, chacune testant une méthode différente de la classe Calculator.
- Les méthodes de test utilisent les méthodes d'assertion de unittest pour vérifier si les résultats des opérations sont corrects.
- Enfin, nous exécutons les tests avec unittest.main().
- Cet exemple illustre comment écrire des tests unitaires pour une classe Python avec unittest. Chaque méthode de test isole une unité de code et vérifie son comportement attendu.