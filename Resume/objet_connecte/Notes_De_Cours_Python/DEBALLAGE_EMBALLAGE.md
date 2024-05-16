# Emballage et Déballage

L'emballage (packing) et le déballage (unpacking) sont des concepts en Python qui permettent de manipuler des collections de données telles que les listes, les tuples ou les dictionnaires de manière flexible. Voici une explication concise avec des exemples : 

1. **Emballage (Packing)** : L'emballage consiste à regrouper plusieurs valeurs dans une seule collection. Cela se fait généralement avec des tuples, mais cela peut également se faire avec des listes ou des ensembles. Voici un exemple :

```python
# Emballage dans un tuple
my_tuple = 1, 2, 3  # Les valeurs sont automatiquement regroupées dans un tuple
print(my_tuple)     # Output: (1, 2, 3)

# Emballage dans une liste
my_list = [1, 2, 3]  # Les valeurs sont regroupées dans une liste
print(my_list)       # Output: [1, 2, 3]
```

2. **Déballage (Unpacking)** : Le déballage consiste à extraire les valeurs d'une collection (comme un tuple ou une liste) et à les assigner à des variables individuelles. Voici un exemple :
```python
# Déballage d'un tuple
my_tuple = (1, 2, 3)
a, b, c = my_tuple  # Les valeurs sont extraites du tuple et assignées à a, b et c
print(a, b, c)      # Output: 1 2 3

# Déballage d'une liste
my_list = [4, 5, 6]
x, y, z = my_list   # Les valeurs sont extraites de la liste et assignées à x, y et z
print(x, y, z)      # Output: 4 5 6
```

L'emballage et le déballage sont des fonctionnalités très utiles en Python, car elles permettent de manipuler les données de manière concise et efficace. Elles sont couramment utilisées dans divers contextes, tels que les fonctions renvoyant plusieurs valeurs, les boucles et les opérations sur les collections de données.