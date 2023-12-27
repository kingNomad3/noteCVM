# Résumé des Sujets Expliqués

## 1. Conversion d'Années en Secondes
- **Objectif:** Convertir un nombre d'années en secondes.
- **Exemple:**
```cpp
  int années, secondes;
  années = 10;
  secondes = années * 365 * 24 * 60 * 60;
  cout << années << " ans" << " = " << secondes << " secs" << endl;

```

## 2. Conversion de Celsius en Fahrenheit
Objectif: Convertir une température de Celsius à Fahrenheit.
Exemple:
```cpp

const double TAUX = 9.0/5.0;
double celsius = 20.5, fahrenheit;
fahrenheit = (celsius * TAUX) + 32;
cout << celsius << " celsius" << " = " << fahrenheit << " fahrenheit" << endl;
```

## 3. Temps de Voyage à la Vitesse de la Lumière
Objectif: Calculer le temps de voyage vers le soleil à la vitesse de la lumière.
Exemple:
```cpp
const int LIGHTSPEED = 300000;
double km = 150000000, temps;
temps = km / LIGHTSPEED;
cout << "Temps moyen du voyage vers le soleil a la vitesse lumiere : " << temps << " secs" << endl;
```
## 4. Salutation à partir de Variables
Objectif: Saluer des étudiants avec des noms et prénoms stockés dans des variables.
Exemple:
```cpp
const string CEGEP = "Cegep du Vieux-Montreal";
string prenom = "Gustave", nom = "Sylvestre";
cout << "Bonjour " << prenom << " " << nom << ", bonne session au " << CEGEP << " !" << endl << endl;
```
## 5. Manipulation de Caractères
Objectif: Illustrer la manipulation de caractères en C++.
Exemple:
```cpp
const char HASHTAG = '#';
char voy_a = 'a', voy_e = '\145', voy_i = '\x69', voy_o = 111, voy_u = 0165, voy_y = 0x79;
cout << "Exemple " << HASHTAG << '1' << " les voyelles : ";
cout << voy_a << ", " << voy_e << ", " << voy_i << ", " << voy_o << ", " << voy_u << ", " << voy_y << endl;
```