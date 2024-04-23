# Modèle de Conception : State

## But
Le modèle de conception State permet à un objet de modifier son comportement lorsqu'il change son état interne. Il semble modifier sa classe.

## Structure
1. **Contexte** : Il est l'objet qui possède un état interne et qui peut déclencher des actions basées sur cet état.
2. **État** : Interface définissant les méthodes qui correspondent à chaque état possible du contexte.
3. **ÉtatConcret** : Implémente l'interface État et représente un état spécifique du contexte.

## Diagramme UML
                  +--------------+
                  |   Contexte   |
                  +--------------+
                  | -état: État  |
                  +--------------+
                  | +action()    |
                  +--------------+
                           |
                           v
              +----------------------+
              |       État           |
              +----------------------+
              | +action()            |
              +----------------------+
                  ^       ^       ^
                  |       |       |
        +---------+  +----+  +------+
        |          |  |         |
        +----------------+ | | +----------------+
        | ÉtatConcret1 | | | | ÉtatConcret2 |
        +----------------+ | | +----------------+
        | +action() | | | | +action() |
        +----------------+ | | +----------------+
        | |
        +---------+ +------+
        | |
        +-------------------+ +-------------------+
        | ÉtatConcret3 | | ÉtatConcret4 |
        +-------------------+ +-------------------+
        | +action() | | +action() |
+-------------------+ +-------------------+


## Participants et Responsabilités
- **Contexte** :
  - Maintient une référence vers l'objet État actuel.
  - Permet aux objets ÉtatConcret d'accéder et de modifier son état actuel.
- **État** :
  - Définit une interface pour encapsuler le comportement associé à un état particulier du Contexte.
- **ÉtatConcret** :
  - Implémente le comportement associé à un état particulier du Contexte.

## Avantages
- Favorise une meilleure organisation du code en séparant les différents états et leurs comportements associés.
- Facilite l'ajout de nouveaux états et de nouveaux comportements sans modifier le Contexte.

## Exemple
Considérez une machine à café qui peut être dans différents états tels que "en attente", "en cours de préparation" et "prête". Chaque état peut avoir des comportements différents comme démarrer, interrompre ou terminer la préparation du café.

## Conseils d'Implémentation
- Veillez à ce que chaque ÉtatConcret soit responsable de son propre comportement et de sa transition vers d'autres états si nécessaire.
- Utilisez le modèle de conception State lorsque le comportement d'un objet dépend de son état interne et que cet état peut changer au cours du temps.

## Quand Utiliser
- Utilisez le modèle de conception State lorsque vous avez un objet qui change de comportement en fonction de son état interne, et que ce changement est représenté par de multiples instructions conditionnelles dans le code.

En appliquant le modèle de conception State, vous pouvez rendre votre code plus modulaire, extensible et maintenable en regroupant les comportements associés à chaque état dans des classes distinctes.

## exemple
```python
from abc import ABC, abstractmethod

# Contexte : La classe dont l'état va changer
class Contexte:
    def __init__(self, etat):
        self._etat = etat

    def requete(self):
        self._etat.gerer()

    def changer_etat(self, etat):
        self._etat = etat

# État : Interface pour encapsuler le comportement associé à un état particulier du Contexte
class Etat(ABC):
    @abstractmethod
    def gerer(self):
        pass

# État Concret 1 : Représente un état spécifique du Contexte
class EtatConcret1(Etat):
    def gerer(self):
        print("Traitement de la requête dans l'État Concret 1")
        # Logique supplémentaire spécifique à cet état

# État Concret 2 : Représente un autre état spécifique du Contexte
class EtatConcret2(Etat):
    def gerer(self):
        print("Traitement de la requête dans l'État Concret 2")
        # Logique supplémentaire spécifique à cet état

# Code Client
if __name__ == "__main__":
    # Créer un Contexte avec un état initial
    contexte = Contexte(EtatConcret1())

    # Effectuer des requêtes, qui délèguent à l'état actuel
    contexte.requete()  # Sortie : Traitement de la requête dans l'État Concret 1

    # Changer l'état du contexte
    contexte.changer_etat(EtatConcret2())

    # Effectuer à nouveau des requêtes avec le nouvel état
    contexte.requete()  # Sortie : Traitement de la requête dans l'État Concret 2
```

## Résumé
Nous avons une classe Contexte représentant l'objet dont l'état va changer. Elle possède une méthode requete() qui délègue à la méthode gerer() de l'état actuel.
Nous avons une interface Etat définissant la méthode gerer(), qui encapsule le comportement associé à un état particulier du contexte.
Nous avons des implémentations concrètes de Etat pour EtatConcret1 et EtatConcret2, chacune fournissant sa propre implémentation de la méthode gerer().
Dans le code client, nous créons un objet Contexte avec un état initial (EtatConcret1), effectuons des requêtes, changeons l'état du contexte, et effectuons à nouveau des requêtes avec le nouvel état.