# Encapsule la notion de Trigger et de ElapsedTimer

from time import perf_counter


class Trigger:
    
    def __init__(self, start_time, duration, action):
        # Exemple de validation
        if not isinstance(duration, (int, float)):
            raise TypeError("duration must be an int or floating point")
        if not isinstance(start_time, (int, float)):
            raise TypeError("start_time must be an int or floating point")
        
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


# Flashing
def flashing(text_on, text_off, cycle_duration, total_duration):
    
    # objets timer
    timer = ElapsedTimer()

    # objets trigger
    go = [True] ### On remarque l'utilisation d'une liste (mutable)
    def terminate():
        go[0] = False
    trigger_off = Trigger(0.0, cycle_duration, lambda : print(f'\r{text_off}', end='     '))
    trigger_on = Trigger(cycle_duration / 2, cycle_duration, lambda : print(f'\r{text_on}', end='     '))
    trigger_quit = Trigger(0.0, total_duration, terminate)
    
    # boucle principale
    while go[0]:
        elapsed_time = timer.elapsed

        trigger_off.process(elapsed_time)
        trigger_on.process(elapsed_time)
        trigger_quit.process(elapsed_time)

    print('')



# Main
def main():
    flashing('*****', '     ', 0.5, 3.0)

# execution
if __name__ == '__main__':
    main()
    
    
    
def f(value = [True]):
    value[0] = False