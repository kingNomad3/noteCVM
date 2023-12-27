# Notes sur l'Utilisation des Manipulateurs iomanip en C++

## 1. Introduction
Les manipulateurs iomanip (input/output manipulation) en C++ sont inclus dans la bibliothèque `<iomanip>` et sont utilisés pour formater la sortie à l'écran. Ces exemples démontrent l'utilisation de `setw`, `setprecision`, et d'autres manipulations.

## 2. Manipulateur `setw`
Le manipulateur `setw` est utilisé pour définir la largeur du champ de sortie.

### Exemple 1 - Centrer un Titre
```cpp
const int LARG = 120;
const string TITRE = "Exemple d'utilisation du manipulateur setw(x)";

size_t larg_titre = TITRE.size();
cout << right << setw((LARG - larg_titre) / 2 + larg_titre) << TITRE;
```

## Exemple 2 - Tableaux Cadrés à Gauche et à Droite

```cpp
// Tableau cadré à gauche
x = 15;
cout << left << setw(x) << "Op\x82rateur" << setw(x) << "Nom" << "\n";

// Tableau cadré à droite
x = 15;
cout << right << setw(x) << "Op\x82rateur" << setw(x) << "Nom" << "\n";
```

## 3. Manipulateur setprecision
Le manipulateur setprecision est utilisé pour définir le nombre de chiffres après la virgule pour les nombres à virgule flottante.

## Exemple 3 - Affichage avec Précision
```cpp
double pi = 3.1415927, _2tiers = 2.0/3.0;

cout << fixed << setprecision(2) << "pi  = " << pi << "\n";
cout << fixed << setprecision(0) << "2/3 = " << _2tiers << "\n";
```
## 4. Manipulateur scientific
Le manipulateur scientific est utilisé pour l'affichage en notation scientifique.

## Exemple 4 - Affichage Scientifique
```cpp

cout << scientific << setprecision(3) << "pi  = " << pi << "\n";
cout << scientific << setprecision(3) << "2/3 = " << _2tiers << "\n";
```
5. Manipulateurs d'Affichage des Entiers
Les manipulateurs oct, dec, et hex sont utilisés pour définir la base d'affichage des entiers.

## Exemple 5 - Affichage d'Entiers en Octal, Décimal et Hexadécimal
```cpp
int x = 37, y = 50, z = 75;

cout << oct << "oct:  " << "x = " << x << ", y = " << y << ", z = " << z << "\n";
cout << dec << "dec:  " << "x = " << x << ", y = " << y << ", z = " << z << "\n";
cout << hex << "hex:  " << "x = " << x << ", y = " << y << ", z = " << z << "\n";
```