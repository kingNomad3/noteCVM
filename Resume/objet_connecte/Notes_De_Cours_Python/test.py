class MaClasse:
    def __init__(self, limit):
        self.limit = limit
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.limit:
            self.current += 1
            return self.current
        else:
            raise StopIteration

# Création d'une instance de MaClasse
obj = MaClasse(5)

# Utilisation de l'objet dans une boucle for
for valeur in obj:
    print(valeur)
