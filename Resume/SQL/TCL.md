# 420-C42 Langages d'exploitation des bases de données
## Partie 13: TCL - Contrôle de transaction
### 1. TCL introduction:
    TCL (Transaction Control Language) se rapporte au contrôle de transactions. Dans les bases de données, une transaction est une séquence d'une ou plusieurs opérations exécutées comme une seule unité de travail. Si toutes ces opérations réussissent, la transaction est confirmée. Si une de ces opérations échoue, toutes les autres opérations de la transaction sont annulées.

### 2. ACID:
    *La garantie* de transactions sûres et fiables est donnée par la propriété ACID:

    **Atomicité**: Une transaction est considérée comme un tout. Elle est soit complètement exécutée, soit complètement annulée.

    **Cohérence**: Après l'achèvement d'une transaction, la base de données doit rester dans un état cohérent.

    **Isolation**: Chaque transaction est isolée des autres. Les opérations d'une transaction ne doivent pas être visibles par d'autres transactions avant la confirmation.

    ** Durabilité** : Une fois qu'une transaction a été confirmée, ses effets sont permanents.

### 3. TCL Concept:
    Pour illustrer le concept de transaction, prenons l'exemple d'une transaction bancaire. Si Frédérick veut transférer 1000$ à Caroline, il y a deux opérations: débiter 1000$ du compte de Frédérick et créditer 1000$ sur le compte de Caroline. Les deux opérations doivent être exécutées ou aucune d'elles ne doit l'être.

### 4. BEGIN & COMMIT:
    Pour garantir que toutes les opérations d'une transaction sont exécutées ou aucune d'elles ne l'est, on utilise BEGIN pour démarrer la transaction et COMMIT pour la confirmer.

```sql
BEGIN;
...
COMMIT;
```

BEGIN;
INSERT INTO employes (nom, age) VALUES ('Martin', 30);
INSERT INTO employes (nom, age) VALUES ('Julie', 25);
COMMIT;

BEGIN;
UPDATE employes SET salaire = salaire * 1.05 WHERE dernier_travail < '2023-01-01';
DELETE FROM employes WHERE dernier_travail < '2022-01-01';
COMMIT;


BEGIN;
INSERT INTO auteurs (nom) VALUES ('J.K. Rowling');
INSERT INTO livres (titre, id_auteur) VALUES ('Harry Potter', (SELECT id FROM auteurs WHERE nom = 'J.K. Rowling'));
COMMIT;

BEGIN;
-- Supposons que nous voulons nous assurer qu'il n'y a pas de doublons
IF NOT EXISTS (SELECT 1 FROM employes WHERE nom = 'Martin') THEN
    INSERT INTO employes (nom, age) VALUES ('Martin', 30);
END IF;
COMMIT;

### 5. SAVEPOINT & ROLLBACK:
    Il est possible de définir des points intermédiaires dans une transaction avec SAVEPOINT. Si nécessaire, vous pouvez annuler certaines opérations et revenir à un savepoint avec ROLLBACK TO.

```sql
BEGIN;
...
SAVEPOINT mon_point;
...
ROLLBACK TO mon_point;
...
COMMIT;
```

BEGIN; -- Commencez la transaction

INSERT INTO employes (nom, age) VALUES ('Martin', 30);

SAVEPOINT mon_point; -- Définir un point de sauvegarde après l'insertion


** ROLLBACK ** sans spécifier un savepoint annule toutes les opérations depuis le BEGIN.

## Conclusion:  
    Le TCL est crucial pour assurer l'intégrité et la cohérence des données dans une base de données. En utilisant TCL, on peut s'assurer que les opérations sur la base de données sont complètes et correctes, et que les données restent cohérentes même en cas d'erreurs ou de pannes.