# Ajoute l'encapsulation de l'application

from time import perf_counter

class ElapsedTimer:
    
    def __init__(self):
        self._prev_time = perf_counter()
        
    @property
    def elapsed(self) -> None:
        cur_time = perf_counter()
        elapsed_time = cur_time - self._prev_time
        self._prev_time = cur_time
        return elapsed_time
    
    def reset(self) -> None:
        self._prev_time = perf_counter()


class Trigger:
    
    def __init__(self, start_time, duration, action):
        # Exemple de validation
        if not isinstance(duration, (int, float)):
            raise TypeError("duration must be an int or floating point")
        if not isinstance(start_time, (int, float)):
            raise TypeError("start_time must be an int or floating point")
        if not callable(action):
            raise TypeError("action must be a callable")
        
        if duration <= 0.0:
            raise ValueError("duration must be strictly positive")
        if not (0.0 <= start_time <= duration):
            raise ValueError("start_time must be between 0 and duration")
        
        self._duration = float(duration)
        self._current = self._duration - float(start_time)
        self._action = action

    def process(self, elapsed_time):
        self._current -= elapsed_time
        
        if self._current <= 0.0:
            self._current += self._duration
            self._action()
            

class FlashingApplication:
    
    def __init__(self, cycle_duration = 1.0, total_duration = 10.0, text_size = 10):
        
        self._pursue = True
        self._timer = ElapsedTimer()
        self._text = '\u25A0' * text_size
        
        def set(color):
            r, g, b = color
            print(f'\r\x1b[38;2;{r};{g};{b}m{self._text}\x1b[0m', end='') ### On remarque l'usage des codes d'échapement pour l'ajout de couleur dans la console (voir : https://en.wikipedia.org/wiki/ANSI_escape_code)
            
        def terminate():
            self._pursue = False
        
        self._trigger_off = Trigger(0.0, cycle_duration, lambda: set((64, 16, 16)))
        self._trigger_on = Trigger(cycle_duration / 2, cycle_duration, lambda: set((255, 0, 0)))
        self._trigger_quit = Trigger(0.0, total_duration, terminate)

    @property
    def pursue(self):
        return self._pursue
    
    def tic(self):
        elapsed_time = self._timer.elapsed

        self._trigger_off.process(elapsed_time)
        self._trigger_on.process(elapsed_time)
        self._trigger_quit.process(elapsed_time)
        
    def run(self):
        while self._pursue:
            self.tic()            


# Main
def main():
    
    flashing = FlashingApplication(0.5, 5.0)
    flashing.run()


# execution
if __name__ == '__main__':
    main()