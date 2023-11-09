import sys
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import Qt, Signal, Slot
from PySide6.QtGui import QColor
from PySide6.QtWidgets import QWidget, QLabel, QScrollBar, QVBoxLayout, QHBoxLayout
import random

from __feature__ import snake_case, true_property


from gol_engine_01 import GOLEngine


class GOLApp(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.__gol_engine = GOLEngine(50, 40)
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
        image = QtGui.QImage(self.__gol_engine.width, self.__gol_engine.height, QtGui.QImage.Format_ARGB32)
        for x in range(self.__gol_engine.width):
            for y in range(self.__gol_engine.height):
                image.set_pixel_color(x, y, QColor(0,0,0) if self.__gol_engine.get_cell_value(x, y) else QColor(255,255,255))
        pixmap = QtGui.QPixmap.from_image(image)
        self.__gol_view.pixmap = pixmap
        
    

def main():
    app = QtWidgets.QApplication(sys.argv)

    w = GOLApp()
    w.show()
    sys.exit(app.exec())
    

if __name__ == '__main__':
    main()