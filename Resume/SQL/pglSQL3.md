# Notes sur la Partie 17 - PL/pgSQL III: Gestion des exceptions et imbrication de blocs

1. Gestion d’exceptions avec RAISE

Le PL/pgSQL fournit le mécanisme RAISE pour générer des messages.

Il y a six niveaux de priorité pour les messages:

## DEBUG

- Objectif : Fournir des informations détaillées principalement utiles pour les développeurs et les personnes déboguant une application ou une fonction.
Usage courant : Afficher des valeurs variables, indiquer où le code en est dans son exécution, etc.
- Visibilité : Ces messages sont souvent désactivés en environnement de production car ils peuvent être très verbeux et ne sont généralement pertinents que pendant les phases de développement et de test.

## LOG

- Objectif : Enregistrer des informations sur les opérations du système ou sur des événements particuliers jugés importants pour les logs.
Usage courant : Tracer des actions spécifiques, comme les connexions/déconnexions des utilisateurs, les modifications importantes des données, etc.
- Visibilité : Les messages de ce niveau sont souvent conservés dans les fichiers de log pour une analyse ultérieure.

## INFO

- Objectif : Fournir des messages d'information générale sur le fonctionnement normal de l'application ou de la fonction.
Usage courant : Informer de la progression d'un processus, confirmer la réussite d'une opération, etc.
- Visibilité : C'est un message purement informatif, sans connotation d'erreur ou d'avertissement.

## NOTICE

- Objectif : Donner des avis ou des suggestions sur quelque chose qui pourrait nécessiter l'attention de l'utilisateur, mais qui ne constitue pas nécessairement un problème.
Usage courant : Signaler des situations qui ne sont pas des erreurs mais qui pourraient être optimisées, ou indiquer des comportements obsolètes.
- Visibilité : Les développeurs ou les administrateurs de bases de données les 
voient souvent pour prendre des décisions ou améliorer le système.

## WARNING

- Objectif : Alerter l'utilisateur ou le développeur d'un problème potentiel ou d'une situation qui, bien que non critique, pourrait conduire à des erreurs dans certaines conditions.
Usage courant : Alerter d'une configuration non optimale, d'une limite presque atteinte, etc.
- Visibilité : Ils signalent des conditions qui ne sont pas correctes mais qui ne causent pas l'arrêt du processus en cours.

## EXCEPTION (par défaut)

- Objectif : Signaler une erreur qui empêche l'opération ou la fonction de continuer normalement.
Usage courant : Rapporter des erreurs comme une violation de contrainte, une division par zéro, un élément non trouvé, etc.
- Visibilité : Ces erreurs interrompent généralement l'exécution en cours, entraînant un ROLLBACK de la transaction. Les exceptions doivent être gérées soit pour corriger le problème, soit pour fournir des messages d'erreur plus explicites.
Seul le niveau EXCEPTION arrête les opérations en cours et déclenche un ROLLBACK.

Syntaxe :

```sql
RAISE [ level ] 'format' [, expression [, ... ]]
[ USING option = expression [, ... ] ];
```
2. Bloc EXCEPTION en PL/pgSQL

Le bloc EXCEPTION permet de gérer et de réagir aux erreurs.

Permet de capturer des exceptions spécifiques et de les traiter.

Peut être utilisé pour transformer une exception en un simple message d'avertissement.

Exemple :

```sql
BEGIN
    ...
EXCEPTION
    WHEN condition THEN
        ... actions ...
    WHEN OTHERS THEN 
        ... actions ...
END;
```
3. Imbrication de blocs PL/pgSQL

Les blocs PL/pgSQL peuvent être imbriqués les uns dans les autres.

Avantages :

Clarifie le code en le divisant en sections logiques.
Crée des espaces de variables distincts. Les sous-blocs peuvent accéder aux variables du bloc parent, mais pas l'inverse.
Permet de gérer des exceptions spécifiques à un ensemble particulier d'opérations.
Structure générale :

```sql
DECLARE
    v_user_id NUMBER := 101; -- exemple d'ID d'utilisateur
    v_nom_utilisateur VARCHAR2(100);
    v_id_commande NUMBER;
    v_id_article NUMBER;
BEGIN
    -- Niveau 1 : récupérer l'utilisateur
    SELECT nom INTO v_nom_utilisateur FROM utilisateurs WHERE id = v_user_id;

    DECLARE
        v_temp_date DATE;
    BEGIN
        -- Niveau 2 : récupérer la dernière commande de cet utilisateur
        SELECT MAX(date_commande) INTO v_temp_date FROM commandes WHERE user_id = v_user_id;
        
        SELECT id INTO v_id_commande FROM commandes WHERE user_id = v_user_id AND date_commande = v_temp_date;

        DECLARE
        BEGIN
            -- Niveau 3 : récupérer le premier article de cette commande
            SELECT MIN(article_id) INTO v_id_article FROM articles_commande WHERE commande_id = v_id_commande;

            -- Supposons que vous vouliez faire quelque chose avec ces informations, par exemple :
            DBMS_OUTPUT.PUT_LINE('L''utilisateur ' || v_nom_utilisateur || ' a commandé l''article ID ' || v_id_article || ' dans sa dernière commande.');

        EXCEPTION
            WHEN NO_DATA_FOUND THEN
                DBMS_OUTPUT.PUT_LINE('Pas d''articles trouvés pour cette commande.');
        END;
        
        -- Encore au niveau 2: vous pourriez avoir d'autres opérations ici

    EXCEPTION
        WHEN NO_DATA_FOUND THEN
            DBMS_OUTPUT.PUT_LINE('Pas de commandes trouvées pour l''utilisateur ' || v_nom_utilisateur || '.');

    END;

    -- Retour au niveau 1: autres opérations potentielles pour l'utilisateur

EXCEPTION
    WHEN NO_DATA_FOUND THEN
        DBMS_OUTPUT.PUT_LINE('Utilisateur avec ID ' || v_user_id || ' non trouvé.');
END;
/

```