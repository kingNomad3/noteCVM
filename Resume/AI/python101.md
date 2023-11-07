# Ptyhon 101

- language compiler: traduit en binarie, en code machine par le processeur, +performence, memire plus petit. pas de protable possible si on travail avec un OS will not work with another one. Exemple C++
- language interpretation: on peut l'utiliser sur n'importe quel environement par exemple python peut etre use sur l'ordi et sur un robot Tout les autres language a part c++

## norme de codage 
- Il exite des pep pour comprendre la base en python pep 8 nous donnes la norme de codage la plus mondials 

```python 
    #snake_case: variable, fonction...
    #PascalCase: types: (classe, enum, )
    #CONSTANT: il n'y a pas de variable constante, alors c'est pourquoi on le met en majuscule pour les identifies
    # en python tout est un objet, meme les functions, meme un entier
     
 ```   
  ## Recommendations
    - CALTAL: Code a little, test a little
    - DRY: Dont repeat Yourself
    - OFOT: one function, On Task
    - UMUD: yoU Must Use the Debugger

```Python
    # types fondamentaux
    #tout les type sont immuables*
    a = 4 #entier
    b = 3.15 #float
    c = False #bool
    d = 'allo' #str single and double quote same thing 
    e = 1+2j # nombre complex : deux float ensemble 
    f = None # NoneType
    y = #il existe des variantes de chacune comme les strings mais ne gros c;est ca
    z = # pas de char en python, c'est un string the lognegueyr 1

    #swipe - notion de binding 
    a,b = 10,100
    a,b = b,a
```
## Structures de donnes INCLUSES
    - la plus part des elements sont dans le core du language, lorsqu'on utilise import alors il ne fat pas partie du core. Par exemple C++ n'a pas de core, exemple #include <iostream>
                                            using namespace std;

- il n'y a pas de matrice 2 d alors on utilise une liste de liste
```python           
 # structures de données INCLUSES                 print(my_string[1] = 'L')
#                            type  | immutable | subscritable[read/write] | iterable | duplicate
#                                  | constant  | indexable[read/write]    | itérable | doublon
my_string = 'allo'         # str   |     x     | oui/non                  | oui      | oui
my_list = [0, 1, 2, 3, 4]  # list  |     ok    | oui/oui                  | oui      | oui
my_tuple = (0, 1, 2, 3, 4) # tuple |     x     | oui/non                  | oui      | oui
my_set = {0, 1, 2, 4, 4}   # set   |     ok    | non/non                  | oui      | non 
my_dict = { 0:'zero',      # dict  |     ok    | oui/oui                  | oui      | non:oui
            1:'un', 
            2:'deux', 
            3:'trois', 
            4:'quatre'} # dict
my_bytes = bytes([0, 10, 100])   # |     x     | oui/non                  | oui      | oui
my_array = bytearray([0, 10, 100])#|     ok    | oui/oui                  | oui      | oui
```
- on peut mettre n;importe quoi dans une liste, string, entier, set dict et chaque element de la lsite peuvent de type different. De dimmention variable, taille dynamique. 
- Un tuble est la meme chose qu'une liste, mais ne peut pas etre modifie
- Un tuble est la meme chose qu'une liste, mais ne peut pas etre modifie
- les tubles sont legerement plus performent 

## iterator -concept

```python
#pas du vrai python
# i = my_liste.iterator()
#while it != my_list.last_iterator():
#   print(it) <<< it donne acces a la prochaine valeur
#   it+= 1

for char in my_string:
    print(char)
for value in my_list: 
    print(value)
for value in my_tuple: 
    print(value)
for value in my_set: 
    print(value)
# for value in my_dict:
# for value in my_dict.values():
# for key in my_dict.keys():
for key, value in my_dict.items(): # binding
    print(key, value)
for value in my_bytes: 
    print(value)
for value in my_array: 
    print(value)
```
```python
my_data = [[1,0],[0,1]]

for data in my_data
    print(data)
for x,y in my_data
    print(x,y)
        # resultat 1 0
        #          0 1
for i, value in enumerate(my_list):
    print(f'La {i:^5}e valeur est {value}')

my_list1 = [0, 1, 2, 3, 4]
my_list2 = [10, 11, 12, 13, 14]

for val1, val2 in zip(my_list1, my_list2):
    print(f'{val1=} -> {val2=}')
    


#format string
int = 0
for value in my_liste
    print(f'La {i:10}e valeur est {value}')
    i+=1
pass
for value in my_liste
    #padding a  gauche et < padding a droite 
    #^ va mettre des esapces entre chacun des string
    print(f'La {i>10}e valeur est {value}')
    i+=1
    print(f'{value=}')
         #values=4

int = 0
for i,value in enumerate(my_liste)
    print(f'La {i>10}e valeur est {value}')
    i+=1

#traverser deux tableua a la fois, zip doit etre de taill pareil
my_list1 = [0,1,2,3,4]
my_list2 = [10,11,12,13,14]
i = 0
for val1,val2 in zip(my_list1, my_list2):
    print(f'La {val1=} -> {val2}')
    i+=1
```

# comprehension liste
```sql
my_list2 = [10, 11, 12, 13, 14]
# comprehension list
# 
# my_list = [ _expression_ for _member_ in _iterable_ (if _condition_) ] # () optional
# équivalent à 
# my_list = []
# for _member_ in _iterable_:
#   if _condition_:
#       my_list.append(_expression_)
val = 11
val = 1 if val == 0 else 2
print([i for i in range(10)])
print([i*2 for i in range(10)])
print([i**2 for i in range(10)])
print([i if i < 5 else 0 for i in range(10)])
print([i for i in range(10) if not i % 2])
print([0 for _ in range(10)])
```

exercice game of life

- faire un matrice de taille m x n. w,h:[3,2000] 
- sois vivant sois mort 0 ou 1 allumer ou eteint
- randome du contenue de la matrice 
- game of life, pour 1 cellule cmb des 8(qui sont autour) sont vivent, si 1  and nbvivant = 2 OR 3 then vivant else 0
if 0 
    if nbvivant = 3
        1
        else
        0

- il faut ignorer le contour il sont tjrs 0
- hint 2 matrice 


## variable membre VS variable global 

```python
# va vivre dans tout le code 
glo = 5
class GOLEngine:
    # variable local
    def __init__(self,with,height):
            # la variable w n'existe plus a l'exterieur de la fonction  
        w =with
            # la varaible va mourrire lorsque l'objet va mourrir, une varaible membre si on passe par l'objet courant 
        self.with = with