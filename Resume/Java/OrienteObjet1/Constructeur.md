# Annexe 4 – Notes de cours – les constructeurs

## A) Méthode constructeur

- Assigne des paramètres à des variables d’instance à l’interne de la classe.
- Son appel permet la création d’objets à l’extérieur de la classe.
- A toujours le même nom que la classe dont il fait partie.
- N’a pas de type de retour (même pas void).

**Exemple :**

```java
public class EtudiantCegep {
    private String matricule;
    private int note;

    public EtudiantCegep(String matricule1, int note1) {
        matricule = matricule1;
        note = note1;
    }
}
```
À l'extérieur de la classe
```java
EtudiantCegep e1 = new EtudiantCegep("1662413", 79);
```
Problème : Les variables d’instance ne seront pas initialisées, car le paramètre a le même nom.

Solutions :

On donne des noms différents pour le paramètre et pour la variable.
Utiliser le mot-clé this pour distinguer la variable du paramètre.
```java

public class EtudiantCegep {
    private String matricule;
    private int note;

    public EtudiantCegep(String matricule1, int note1) {
        this.matricule = matricule1;
        this.note = note1;
    }
}
```
À l'extérieur de la classe
```java
EtudiantCegep e1 = new EtudiantCegep("1662413", 79);
```
## B) Surcharge de méthodes

Habituellement, une classe a plusieurs méthodes « constructeur » qui représentent différentes situations de création d’objets. Solution : surcharge de méthode : plusieurs méthodes peuvent avoir le même nom à condition que soit :

Le nombre.
Le type.
L’ordre.
des paramètres varient d’une méthode à l’autre.
Exemple : On tient à modéliser pour des fins d’inventaire, différents modèles de réfrigérateurs. La classe Refrigerateur a 4 variables d’instance :

nomModele
prix
capacite (pieds cubes)
distributeurAGlace (oui ou non)

```java
public class Refrigerateur {
    private String nomModele;
    private double prix;
    private double capacite;
    private boolean aDistributeurAGlace;

    // A-constructeur par défaut sans paramètre
    public Refrigerateur() {
        // Initialiser les valeurs par défaut ou laisser les variables d'instance non initialisées
        this.nomModele = "Nom par défaut";
        this.prix = 0.0;
        this.capacite = 0.0;
        this.aDistributeurAGlace = false;
    }

    // B- constructeur pour créer n’importe quel réfrigérateur
    public Refrigerateur(String modele, double prix, double capacite, boolean distributeurAGlace) {
        this.nomModele = modele;
        this.prix = prix;
        this.capacite = capacite;
        this.aDistributeurAGlace = distributeurAGlace;
    }

    // C-80% des réfrigérateurs reçus sont des Frigidaire, 16 pieds cubes, à 900$ sans distributeurs à glace
    public Refrigerateur(String modele) {
        this.nomModele = modele;
        this.prix = 900.0;
        this.capacite = 16.0;
        this.aDistributeurAGlace = false;
    }

    // D- constructeur n'initalisant pas le prix, il sera déterminé plus tard dans le programme
    public Refrigerateur(String modele, double capacite, boolean distributeurAGlace) {
        this.nomModele = modele;
        this.capacite = capacite;
        this.aDistributeurAGlace = distributeurAGlace;
        // Laisser le prix non initialisé pour être déterminé plus tard dans le programme
    }
}
```