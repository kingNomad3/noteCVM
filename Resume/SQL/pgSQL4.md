## Procédures
````sql
CREATE OR REPLACE PROCEDURE create_stats(mode INT DEFAULT 4)
LANGUAGE PLPGSQL
AS $$
-- le BEGIN est du procédurale
BEGIN
DROP TABLE IF EXISTS stats_employe;
CREATE TABLE stats_employe(
id SERIAL PRIMARY KEY,
quand TIMESTAMP NOT NULL,
qui TEXT NOT NULL,
nombre INT NOT NULL,
salaire_min NUMERIC(7,2) NULL,
salaire_moy
salaire_max NUMERIC(7,2) NULL
);
CALL snapshot_stats(mode); -- cette procédure sera créée par la suite
END$$;
```

## Si procedural on doit faire du plpgsql sinon ont peut utiliser sql

DROP FUNCTION IF EXISTS compare_taux;
CREATE OR REPLACE FUNCTION compare_taux(
depth INT DEFAULT 100,
format TEXT DEFAULT '0.999999990’)
RETURNS TABLE (i INT, pi_reel TEXT, pi_a TEXT, pi_b TEXT, taux_conv_a TEXT, taux_conv_b TEXT)
LANGUAGE SQL
AS $$
SELECT depth AS i,
to_char(pi(), format) AS "Pi réel",
to_char(pi_A(depth), format) AS "Pi série A",
to_char(pi_B(depth), format) AS "Pi série B",
to_char(taux_convergence(pi_A(depth + 1), pi_A(depth), pi()), format) AS "Taux conv. A",
to_char(taux_convergence(pi_B(depth + 1), pi_B(depth), pi()), format) AS "Taux conv. B";
$$;
SELECT compare_taux(100); -- voir note 1
SELECT * FROM compare_taux(100); -- voir note 2
• Attention, cette fonction retourne une table! Ainsi, la requête 1 retourne la table et non pas une
requête sur la table. Ainsi, le résultat correspond à une seule colonne contenant une liste de
valeurs pour chaque ligne. La requête 2 retourne toutes les colonnes tel qu’attendu.