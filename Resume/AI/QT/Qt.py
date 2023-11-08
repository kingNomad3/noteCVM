# dans cmd pip install pyside6

# sys est l'OS, aura le look natif selon windows ou apple 
# argv for argument value
from sys import argv, exit


# from PySide6 import QtWidgets
#QMainWindow 
from PySide6.QtCore import Qt, Slot, Signal
from PySide6.QtGui import QPixmap, QColor
from PySide6.QtWidgets import (QApplication, QMainWindow,QLabel,
                               QScrollBar,QVBoxLayout, QHBoxLayout,QWidget) #parenthse ou sans parentheres (sur la meme ligne) 
# possible 
# from PySide6.QtWidgets import (QApplication, QMainWindow,QLabel,\
#                                QScrollBar,QVBoxLayou, QHBoxLayout)

class ColorPickerApp(QMainWindow):
    def __init__(self, parent=None):
      super().__init__(parent)
      
      self.__red_title = QLabel()
      self.__red_value = QLabel()
      self.__red_color = QLabel()
      self.__red_sb = QScrollBar()
      self.__green_title = QLabel()
      self.__green_value = QLabel()
      self.__green_color = QLabel()
      self.__green_sb = QScrollBar()
      self.__blue_title = QLabel()
      self.__blue_value = QLabel()
      self.__blue_color = QLabel()
      self.__blue_sb = QScrollBar()
      self.__mixed_color = QLabel()
        
      
      fixed_width = 75
        
      self.__mixed_color.setFixedWidth(fixed_width)
      
      red_layout = self.__create_channel('Rouge', self.__red_title, self.__red_sb, self.__red_value, self.__red_color, fixed_width)
      green_layout = self.__create_channel('Vert', self.__green_title, self.__green_sb, self.__green_value, self.__green_color, fixed_width)
      blue_layout = self.__create_channel('Bleu', self.__blue_title, self.__blue_sb, self.__blue_value, self.__blue_color, fixed_width)
            
      channel_layout = QVBoxLayout()
      channel_layout.addLayout(red_layout)
      channel_layout.addLayout(green_layout)
      channel_layout.addLayout(blue_layout)
      
      mixed_layout = QHBoxLayout()
      mixed_layout.addLayout(channel_layout)
      mixed_layout.addWidget(self.__mixed_color)
      
      # etape 1 faire central layout
      central_layout = QVBoxLayout()
      central_layout.addLayout(mixed_layout)
      central_layout.addStretch()

      # etape 2 faire widget layout
      widget_central = QWidget()
      widget_central.setLayout(central_layout)
      
      self.setCentralWidget(widget_central)
    
    def __create_channel(self, title, title_label, sb, value, color, width):
        title_label.setText(title)
        title_label.setFixedWidth(width)
        
        sb.setOrientation(Qt.Horizontal)
        sb.setRange(0, 255)
        sb.setValue(0)
        sb.setMinimumWidth(2 * width)
        
        value.setText('0')
        value.setAlignment(Qt.AlignCenter)
        value.setFixedWidth(width)
        
        color.setFixedWidth(width)
        
        layout = QHBoxLayout()
        layout.addWidget(title_label)
        layout.addWidget(sb)
        layout.addWidget(value)
        layout.addWidget(color)
        
        sb.valueChanged.connect(value.setNum)
        #self.__red_sb.valueChanged.connect(self.__red_value.setNum)
        #    ^--- objet Ã©metteur            ^--- objet rÃ©cepteur
        #               ^--- signal Ã©mis                     ^--- slot Ã  exÃ©cuter
        sb.valueChanged.connect(self.__update_colors)
        
        return layout
      
    @Slot()
    def __update_colors(self):
        red = self.__red_sb.value()
        green = self.__green_sb.value()
        blue = self.__blue_sb.value()
        self.__update_color(self.__red_color, red, 0, 0)
        self.__update_color(self.__green_color, 0, green, 0)
        self.__update_color(self.__blue_color, 0, 0, blue)
        self.__update_color(self.__mixed_color, red, green, blue)
        
    def __update_color(self, label, red, green, blue):
        pixmap = QPixmap(label.size())
        pixmap.fill(QColor(red, green, blue))
        label.setPixmap(pixmap)
        
        
        
def main():
    app = QApplication(argv)
    
    Window = ColorPickerApp()
    Window.show()
    
    # le main loop qui va gerer les message de windows, bouger la sourire ecrit avec les touches etc
    exit(app.exec())
    

if __name__ == '__main__':
     main()

