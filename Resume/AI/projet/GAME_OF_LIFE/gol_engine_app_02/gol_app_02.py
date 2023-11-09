import sys
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import Qt, Signal, Slot
from PySide6.QtGui import QImage, QPixmap, QColor
from PySide6.QtWidgets import QWidget, QLabel, QScrollBar, QVBoxLayout, QHBoxLayout
import random

from __feature__ import snake_case, true_property


from gol_engine_02 import GOLEngine


class GOLApp(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.__gol_engine = GOLEngine(250, 250)
        self.__gol_engine.randomize()
        
        self.set_window_title('Color picker')
        
        self.__gol_view = QLabel()
        self.__gol_view.alignment = Qt.AlignCenter
                
        self.set_central_widget(self.__gol_view)
        
        self.__timer = QtCore.QTimer()
        self.__timer.timeout.connect(self.__process_simulation)
        self.__timer.start(100)
        
    @Slot()
    def __process_simulation(self):
        self.__gol_engine.process()
        self.__update_gol()

    def __update_gol(self):
        # créer l'image
        image = QImage(self.__gol_engine.width, self.__gol_engine.height, QImage.Format_ARGB32)
        image.fill(Qt.black)
        # dessiner
        for x in range(self.__gol_engine.width):
            for y in range(self.__gol_engine.height):
                if self.__gol_engine.get_cell_value(x, y):
                    image.set_pixel_color(x, y, Qt.white)
        # mettre l'image à l'écran
        pixmap = QPixmap.from_image(image.scaled(self.__gol_view.width, self.__gol_view.height, Qt.KeepAspectRatio, Qt.FastTransformation))
        self.__gol_view.pixmap = pixmap

def main():
    app = QtWidgets.QApplication(sys.argv)

    w = GOLApp()
    w.show()
    sys.exit(app.exec())
    

if __name__ == '__main__':
    main()