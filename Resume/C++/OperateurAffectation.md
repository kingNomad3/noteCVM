# Notes sur les Opérateurs d'Affectation en C++

Les opérateurs d'affectation sont utilisés pour attribuer une valeur à une variable. Voici les principaux opérateurs d'affectation en C++ :

- **Affectation (`=`)** : Cet opérateur attribue la valeur de l'expression de droite à la variable de gauche.

- **Affectation Additionnée (`+=`)** : Ajoute la valeur de l'expression à la variable.

- **Affectation Soustraite (`-=`)** : Soustrait la valeur de l'expression à la variable.

- **Affectation Multipliée (`*=`)** : Multiplie la variable par la valeur de l'expression.

- **Affectation Divisée (`/=`)** : Divise la variable par la valeur de l'expression.

- **Affectation Modulée (`%=`)** : Affecte à la variable le reste de la division par la valeur de l'expression.

## Exemples d'Utilisation

```cpp
int a, b, c;

// Affectation de valeurs initiales
c = b = a = 0;

// Opérations d'affectation combinées
c += 1;             // c = c + 1;
c += a * b;         // c = c + (a * b)
c -= 2 + a * 4;     // c = c - (2 + a * 4)
c *= 2 * c;         // c = c * (2 * c)
c /= a;             // c = c / a
c %= 10;            // c = c % 10
