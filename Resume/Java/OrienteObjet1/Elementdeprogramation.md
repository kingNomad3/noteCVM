# Notes sur les Éléments de Programmation Java - Annexe 3

## 1. Hiérarchie :

- **Package :**
  - Regroupement de classes ayant un but commun.
  - Importer une classe d'un package :
    - `import java.util.*` → Toutes les classes du package.
    - `import java.util.Calendar` → Une classe en particulier.
  - **java.lang :**
    - Package par défaut comprenant les classes de base.
    - Pas besoin de l'importer explicitement.

- **Classe :**
  - Sert de modèle aux objets.
  - Exécutable si elle contient une méthode main.
  - Un type défini par le programmeur (contrairement aux types prédéfinis tels que int, double, char, etc.).
  - Le nom d'une classe commence toujours par une majuscule.

- **Méthode :**
  - Créée pour accomplir une tâche spécifique (afficher des résultats, demander d'entrer son nom, etc.).
  - Permet la réutilisation du code.
  - Choix du nom très important pour faciliter la réutilisation et la compréhension du code.
  - Le nom d'une méthode commence toujours par une minuscule.

## 2. Exemple : Compagnie de taxis

## 3. Signature / en-tête d’une méthode :

- **Exemple :** `public static void ecrire(String texte)`

  - **A - Modificateurs d'accès (voir Annexe 3B) :**
    - **Public :** Accès à la méthode partout (sous réserve d'un import correct).
    - **Protected :** Accès à la méthode dans les packages d'origine et dans les sous-classes d'un package différent (avec un import correct).
    - **Rien (package-private) :** Accès à la méthode uniquement dans le package d'origine.
    - **Private :** Accès à la méthode uniquement dans la classe d'origine.
