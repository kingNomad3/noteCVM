# width 10 mais doit etre modulaire
# height 6 mais doit etre modulaire
# vivant-mort pour uen case de la matrice
# randomize les case de la matrice selon vivant-mort

# on ignore les contours aka contour tjrs dead

# lorsqu'on verifie les voisins on cree une nouvelle matrice pour faire les verifications

# loop a travers une matrice double

# pour une case check le nombre de voisins vivants
# si vivant
#   si nb vivant 2, 3 alors vivant
# else mort

# si mort
#   si nb voisin vivant = 3
#   else mort

import random
import sys
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
        # center = self.matrice[1:-1]
        # left = self.matrice[0:2]
        # right = self.matrice[2:]
        # return left + right


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
SQUARE_SIZE = 5

class GameOfLifeWindow(QMainWindow):
    def __init__(self, gestion):
        super().__init__()

        self.gestion = gestion
        self.initUI()

    def initUI(self):
        # Set the title and initial size of the window
        self.setWindowTitle("Jeu de la vie")
        self.setGeometry(100, 100, self.gestion.width * SQUARE_SIZE, self.gestion.height * SQUARE_SIZE)

        # Create the central widget and set the vertical layout
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)
        self.central_layout = QVBoxLayout(self.central_widget)
        self.central_widget.setLayout(self.central_layout)
        self.central_widget.setStyleSheet("background-color: black;")

        # Initialize QLineEdit objects for user input on the grid size
        self.input_height = QLineEdit(self)
        self.input_width = QLineEdit(self)
        self.input_height.setStyleSheet("color: white;")
        self.input_width.setStyleSheet("color: white;")

        # Initialize the QPushButton to resize the grid
        self.resize_button = QPushButton('Redimensionner', self)
        self.resize_button.setStyleSheet("background-color: grey; color: white;")
        self.resize_button.clicked.connect(self.on_resize_clicked)

        # Add the widgets related to resizing to the vertical layout
        self.central_layout.addWidget(QLabel('Hauteur :'))
        self.central_layout.addWidget(self.input_height)
        self.central_layout.addWidget(QLabel('Largeur :'))
        self.central_layout.addWidget(self.input_width)
        self.central_layout.addWidget(self.resize_button)

        # Add the start button to the vertical layout
        self.start_button = QPushButton('Démarrer', self)
        self.start_button.setStyleSheet("background-color: grey; color: white;")
        self.start_button.clicked.connect(self.start_game)
        self.central_layout.addWidget(self.start_button)

        # Timer to control when the game starts
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_game)

        # Initialize the squares for the grid
        self.squares = [[QLabel(self.central_widget) for _ in range(self.gestion.width)] for _ in range(self.gestion.height)]
        
        # Set the horizontal layout for the squares
        self.squares_layout = QHBoxLayout()
        self.central_layout.addLayout(self.squares_layout)
        
        for i in range(self.gestion.height):
            for j in range(self.gestion.width):
                pixmap = QPixmap(SQUARE_SIZE, SQUARE_SIZE)
                self.squares[i][j].setPixmap(pixmap)
                self.squares_layout.addWidget(self.squares[i][j])

        self.draw_matrix()

    def start_game(self):
        if self.timer.isActive():
            self.timer.stop()
            self.start_button.setText('Démarrer')
        else:
            self.timer.start(100)
            self.start_button.setText('Arrêter')

    def update_game(self):
        self.gestion.life_or_death()
        self.draw_matrix()

    def draw_matrix(self):
        for i in range(self.gestion.height):
            for j in range(self.gestion.width):
                color = QColor(0, 0, 0) if self.gestion.matrice[i][j] == 0 else QColor(255, 255, 255)
                self.paint_square(i, j, color)

    def on_resize_clicked(self):
        new_height = int(self.input_height.text())
        new_width = int(self.input_width.text())
        self.gestion.resize(new_height, new_width)
        self.recreate_grid()

    def recreate_grid(self):
        for i in reversed(range(self.squares_layout.count())):
            item = self.squares_layout.itemAt(i)
            if item is not None:
                widget = item.widget()
                if widget is not None:
                    widget.deleteLater()

        self.draw_matrix()

    def paint_square(self, i, j, color):
        pixmap = QPixmap(SQUARE_SIZE, SQUARE_SIZE)
        pixmap.fill(Qt.transparent)
        painter = QPainter(pixmap)
        painter.fillRect(0, 0, SQUARE_SIZE, SQUARE_SIZE, color)
        painter.end()
        self.squares[i][j].setPixmap(pixmap)


    
  
        

def main():
    app = QApplication(sys.argv)
    gestion = Gestion(6, 10) 
    window = GameOfLifeWindow(gestion)
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()



# Qgroupbox,
# Qpush butoon stop start  
# Qscroll bar ralentie ou accelere 


