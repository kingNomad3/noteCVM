# DunderFunction

- Ils sont lier au cicle de vie de l'objet. ils sont appeler l'un apres l'autre.

__new__ : il est appelé avant __init__ et est utilisé pour créer une nouvelle instance de la classe. Il est également utilisé pour créer des classes immuables. TJRS appeler, constructeur
__init__ : il est appelé après __new__ et est utilisé pour initialiser l'instance de la classe. TJRS appeler, initialisateur
__del__ : il est appelé avant la suppression de l'instance de la classe. TJRS appeler, destructeur. On ne devrait pas utiliser celui la car il est difficile de savoir quand il sera appeler.


# representation des objets

__str__(self)->str : il est appelé par la fonction print() pour afficher l'objet. c'est la conversion de l'objet sous forme character Il doit retourner une chaîne de caractères, in humain readerble
__repr__(self)->str : il est appelé par la fonction repr() pour afficher l'objet. onversion sous forme de caractere Il doit retourner une chaîne de caractères. representation technique (codeux)
__format__(self, format:str)->str : il est appelé par la fonction format() pour afficher l'objet. Il doit retourner une chaîne de caractères. String format, customizer notre string


# operation mathematique

- Conversion de l'objet en un autre type

__int__(self)->int : il est appelé par la fonction int() pour convertir l'objet en entier. Il doit retourner un entier.
__float__(self)->float : il est appelé par la fonction float() pour convertir l'objet en flottant. Il doit retourner un flottant.
__complex__(self)->complex : il est appelé par la fonction complex() pour convertir l'objet en complexe. Il doit retourner un complexe.
__bool__(self)->bool : il est appelé par la fonction bool() pour convertir l'objet en booléen. Il doit retourner un booléen.


# operation de conteneur
__eq__ : a==b, 
__lt__ : a<b, nous pouvons appeler la fonction sort sur notre objet 



__len__(self)->int : il est appelé par la fonction len() pour retourner la longueur de l'objet. Il doit retourner un entier.



# operation sur les sequences
__next__(self) : il est appelé par la fonction next() pour retourner l'élément suivant de l'objet. Il doit retourner l'élément suivant de l'objet. Il doit lever l'exception StopIteration si l'objet n'a pas d'élément suivant.
__iter__(self) : il est appelé par la fonction iter() pour retourner un itérable de l'objet. Il doit retourner un itérable de l'objet.
__reversed__(self) : il est appelé par la fonction reversed() pour retourner un itérable inversé de l'objet. Il doit retourner un itérable inversé de l'objet.

# bufer circulair

- nous avons 10 espaces, lorsque nous arrivons a 10, nous revenons a 0

