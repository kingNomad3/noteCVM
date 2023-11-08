import random
import sys
from typing import Optional
from PySide6.QtCore import QTimer, Qt
from PySide6.QtGui import QPainter, QPixmap, QColor
from PySide6.QtWidgets import (QApplication, QMainWindow, QLabel, QGridLayout, QVBoxLayout, QHBoxLayout,QLineEdit,
                               QPushButton, QWidget) #parenthse ou sans parentheres (sur la meme ligne) 
# possible 

class Gestion:
    def __init__(self, height, width):
        # Vérification des dimensions et initialisation de la matrice
         # puis crée la matrice initiale avec ces dimensions.
        # self.height = self.check_size(height)
        # self.width = self.check_size(width)
        self.__height = None
        self.__width = None
        
        self.height = height
        self.width = width
        self.matrice = self.__create_matrice(self.height, self.width)

    def check_size(self, size):
        # Vérifier et ajuster la taille pour qu'elle soit entre 3 et 2000
         # Si la taille est hors de cette plage, elle est ajustée en conséquence.
        if size < 3:
            size = 3
        elif size > 2000:
            size = 2000
        return size

    def __create_matrice(self, height, width):
        # Créer une matrice avec des bordures de 0 (mort) et le reste avec des valeurs aléatoires 0 (mort) ou 1 (vivant)
         # L'intérieur de la matrice est rempli de valeurs aléatoires (0 pour mort, 1 pour vivant).
        matrice = []
        for i in range(height):
            if i == 0 or i == height - 1:
                matrice.append([0] * width)
            else:
                matrice.append([0] + [random.randint(0, 1) for _ in range(width-2)] + [0])
        return matrice

    def get_alive_voisin(self, i, j):
        # Cette méthode calcule la prochaine génération de la matrice, on pourrait mettre cette methode dans une loop qui va tjrs changer la matrice grace a life_or_death fonction
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        count = 0
        for dx, dy in directions:
            ni, nj = i + dx, j + dy
            if 0 <= ni < self.height and 0 <= nj < self.width:
                count += self.matrice[ni][nj]
        return count

    def life_or_death(self):
        # Calculer la génération suivante en fonction des règles du jeu
        # Une nouvelle matrice est créée et remplie en fonction de l'état actuel et du nombre de voisins vivants.
        new_matrice = [[0 for _ in range(self.width)] for _ in range(self.height)]
        for i in range(1, self.height-1):  # Ignorer les contours
            for j in range(1, self.width-1):  # Ignorer les contours
                alive_voisin = self.get_alive_voisin(i, j)
                if self.matrice[i][j] == 1:  # Si la cellule est vivante
                    new_matrice[i][j] = 1 if alive_voisin in [2, 3] else 0
                else:  # Si la cellule est morte
                    new_matrice[i][j] = 1 if alive_voisin == 3 else 0
        self.matrice = new_matrice


    def __str__(self):
        # afficher la matrice sous une forme lisible.
        return '\n'.join([' '.join(map(str, row)) for row in self.matrice])


    def resize(self, height, width):
        self.height = height
        self.width = width
        self.matrice = self.__create_matrice(height, width)
    def reset_grid(self):
        self.matrice = [[0 for _ in range(self.width)] for _ in range(self.height)]
        pass
    
        
    

@property
def height(self):
    return self.__height

@height.setter
def height(self, value):
    self.__height = self.check_size(value)

@property
def width(self):
    return self.__width

@width.setter
def width(self, value):
    self.__width = self.check_size(value)

test = Gestion(6, 30)
test.resize(4,10)
print(test)
test.life_or_death()
SQUARE_SIZE = 20



class GameOfLifeWindow(QMainWindow):
    def __init__(self,gestion):
        super().__init__()
        
        self.gestion = gestion
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle("Game of life")
        
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)
        
        self.cmdLayout = QVBoxLayout()
        self.matrixLayout= QVBoxLayout()
        
            
        self.input_height = QLineEdit(self)
        self.input_width = QLineEdit(self)
        self.input_height.setStyleSheet("color: white;")  # Définir la couleur du texte en blanc
        self.input_width.setStyleSheet("color: white;")   # Définir la couleur du texte en blanc

        # Initialiser le bouton QPushButton pour redimensionner la grille
        self.resize_button = QPushButton('Redimensionner', self)
        self.resize_button.setStyleSheet("background-color: grey; color: white;")  # Bouton avec fond gris et texte blanc
        # self.resize_button.clicked.connect(self.on_resize_clicked)

        
        self.cmdLayout.addWidget(self.input_height)
    
    
    def recreate_grid(self):
        # Effacer la grille existante et en créer une nouvelle
        for i in reversed(range(self.grid_layout.count())): 
            widget = self.grid_layout.itemAt(i).widget()
            if widget is not None:
                widget.deleteLater()

        # Réinitialiser la disposition en grille pour inclure uniquement les contrôles de redimensionnement
        self.initUI()  # ou écrire une autre fonction qui fait uniquement la grille

        # Dessiner la nouvelle matrice
        self.draw_matrix()
        
        
def main():
    app = QApplication(sys.argv)
    gestion = Gestion(6, 10) 
    window = GameOfLifeWindow(gestion)
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()