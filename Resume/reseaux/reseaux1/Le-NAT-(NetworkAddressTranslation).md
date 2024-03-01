- Le NAT existe, car il commence a avor un manque d'adresse IPV4 -> 32 bits


# Exercice théorique sur la notion de passerelle par défaut et route

## Objectifs
1. **Comprendre et appliquer** le concept de passerelle par défaut.
2. **Comprendre et appliquer** le concept de route statique.

### La notion de passerelle par défaut
- La passerelle par défaut est l'adresse IP qui dirige vers le routeur permettant au réseau local de communiquer avec d'autres réseaux.

### La notion de route statique
- Le routage détermine le chemin que les paquets de données vont emprunter sur le réseau.
- Les routes statiques sont définies manuellement par l'administrateur.

---

## DIAGRAMME RÉSEAU DU SCÉNARIO 1

Chaque dispositif (ordinateur, routeur) doit avoir la possibilité de communiquer avec tous les autres dispositifs du réseau.

### Configuration des routeurs
- ROUTEUR1 pointe vers ROUTEUR2
- ROUTEUR2 pointe vers ROUTEUR1

| Routeur    | Passerelle par défaut | Routes additionnelles  |
|------------|-----------------------|------------------------|
| ROUTEUR1   | 10.11.0.2             | Aucune                 |
| ROUTEUR2   | 10.11.0.1             | Aucune                 |

---

### Configuration possible des hôtes

1. **Réseau 10.12.0.0/16**
   - Adresses hôtes: 10.12.0.2 - 10.12.255.254
   - Passerelle par défaut: 10.12.0.1

2. **Réseau 10.11.0.0/16**
   - Adresses hôtes: 10.11.0.3 - 10.11.255.254
   - Passerelles par défaut: 10.11.0.1, 10.11.0.2

3. **Réseau 10.10.0.0/16**
   - Adresses hôtes: 10.10.0.2 - 10.10.255.254
   - Passerelle par défaut: 10.10.0.1

---

## Validation des accès pour les hôtes

- **10.12.0.0 à 10.12.0.0** - Accès local uniquement
- **10.11.0.0 à 10.12.0.0** - Accès via ROUTEUR1 (10.11.0.1) pour réseau 10.12.0.0 si passerelle est 10.11.0.1. Non direct si 10.11.0.2.
- **10.10.0.0 à 10.12.0.0** - Chemin: ROUTEUR2 (10.10.0.1) > ROUTEUR1 (10.11.0.1) > Réseau 10.12.0.0
- **10.12.0.0 à 10.11.0.0** - Chemin via ROUTEUR1 (10.12.0.1) pour accéder au réseau 10.11.0.0
- **10.11.0.0 à 10.11.0.0** - Accès local uniquement
- **10.10.0.0 à 10.11.0.0** - Chemin: ROUTEUR2 (10.10.0.1) > Réseau 10.11.0.0
- **10.12.0.0 à 10.10.0.0** - Chemin: ROUTEUR1 (10.12.0.1) > ROUTEUR2 (10.11.0.2) > Réseau 10.10.0.0
- **10.11.0.0 à 10.10.0.0** - Si la passerelle est 10.11.0.1, chemin indirect. Si 10.11.0.2, chemin direct vers réseau 10.10.0.0.
- **10.10.0.0 à 10.10.0.0** - Accès local uniquement
