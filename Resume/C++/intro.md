# Note sur le Programme C++

## Code
```cpp
#include <iostream>
#include <conio.h>

using namespace std;

int main()
{
    cout << "Bonjour";
    cout << endl;
    // ... (autres messages)
    cout << "Salut";
    _getch();
```

# Résumé
## Objectif: Afficher des messages sur la console en utilisant C++.

### Fichiers d'En-tête:

- <iostream> : Opérations d'entrée et de sortie.
- <conio.h> : Inclut la fonction _getch().

### Espace de Noms:
- using namespace std;

### Fonction Principale:
- int main()

### Instructions d'Affichage:

- Utilisation de cout pour afficher des messages, dont "Bonjour" et "Salut".

### Pause pour une Saisie Utilisateur:
_getch() est utilisé pour attendre une pression de touche avant de fermer la console