# Modèle de Conception : Factory Method

## Objectif
Le modèle de conception Factory Method définit une interface pour créer des objets mais permet aux sous-classes de modifier le type d'objets qui seront créés.

## Structure
1. **Produit** : Définit l'interface des objets créés par la méthode de fabrique.
2. **ProduitConcret** : Implémente l'interface Produit.
3. **Créateur** : Déclare la méthode de fabrique, qui retourne un objet de type Produit. Il peut également définir une implémentation par défaut de la méthode de fabrique qui retourne un objet ProduitConcret par défaut.
4. **CréateurConcret** : Remplace la méthode de fabrique pour retourner une instance de ProduitConcret.

## Diagramme UML

                  +--------------+
                  |   Créateur   |
                  +--------------+
                  | +methodeFabrique()|
                  +--------------+
                           |
                           v
              +----------------------+
              |  CréateurConcret     |
              +----------------------+
              | +methodeFabrique()   |
              +----------------------+
                           |
                           v
              +----------------------+
              |       Produit        |
              +----------------------+
              |                      |
              +----------------------+
                           |
            -------------------------
            |                       |
            v                       v
+---------------------+   +---------------------+
|  ProduitConcret1    |   |  ProduitConcret2    |
+---------------------+   +---------------------+


## Participants et Responsabilités
- **Produit** :
  - Définit l'interface des objets créés par la méthode de fabrique.
- **ProduitConcret** :
  - Implémente l'interface Produit.
- **Créateur** :
  - Déclare la méthode de fabrique, qui retourne un objet de type Produit.
- **CréateurConcret** :
  - Remplace la méthode de fabrique pour retourner une instance de ProduitConcret.
  
## Avantages
- Fournit un moyen simple de créer des objets sans exposer la logique de création.
- Permet la flexibilité en permettant aux sous-classes de modifier le type d'objets créés.
- Favorise la réutilisation du code et respecte le principe ouvert/fermé.

## desavantage
- Complexité accrue : L'ajout de nombreuses sous-classes pour chaque type de produit peut rendre la hiérarchie de classes complexe, ce qui peut rendre la maintenance et la compréhension du code plus difficiles.

- Abstraction supplémentaire : L'introduction d'une couche supplémentaire d'abstraction peut rendre le code plus difficile à comprendre pour les nouveaux développeurs qui ne sont pas familiers avec le modèle de conception Factory Method.

- Inflexibilité lors de la création de nouveaux produits : Si de nouveaux types de produits doivent être ajoutés, cela peut nécessiter la création de nouvelles sous-classes de créateurs, ce qui peut entraîner une surcharge de classes et une augmentation de la complexité.

- Difficulté à choisir la bonne méthode de création : Il peut être difficile de déterminer quelle méthode de création convient le mieux à une situation donnée, en particulier dans des systèmes complexes avec de nombreuses classes interdépendantes.

- Impact sur les performances : L'utilisation de méthodes de fabrication peut entraîner une surcharge de performances, en particulier dans les systèmes où la création d'objets est une opération fréquente et intensive.

## Exemple
Considérez un scénario où vous construisez une application de restaurant de pizza. Vous avez une classe Pizza comme Produit, avec des sous-classes représentant différents types de pizzas comme PizzaFromage et PizzaPepperoni. La classe PizzaStore agit comme le Créateur, avec des sous-classes telles que NYStylePizzaStore et ChicagoStylePizzaStore qui implémentent la méthode de fabrique pour créer des types spécifiques de pizzas.

## Conseils d'Implémentation
- Définissez une interface commune pour tous les produits pour garantir la cohérence.
- Envisagez d'utiliser un paramètre pour spécifier le type de produit à créer.
- Utilisez l'héritage et le polymorphisme pour permettre aux sous-classes de fournir des implémentations spécifiques de la méthode de fabrique.

## Quand Utiliser
- Utilisez le modèle de conception Factory Method lorsqu'une classe ne peut pas anticiper la classe des objets qu'elle doit créer.
- Utilisez lorsque vous souhaitez que les sous-classes spécifient les objets qu'elles créent.

En appliquant le modèle de conception Factory Method, vous pouvez obtenir plus de flexibilité dans la création d'objets et respecter davantage les principes d'encapsulation et d'abstraction.


## exemple
```python
from abc import ABC, abstractmethod

# Interface for shapes
class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass

# Concrete implementation of Shape for Circle
class Circle(Shape):
    def draw(self):
        return "Circle drawn"

# Concrete implementation of Shape for Square
class Square(Shape):
    def draw(self):
        return "Square drawn"

# Concrete implementation of Shape for Triangle
class Triangle(Shape):
    def draw(self):
        return "Triangle drawn"

# Factory for creating shapes
class ShapeFactory:
    @staticmethod
    def create_shape(shape_type):
        if shape_type == "circle":
            return Circle()
        elif shape_type == "square":
            return Square()
        elif shape_type == "triangle":
            return Triangle()
        else:
            raise ValueError("Invalid shape type")

# Client code
def draw_shape(shape_type):
    shape = ShapeFactory.create_shape(shape_type)
    return shape.draw()

# Example usage
print(draw_shape("circle"))    # Output: Circle drawn
print(draw_shape("square"))    # Output: Square drawn
print(draw_shape("triangle"))  # Output: Triangle drawn
```