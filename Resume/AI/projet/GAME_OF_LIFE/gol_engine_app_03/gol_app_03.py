import sys
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import Qt, Signal, Slot, QTimer, QSize
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtWidgets import QWidget, QGroupBox, QLabel, QPushButton, QSlider, QVBoxLayout, QHBoxLayout, QFormLayout, QSizePolicy
import random

from __feature__ import snake_case, true_property


from gol_engine_03 import GOLEngine



class QEventController(QGroupBox):
    
    eventTriggered = Signal()
    
    def __init__(self, parent=None):
        super().__init__('Contrôle', parent)
        
        self.__speed_values = (('Plus lent', 1000),
                               ('Lent', 600),
                               ('Moyen lent', 300),
                               ('Moyen', 100),
                               ('Moyen rapide', 60),
                               ('Rapide', 30),
                               ('Plus rapide', 1))
        
        self.__timer = QTimer()
        
        self.__setup_gui()
        self.__establish_connection()        
        self.__update_speed()
        self.__update_gui()
        
    def __setup_gui(self):
        self.__start_stop_button = QPushButton('Start')
        self.__single_event_button = QPushButton('Single step')
        self.__speed_slider = QSlider()
        self.__speed_label = QLabel()
        
        self.__speed_slider.orientation = Qt.Horizontal
        self.__speed_slider.set_range(0, len(self.__speed_values) - 1)
        self.__speed_slider.value = 4
        self.__speed_label.alignment = Qt.AlignCenter

        layout = QVBoxLayout(self)
        layout.add_widget(self.__start_stop_button)
        layout.add_widget(self.__single_event_button)
        layout.add_widget(self.__speed_slider)
        layout.add_widget(self.__speed_label)

        self.size_policy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        
    def __establish_connection(self):
        self.__start_stop_button.clicked.connect(self.__start_stop)
        self.__single_event_button.clicked.connect(self.eventTriggered)
        self.__speed_slider.valueChanged.connect(self.__update_speed)
        self.__timer.timeout.connect(self.eventTriggered)
        
    def __update_gui(self):
        self.__start_stop_button.text = ['Start', 'Stop'][self.__timer.active]
        self.__single_event_button.enabled = not self.__timer.active
        
    @Slot()
    def __update_speed(self):
        speed_name, speed_value = self.__speed_values[self.__speed_slider.value]
        self.__timer.interval = speed_value
        self.__speed_label.text = speed_name

    @Slot()
    def __start_stop(self):
        self.active = not self.active
        
    @property
    def active(self):
        return self.__timer.active
    
    @active.setter
    def active(self, value):
        if value != self.__timer.active:
            if self.__timer.active:
                self.__timer.stop()
            else:
                self.__timer.start(self.__speed_values[self.__speed_slider.value][1])
            self.__update_gui() 
    
    
class QGOLViewer(QLabel):
    
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.alignment = Qt.AlignCenter
        # self.minimum_size = QSize(200, 200)
        self.size_policy = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)

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
        

class QGOLInformation(QGroupBox):
    
    def __init__(self, parent=None):
        super().__init__('Information', parent)
        
        self.__generation_count = QLabel()
        self.__cells_count = QLabel()
        self.__cells_alive = QLabel()
        self.__cells_dead = QLabel()
        
        layout = QFormLayout(self)
        layout.add_row('Génération courante', self.__generation_count)
        layout.add_row('Nombre de cellules', self.__cells_count)
        layout.add_row('Cellules mortes', self.__cells_dead)
        layout.add_row('Cellules vivantes', self.__cells_alive)
        
        self.size_policy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)

    @Slot()
    def update_info(self, gol_engine):
        cells_count = gol_engine.cells_count
        self.__generation_count.text = f'{gol_engine.current_generation}'
        self.__cells_count.text = f'{gol_engine.cells_count}'
        self.__cells_dead.text = f'{gol_engine.cells_dead} [{gol_engine.cells_dead / gol_engine.cells_count * 100.0:0.1f}%]'
        self.__cells_alive.text = f'{gol_engine.cells_alive} [{gol_engine.cells_alive / gol_engine.cells_count * 100.0:0.1f}%]'
    


class GOLApp(QtWidgets.QMainWindow):
    
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.__gol_engine = GOLEngine(250, 250)
        self.__gol_engine.randomize()
        
        self.__setup_gui()
        
        self.__gol_controller.eventTriggered.connect(self.__process_simulation)


    def __setup_gui(self):
        self.set_window_title('Color picker')
        
        self.__gol_controller = QEventController()
        self.__gol_view = QGOLViewer()
        self.__gol_info = QGOLInformation()
        
        left_panel_layout = QVBoxLayout()
        left_panel_layout.add_widget(self.__gol_controller)
        left_panel_layout.add_stretch()
        
        right_panel_layout = QVBoxLayout()
        right_panel_layout.add_stretch()
        right_panel_layout.add_widget(self.__gol_info)
        
        central_widget = QWidget()
        central_layout = QHBoxLayout(central_widget)
        central_layout.add_layout(left_panel_layout)
        central_layout.add_widget(self.__gol_view)
        central_layout.add_layout(right_panel_layout)
        
        self.set_central_widget(central_widget)
        
    @Slot()
    def __process_simulation(self):
        # update modèle
        self.__gol_engine.process()
        # update vue
        self.__gol_view.update_view(self.__gol_engine)
        self.__gol_info.update_info(self.__gol_engine)



def main():
    app = QtWidgets.QApplication(sys.argv)

    w = GOLApp()
    w.show()
    sys.exit(app.exec())
    
    
if __name__ == '__main__':
    main()
