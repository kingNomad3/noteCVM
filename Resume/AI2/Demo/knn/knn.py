from sys import argv
import numpy as np

SEP = ';'
QUITTER = 'Q'
MESS_CANDIDAT = f"Veuillez entrer les features d'un objet inconnu ({QUITTER} pour quitter): "
MESS_VOISINS = "Veuillez entrer le nombre de voisins à considérer: "
MESS_TYPE_VOTE = "Méthode de vote: 0 (démocrate), 1 (harmonique), 2 (distance): "
MESS_NORM = "Normaliser? 1 (oui), 0 (non): "

def democrate(distance2: float, position: int) -> float: return 1.0
def harmonique(distance2: float, position: int) -> float: return 1.0/(position + 1)
def distance(distance2: float, position: int) -> float: return 1.0/(distance2 + 1)

class KNN():
    def __init__(self, chFeatures: str, chClasses: str, enc: str) -> None:
        self.features = self.lire_features(chFeatures, enc)
        self.classes, self.etiquettes = self.lire_classes(chClasses, enc)
        
    def lire(self, chemin: str, enc: str) -> tuple[list[str], list[str]]:
        with open(chemin, encoding = enc) as f:
            lignes = f.read().splitlines()
        noms = lignes[0].split(SEP)
        return noms, lignes[1:]

    def lire_features(self, chemin: str, enc: str) -> list[list[float]]:
        noms, rangees = self.lire(chemin, enc)
        return [[float(valeur) for valeur in rangee.split(SEP)] for rangee in rangees]

    def lire_classes(self, chemin: str, enc: str) -> tuple[list[str], list[str]]:
        classes, rangees = self.lire(chemin, enc)
        etiquettes = [classes[int(valeur)] for valeur in rangees]
        return classes, etiquettes
        
    def voter(self, candidat: list, nb_voisins: int, type_vote: int, normaliser: int) -> list[tuple[str, float]]:
        self.features.append(candidat)
        features = np.array(self.features)
        self.features.pop()
        if normaliser:
            features = self.normaliser(features)
        
        # À l'étape nécessaire, le clustering fournit DÉJÀ
        # les distances d'un mot à son cluster
        distances = np.sum( (features[-1] - features[:-1])**2, axis = 1 )
        voisins = np.argsort(distances)[:nb_voisins]
        fonction_vote = [democrate, harmonique, distance][type_vote]
        votes = {classe:0 for classe in self.classes}
        for position_voisin in range(len(voisins)):
            rangee_voisin = voisins[position_voisin]
            distance_voisin = distances[rangee_voisin]
            etiquette_voisin = self.etiquettes[rangee_voisin]
            votes[etiquette_voisin] += fonction_vote(distance_voisin, position_voisin)
        return sorted(votes.items(), key=lambda t:t[1], reverse=True)
        
    # chaque vecteur de feature (coordonnée) est transformé
    # en vecteur unitaire, donc divisé par sa norme
    def normaliser(self, m: np.ndarray) -> np.ndarray:
            return (m.transpose()/np.linalg.norm(m, axis=1)).transpose()
    
    
def main() -> int:
    chFeatures, chClasses, enc = argv[1:]
    knn = KNN(chFeatures, chClasses, enc)
    
    candidat = input(MESS_CANDIDAT)
    while candidat != QUITTER:
        nb_voisins = int(input(MESS_VOISINS))
        type_vote = int(input(MESS_TYPE_VOTE))
        normaliser = int(input(MESS_NORM))
        
        candidat = [float(x) for x in candidat.split()]
        votes = knn.voter(candidat, nb_voisins, type_vote, normaliser)
        # On retourne la clé (classe) de la classe ayant reçu le plus de votes
        # donc l'élément 0 du tuple en première position
        print(votes)
        print(f'Le candidat est de type -> {votes[0][0]}\n')
        
        candidat = input(MESS_CANDIDAT)
        
    return 0
    
    
    
if __name__ == '__main__':
    main()
    
    