# Notes sur l'Utilisation de la Fonction `getline()` en C++

## 1. Entrée avec `getline()` :
   - `getline(cin, variable)` est utilisé pour obtenir une ligne complète de texte à partir de l'entrée standard (`cin`) et la stocker dans une variable de type `string`.
   - Il est particulièrement utile lorsque l'entrée peut contenir des espaces, car `cin` s'arrête à la première occurrence d'un espace.
   - Exemple :
     ```cpp
     string nom;
     cout << "Entrez votre nom : ";
     getline(cin, nom);
     ```

## 2. Avantages de `getline()` :
   - Permet la saisie de lignes de texte complètes, y compris les espaces.
   - Évite les problèmes de tampon lorsque l'entrée contient des caractères spéciaux ou des espaces.
   - Utile pour la saisie de données de texte plus complexes, comme les noms, les adresses, etc.
   - Exemple :
     ```cpp
     string adresse;
     cout << "Entrez votre adresse : ";
     getline(cin, adresse);
     ```

## 3. Utilisation avec d'autres types de données :
   - Bien que souvent utilisé avec des variables de type `string`, `getline()` peut également être utilisé avec d'autres types de données.
   - Il peut être utilisé pour lire une ligne complète de texte et ensuite convertir cette chaîne en d'autres types de données si nécessaire.
   - Exemple :
     ```cpp
     int age;
     string ligne;
     cout << "Entrez votre age : ";
     getline(cin, ligne);
     age = stoi(ligne); // Convertit la chaîne en entier
     ```

## 4. Attention aux caractères de nouvelle ligne :
   - Lors de la lecture d'une ligne avec `getline()`, le caractère de nouvelle ligne (`\n`) reste dans le flux d'entrée.
   - Cela peut causer des problèmes si vous utilisez d'autres opérations d'entrée après `getline()`.
   - Il est souvent nécessaire de vider le tampon (`cin.ignore()`) après `getline()` pour éviter ces problèmes.
   - Exemple :
     ```cpp
     string commentaire;
     cout << "Entrez un commentaire : ";
     getline(cin, commentaire);
     cin.ignore(); // Vide le tampon pour éviter les problèmes ultérieurs
     ```

## 5. Conclusion :
   - `getline()` est une fonction puissante pour la saisie de lignes complètes de texte en C++.
   - Elle est particulièrement utile lorsque l'entrée peut contenir des espaces ou des caractères spéciaux.
   - Assurez-vous de gérer correctement le caractère de nouvelle ligne et de vider le tampon si nécessaire pour éviter les problèmes de flux d'entrée.

```cpp
int main()
{
	// VARIABLES
	int x = 28;
	string voiture_marque, voiture_modele, voiture_couleur;

	// INPUT AVEC GETLINE AU LIEU DE CIN QUAND C'EST DU TEXTE (string)
	// Attention: tout le texte, incluant les blancs, sera mis dans la variable
	
	cout << "\xB7 propos de votre voiture :" << "\n\n";

	cout << setw(x) << "Quelle est la marque ? ";
	getline(cin, voiture_marque);

	cout << "\n";
	cout << setw(x) << "Quelle est le mod\x8ale ? ";
	getline(cin, voiture_modele);

	cout << "\n";
	cout << setw(x) << "Quelle est la couleur ? ";
	getline(cin, voiture_couleur);

	// OUTPUT
	cout << "\n"  << "Votre voiture est une " << voiture_marque << " mod\x8ale " << voiture_modele << " de couleur " << voiture_couleur << " !" << "\n";

	_getch();
}
```