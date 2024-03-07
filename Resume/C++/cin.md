# Notes sur l'utilisation de cin en C++

## 1. Conversion de Livres en Kilogrammes
```cpp
#include <iostream>  // pour le cout
#include <conio.h>   // pour le _getch()

using namespace std;

int main()
{
	// CONSTANTES
	const double TAUX_DE_CONVERSION = 0.453592;

	// VARIABLES
	double poids_lb; // lue du clavier
	double poids_kg; // calculé par le programme

	// INPUT
	cout << "Quel est le poids en livres ? ";
	cin >> poids_lb;		// Attention: l'utilisateur doit appuyer sur Enter, ce qui provoque aussi un changement de ligne

	// TRAITEMENT
	poids_kg = poids_lb * TAUX_DE_CONVERSION;

	// OUTPUT
	cout << "\n" << poids_lb << " lb --> " << poids_kg << " kg" << "\n";

	_getch();
}
```

### Explication :
- Objectif: Convertir un poids de livres en kilogrammes.
- Déclaration des Constantes et Variables: const double TAUX_DE_CONVERSION = 0.453592;, double poids_lb, poids_kg;
- Entrée: Utilisation de cin pour obtenir le poids en livres.
- Calculs: Conversion du poids en kilogrammes.
- Sortie: Affiche le poids en livres et en kilogrammes.
## 2. Saisie d'Information sur une Ville

```cpp
#include <iostream>	// pour le cout
#include <conio.h>	// pour le _getch()
#include <string>	// pour le type string

using namespace std;

int main()
{
	// VARIABLES
	int population = 0;
	string ville = ""; // initialisée à la chaine vide ""

	// INPUT
	cout << "Ville ? ";
	cin >> ville;				// Attention: ne pas mettre de blanc dans le nom. Le trait d'union pour les noms composés

	cout << "Population ? ";
	cin >> population;

	// OUTPUT
	cout << "\n" << ville << " est une jolie ville de " << population << " habitants !" << "\n";

	_getch();
}
```

### Explication :
- Objectif: Saisir des informations sur une ville (nom et population).
- Déclaration des Variables: int population = 0;, string ville = "";
- Entrée: Utilisation de cin pour obtenir le nom de la ville et sa population.
- Sortie: Affiche le nom de la ville et sa population.

## Conclusion
- cin est utilisé pour recevoir des entrées de l'utilisateur.
- L'opérateur >> est utilisé avec cin pour stocker la valeur entrée dans une variable.
Attention aux espaces dans les saisies pour éviter des comportements indésirables.


# Notes sur le Programme C++ de Démo

## 1. Introduction
Le programme C++ de démo effectue la saisie de données utilisateur et affiche différentes informations formatées. Chaque concept clé est expliqué ci-dessous.

## 2. Constantes et Variables
- **Constantes :**
  - `carac`: Un caractère défini en hexadécimal (\x41).
  - `entier`, `entierCourt`, `entierLong`: Variables entières de différents types.
  - `reel`, `reelDouble`: Variables à virgule flottante de différents types.
  - `sansSigne`: Variable entière non signée.
  - `titre1`, `titre2`, `titre3`: Chaînes de caractères décrivant les sections du programme.

- **Variables :**
  - `prenom`, `nom`, `numeroGroupe`: Variables de type chaîne de caractères pour stocker les données de l'utilisateur.

## 3. Saisie d'Utilisateur (Input)
- Utilisation de `cin` pour récupérer les valeurs de `prenom`, `nom`, et `numeroGroupe` depuis l'utilisateur.

## 4. Affichage de Données (Output)
### Section 1 - Essai du cadrage à gauche et de la notation en virgule flottante:
- Utilisation de `cout` avec `left` pour l'alignement à gauche.
- Utilisation de `setw` pour définir la largeur des champs.
- Affichage de variables entières et à virgule flottante.

### Section 2 - Essai du cadrage à droite et de la notation scientifique:
- Utilisation de `cout` avec `right` pour l'alignement à droite.
- Affichage de variables entières, à virgule flottante en notation scientifique.

### Section 3 - Essai de mise en page:
- Affichage de variables avec différentes bases (hexadécimale).
- Utilisation de `setw` et `fixed` pour un affichage formaté.

## 5. Message de Salutation
- Utilisation de `cout` pour afficher un message de salutation personnalisé avec les données saisies.

## 6. Fonction `_getch()`
- Utilisation de `_getch()` pour maintenir la console ouverte jusqu'à ce qu'une touche soit pressée.

## 7. Conclusion
Ce programme démontre la saisie d'utilisateur, l'affichage de données formatées, l'utilisation de constantes et variables de différents types, ainsi que la mise en page avancée.


```cpp
/*
* Auteur		: Benjamin Joinvil
	Description	: 
	Input		: 
	Output		:
	Version		: 1.0

*/
using namespace std;

#include <iostream>  // pour le cout
#include <conio.h>   // pour le _getch()
#include <string> // pour le type 
#include <iomanip>

int main() {
	//variable
	string prenom = "";
	string nom = "";
	string numeroGroupe = "";

	// constante
	char carac = '\x41';
	int entier = 75000;
	short entierCourt = -42;
	long entierLong = 57000;
	float reel = 123.456;
	double reelDouble = 12.0123456789;
	unsigned int sansSigne = 54321;
	string titre1 = "Essai du cadrage \x85 gauche et de la notation en virgule flottante:"; 
	string titre2 = "Essai du cadrage \x85 droite et de la notation scientifique:";
	string titre3 = "Essai de mise en page:";
		

	//input
	cout << "Taper votre pr\x82nom:";
		cin >> prenom;
	cout << "taper votre nom:";
		cin >> nom;
	cout << "taper votre num\x82ro de groupe:" ;
	cin >> numeroGroupe; cout << "\n";

 //output
	cout << left << titre1; "\n";
	cout << left << "\n" << setw(8) << entier << setw(7) << entierCourt << setw(8) << entierLong << setw(8) << sansSigne << setw(8) << carac;
	cout << left << "\n" << setw(8) << setprecision(5) << reel << setw(10) << setprecision(4) << reelDouble;

	cout << "\n\n";  
	cout << right << titre2; "\n";
	cout << right << "\n" << setw(12) << entier << ' ' << setw(8) << entierCourt << setw(12) << entierLong << setw(12) << sansSigne << setw(14) << carac;
	cout << right << "\n"<< setw(4) << ' ' << scientific << reel << "\t" << setw(6) << reelDouble;

	cout << "\n\n";
	cout << titre3;
	cout << "\n\t" << "entier\t\t = " << hex << entier; 
	cout << "\n\t" << "entierCourt\t = " << hex << entierCourt;
	cout << "\n\t" << "entierLong\t = " << hex << entierLong;
	cout << "\n\t" << "SansSigne\t = " << hex << sansSigne;
	cout << "\n\t" << "carac\t\t = " << carac;
	cout << "\n\t" << "reel\t\t ="<< setw(11) <<fixed << setprecision(3) << reel;
	cout << "\n\t" << "reelDouble\t =" << setw(11) << fixed << reelDouble;
		

	cout << "\n\nSalut"<<' '<< nom << ' ' << prenom << ' ' << "du groupe" << ' ' << numeroGroupe << "!";

}
```

```cpp
int main()
{
	// VARIABLES
	int jour, mois, annee;

	// INPUT
	cout << "Entrez votre date de naissance (jj mm aaaa) : ";
	cin >> jour >> mois >> annee;			// Lecture en cascade -- attention --> mettre au moins un blanc entre chaque nombre lors de l'entrée

	// OUTPUT
	cout << "\n" << "date de naissance lue : " << jour << "-" << mois << "-" << annee << " !";

	_getch();
}
```