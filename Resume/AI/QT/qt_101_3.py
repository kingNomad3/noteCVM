from sys import argv, exit

# from PySide6 import QtWidgets
from PySide6.QtCore import Qt, Slot, Signal
from PySide6.QtGui import QPixmap, QColor
from PySide6.QtWidgets import QApplication, QMainWindow, \
                              QWidget, QLabel, QScrollBar, \
                              QVBoxLayout, QHBoxLayout

from __feature__ import snake_case, true_property
        
    
    
class QColorPicker(QWidget):
    
    colorChanged = Signal(QColor)
    
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
        
        self.__mixed_color.set_fixed_width(fixed_width)
        
        red_layout = self.__create_channel('Rouge', self.__red_title, self.__red_sb, self.__red_value, self.__red_color, fixed_width)
        green_layout = self.__create_channel('Vert', self.__green_title, self.__green_sb, self.__green_value, self.__green_color, fixed_width)
        blue_layout = self.__create_channel('Bleu', self.__blue_title, self.__blue_sb, self.__blue_value, self.__blue_color, fixed_width)
        
        channel_layout = QVBoxLayout()
        channel_layout.add_layout(red_layout)
        channel_layout.add_layout(green_layout)
        channel_layout.add_layout(blue_layout)
        
        mixed_layout = QHBoxLayout()
        mixed_layout.add_layout(channel_layout)
        mixed_layout.add_widget(self.__mixed_color)
        
        layout = QVBoxLayout(self)
        layout.add_layout(mixed_layout)
        layout.add_stretch()

        
    def __create_channel(self, title, title_label, sb, value, color, width):
        title_label.text = title
        title_label.set_fixed_width(width)
        
        sb.orientation = Qt.Horizontal
        sb.set_range(0, 255)
        sb.value = 0
        sb.minimum_width = 2 * width
        
        value.text = '0'
        value.alignment = Qt.AlignCenter
        value.set_fixed_width(width)
        
        color.set_fixed_width(width)
        
        layout = QHBoxLayout()
        layout.add_widget(title_label)
        layout.add_widget(sb)
        layout.add_widget(value)
        layout.add_widget(color)
        
        sb.valueChanged.connect(value.set_num)
        #self.__red_sb.valueChanged.connect(self.__red_value.setNum)
        #    ^--- objet émetteur            ^--- objet récepteur
        #               ^--- signal émis                     ^--- slot à exécuter
        sb.valueChanged.connect(self.__update_colors)
        sb.valueChanged.connect(self.__emit_color_changed)
        
        return layout
        
    
    @Slot()
    def __update_colors(self):
        red = self.__red_sb.value
        green = self.__green_sb.value
        blue = self.__blue_sb.value
        self.__update_color(self.__red_color, red, 0, 0)
        self.__update_color(self.__green_color, 0, green, 0)
        self.__update_color(self.__blue_color, 0, 0, blue)
        self.__update_color(self.__mixed_color, red, green, blue)
        
    def __update_color(self, label, red, green, blue):
        pixmap = QPixmap(label.size)
        pixmap.fill(QColor(red, green, blue))
        label.pixmap = pixmap
        
    @Slot()
    def __emit_color_changed(self):
        self.colorChanged.emit(self.color)
        
    def show_event(self, event):
        self.__update_colors()
        
    @property
    def color(self):
        return QColor(self.__red_sb.value, self.__green_sb.value, self.__blue_sb.value)

    @color.setter
    def color(self, value):
        self.__red_sb.block_signals(True)
        self.__green_sb.block_signals(True)
        self.__blue_sb.block_signals(True)
        
        self.__red_sb.value = value.red()
        self.__green_sb.value = value.green()
        self.__blue_sb.value = value.blue()
        self.__red_value.set_num(value.red())
        self.__green_value.set_num(value.green())
        self.__blue_value.set_num(value.blue())

        self.__red_sb.block_signals(False)
        self.__green_sb.block_signals(False)
        self.__blue_sb.block_signals(False)

        self.__update_colors()
        self.__emit_color_changed()
        
    @Slot()
    def set_color(self, color):
        self.color = color

class ColorPickerApp(QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        
        
        central_widget = QWidget()
        central_layout = QVBoxLayout(central_widget)
        
        self.__color_pickers = [QColorPicker() for _ in range(5)]
        for color_picker in self.__color_pickers:
            central_layout.add_widget(color_picker)
        central_layout.add_stretch()
        
        self.__color_pickers[0].colorChanged.connect(self.__color_pickers[2].set_color)
        self.__color_pickers[2].colorChanged.connect(self.__color_pickers[-1].set_color)
        
        self.set_central_widget(central_widget)
        
        
        
        
        


def main():
    app = QApplication(argv)
    
    window = ColorPickerApp()
    window.show()
    
    exit(app.exec())
    
    
if __name__ == '__main__':
    main()
    