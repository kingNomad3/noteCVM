# Classification: K-Nearest Neighbors (KNN)

Une autre tâche classique de l'IA est la classification.
Applications:
- Biologie: Prédiction de phénotypes
- Économie: Prédiction de tendances économiques
- Commerce: Suggestions de produits
- Profilage: Analyse de comportement utilisateur

## Classification

La classification se fait à partir de données qui possèdent un ensemble de caractéristiques (features) quantifiées. Nous manipulons déjà de telles données avec nos vecteurs de mots, où chaque dimension représente un feature. Cependant, pour l'apprentissage supervisé, il est essentiel que nos données soient étiquetées, possédant une méta-information qui constitue sa classe.

### Exemple:
Un vecteur de mot (0, 2, 0, 4, 0, ..., 1, 2) pourrait représenter un verbe. L'étiquette "verbe" est commune à plusieurs mots, contrairement à une étiquette spécifique comme "jardiner".

## KNN - K-Nearest Neighbors

Le KNN est un algorithme de classification qui commence par explorer le voisinage de la donnée que nous voulons classifier. Ensuite, il détermine la classe de ses voisins et enfin, infère la classe de notre donnée à partir de celles des voisins.

### Processus:
1. **Initiation**: Trouver la donnée étiquetée la plus proche et attribuer cette classe à notre donnée.
2. **Réduction du risque d'erreur**: Augmenter la taille de l'échantillon à `k` voisins pour éviter les erreurs dues aux outliers.

```python
def predireClasseAvecKNN(k, p, ensemble):
    # Calcule la distance de p à tous les points étiquetés de l'ensemble de données
    # Conserve les k voisins les plus proches
    # Chaque voisin vote pour sa catégorie
    return categorie_obtenant_le_plus_de_votes
```

# Exemple avec Pondération

## Vote à l'aide de la série harmonique

L'approche utilise la série harmonique pour pondérer les votes des voisins en fonction de leur proximité. La formule est la suivante:

$$
\sum_{i=0}^{k-1} \frac{1}{i+1} = 1 + \frac{1}{2} + \frac{1}{3} + \ldots + \frac{1}{k}
$$

Cette méthode accorde plus d'importance aux voisins les plus proches en attribuant un poids décroissant aux positions éloignées dans la liste des voisins triés par distance.

## Vote inversement proportionnel au carré de la distance

Cette méthode attribue un poids aux votes basé sur l'inverse du carré de la distance entre le point de référence et chaque voisin, ce qui minimise l'impact des voisins éloignés :

$$
\sum_{i=0}^{k-1} \frac{1}{d_i^2 + 1}
$$

où \( d_i \) est la distance du \( i \)-ème voisin le plus proche.

## Normalisation

La question de savoir s'il faut normaliser ou non les données est cruciale :

"To normalize or not to normalize, that is the question": La normalisation des données transforme les vecteurs de position des mots en vecteurs unitaires. Cela augmente l'importance relative des features tout en perdant l'importance absolue de certains.

### En numpy:

Pour normaliser un ensemble de vecteurs, on peut utiliser la fonction suivante:

```python
m = (m.transpose() / np.linalg.norm(m, axis=1)).transpose()
```

### Conseil:
Il est recommandé de stocker la matrice dans la base de données sans normalisation pour conserver l'intégrité des valeurs entières. Normalisez uniquement pour la recherche et le partitionnement, après avoir chargé la matrice.