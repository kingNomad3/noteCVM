
# Calcul du Nombre de Fibonacci en Python

Ce document explique et compare trois méthodes pour calculer les nombres de Fibonacci en Python : itérative, récursive et dynamique.

## Importation des Modules Nécessaires

```python
from sys import argv
from time import time
```

## Méthodes de Calcul de Fibonacci

### Fibonacci Itératif

La fonction `fibiter` utilise une approche itérative pour calculer le nombre de Fibonacci. C'est la méthode la plus directe et efficace pour les grands nombres.

```python
def fibiter(n):
    f2 = f1 = fn = 1
    while n >= 2:
        fn = f1 + f2
        f2 = f1
        f1 = fn
        n -= 1
    return fn
```

### Fibonacci Récursif

La fonction `fibrec` utilise la récursivité. Bien que conceptuellement simple, cette méthode peut être inefficace pour de grands nombres en raison de sa complexité exponentielle.

```python
def fibrec(n):
    if n == 0 or n == 1:
        return 1
    return fibrec(n-1) + fibrec(n-2)
```

### Fibonacci Dynamique (Mémoïsation)

La fonction `fibdyn` emploie la programmation dynamique avec mémoïsation pour améliorer l'efficacité de la méthode récursive, en stockant les résultats des calculs précédents.

```python
def fibdyn(n, solutions = {0:1, 1:1}):
    if n not in solutions:
        solutions[n] = fibdyn(n-1, solutions) + fibdyn(n-2, solutions)
    return solutions[n]
```

## Fonction Principale

La fonction `main` utilise les arguments de la ligne de commande pour déterminer quel nombre de Fibonacci calculer, et mesure le temps d'exécution de chaque méthode.

```python
def main():
    n = int(argv[1])
    
    t = time()
    fn = fibiter(n)
    t = time() - t
    print(f'fibiter({n}) = {fn} en {t} secondes.')
    
    t = time()
    fn = fibrec(n)
    t = time() - t
    print(f'fibrec({n}) = {fn} en {t} secondes.')
    
    t = time()
    fn = fibdyn(n)
    t = time() - t
    print(f'fibdyn({n}) = {fn} en {t} secondes.')
    
    return 0

if __name__ == '__main__':
    main()
```

## Utilisation du Script

Pour utiliser ce script, exécutez-le en ligne de commande avec le numéro du terme de Fibonacci que vous souhaitez calculer. Chaque méthode affichera le résultat et le temps d'exécution.
