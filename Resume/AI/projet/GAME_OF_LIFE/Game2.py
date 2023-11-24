import random
import sys
import PySide6
from typing import Optional
from PySide6.QtCore import QTimer, Qt
from PySide6.QtGui import QPainter, QPixmap, QColor
from PySide6.QtWidgets import (QApplication, QMainWindow, QLabel, QGridLayout, QVBoxLayout, QHBoxLayout,QLineEdit,
                               QPushButton, QWidget) #parenthse ou sans parentheres (sur la meme ligne) 
# possible 
import sys
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import Qt, Signal, Slot, QTimer, QSize
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtWidgets import QWidget, QGroupBox, QLabel, QPushButton, QSlider, QVBoxLayout, QHBoxLayout, QFormLayout, QSizePolicy


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


class GameOfLife(QMainWindow):
    def __init__(self, gestion):
        super().__init__()

        self.gestion = gestion
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_game)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Game of Life")

        self.central_Widget = QWidget(self)
        self.setCentralWidget(self.central_Widget)

        # Définir la couleur de fond du widget central en noir
        self.central_Widget.setStyleSheet("background-color: black;")

        # Créer une disposition horizontale pour le widget central
        self.central_layout = QHBoxLayout(self.central_Widget)
        self.central_Widget.setLayout(self.central_layout)

        # Créer une disposition verticale pour les boutons
        self.button_layout = QVBoxLayout()

        # Ajouter le bouton de démarrage à la disposition des boutons
        self.start_button = QPushButton("Demarrer", self)
        self.start_button.setStyleSheet("background-color: grey; color: white;")
        self.start_button.clicked.connect(self.start_game)
        self.button_layout.addWidget(self.start_button)

        self.resize_button = QPushButton("Redimensionner", self)
        self.resize_button.setStyleSheet("background-color: grey; color: white;")
        self.resize_button.clicked.connect(self.on_resize_clicked)
        self.button_layout.addWidget(self.resize_button)

        # Ajouter des étiquettes et des champs de saisie pour la hauteur et la largeur
        self.button_layout.addWidget(QLabel("Hauteur"))
        self.input_height = QLineEdit(self)
        self.input_height.setStyleSheet("color: white;")
        self.button_layout.addWidget(self.input_height)

        self.button_layout.addWidget(QLabel("Grosseur"))
        self.input_width = QLineEdit(self)
        self.input_width.setStyleSheet("color: white;")
        self.button_layout.addWidget(self.input_width)

        # Information
        self.__generation_count = QLabel()
        self.__cells_count = QLabel()
        self.__cells_alive = QLabel()
        self.__cells_dead = QLabel()

        self.layoutInfo = QFormLayout()
        for label in [self.__generation_count, self.__cells_count, self.__cells_alive, self.__cells_dead]:
            label.setStyleSheet("color: black;")  # Set text color to black

        self.layoutInfo.addRow('Génération courante', self.__generation_count)
        self.layoutInfo.addRow('Nombre de cellules', self.__cells_count)
        self.layoutInfo.addRow('Cellules mortes', self.__cells_dead)
        self.layoutInfo.addRow('Cellules vivantes', self.__cells_alive)

        self.size_policy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)

        

        # Ajouter la disposition des boutons à la disposition centrale
        self.central_layout.addLayout(self.button_layout)

      

        # Créer une disposition en grille pour la matrice de carrés
        self.matrix_layout = QGridLayout()

        # Ajouter la disposition en grille de la matrice à la disposition centrale
        self.central_layout.addLayout(self.matrix_layout)

        self.squares = [[QLabel(self.central_Widget) for _ in range(self.gestion.width)] for _ in range(self.gestion.height)]
        for i in range(self.gestion.height):
            for j in range(self.gestion.width):
                pixmap = QPixmap(SQUARE_SIZE, SQUARE_SIZE)
                self.squares[i][j].setPixmap(pixmap)
                self.matrix_layout.addWidget(self.squares[i][j], i, j)

        self.draw_matrix()

          # Ajouter la disposition d'information à la disposition centrale
        self.central_layout.addLayout(self.layoutInfo)


    def start_game(self):
        # Cette méthode est appelée lorsque le bouton de démarrage est cliqué
        if self.timer.isActive():
            self.timer.stop()
            self.start_button.setText('Démarrer')
        else:
            self.timer.start(100)  # Mise à jour toutes les 100 millisecondes
            self.start_button.setText('Arrêter')

    def update_game(self):
        # Mettre à jour le jeu
        self.gestion.life_or_death()
        self.draw_matrix()

    def draw_matrix(self):
        # Dessiner la matrice
        for i in range(self.gestion.height):
            for j in range(self.gestion.width):
                color = QColor(0, 0, 0) if self.gestion.matrice[i][j] == 0 else QColor(255, 255, 255)
                self.paint_square(i, j, color)

    def on_resize_clicked(self):
        # Cette méthode est appelée lorsque le bouton de redimensionnement est cliqué
        new_height = int(self.input_height.text())
        new_width = int(self.input_width.text())

        # Valider la saisie puis redimensionner
        self.gestion.resize(new_height, new_width)
        self.recreate_grid()

    def recreate_grid(self):
        # Effacer la grille existante et en créer une nouvelle
        for i in reversed(range(self.matrix_layout.count())):
            widget = self.matrix_layout.itemAt(i).widget()
            if widget is not None:
                widget.deleteLater()

        # Réinitialiser la disposition en grille pour inclure uniquement les contrôles de redimensionnement
        self.initUI()  # ou écrire une autre fonction qui fait uniquement la grille

        # Dessiner la nouvelle matrice
        self.draw_matrix()

    def paint_square(self, i, j, color):
        # Peindre un carré
        pixmap = QPixmap(SQUARE_SIZE, SQUARE_SIZE)
        pixmap.fill(Qt.transparent)
        painter = QPainter(pixmap)
        painter.fillRect(0, 0, SQUARE_SIZE, SQUARE_SIZE, color)
        painter.end()
        self.squares[i][j].setPixmap(pixmap)


def main():
    app = QApplication(sys.argv)
    gestion = Gestion(6, 10) 
    window = GameOfLife(gestion)
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()