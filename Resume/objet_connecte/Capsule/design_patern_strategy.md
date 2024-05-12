# Modèle de Conception : Strategy

## But
Le modèle de conception Strategy permet de définir une famille d'algorithmes, encapsuler chacun d'eux et les rendre interchangeables. Les algorithmes peuvent varier indépendamment des clients qui les utilisent.

## Structure
1. **Contexte** : Il est l'objet qui a une référence vers un objet Stratégie et qui délègue à cet objet l'exécution de l'algorithme.
2. **Stratégie** : Interface définissant la méthode à utiliser pour l'exécution de l'algorithme.
3. **StratégieConcrète** : Implémente l'algorithme spécifique à utiliser dans un contexte donné.

## Diagramme UML
                  +--------------+
                  |   Contexte   |
                  +--------------+
                  | -strategie: Stratégie |
                  +--------------+
                  | +executerAlgorithme()|
                  +--------------+
                           |
                           v
              +----------------------+
              |     Stratégie        |
              +----------------------+
              | +executerAlgorithme()|
              +----------------------+
                           ^
                           |
      +--------------------+-------------------+
      |                    |                   |
      +------------------+ +------------------+ +------------------+
      | StratégieConcrète1| | StratégieConcrète2| | StratégieConcrète3|
      +------------------+ +------------------+ +------------------+
      | +executerAlgorithme()| | +executerAlgorithme()| | +executerAlgorithme()|
      +------------------+ +------------------+ +------------------+
  

## Participants et Responsabilités
- **Contexte** :
  - Possède un objet Stratégie et délègue à cet objet l'exécution de l'algorithme.
- **Stratégie** :
  - Définit une interface commune pour tous les algorithmes supportés.
- **StratégieConcrète** :
  - Implémente l'algorithme spécifique à utiliser dans un contexte donné.

## Avantages
- Permet de changer dynamiquement le comportement d'un objet en fonction du contexte ou des besoins du client.
- Encourage la modularité et la réutilisation du code en séparant les algorithmes des objets qui les utilisent.

## Exemple
Supposons que nous ayons une application de tri de listes. Nous pouvons utiliser le modèle de conception Strategy pour permettre à l'utilisateur de choisir différents algorithmes de tri tels que le tri à bulles, le tri rapide ou le tri fusion.

## Conseils d'Implémentation
- Utilisez le modèle de conception Strategy lorsque vous avez plusieurs algorithmes similaires et que vous souhaitez les encapsuler pour les rendre interchangeables.
- Assurez-vous que les classes StratégieConcrète sont indépendantes des autres et peuvent être utilisées sans modifications.

## Quand Utiliser
- Utilisez le modèle de conception Strategy lorsque vous souhaitez éviter la duplication de code en encapsulant les algorithmes qui peuvent varier.
- Utilisez lorsque vous avez besoin de plusieurs variantes d'un algorithme et que vous souhaitez les utiliser dynamiquement à l'exécution.

En utilisant le modèle de conception Strategy, vous pouvez rendre votre code plus flexible, extensible et maintenable en séparant les algorithmes des objets qui les utilisent.


## exemple
```python
from abc import ABC, abstractmethod

# Contexte : La classe qui a une référence à un objet Stratégie et délègue à cet objet l'exécution de l'algorithme
class Contexte:
    def __init__(self, strategie):
        self._strategie = strategie

    def executer_strategie(self):
        return self._strategie.executer()

# Stratégie : Interface définissant la méthode à utiliser pour l'exécution de l'algorithme
class Strategie(ABC):
    @abstractmethod
    def executer(self):
        pass

# Stratégie Concrète 1 : Implémente un algorithme spécifique à utiliser dans un contexte donné
class StrategieConcrète1(Strategie):
    def executer(self):
        return "Exécution de la Stratégie Concrète 1"

# Stratégie Concrète 2 : Implémente un autre algorithme spécifique à utiliser dans un contexte donné
class StrategieConcrète2(Strategie):
    def executer(self):
        return "Exécution de la Stratégie Concrète 2"

# Code Client
if __name__ == "__main__":
    # Créer un Contexte avec une stratégie spécifique
    contexte = Contexte(StrategieConcrète1())

    # Exécuter la stratégie
    print(contexte.executer_strategie())  # Sortie: Exécution de la Stratégie Concrète 1

    # Changer la stratégie du contexte
    contexte = Contexte(StrategieConcrète2())

    # Exécuter la nouvelle stratégie
    print(contexte.executer_strategie())  # Sortie: Exécution de la Stratégie Concrète 2
```

## Résumé
Nous avons une classe Contexte représentant l'objet qui a une référence à un objet Stratégie et délègue à cet objet l'exécution de l'algorithme.
Nous avons une interface Stratégie définissant la méthode exécuter(), qui encapsule l'algorithme à utiliser.
Nous avons des implémentations concrètes de Stratégie pour StratégieConcrète1 et StratégieConcrète2, chacune fournissant sa propre implémentation de la méthode exécuter().
Dans le code client, nous créons un objet Contexte avec une stratégie spécifique (StratégieConcrète1), exécutons la stratégie, puis changeons la stratégie du contexte en StratégieConcrète2 et l'exécutons à nouveau.