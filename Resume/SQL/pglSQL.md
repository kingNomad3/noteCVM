# 420-C42 Langages d'exploitation des bases de données
## Partie 15 PL/pgSQL I Introduction

### PL/pgSQL I Introduction
    PL/pgSQL est l'extension de langage procédural de PostgreSQL pour SQL. Contrairement au SQL qui est déclaratif, le PL/pgSQL permet des opérations procédurales, donnant ainsi plus de flexibilité et de contrôle aux développeurs pour l'exécution des requêtes.

    **Tandis**  que des SGBD comme Oracle possèdent PL/SQL, PostgreSQL a son propre PL/pgSQL. C'est un langage inspiré du PL/SQL d'Oracle, mais ils diffèrent en syntaxe et en fonctionnalités.

### PL/pgSQL I Sommaire
    PL/pgSQL est une extension qui offre des avantages tels que la manipulation des variables, l'utilisation de conditions, de boucles et autres structures de contrôle communes dans la programmation procédurale. Cela permet d'améliorer l'intégrité, la sécurité, et la performance des requêtes exécutées.

### PL/pgSQL I Avantages et inconvénients
    L'utilisation de PL/pgSQL présente plusieurs avantages tels que l'optimisation des requêtes, la centralisation du code et une meilleure gestion des erreurs. Toutefois, cela rend aussi le code plus complexe à maintenir et à déboguer.

### PL/pgSQL I Syntaxe générale
    La structure de base d'un bloc PL/pgSQL comprend trois sections : DECLARE pour la déclaration des variables, BEGIN pour le corps du code, et EXCEPTION pour la gestion des erreurs.

### PL/pgSQL I Outils de débogage
    Il est essentiel d'avoir des outils de débogage pour identifier et corriger les erreurs. PL/pgSQL offre des méthodes pour afficher des messages d'erreur (RAISE NOTICE) et pour valider des conditions (ASSERT).

### PL/pgSQL I Bloc anonyme
    Un bloc anonyme permet d'exécuter des instructions PL/pgSQL sans avoir à créer une fonction ou une procédure stockée. C'est particulièrement utile pour des opérations ponctuelles.

Exemple :
```sql
DO $$
BEGIN
   RAISE NOTICE 'Début de l’exécution...';
   -- Autres instructions PL/pgSQL
   RAISE NOTICE 'Fin de l’exécution.';
END
$$ LANGUAGE plpgsql;
```
## Conclusion
    En résumé, le PL/pgSQL est une extension puissante de PostgreSQL qui permet aux développeurs d'écrire des scripts SQL plus avancés et dynamiques. Sa capacité à intégrer des éléments de programmation procédurale dans le SQL rend les opérations de base de données plus flexibles et optimisées.
```sql
CREATE TABLE employe (
   id SERIAL PRIMARY KEY,
   nom VARCHAR(100),
   salaire NUMERIC(10, 2)
);

CREATE TABLE employes_bien_payes (
   id SERIAL PRIMARY KEY,
   employe_id INT,
   nom VARCHAR(100),
   salaire NUMERIC(10, 2)
);
DO $$
DECLARE 
   employe_id INT;
   salaire_limite NUMERIC(10, 2) := 50000; -- salaire limite pour être considéré comme bien payé
BEGIN
   -- Insérer un nouvel employé
   INSERT INTO employe (nom, salaire) VALUES ('Martin', 60000) RETURNING id INTO employe_id;

   -- Vérifier si le salaire est supérieur à la limite
   IF (SELECT salaire FROM employe WHERE id = employe_id) > salaire_limite THEN
      INSERT INTO employes_bien_payes (employe_id, nom, salaire) 
      VALUES (employe_id, (SELECT nom FROM employe WHERE id = employe_id), (SELECT salaire FROM employe WHERE id = employe_id));
      RAISE NOTICE 'L’employé % a été ajouté à la liste des employés bien payés', (SELECT nom FROM employe WHERE id = employe_id);
   ELSE
      RAISE NOTICE 'L’employé % n’est pas ajouté à la liste des employés bien payés', (SELECT nom FROM employe WHERE id = employe_id);
   END IF;

EXCEPTION 
   WHEN OTHERS THEN 
      RAISE WARNING 'Une erreur s’est produite lors de l’ajout de l’employé.';
END 
$$ LANGUAGE plpgsql;
```
Dans cet exemple, le bloc PL/pgSQL insère d'abord un nouvel employé. Ensuite, il vérifie si le salaire de cet employé dépasse un certain montant. Si c'est le cas, l'employé est également ajouté à la table des employés bien payés. En cas d'erreur, un message d'erreur est affiché.

```sql
BEGIN
-- 1. Assignation des variables

	drone := NEW.drone;
	state := NEW.state;
	employee := NEW.employee;
	start_date_time := NEW.start_date_time;
	IF NEW.location IS NOT NULL THEN
		location = NEW.location;
	END IF;
	
 -- 2. fonction qui verifie si le state est bon ou mauvais
-- verifier si le n-a-s de l'du plus recent insert est le state du l'insert en cours
																
	old_state := (SELECT get_most_recent_insert_state(drone));
	old_state_next_accepted_state := (SELECT get_next_accepted_state(old_state));
	old_state_next_rejected_state := (SELECT get_next_rejected_state(old_state));
																				  
	IF state = old_state_next_accepted_state OR state = old_state_next_rejected_state THEN
 		insert_correct := true;
		RAISE NOTICE 'BONNE INSERTION'; 
	ELSE 
		RAISE NOTICE 'MAUVAISE INSERTION LE STATE DOIT EGAL a % ou a %', old_state_next_accepted_state, old_state_next_rejected_state;
	END IF;
 
 -- 3. fonction qui verifie les noms et les dates ensembles apparaissent
 
  IF insert_correct THEN
    RETURN NEW;
  ELSE
    RAISE EXCEPTION 'Insert validation failed';
  END IF;
END;
$$;

/****************************** TRIGGER  *****************************/
--DROP TRIGGER IF EXISTS validate_insert_drone_state ON drone_state;																				 
CREATE TRIGGER validate_insert_drone_state
BEFORE INSERT
ON drone_state
FOR EACH ROW
EXECUTE FUNCTION validate_insert_drone_state();
```

- Trigger
- arrete une operation en cours 
- automatiser des taches clasique
- generer du data