# Notes sur l'utilisation de `setfill` en C++

## Introduction

La fonction `setfill` est utilisée en C++ pour définir le caractère de remplissage utilisé par certaines fonctions de formatage, telles que `setw`, afin de remplir les champs de largeur fixe. Elle permet de spécifier un caractère qui sera utilisé pour combler les espaces vides lors de la mise en forme de la sortie.

## Exemples d'utilisation

### Exemple #1 - Soulignement d'un texte

```cpp
string texte = "Introduction à la programmation";

cout << setfill('-');
cout << "\n" << texte << "\n" << setw(texte.size()) << "" << "\n\n";
cout << setfill(' '); // Remettre le caractère de remplissage par défaut
```

Resultat:
Introduction à la programmation
-------------------------------


## Exemple #2 - Présentation d'une facture
```cpp
int x = 30;
double T1 = 80.45, T2 = 56.12, T3 = 120.5;

cout << left << setfill('.'); // Permanent, remplace le caractère de remplissage qui doit être utilisé dans le setw()

cout << "\n"
     << "FACTURE" << "\n\n"
     << setw(x) << "Épicerie "   << " " << T1 << " $" << "\n"
     << setw(x) << "Pharmacie "  << " " << T2 << " $" << "\n"
     << setw(x) << "SAQ "        << " " << T3 << " $" << "\n\n"
     << setw(x) << "TOTAL "      << " " << T1 + T2 + T3 << " $" << "\n\n";
```

Resultat:
FACTURE

Épicerie ................. 80.45 $
Pharmacie ................ 56.12 $
SAQ ...................... 120.5  $
TOTAL .................... 257.07 $

## Exemple #3 - Formatage d'un tableau
```cpp
const int MARGE = 5;
const int C1 = MARGE + 15, C2 = 15, C3 = 15, C4 = 15, C5 = 10; // largeurs des colonnes

cout << right << "\n\n\n\n";

// Entête
cout << setw(C1) << "RANG"       << setw(C2) << "PAYS"          << setw(C3) << "CAPITALE"  << setw(C4) << "POPULATION" << setw(C5) << "ANNÉE"     << "\n";
cout << setw(C1) << "----"       << setw(C2) << "----"          << setw(C3) << "--------"  << setw(C4) << "----------" << setw(C5) << "-----"     << "\n\n";

// Données
cout << setw(C1) << 1            << setw(C2) << "Chine"         << setw(C3) << "Beijing"   << setw(C4) << "21,710,000" << setw(C5) << 2017        << "\n\n";
cout << setw(C1) << 2            << setw(C2) << "Inde"          << setw(C3) << "New Delhi" << setw(C4) << "16,787,949" << setw(C5) << 2014        << "\n\n";
cout << setw(C1) << 3            << setw(C2) << "Japon"         << setw(C3) << "Tokyo"     << setw(C4) << "13,742,906" << setw(C5) << 2017        << "\n\n";
cout << setw(C1) << 4            << setw(C2) << "Philippines"   << setw(C3) << "Manille"   << setw(C4) << "12,877,253" << setw(C5) << 2015        << "\n\n";
cout << setw(C1) << 5            << setw(C2) << "Russie"        << setw(C3) << "Moscou"    << setw(C4) << "11,541,000" << setw(C5) << 2011;
```
Resultat
  RANG            PAYS         CAPITALE  POPULATION  ANNÉE
  ----            ----         --------  ----------  -----
    1             Chine         Beijing  21,710,000   2017

    2             Inde          New Delhi  16,787,949   2014

    3             Japon         Tokyo   13,742,906   2017

    4             Philippines   Manille  12,877,253   2015

    5             Russie        Moscou  11,541,000   2011


- setfill est un outil puissant pour contrôler la mise en forme de la sortie en C++, permettant de remplir les espaces vides avec un caractère spécifié. Il est souvent utilisé en conjonction avec setw pour formater les sorties de manière élégante et lisible.