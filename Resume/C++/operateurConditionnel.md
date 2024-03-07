# Notes sur les Opérateurs Conditionnels en C++

## Utilisation de l'Opérateur Conditionnel (`?:`)

L'opérateur conditionnel est utilisé pour évaluer une expression booléenne et retourner une valeur en fonction du résultat de cette évaluation.

### Syntaxe

```cpp
exp_bool ? exp_1 : exp_2
```
## Exemple 1 : Accorder un Mot au Pluriel
- Avec une Instruction if
```cpp
int nbVoituresMoy = 0;
cout << "Les familles possèdent en moyenne " << nbVoituresMoy << " voiture";
if (nbVoituresMoy >= 2)
    cout << "s";    // pour le pluriel
cout << "\n";
```
- Avec l'Opérateur Conditionnel
```cpp
int nbVoituresMoy = 0;
cout << "Les familles possèdent en moyenne "
     << nbVoituresMoy
     << " voiture"
     << ( nbVoituresMoy >= 2 ? "s" : "" )  // pour le pluriel
     << "\n";
```