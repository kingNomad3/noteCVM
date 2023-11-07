# Langages d'exploitation des bases de données - Partie 16 - PL/pgSQL II

1. Variables en PL/pgSQL :

    Les variables sont déclarées dans la section DECLARE.
    Types de données possibles : types SQL standards, types personnalisés, types basés sur une autre variable ou colonne de table, types d'enregistrement.

Exemple de déclaration :
```plpgsql
ma_var ma_table.ma_colonne%TYPE;
mon_enregistrement ma_table%ROWTYPE;
```
2. Structures de contrôle :

IF : utilisé pour des conditions simples.

```plpgsql
IF condition THEN
    -- code
ELSE
    -- autre code
END IF;
```
CASE : utilisé pour les branchements conditionnels. Deux formes principales : directe et par recherche.
SELECT 
    titre,
    CASE categorie
        WHEN 'science-fiction' THEN 'SF'
        WHEN 'fantasy' THEN 'Fantaisie'
        ELSE 'Autre'
    END AS "Type"
FROM livres;
SELECT 
    titre,
    CASE 
        WHEN pages > 500 THEN 'Long'
        WHEN pages < 100 THEN 'Court'
        ELSE 'Moyen'
    END AS "Taille"
FROM livres;

LOOP : boucle sans fin qui doit être contrôlée par un EXIT ou EXIT WHEN.
DO $$ 
DECLARE 
    var INTEGER := 0; 
BEGIN 
    LOOP 
        var := var + 1; 
        RAISE NOTICE 'Value of var: %', var; 

        EXIT WHEN var >= 5; 
    END LOOP; 
END $$;
Explication :
Ce code définit une boucle qui incrémente la variable var à chaque itération et affiche sa valeur. La boucle s'arrête lorsque var est supérieur ou égal à 5.

3. WHILE
sql
Copy code
DO $$ 
DECLARE 
    var INTEGER := 0; 
BEGIN 
    WHILE var < 5 LOOP 
        var := var + 1; 
        RAISE NOTICE 'Value of var: %', var; 
    END LOOP; 
END $$;
Explication :
Semblable à l'exemple précédent, ce code utilise une boucle WHILE pour incrémenter et afficher la valeur de var tant qu'elle est inférieure à 5.

4. FOR
a. Boucle FOR avec une séquence d'entiers :

sql
Copy code
DO $$ 
BEGIN 
    FOR i IN 1..5 LOOP 
        RAISE NOTICE 'Value of i: %', i; 
    END LOOP; 
END $$;
Explication :
Ce code passe en boucle sur une séquence d'entiers de 1 à 5 et affiche la valeur actuelle.

b. Boucle FOR avec le résultat d'une requête :

sql
Copy code
DO $$ 
DECLARE 
    titre_record RECORD; 
BEGIN 
    FOR titre_record IN (SELECT titre FROM livres) LOOP 
        RAISE NOTICE 'Titre: %', titre_record.titre; 
    END LOOP; 
END $$;
Explication :
Ce code parcourt tous les titres de la table livres et les affiche un par un.

J'espère que ces exemples clarifient l'utilisation de ces structures de contrôle dans le contexte de PostgreSQL et PL/pgSQL !


WHILE : boucle conditionnelle.
DO $$ 
DECLARE 
    var INTEGER := 0; 
BEGIN 
    WHILE var < 5 LOOP 
        var := var + 1; 
        RAISE NOTICE 'Value of var: %', var; 
    END LOOP; 
END $$;

Explication :
Ce code définit une boucle qui incrémente la variable var à chaque itération et affiche sa valeur. La boucle s'arrête lorsque var est supérieur ou égal à 5.

3. WHILE
sql
Copy code
DO $$ 
DECLARE 
    var INTEGER := 0; 
BEGIN 
    WHILE var < 5 LOOP 
        var := var + 1; 
        RAISE NOTICE 'Value of var: %', var; 
    END LOOP; 
END $$;

FOR : boucle itérative pour parcourir une séquence d'entiers ou le résultat d'une requête.
DO $$ 
BEGIN 
    FOR i IN 1..5 LOOP 
        RAISE NOTICE 'Value of i: %', i; 
    END LOOP; 
END $$;
Explication :
Ce code passe en boucle sur une séquence d'entiers de 1 à 5 et affiche la valeur actuelle.

b. Boucle FOR avec le résultat d'une requête :

sql
Copy code
DO $$ 
DECLARE 
    titre_record RECORD; 
BEGIN 
    FOR titre_record IN (SELECT titre FROM livres) LOOP 
        RAISE NOTICE 'Titre: %', titre_record.titre; 
    END LOOP; 
END $$;

3. Curseur :

Utilisé pour parcourir le résultat d'une requête ligne par ligne.
Types de curseurs :
Curseur lié : associe une requête fixe au curseur lors de sa déclaration.
Curseur lié paramétré : associe une requête avec des paramètres au curseur lors de sa déclaration.
Curseur non lié : associe une requête au curseur au moment de son ouverture.
Syntaxe basique :
plpgsql
Copy code
DECLARE
    mon_curseur CURSOR FOR SELECT ...;
BEGIN
    OPEN mon_curseur;
    FETCH mon_curseur INTO ma_variable;
    ...
    CLOSE mon_curseur;
END;
4. Outils de débogage :

RAISE NOTICE : permet d'afficher un message à l'utilisateur.
ASSERT : valide une condition et déclenche une exception si elle est fausse.
Conclusions :

PL/pgSQL est un langage procédural intégré à PostgreSQL qui ajoute des structures de contrôle et d'autres fonctionnalités avancées pour faciliter le développement et la gestion des données.
Utiliser PL/pgSQL permet de centraliser la logique de l'application directement dans la base de données, ce qui peut améliorer la performance, la sécurité et l'intégrité des données.
Toutefois, il faut faire attention à la complexité ajoutée et veiller à ce que la logique soit bien documentée et testée.

-- drone state
CREATE TRIGGER interdire_modification_suppression_sur_drone_state
BEFORE UPDATE OR DELETE ON drone_state
BEGIN
    RAISE EXCEPTION 'Les modifications ou suppressions sur drone_state ne sont pas autorisées';
END;






```plpgsql
CREATE OR REPLACE FUNCTION getLastDroneState(p_drone_id INT) 
RETURNS drone_state%ROWTYPE AS $$
DECLARE
LANGUAGE plpgsql
    v_last_state drone_state%ROWTYPE;
BEGIN
    SELECT * INTO v_last_state
    FROM drone_state
    WHERE drone_id = p_drone_id
    ORDER BY start_date_time DESC
    LIMIT 1;


    RETURN v_last_state%ROWTYPE;
END;
$$ ;
```
```plpgsql
CREATE OR REPLACE FUNCTION validate_insert_drone_state() 
RETURNS TRIGGER AS $$
LANGUAGE plpgsql;
DECLARE
    v_current_state drone_state%ROWTYPE;
BEGIN
    -- Récupérer l'état actuel du drone
    v_current_state := getLastDroneState(NEW.drone_id);


   -- Vérifier la validité de la transition d'état
    IF NEW.state_symbol != (SELECT next_accepted_state FROM state WHERE symbole = v_current_state drone_state%ROWTYPE;) THEN
        RAISE EXCEPTION 'Transition d''état invalide'
    END IF;


    RETURN NEW;??
END;
$$
```








-- Fonction pour insérer une note:
CREATE FUNCTION inserer_note(drone_state INTEGER, note note_type, employee INTEGER, details VARCHAR(2048)) RETURNS VOID 
AS $$
BEGIN
LANGUAGE plpgsql;


    INSERT INTO state_note(drone_state, note, date_time, employee, details) 
    VALUES (drone_state, note, NOW(), employee, details);
END;
$$ 




