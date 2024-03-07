# Notes sur les Booléens en C++

## 1. Introduction
Les booléens en C++ sont des variables de type `bool` pouvant prendre les valeurs `true` (vrai) ou `false` (faux). Ils sont souvent utilisés dans les tests logiques et les opérations de comparaison.

## 2. Utilisation des Booléens
### Exemple 1 - Affichage de Booléens
```cpp
bool reponse; // entier sur 1 octet

reponse = false;
cout << reponse << endl; // affiche 0 pour false

reponse = true;
cout << reponse << endl; // affiche 1 pour true
```

# BON À SAVOIR
- En C++, l'entier zéro représente la valeur "false". Tous les autres entiers sont considérés comme la valeur "true".

```cpp
reponse = 0;
cout << reponse << endl; // affiche 0

reponse = 1;
cout << reponse << endl; // affiche 1

reponse = 4;
cout << reponse << endl; // affiche 1

reponse = -4;
cout << reponse << endl; // affiche 1
```
# Manipulateurs pour Afficher ou Non le Booléen en Texte
```cpp
cout << boolalpha;		// pour afficher: "true" ou "false"
cout << noboolalpha;	// pour afficher:  "1"   ou  "0"
```
# 3. Comparaisons de Chaînes de Caractères avec Booléens
- Exemple 2 - Comparaisons de Chaînes de Caractères
```cpp
string texte_1, texte_2;
bool resultat;

texte_1 = "Bonjour";
texte_2 = "bonjour";

resultat = texte_1 != texte_2;	// true
cout << resultat << endl;

resultat = texte_1 == texte_2;	// false
cout << resultat << endl;
```

# ATTENTION: Ordre Lexical
- Les comparaisons de chaînes de caractères sont sensibles à l'ordre lexical (majuscules avant minuscules).

# 4. Opérateurs de Comparaison avec Booléens
## Exemple 3 - Opérateurs de Comparaison

```cpp
int x = 10, y = 20, z = 10;
bool resultat;

resultat = x < y;		// true
cout << resultat << endl;

resultat = x < z;		// false
cout << resultat << endl;

resultat = x <= z;		// true
cout << resultat << endl;

resultat = x != y;		// true
cout << resultat << endl;

resultat = x != z;		// false
cout << resultat << endl;

resultat = x == z;		// true
cout << resultat << endl;

resultat = (x * y) <= (z * z);	// false
cout << resultat << endl;
```

## 5. Autres Tests avec Booléens
```cpp
bool resultat = false;

resultat = resultat == false;	// true
cout << resultat << endl;

resultat = resultat != true;	// false
cout << resultat << endl;
```
## bool avec les string 
```cpp
// VARIABLES
	string texte_1, texte_2;
	bool resultat;

	// TESTS

	texte_1 = "Bonjour";
	texte_2 = "bonjour";

	resultat = texte_1 != texte_2;				// true
	cout << resultat << endl;

	resultat = texte_1 == texte_2;				// false
	cout << resultat << endl;


	// ATTENTION: ordre lexical, majuscule avant minuscule

	texte_1 = "Allo";
	texte_2 = "allo";

	resultat = texte_1 < texte_2;				// true
	cout << resultat << endl;

	texte_1 = "estelle";
	texte_2 = "paul";

	resultat = texte_1 < texte_2;				// true
	cout << resultat << endl;

	_getch();
```