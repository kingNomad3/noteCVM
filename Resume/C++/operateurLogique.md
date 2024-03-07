# Notes sur les Opérateurs Logiques en C++

## 1. Les Opérateurs Logiques: ET (&&), OU (||), Négation (!)

### Table de Vérité du ET Logique (&&)

- `true  && true`   : true
- `false && true`   : false
- `true  && false`  : false
- `false && false`  : false

### Table de Vérité du OU Logique (||)

- `false || false`  : false
- `false || true`   : true
- `true  || false`  : true
- `true  || true`   : true

### Table de Vérité de la Négation Logique (!)

- `!true`  : false
- `!false` : true

## 2. Utilisation des Opérateurs Logiques

### Exemple d'Opérateur OU Logique (||)

```cpp
string animal = "chien";

if (animal == "chat" || animal == "chien") {
    cout << "Votre " << animal << " est un animal de compagnie" << "\n";
}
```
## Exemple d'Opérateur ET Logique (&&)
```cpp
double prix_condo = 325000;

if (prix_condo >= 300000 && prix_condo <= 400000) {
    cout << "Le prix de votre condo est dans la moyenne" << "\n";
}
```
## Exemple d'Opérateur de Négation (!)
```cpp
bool éveillé = false;

if (!éveillé) {
    cout << "Lui resservir du café svp !!!" << "\n";
}
```

## 3. Priorité des Opérateurs Logiques

### Priorité des Opérateurs Logiques entre Eux

- `!` est plus prioritaire que `&&`
- `&&` est plus prioritaire que `||`

### Priorité Générale des Opérateurs (du plus au moins prioritaire)

1. ()
2. !, "signe" +, "signe" -
3. *, /
4. +, -
5. <, <=, >, >=
6. ==, !=
7. &&
8. ||
9. =

# Notes sur les Opérateurs de Division Entière et Modulo en C++

## 1. Opérateur de Division Entière (`/`)

- La division entière (`/`) divise un nombre par un autre et retourne le quotient entier.
- Attention : La division par zéro est interdite et provoque une erreur grave à l'exécution.
- Exemples :
```cpp
  int nombre = 6, resultat;
  resultat = nombre / 2;   // resultat = 3
  resultat = nombre / 4;   // resultat = 1
```
##  2. Opérateur Modulo (%)
- L'opérateur modulo (%) retourne le reste de la division entière entre deux nombres.
- Attention : La division par zéro est interdite et provoque une erreur grave à l'exécution.

```cpp
int nombre = 6, reste;
reste = nombre % 4;   // reste = 2
```cpp
## 3. Exemples d'Utilisation
```cpp
int nombre = 7776;
if (nombre % 2 == 0) {
    cout << "Le nombre est pair";
} else {
    cout << "Le nombre est impair";
}
```
### Vérification de Multiples
```cpp
int nombre = 7776;
if (nombre % 6 == 0) {
    cout << "Le nombre est un multiple de 6";
} else {
    cout << "Le nombre n'est pas un multiple de 6";
}
```
### Utilisation de Modulo
```cpp
unsigned int reste;
reste = 8 % 3;  // reste = 2
```

### Explications Mathématiques
- Pour n % m, si n >= 0 et m != 0, alors n % m == n - (m * (n / m)).
- Pour n % m, si n < 0 et m != 0, alors n % m == -(-n % m).

# ToUpper et ToLower
```cpp
# Notes sur les Fonctions toupper() et tolower()

## Utilisation de toupper() et tolower()

Les fonctions `toupper()` et `tolower()` sont utilisées pour convertir les caractères en majuscules et en minuscules respectivement.

Exemple d'utilisation :

```cpp
#include <iostream>
#include <cctype>   // Inclure la bibliothèque pour toupper() et tolower()

using namespace std;

int main() {
    char lettre = 'e';
    char majuscule = toupper(lettre);
    cout << "Lettre: " << lettre << "  majuscule: " << majuscule << "\n";

    char minuscule = tolower(majuscule);
    cout << "Lettre: " << majuscule << "  minuscule: " << minuscule << "\n";
    return 0;
}

```