# Fonctions Mathématiques de Transformation

Les fonctions mathématiques de transformation sont utilisées pour effectuer des opérations de transformation sur les nombres. Voici quelques-unes des fonctions les plus couramment utilisées :

- `round()` : Arrondit le nombre à l'entier le plus proche.
- `floor()` : Renvoie l'entier le plus grand (ou égal) qui est inférieur ou égal au nombre.
- `ceil()` : Renvoie l'entier le plus petit (ou égal) qui est supérieur ou égal au nombre.
- `trunc()` : Tronque le nombre pour supprimer la partie décimale.
- `abs()` : Renvoie la valeur absolue du nombre.

## Exemples d'utilisation

```cpp
#include <iostream>
#include <iomanip>
#include <conio.h>
#include <cmath>		

using namespace std;

int main()
{
    const int S = 10;
    const double V1 = 2.3;
    const double V2 = 3.8;
    const double V3 = 5.5;
    const double V4 = -V1;
    const double V5 = -V2;
    const double V6 = -V3;

    cout << fixed << setprecision(2) << right << endl;

    cout << setw(S) << "value" << setw(S) << "round" << setw(S) << "floor" << setw(S) << "ceil" << setw(S) << "trunc" << setw(S) << "abs" << "\n\n";

    cout << setw(S) << V1 << setw(S) << round(V1) << setw(S) << floor(V1) << setw(S) << ceil(V1) << setw(S) << trunc(V1) << setw(S) << abs(V1) << "\n";
    cout << setw(S) << V2 << setw(S) << round(V2) << setw(S) << floor(V2) << setw(S) << ceil(V2) << setw(S) << trunc(V2) << setw(S) << abs(V2) << "\n";
    cout << setw(S) << V3 << setw(S) << round(V3) << setw(S) << floor(V3) << setw(S) << ceil(V3) << setw(S) << trunc(V3) << setw(S) << abs(V3) << "\n";
    cout << setw(S) << V4 << setw(S) << round(V4) << setw(S) << floor(V4) << setw(S) << ceil(V4) << setw(S) << trunc(V4) << setw(S) << abs(V4) << "\n";
    cout << setw(S) << V5 << setw(S) << round(V5) << setw(S) << floor(V5) << setw(S) << ceil(V5) << setw(S) << trunc(V5) << setw(S) << abs(V5) << "\n";
    cout << setw(S) << V6 << setw(S) << round(V6) << setw(S) << floor(V6) << setw(S) << ceil(V6) << setw(S) << trunc(V6) << setw(S) << abs(V6) << "\n";

    _getch();
}
```
# Fonctions Mathématiques Standards

- pow(x, y) : Calcule x élevé à la puissance y.
- log2(x) : Calcule le logarithme en base 2 de x.
- log10(x) : Calcule le logarithme en base 10 de x.
- log(x) : Calcule le logarithme népérien de x.
- sqrt(x) : Calcule la racine carrée de x.

```cpp
#include <iostream>
#include <iomanip>
#include <conio.h>
#include <cmath>		

using namespace std;

int main()
{
    cout << fixed << setprecision(2) << endl;

    cout << "pow(2,6)     = " << pow(2,6) << "\n\n";					
    cout << "log2(64)     = " << log2(64) << "\n";						
    cout << "log10(100)   = " << log10(100) << "\n";					
    cout << "log_" << b << "(27)    = " << log2(27) / log2(b) << "\n";	
    cout << "log_e(10)    = " << log(10) << "\n\n";					
    cout << "sqrt(64)     = " << sqrt(64) << "\n";						

    _getch();
}
```