from typing import Callable
from time import sleep
from circular_buffer import CircularBuffer


# -----------------------------------------------------------------------------
# Utilities
# -----------------------------------------------------------------------------


def color_text(text : str, color : tuple[int, int, int]) -> None:
    """Returns the text with the specified color.
    
    Args:
        text (str): The text to color.
        color (tuple[int, int, int]): The RGB color to use.
    """
    r, g, b = color
    return f'\033[38;2;{r};{g};{b}m{text}\033[0m'


def hsl_to_rgb(h : float, s : float, l : float) -> tuple[int, int, int]:
    """Converts an HSL color to an RGB color.
    
    Args:
        h (float): The normalized hue value.
        s (float): The normalized saturation value.
        l (float): The normalized lightness value.
    """
    if s == 0:
        r = g = b = l
    else:
        def hue_to_rgb(p, q, t):
            if t < 0: t += 1
            if t > 1: t -= 1
            if t < 1/6: return p + (q - p) * 6 * t
            if t < 1/2: return q
            if t < 2/3: return p + (q - p) * (2/3 - t) * 6
            return p
        q = l * (1 + s) if l < 0.5 else l + s - l * s
        p = 2 * l - q
        r = hue_to_rgb(p, q, h + 1/3)
        g = hue_to_rgb(p, q, h)
        b = hue_to_rgb(p, q, h - 1/3)
    return tuple(int(c * 255) for c in (r, g, b))


def hsv_to_rgb(h : float, s : float, v : float) -> tuple[int, int, int]:
    """Converts an HSV color to an RGB color.
    
    Args:
        h (float): The normalized hue value.
        s (float): The normalized saturation value.
        v (float): The normalized value value.
    """
    h_i = int(h * 6)
    f = h * 6 - h_i
    p = v * (1 - s)
    q = v * (1 - f * s)
    t = v * (1 - (1 - f) * s)
    r, g, b = ((v, t, p),
               (q, v, p),
               (p, v, t),
               (p, q, v),
               (t, p, v),
               (v, p, q))[h_i % 6]
    return tuple(int(c * 255) for c in (r, g, b))   


def print_on(text : str, *, fill_char : str = ' ', max_length : int | None = None) -> None:
    """Prints text on the same line, replacing the previous text. 
    
    If the new text is shorter than the previous text, the remaining characters 
    are filled with the fill_char. If max_length is specified, the text is 
    truncated to that length.
    
    Args:
        text (str): The text to print.
        fill_char (str, optional): The character to fill the remaining space 
            with. Defaults to ' '.
        max_length (int | None, optional): The maximum length of the text. 
            Defaults to None.
    """
    if not hasattr(print_on, '_prev_length'):
        setattr(print_on, '_prev_length', 0)
    
    if max_length is not None:
        text = text[:max_length]
        
    print(f'\r{text}', end=fill_char * max(0, print_on._prev_length - len(text) + 1))
    
    print_on._prev_length = len(text)
    

def progress_text( percent : float, width : int = 80, *
                 , foreground_char : str = '-'
                 , foreground_color : Callable[[float], tuple[int, int, int]] = lambda x: (255, 196, 0)
                 , background_char : str = ' '
                 , background_color : Callable[[float], tuple[int, int, int]] = lambda x: (0, 0, 0)
                 , show_percent : bool = True
                 , show_color : Callable[[float], tuple[int, int, int]] = lambda x: (222, 222, 222)):
    """Returns a progress bar text.
    
    Args:
        percent (float): The percentage of the progress bar.
        width (int, optional): The width of the progress bar. Defaults to 80.
        foreground_char (str, optional): The character to use for the foreground.
            Defaults to '-'.
        foreground_color (Callable[[float], tuple[int, int, int]], optional): The
            function to use to determine the color of the foreground. Defaults to
            lambda x: (255, 196, 0).
        background_char (str, optional): The character to use for the background.
            Defaults to ' '.
        background_color (Callable[[float], tuple[int, int, int]], optional): The
            function to use to determine the color of the background. Defaults to
            lambda x: (0, 0, 0).
        show_percent (bool, optional): Whether to show the percentage. Defaults to
            True.
        show_color (Callable[[float], tuple[int, int, int]], optional): The function
            to use to determine the color of the percentage. Defaults to lambda x: (222, 222, 222).
    """
    percent = max(0.0, min(percent, 1.0))
    foreground_length = round(width * percent)
    background_length = width - foreground_length
    progress_text = color_text(foreground_char * foreground_length, foreground_color(percent))
    background_text = color_text(background_char * background_length, background_color(percent))
    text = f'{progress_text}{background_text}'
    if show_percent:
        percent_text = f'{round(percent * 100)}%'
        color_percent_text = color_text(percent_text, show_color(percent))
        text += f' {color_percent_text}'
    return text



# -----------------------------------------------------------------------------
# Application
# -----------------------------------------------------------------------------


def show(data, delay = 0.25): 
    """Shows the circular buffer data with a progress bar."""    
    progress = progress_text( percent = data.size / data.capacity
                            , width = 25
                            , foreground_char = '-'
                            , foreground_color = lambda x: hsl_to_rgb(x / 3.0, 1.0, 0.5)
                            , background_char = '-'
                            , background_color = lambda x: hsl_to_rgb(x / 3.0, 0.5, 0.35)
                            , show_percent = True
                            , show_color = lambda x: hsl_to_rgb(x / 3.0, 0.85, 0.75))
    
    value = color_text(f'{data:full}', (32, 64, 255))
    print_on(f'{progress} {value}')
    sleep(delay)


def main():
    data = CircularBuffer(capacity=17)
    for i in range(50):
        data.push(i)
        show(data, 0.1)
        
    while not data.is_empty:
        data.pop()
        show(data, 0.5)


if __name__ == '__main__':
    main() 

