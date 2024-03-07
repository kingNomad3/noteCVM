# Notes sur l'Instruction For en C++

L'instruction `for` est utilisée pour répéter un bloc d'instructions un nombre spécifié de fois. Voici les principaux points à retenir :

## Structure de l'Instruction For

```cpp
for ( initialisation ; condition ; post-incrémentation/décrémentation )
{
    instructions à répéter
}
```
- Initialisation : Cette partie est utilisée pour initialiser une variable de contrôle de la boucle.
- Condition : Cette partie est évaluée avant chaque itération. Si elle est vraie, le bloc d'instructions est exécuté. Sinon, la boucle est terminée.
- Post-incrémentation/décrémentation : C'est l'étape d'incrémentation ou de décrémentation effectuée après chaque itération de la boucle.

## Séquence d'exécution du For
- L'initialisation est effectuée.
- La condition est évaluée. Si elle est fausse, la boucle se termine. Sinon, les instructions du bloc sont exécutées.
- Après chaque exécution du bloc, l'étape de post-incrémentation/décrémentation est effectuée.
- La condition est à nouveau évaluée. Si elle est vraie, les étapes 2 et 3 sont répétées. Sinon, la boucle se termine.

### Calcul de la somme des n premiers nombres
```cpp
int somme = 0;
for (int n = 1; n <= 100; ++n)
{
    somme += n;
}
```
### Calcul de la factorielle d'un nombre
```cpp 
int fact = 1;
for (int n = 10; n >= 1; --n)
{
    fact *= n;
}
```
### Affichage d'une table de multiplication
```cpp
const int table = 12;
for (int i = 0; i <= table; ++i)
{
    cout << setw(2) << i << " x " << table << " = " << i * table << endl;
}
```
### Vérification de la parité d'un nombre
```cpp 
for (int i = 3; i <= 9; ++i)
{
    cout << i << " est ";
    if (i % 2 == 1)
        cout << "impair";
    else
        cout << "pair";
    cout << endl;
}
```
### Affichage de l'alphabet en majuscules
```cpp
for (char c = 'A'; c <= 'Z'; ++c)
{
    cout << c;
}
```

```markdown
# Test de Primalité en C++

Le test de primalité consiste à déterminer si un nombre donné est premier, c'est-à-dire s'il n'a que deux diviseurs distincts (1 et lui-même).

## Version Inefficace

Cette version utilise une méthode simple pour vérifier la primalité d'un nombre, mais elle peut être inefficace pour les grands nombres.

```cpp
uint64_t n, d;
bool estPremier;

n = 2147483647;
d = 1;
estPremier = false;

if (n >= 2)
{
    estPremier = true;
    for (d = 2; d < n && estPremier; d += 1)
        if (n % d == 0)
            estPremier = false;
    d -= 1;
}
```

### Version Plus Rapide

```cpp
uint64_t n, d;
bool estPremier;

n = 18446744073709551557;
d = 1;
estPremier = false;

if (n > 2 && n % 2 == 0)
    d = 2;
else if (n >= 2)
{
    estPremier = true;
    for (d = 3; d <= sqrt(n) && estPremier; d += 2)
        if (n % d == 0)
            estPremier = false;
    d -= 1;
}
```