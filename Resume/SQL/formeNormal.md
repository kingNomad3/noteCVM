# 420-C42 Langages d'exploitation des bases de données
### Partie 14: PL/SQL et Extensions
### 1. Introduction au PL/SQL:
    PL/SQL est une extension de SQL proposée par Oracle qui combine le langage de programmation procédurale avec le SQL pour offrir une solution plus flexible et puissante aux développeurs de bases de données. Grâce au PL/SQL, les développeurs peuvent créer des procédures, des fonctions, des packages, des types et des déclencheurs, et les gérer dans la base de données.

### 2. Avantages du PL/SQL:
    Performance accrue: Comme le code PL/SQL est traité par l'optimiseur Oracle, il s'exécute plus rapidement.
    
    Développement plus rapide: Les développeurs peuvent utiliser des structures de contrôle, des boucles et d'autres fonctionnalités du langage de programmation pour écrire du code de manière plus efficace.
    
    Sécurité renforcée: Il est possible d'encapsuler ou de masquer la logique d'entreprise, ce qui rend le code plus sécurisé.
    
    Gestion des exceptions: PL/SQL permet une gestion efficace des erreurs grâce à son système d'exception.
### 3. Blocs PL/SQL:
    Un programme PL/SQL est composé de blocs, qui peuvent être anonymes ou nommés (procédures, fonctions). Un bloc typique PL/SQL a une structure :

```sql
DECLARE
   -- Déclarations de variables et constantes
BEGIN
   -- Corps du bloc: code exécutable
EXCEPTION
   -- Gestion des exceptions
END;
```
### 4. Procédures et Fonctions:
    En PL/SQL, vous pouvez définir des procédures et des fonctions:

    ** Procédures**: Utilisées pour effectuer une action spécifique et ne renvoient pas de valeur.
    **Fonctions** : Utilisées pour effectuer une action et renvoyer une valeur.

### 5. Déclencheurs (Triggers):
    Ce sont des programmes qui s'exécutent automatiquement en réponse à un événement dans une table ou une vue. Ils sont utiles pour garantir la cohérence des données, la validation des données, la journalisation des modifications, etc.

### 6. Extensions avec PostgreSQL:
    PostgreSQL prend en charge une version du PL/SQL appelée PL/pgSQL, qui permet une programmation procédurale dans le contexte de la base de données PostgreSQL. De plus, grâce à son architecture extensible, PostgreSQL prend également en charge d'autres langages de programmation procédurale tels que PL/Tcl, PL/Perl et PL/Python.

## Conclusion:
    Le PL/SQL, avec ses capacités procédurales étendues, est un outil puissant pour les développeurs de bases de données pour écrire des applications plus complexes et interactives directement dans la base de données. L'extension de ces capacités dans des bases de données comme PostgreSQL offre une flexibilité et une puissance encore plus grandes aux développeurs.

```sql
DECLARE
   -- Déclarations des variables
   num1 NUMBER := 10;
   num2 NUMBER := 0;
   resultat NUMBER;

BEGIN
   -- Tentative de diviser num1 par num2
   resultat := num1 / num2;
   DBMS_OUTPUT.PUT_LINE('Le résultat de la division est: ' || resultat);

EXCEPTION
   -- Gérer l'erreur de division par zéro
   WHEN ZERO_DIVIDE THEN
      DBMS_OUTPUT.PUT_LINE('Erreur: Division par zéro n’est pas autorisée!');
   -- Gérer les autres erreurs
   WHEN OTHERS THEN
      DBMS_OUTPUT.PUT_LINE('Une erreur inconnue s’est produite.');
END;
```
- la sortie : Erreur: Division par zéro n’est pas autorisée!

```sql
DECLARE
    v_id NUMBER := 1; -- On présume que vous voulez obtenir les détails de l'employé avec l'ID 1
    v_nom VARCHAR2(100);

BEGIN
    -- Récupérer le nom de l'employé à partir de sa table en utilisant l'ID fourni
    SELECT nom INTO v_nom FROM employes WHERE id = v_id;

    -- Afficher le nom de l'employé
    DBMS_OUTPUT.PUT_LINE('Nom de l''employé avec ID ' || v_id || ' est ' || v_nom);

EXCEPTION
    -- Si aucun employé avec cet ID n'est trouvé
    WHEN NO_DATA_FOUND THEN
        DBMS_OUTPUT.PUT_LINE('Aucun employé trouvé avec l''ID ' || v_id);

    -- Si une autre erreur se produit
    WHEN OTHERS THEN
        DBMS_OUTPUT.PUT_LINE('Une erreur inattendue est survenue.');
        
END;
```