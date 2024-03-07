# Notes sur les Opérateurs de Condition et les Structures de Contrôle en C++

Les opérateurs de condition et les structures de contrôle permettent d'exécuter des instructions en fonction de conditions spécifiques. Voici quelques exemples d'utilisation en C++ :

## Switch-Case

### Exemple 1 : Utilisation du Switch-Case avec un entier

```cpp
int x = 2;
switch (x)
{
    case 1:
        cout << "choix 1";
        break;

    case 2:
        cout << "choix 2";
        break;

    case 3:
    case 4:
        cout << "choix 3 ou choix 4";
        break;

    case 5:
        cout << "choix 5";
        break;

    default:
        cout << "choix autre que 1, 2, 3, 4, 5";
}
```
## Utilisation du Switch-Case avec un caractère
```cpp
char note = 'B';

switch (note)
{
    case 'A': 
        cout << 'A' << " = Excellent";
        break;
    case 'B':
        cout << 'B' << " = Tr\x8as bien";
        break;
    case 'C':
        cout << 'C' << " = Bien";
        break;
    case 'D':
        cout << 'D' << " = Passable";
        break;
    case 'E':
        cout << 'E' << " = \220chec";
        break;
    default:
        cout << note << " = invalide";
}
```

## Utilisation du Switch-Case pour attribuer des points à un coureur F1
```cpp
unsigned int position, points;

switch (position)
{
    case 1:  points = 25; break;
    case 2:  points = 18; break;
    case 3:  points = 15; break;
    case 4:  points = 12; break;
    case 5:  points = 10; break;
    case 6:  points = 8;  break;
    case 7:  points = 6;  break;
    case 8:  points = 4;  break;
    case 9:	 points = 2;  break;
    case 10: points = 1;  break;
    default: points = 0;
}
```

## Utilisation du Switch-Case avec des instructions multiples
```cpp
unsigned int ouaragan_force = 3;

switch (ouaragan_force)
{
    case 5:	cout << " - Destruction des toitures, des portes et des fen\x88tres."							<< endl;
    case 4:	cout << " - Dommages importants \x85 la structure des batiments."								<< endl;
    case 3:	cout << " - Dommages importants \x85 la v\x82g\x82tation et des grands arbres d\x82racin\x82s."	<< endl;
    case 2:	cout << " - Petites embarcations arrach\202es de leurs amarres."								<< endl;
    case 1:	cout << " - Innondation coti\x8ares et dommages aux rives et aux quais."						<< endl;
}
```

## Utilisation du Switch-Case et de l'opérateur conditionnel ternaire
```cpp
int a = 10, b = 200, c = 30;
int e = 2, t;

switch (e)
{
    case 1: t = (a + b) * c1 + 15; break;
    case 2: t = (a + b) * c2 + 15; break;
    case 3: t = (a + b) * c3 + 15; break;
}
```