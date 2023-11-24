import random
import sys
from copy import deepcopy
import PySide6
from PySide6 import QtCore, QtGui, QtWidgets
from typing import Optional
from PySide6.QtCore import QTimer, Qt,Slot
from PySide6.QtGui import QPainter, QPixmap, QColor
from PySide6.QtWidgets import (QApplication, QMainWindow, QLabel, QGridLayout, QVBoxLayout, QHBoxLayout,QLineEdit,
                               QPushButton, QWidget) #parenthse ou sans parentheres (sur la meme ligne) 
# possible 
from PySide6.QtWidgets import QWidget, QGroupBox, QLabel, QPushButton, QSlider, QVBoxLayout, QHBoxLayout, QFormLayout, QSizePolicy


class GOLEngine:
    def __init__(self, width, height):
        self.__width = None
        self.__height = None
        self.__world = None
        self.__temp = None
        self.__current_generation = None
        self.__cells_alive = None
        
        # nombre de voisins  0  1  2  3  4  5  6  7  8 
        self.__alive_rule = (0, 0, 1, 1, 0, 0, 0, 0, 0)
        self.__dead_rule  = (0, 0, 0, 1, 0, 0, 0, 0, 0)
        # état cellule  0                 1
        self.__rules = (self.__dead_rule, self.__alive_rule)
        
        self.resize(width, height)
    
    @property
    def width(self):
        return self.__width
    
    @width.setter
    def width(self, value):
        self.resize(value, self.__height)
    
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.resize(self.__width, value)
        
    @property
    def current_generation(self):
        return self.__current_generation
        
    @property
    def cells_count(self):
        return self.__width * self.__height
        
    @property
    def cells_alive(self):
        return self.__cells_alive
        
    @property
    def cells_dead(self):
        return self.cells_count - self.__cells_alive
        
    def get_cell_value(self, x, y):
        # no input validation for performance consideration
        return self.__world[x][y]
        
    def set_cell_value(self, x, y, value):
        # no input validation for performance consideration
        self.__world[x][y] = value
    
    def __validate_size(self, size):
        if not isinstance(size, int):
            raise TypeError('size must be an int')
        if not(3 <= size <= 2000):
            raise ValueError('size must be between 3 and 2000')
    
    def resize(self, width, height):
        # l'importance de cette fonction justifie ces étapes de validation
        # => mettre l'importance sur l'interface de programmation
        self.__validate_size(width)
        self.__validate_size(height)
        
        self.__width = width
        self.__height = height
        self.__world = []
        self.__temp = []
        
        self.__world = [[0 for _ in range(self.__height)] for _ in range(self.__width)]
        self.__temp = deepcopy(self.__world)
        
        self.__current_generation = 0
        self.__cells_alive = 0

    def randomize(self, percent = 0.5):
        self.__current_generation = 0
        self.__cells_alive = 0
        for y in range(1, self.__height - 1):
            for x in range(1, self.__width - 1):
                cell_value = int(random.random() > percent)
                self.__world[x][y] = cell_value
                self.__cells_alive += cell_value

    def process(self):
        self.__cells_alive = 0
        for x in range(1, self.__width-1):
            for y in range(1, self.__height-1):
                neighbours = 0

                neighbours = sum(self.__world[x-1][y-1:y+2]) \
                           + sum(self.__world[x][y-1:y+2:2]) \
                           + sum(self.__world[x+1][y-1:y+2])

                cell_value = self.__world[x][y]
                self.__temp[x][y] = self.__rules[cell_value][neighbours]
                self.__cells_alive += cell_value

        self.__world, self.__temp = self.__temp, self.__world
        self.__current_generation += 1
    
    
    
SQUARE_SIZE = 20


class GameOfLife(QMainWindow):
    def __init__(self, gestion):
        super().__init__()

        self.gestion = gestion
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.__process_simulation)
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
        self.start_button = QPushButton("Demarrer",self)
        self.start_button.setStyleSheet("background-color: grey; color: white;")
        # self.start_button.clicked.connect(self.start_game)
        self.button_layout.addWidget(self.start_button)

        self.resize_button = QPushButton("Redimensionner",self)
        self.resize_button.setStyleSheet("background-color: grey; color: white;")
        # self.resize_button.clicked.connect(self.on_resize_clicked)
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

        # Ajouter la disposition des boutons à la disposition centrale
        self.central_layout.addLayout(self.button_layout)

        # Créer une disposition en grille pour la matrice de carrés
        self.matrix_layout = QGridLayout()

        # Créer une disposition en grille pour la matrice de carrés
        self.central_layout.addLayout(self.matrix_layout)

    @Slot()
    def __process_simulation(self):
        self.__gol_engine.process()
        self.__update_gol()

    def __update_gol(self):
        image = QtGui.QImage(self.__gol_engine.width, self.__gol_engine.height, QtGui.QImage.Format_ARGB32)
        for x in range(self.__gol_engine.width):
            for y in range(self.__gol_engine.height):
                image.set_pixel_color(x, y, QColor(0,0,0) if self.__gol_engine.get_cell_value(x, y) else QColor(255,255,255))
        pixmap = QtGui.QPixmap.from_image(image)
        self.__gol_view.pixmap = pixmap

   

    @Slot()
    def update_info(self, gol_engine):
        cells_count = gol_engine.cells_count
        self.__generation_count.text = f'{gol_engine.current_generation}'
        self.__cells_count.text = f'{gol_engine.cells_count}'
        self.__cells_dead.text = f'{gol_engine.cells_dead} [{gol_engine.cells_dead / gol_engine.cells_count * 100.0:0.1f}%]'
        self.__cells_alive.text = f'{gol_engine.cells_alive} [{gol_engine.cells_alive / gol_engine.cells_count * 100.0:0.1f}%]'
       
    @Slot()
    def update_view(self, gol_engine):
        # créer l'image en mémoire (invisible à l'écran)
        image = QImage(gol_engine.width, gol_engine.height, QImage.Format_ARGB32)
        image.fill(Qt.black)
        # dessiner sur l'image en mémoire
        for x in range(gol_engine.width):
            for y in range(gol_engine.height):
                if gol_engine.get_cell_value(x, y):
                    image.set_pixel_color(x, y, Qt.white)
        # mettre l'image à l'écran
        self.pixmap = QPixmap.from_image(image.scaled(self.width, 
                                                      self.height, 
                                                      Qt.KeepAspectRatio, 
                                                      Qt.FastTransformation))   


def main():
    app = QApplication(sys.argv)
    gestion = GOLEngine(6, 10) 
    window = GameOfLife(gestion)
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()