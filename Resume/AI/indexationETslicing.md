# indexation et slicing

```python
#l'indexation sont les crochets
my_list = [i**2 for i in range(10)]
print(my_list[0])
print(my_list[3])
print(my_list[6])
print(my_list[-1])
print(my_list[-2])

#slicing
#va montrer les valeur de l'index 0 a 3 le 4 n'est pas inclus
print(my_list[0:4])
print(my_list[2:6])
print(my_list[:6])
print(my_list[2:9]) 
#Le derier index ne sera pas inclus alors on peut faire:
print(my_list[2:])
#un troisieme element peut etre preciser un step se sont des bon de deux dans ce cas ci 
print(my_list[2:6:2])
#du deux jusqu au dernier, mais le dernier est exclus
print(my_list[2:-1:2])
#le dernier sera inclus 
print(my_list[2::2])
#on peut reculer avec un indicce negatif, dernier exclue
print(my_list[-1:0:-1])
#dernier inclue
print(my_list[-1::-1])
```
# Notion de reference et garbage colector, immuable, ...
```python
a=5
b=5
# retourne le nom de la classe en String, alors on voit, float, int String etc sont tous des classes 
print (type(a)) #int
print (type(b) #int
print (type("allo"))) # String 
#un identifiant unique de l'objet referer par la variable
# la varaible a et b seront a la meme place memoire, a et b ne sont pas des entiers mais des references vers des entiers. car les deux sont 5
print (id(a))
print (id(b))

# tout les types fondamenteaux sont immuables, l'adresse memoire est immuable mais pas les references a et b

#ne change rien, reste tell quel 
b = a
print (id(a))
print (id(b))


a =3 #b a pas changer mais a a changer
print (id(a))
print (id(b))

#si  la valeur 5 n'est plus assigner, le garbage colector va chercher la valeur on ne sait pas quand. Si on veut reassigner une 5 une nouvelle espace memoire (on ne sait jamais ou)
#sera donner 

a *= 3 # une nouvelle instance et un nouvelle objet l'espace va changer 
print (id(a))
print (id(b))

#une nouvelle address sera donner et l'ancienne valeur sera jeter de la memoire mais on ne sait pas quand 
a = "allo" 
print (id(a))
print (id(b))

# n;est pas la meme adresse memoire
a += 'maman'
print (id(a))
print (id(b))

a = [4,5,6]
b =a 
#hex va convertir en hexadecimal
#l'adresse sera une liste qui pointes vers des references qui pointe vers des addresse. c'est l'Assignation dynamique  
print (hex(id(a)))
print (hex(id(b)))

# se sera la meme addresse car nous changent la reference et non l'addresse 
a[0] = 777 
print (hex(id(a)))
print (hex(id(b)))

#toujours la meme liste 
a.append(777)
print (hex(id(a)))
print (hex(id(b)))

#ne sera pas la meme addresse, car est egal a une nouvelle liste
a = [777,5,6]
print (hex(id(a)))
print (hex(id(b)))



# detruire une variable
del a
#un element de la liste a l'index 1
del a[1]

#shadow copy 
from copy importe deepcopy
a = [0,1,2]
b =a 
# ils vont pointer vers la meme place se qu;on appel shalloq cmpy
print (hex(id(a)))
print (hex(id(b)))

b = deepcopy(a) 
# deepcopy
print (hex(id(a)))
print (hex(id(b)))



```