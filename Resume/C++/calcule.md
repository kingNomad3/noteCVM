# Notes d'Étude sur les Calculs en C++


```cpp
#include <iostream>  // pour le cout
#include <conio.h>   // pour le _getch()

using namespace std;

int main()
{
    // CONSTANTES
    const double TVQ = 0.09975, TPS = 0.05; // taux de taxes

    // VARIABLES
    double totalAvantTaxes, tps, tvq, totalApresTaxes;

    // INPUT
    totalApresTaxes = 114.975;
    //totalAvantTaxes = 100.00;

    // TRAITEMENTS
    totalAvantTaxes = totalApresTaxes / (1 + (TVQ + TPS));
    tvq = totalAvantTaxes * TVQ;
    tps = totalAvantTaxes * TPS;
    totalAvantTaxes = totalApresTaxes - tvq - tps;

    // OUTPUT
    cout << endl;
    cout << "Montant avec les taxes : " << totalApresTaxes << " $";
    cout << endl << endl;
    cout << "   tps : " << tps << " $";
    cout << endl << endl;
    cout << "   tvq : " << tvq << " $";
    cout << endl << endl;
    cout << "Montant sans les taxes : " << totalAvantTaxes << " $";
    cout << endl;
    _getch();
}
```

## Constantes
- Déclaration : Utilisez le mot-clé const pour déclarer des constantes.
- Exemple : const double TVQ = 0.09975, TPS = 0.05;

## Variables
- Déclaration : Indiquez le type de variable suivi de son nom.
- Exemple : double totalAvantTaxes, tps, tvq, totalApresTaxes;

Calculs

```cpp
totalAvantTaxes = totalApresTaxes / (1 + (TVQ + TPS));
tvq = totalAvantTaxes * TVQ;
tps = totalAvantTaxes * TPS;
totalAvantTaxes = totalApresTaxes - tvq - tps;
```

- Division : totalApresTaxes / (1 + (TVQ + TPS))
- Multiplication : totalAvantTaxes * TVQ, totalAvantTaxes * TPS
- Soustraction : totalApresTaxes - tvq - tps

Affichage des Résultats
```cpp
Copy code
cout << "Montant avec les taxes : " << totalApresTaxes << " $";
cout << "   tps : " << tps << " $";
cout << "   tvq : " << tvq << " $";
cout << "Montant sans les taxes : " << totalAvantTaxes << " $";
```

