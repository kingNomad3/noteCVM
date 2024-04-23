# Ajoute l'encapsulation de CycleTrigger

from time import perf_counter


class Light:
    
    def __init__(self, color_off, color_on, light_size = 10):
        self._colors = (color_off, color_on)
        self._text = '\u25A0' * light_size
        
    def _set(self, color):
        r, g, b = color
        print(f'\r\x1b[38;2;{r};{g};{b}m{self._text}\x1b[0m', end='')
        
    def set_on(self):
        self._set(self._colors[1])
        
    def set_off(self):
        self._set(self._colors[0])


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
            

class CycleTrigger:
    
    def __init__(self, cycle_duration, percent_on, action_off, action_on):
        # Validation à faire
        self._current_time = 0.0
        self._duration_on = percent_on * cycle_duration
        self._duration_off = cycle_duration - self._duration_on
        self._is_on = False
        self._action_off = action_off
        self._action_on = action_on

    def process(self, elapsed_time):
        self._current_time += elapsed_time
        
        if self._is_on:
            if self._current_time >= self._duration_on:
                self._current_time -= self._duration_on
                self._is_on = False
                self._action_off()
        else:
            if self._current_time >= self._duration_off:
                self._current_time -= self._duration_off
                self._is_on = True
                self._action_on()


class FlashingApplication:
    
    def __init__(self, cycle_duration = 1.0, cycle_on = 0.5, total_duration = 10.0, text_size = 10):
        
        self._pursue = True
        self._timer = ElapsedTimer()
        self._light = Light((64, 16, 16), (255, 0, 0))
        
        self._light_trigger = CycleTrigger(cycle_duration, cycle_on, self._light.set_off, self._light.set_on)
        self._trigger_quit = Trigger(0.0, total_duration, lambda: setattr(self, '_pursue', False)) ### on remarque l'usage d'une lambda avec setattr

    @property
    def pursue(self):
        return self._pursue
    
    def tic(self):
        elapsed_time = self._timer.elapsed

        self._light_trigger.process(elapsed_time)
        self._trigger_quit.process(elapsed_time)
        
    def run(self):
        while self._pursue:
            self.tic()


# Main
def main():
    
    flashing = FlashingApplication(0.75, 0.15, 5.0)
    flashing.run()


# execution
if __name__ == '__main__':
    main()