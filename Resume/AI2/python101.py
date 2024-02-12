import re
# ceci est un commentaire
x =2 # commentarie
x = y = z = 5



# • Exercices
# (-b +/- math.sqrt(b**2 - 4*a*c)) / (2 * a)
# ou
# a= -5.6
# b = 31.1
# c= 9-2
# -b+(b**2 -4*a*c)**(1/2))/(2a)

# 1. 4x2 + 17x - 1 = 0, x = ?
#     (-17+math.sqrt(17**2-4*4*-1))/2*4
#     0.9284983931459578

# 2. -5.6x2 + 31.1x + 9 = 2, x = ?
#     (-31.1 + math.sqrt(31.1**2 - 4*-5.6*7)) / (2 * -5.6)
#     -0.21663021121832812

# 3. 8x2-1265.789x = 0, x = ?
#     a = 8
#     b = -1265.789
#     c = 0

#     (-1265.789 + math.sqrt(-1265.789**2-4*8*0))
#     no root

# 4. L'aire d'un cercle ayant pour diamètre 3.64m
# (indice, utilisez math.pi)

#      import math 
#     -y = 4*math.pi * (x/2)**2

# 5. L'aire extérieur d’un prisme rectangulaire aux
# dimensions suivantes: 4.5cm, 7cm, 12.75cm.

#     largeur = 7
#     longueur = 4.5
#     hauteur = 12.75

#     2*(longueur*largeur) + 2*(longueur*hauteur) + 2*(largeur * hauteur)

# 6. Volume d'un tipi ayant un rayon de 2.176 m et
# une hauteur de 3.5m.
#     (math.pi *2.176**2 *3.5)/3
#     17.35459345261132

# Chaine
    # - sois guillemet simple ou double 

# 'je suis "stupide" '


# • Exercices
# 1. Trouvez comment inverser une chaîne.

# >>> text = "allo" [::-1]
# >>> print(text)

# 2. Si on a des variables dont on veut insérer les
# valeurs dans une chaîne formatée, python
# nous permet de le faire, comment?

# # >>> test = 'une valeur de %s'
# >>> x = ' une string %s avec '
# >>> y = "valeur"
# >>> x % test % y
# ' une string une valeur de valeur avec '

nom = "Alice"
age = 30

# Utilisation de la méthode .format()
message = "Bonjour, je m'appelle {} et j'ai {} ans.".format(nom, age)
# ----------------------------------------------
nom = "Alice"
age = 30

# Utilisation des f-strings
message = f"Bonjour, je m'appelle {nom} et j'ai {age} ans."




# 3. Comment isoleriez-vous la chaîne « les » à
# partir de la chaîne « Allo les amis ! »?


chaine = "Allo les amis !"

# Isoler la sous-chaîne "les" en utilisant l'indexation
sous_chaine = chaine[5:8]


chaine = "Allo les amis !"

# Diviser la chaîne en mots en utilisant la méthode .split()
mots = chaine.split()

# Isoler la sous-chaîne "les" en accédant au deuxième mot
sous_chaine = mots[1]

# Listes

# 1. Dans quel contexte utiliserait-on l[:] = [] plutôt que l = []?


liste1 = [1, 2, 3]
liste2 = liste1  # Les deux variables référencent la même liste

# Si vous affectez simplement une nouvelle liste à l'une des variables,
# cela ne modifie pas l'autre variable
liste1 = []

print(liste2)  # Affiche toujours [1, 2, 3]

# En revanche, si vous utilisez la notation l[:] = [],
# cela modifie directement la liste référencée par les deux variables
liste1[:] = []


# 2. Construisez un tableau de zéros de 2 X 5 avec des listes, au moins de deux manières différentes.


tableau_zeros = [[0] * 5 for _ in range(2)]
print(tableau_zeros)

tableau_zeros = [[0] * 5] * 2

print(tableau_zeros)





#  Nombre de mois
mois = 18

# Initialisation des nombres de paires de lapins pour les deux premiers mois
f0 = 1  # Au mois 0, on a une paire de lapins nouveau-nés
f1 = 1  # Au mois 1, on a une paire de lapins nouveau-nés qui deviennent adultes

# Initialisation du nombre total de paires de lapins
total_paires = 0

# Boucle pour calculer le nombre de paires de lapins pour chaque mois
for i in range(2, mois + 1):
    # Calcul du nombre de paires de lapins pour le mois actuel en utilisant la formule de Fibonacci
    fn = f0 + f1
    
    # Mise à jour des valeurs pour le prochain mois
    f0 = f1
    f1 = fn
    
    # Ajout du nombre de paires de lapins pour ce mois au total
    total_paires += fn

# Affichage du nombre total de paires de lapins après 18 mois
print("Le nombre total de paires de lapins après 18 mois est :", total_paires)

def fib_recursive(n):
    # Cas de base : les deux premiers nombres de Fibonacci sont 1
    if n <= 1:
        return 1
    else:
        # Appel récursif pour calculer le n-ième nombre de Fibonacci en additionnant les deux nombres précédents
        return fib_recursive(n-1) + fib_recursive(n-2)

# Test de la fonction fib() récursive pour calculer le 10e nombre de Fibonacci
resultat_recursif = fib_recursive(10)
print("Le 10e nombre de Fibonacci (récursif) est :", resultat_recursif)



def fib_dynamique(n):
    # Initialisation du tableau de mémoïsation pour stocker les valeurs déjà calculées
    memo = {}

    # Cas de base : les deux premiers nombres de Fibonacci sont 1
    memo[0] = memo[1] = 1

    # Boucle pour calculer les nombres de Fibonacci pour les valeurs de n supérieures à 1
    for i in range(2, n + 1):
        # Calcul du nombre de Fibonacci pour la valeur de n en utilisant la programmation dynamique
        memo[i] = memo[i-1] + memo[i-2]

    # Retourner le résultat pour n
    return memo[n]

# Test de la fonction fib() avec programmation dynamique pour calculer le 10e nombre de Fibonacci
resultat_dynamique = fib_dynamique(10)
print("Le 10e nombre de Fibonacci (dynamique) est :", resultat_dynamique)


# Qu’arrive-t-il lorsqu’on lance la fonction fibonacci récursive sur de grosses valeurs?
# Par exemple, 40…
# Solution?
# Itération
# Programmation dynamique

# L'approche itérative consiste à calculer les nombres de Fibonacci à partir des deux premiers termes (1 et 1) en utilisant une boucle pour itérer jusqu'au nombre désiré. Cela évite la surcharge d'appels de fonction récursive.

# Programmation dynamique :
# Dans cette approche, vous stockez les résultats intermédiaires des nombres de Fibonacci déjà calculés dans une table de mémoïsation. Lorsque vous devez calculer le n-ième nombre de Fibonacci, vous vérifiez d'abord s'il est déjà calculé dans la table de mémoïsation. Si c'est le cas, vous le récupérez à partir de là plutôt que de le recalculer. Cela élimine la redondance des calculs et améliore considérablement les performances.

# Voici comment vous pouvez implémenter ces deux solutions en Python :

# Itération :
# python

def fib_iteratif(n):
    a, b = 1, 1
    for _ in range(n - 1):
        a, b = b, a + b
    return a

# Test de la fonction fib() itérative pour calculer le 40e nombre de Fibonacci
resultat_iteratif = fib_iteratif(40)
print("Le 40e nombre de Fibonacci (itératif) est :", resultat_iteratif)
# Programmation dynamique :
# python


# def fibdyne(n,solutions):
#     if n not in solutions:

#     return solutions[0]

def fib_dynamique(n):
    memo = {}
    memo[0] = memo[1] = 1
    for i in range(2, n + 1):
        memo[i] = memo[i-1] + memo[i-2]
    return memo[n]

# Test de la fonction fib() avec programmation dynamique pour calculer le 40e nombre de Fibonacci
resultat_dynamique = fib_dynamique(40)
print("Le 40e nombre de Fibonacci (dynamique) est :", resultat_dynamique)





# lire les text
from sys import argv

def lire(chemin, encodage):
    f = open(chemin, 'r', encodage=encodage)
    text = f.read()
    f.close()
    
    return text

def main():
    chemin = argv[1]
    encodage= argv[2]
    text = lire(chemin, encodage)
    
    print(text)
    
    return 0

if __name__ == '__main__':
    main()


def compter_lignes(nom_fichier):
    with open(nom_fichier, 'r', encoding='utf-8') as fichier:
        lignes = fichier.readlines()
    return len(lignes)


nb_lignes = compter_lignes("LesTroisMousquetaires.txt")
print("Nombre de lignes dans le fichier:", nb_lignes)


def compter_caracteres(nom_fichier):
    with open(nom_fichier, 'r', encoding='utf-8') as fichier:
        contenu = fichier.read()
    return len(contenu)

nb_caracteres = compter_caracteres("LesTroisMousquetaires.txt")
print("Nombre de caractères dans le fichier:", nb_caracteres)

def compter_mots(nom_fichier):
    with open(nom_fichier, 'r', encoding='utf-8') as fichier:
        contenu = fichier.read()
    mots = contenu.split()
    return len(mots)

nb_mots = compter_mots("LesTroisMousquetaires.txt")
print("Nombre de mots dans le fichier:", nb_mots)


def compter_virgules(nom_fichier):
    with open(nom_fichier, 'r', encoding='utf-8') as fichier:
        contenu = fichier.read()
    nb_virgules = contenu.count(',')
    return nb_virgules

nb_virgules = compter_virgules("LesTroisMousquetaires.txt")
print("Nombre de virgules dans le fichier:", nb_virgules)



# Exercices
# Créer une classe qui peut lire 'LesTroisMousquetaires.txt' et qui peut 'répondre' aux messages suivants:
# Nombre de caractères
# Nombre de lignes
# Nombre de mots
# Nombre de séquences de caractères s, où s est fournie en argument


class AnalyseurTexte:
    def __init__(self, nom_fichier):
        self.nom_fichier = nom_fichier
        self.contenu = self.lire_fichier()

    def lire_fichier(self):
        with open(self.nom_fichier, 'r', encoding='utf-8') as file:
            contenu = file.read()
        return contenu

    def compter_caracteres(self):
        return len(self.contenu)

    def compter_lignes(self):
        return self.contenu.count('\n') + 1

    def compter_mots(self):
        return len(self.contenu.split())

    def compter_sequences(self, sequence):
        return self.contenu.count(sequence)


# Utilisation de la classe pour analyser le fichier LesTroisMousquetaires.txt
analyseur = AnalyseurTexte("LesTroisMousquetaires.txt")

# Exemple d'utilisation des méthodes de la classe
print("Nombre de caractères:", analyseur.compter_caracteres())
print("Nombre de lignes:", analyseur.compter_lignes())
print("Nombre de mots:", analyseur.compter_mots())

# Exemple d'utilisation de la méthode pour compter le nombre de séquences de caractères
sequence_a_compter = 'Athos'
print(f"Nombre de séquences de '{sequence_a_compter}':", analyseur.compter_sequences(sequence_a_compter))
