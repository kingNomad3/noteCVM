# Annexe 6 - Les constructeurs / modélisation

Dans cet exercice, je vous demande de modéliser une classe `CompteBancaire` dans un nouveau projet. Voici les exigences de base :

- Les données d’un objet `CompteBancaire` seront : le nom du propriétaire, le solde au compte et le numéro de celui-ci.
- Le numéro du compte est toujours composé de la première lettre du nom du propriétaire, suivi d’un tiret, suivi du nombre représentant le nombre de comptes créés à ce jour pour l’ensemble de la banque. Par exemple, si le premier compte à avoir été créé était un compte appartenant à Adrien Lachance, son numéro de compte serait : A-1 (pensez à une variable statique).
- Créer des méthodes représentant l’action de déposer ou de retirer une somme dans un `CompteBancaire` donné.

Dans une autre classe `Test` comprenant une méthode `main`, simuler dans la méthode `main` les opérations suivantes :

1. Un compte est créé pour Flavien Larrivée avec un solde initial de 100 $.
2. Un compte est créé pour Denise Lachance avec un solde initial de 36.78$.
3. Faites afficher le nom du propriétaire du premier compte créé.
4. Denise retire 20 $ de son compte.
5. Faites afficher le numéro du compte de M. Larrivée.
6. Un compte est créé pour Martial Maurice avec un solde initial de 40$.
7. Faites afficher le numéro de compte de Martial Maurice.
8. Faites afficher le solde du compte de Mme Lachance.

# Concepts discutés dans l'ensemble
### Variable static
- Une variable est static si une seule copie de sa valeur est nécessaire pour l’ensemble de la classe. Dans l'exemple, nbAnimaux est une variable static qui maintient le nombre total d'objets de la classe Animal.

### Méthodes static
- Une méthode static est une méthode dont le résultat est indépendant de l'état de l'objet. Par exemple, une méthode pour calculer le prêt de bourse ne dépend pas des propriétés d'un objet particulier, elle pourrait donc être static.

### Modificateurs final et static final
- final : Indique que la classe, la méthode ou la variable ne peut pas être modifiée ou héritée.
static final : Indique qu'une variable est à la fois static et final, ce qui signifie qu'elle est partagée par toutes les instances de la classe et ne peut pas être modifiée.

### Allocation dynamique de mémoire
- Cela se réfère à la manière dont la mémoire est allouée pendant l'exécution du programme. L'allocation statique se produit à la compilation, tandis que l'allocation dynamique se produit à l'exécution.

### Classe final
- Une classe final est une classe qui ne peut pas être héritée. Dans l'exemple, Mcdo est déclarée comme une classe final.

### Animal de compagnie

- A1 Race : furet, nom : Fido
- A2 Race : chat, nom : Fido
- A3 Race : python, nom : Léo

Allocation dynamique de mémoire

- C’est une variable `static` si on n’a pas besoin de stocker la valeur dans un objet.
- C’est de l’allocation `static` de mémoire.

```java
public class Animal {
    private String race;
    private String nom;
    public static int nbAnimaux = 0;

    public Animal(String race, String nom) {
        this.race = race;
        this.nom = nom;
        nbAnimaux++;
    }

    // Méthode static : méthode dont le résultat est indépendant de l’état (donc des variables d’instance) de l’objet.
    // Exemple :
    // - CalculerPretBourse() : N’est pas une méthode static, car elle dépend du revenu des parents, etc.
    // - EmplacementDeLEleveDurantLExamen() : Est static, car le résultat est indépendant des variables d’instance.

    // Classe final
    public final class Mcdo {
        // ...
    }
}

exemple
``java
// CompteBancaire.java
public class CompteBancaire {
    private String proprietaire;
    private double solde;
    private static int nbComptes = 0;
    private String numeroCompte;

    public CompteBancaire(String proprietaire, double soldeInitial) {
        this.proprietaire = proprietaire;
        this.solde = soldeInitial;
        nbComptes++;
        this.numeroCompte = genererNumeroCompte();
    }

    public void deposer(double montant) {
        solde += montant;
        System.out.println("Dépôt de " + montant + " effectué. Nouveau solde : " + solde);
    }

    public void retirer(double montant) {
        if (montant <= solde) {
            solde -= montant;
            System.out.println("Retrait de " + montant + " effectué. Nouveau solde : " + solde);
        } else {
            System.out.println("Fonds insuffisants pour le retrait de " + montant);
        }
    }

    public String getProprietaire() {
        return proprietaire;
    }

    public String getNumeroCompte() {
        return numeroCompte;
    }

    private String genererNumeroCompte() {
        return proprietaire.substring(0, 1).toUpperCase() + "-" + nbComptes;
    }
}
```
```java
// Test.java
public class Test {
    public static void main(String[] args) {
        // Création de comptes
        CompteBancaire compteFlavien = new CompteBancaire("Flavien Larrivée", 100);
        CompteBancaire compteDenise = new CompteBancaire("Denise Lachance", 36.78);

        // Affichage du nom du propriétaire du premier compte créé
        System.out.println("Nom du propriétaire du premier compte : " + compteFlavien.getProprietaire());

        // Retrait de Denise
        compteDenise.retirer(20);

        // Affichage du numéro du compte de M. Larrivée
        System.out.println("Numéro du compte de M. Larrivée : " + compteFlavien.getNumeroCompte());

        // Création d'un compte pour Martial Maurice
        CompteBancaire compteMartial = new CompteBancaire("Martial Maurice", 40);

        // Affichage du numéro de compte de Martial Maurice
        System.out.println("Numéro de compte de Martial Maurice : " + compteMartial.getNumeroCompte());

        // Affichage du solde du compte de Mme Lachance
        System.out.println("Solde du compte de Mme Lachance : " + compteDenise.getProprietaire() +
                           " est de " + compteDenise.getSolde());
    }
}
```