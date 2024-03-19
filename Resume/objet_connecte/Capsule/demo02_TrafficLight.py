from time import sleep

# Développement incrémental d'une classe TrafficLight 
# 
# Objectif, pratiquer le changement d'état.
# 
# On utilise 'sleep' dans ces exemples pour simplifier 
# et focuser l'exercice sur le changement d'état


# 
# Implémentation 00
#
# Utilisation d'un pseudo 'switch case' avec des 
# entiers comme flags de contrôle de l'état.
# Utilise des sleeps!

from typing import TypeAlias

class TrafficLight00:
    
    State : TypeAlias = int
    
    def __init__(self, name : str) -> None:
        self.name : str = name
        self.initial_state : TrafficLight00.State = 0
        self.current_state : TrafficLight00.State = self.initial_state

    def reset(self) -> None:
        self.current_state = self.initial_state

    def tic(self) -> None:
        if self.current_state == 0:
            print(f'\r{self.name}  Rouge', end='')
            sleep(1.0)
            self.current_state = 1
        elif self.current_state == 1:
            print(f'\r{self.name}  Vert ', end='')
            sleep(0.8)
            self.current_state = 2
        elif self.current_state == 2:
            print(f'\r{self.name}  Jaune', end='')
            sleep(0.2)
            self.current_state = 0

        # self.current_state = (self.current_state + 1) % 3
        # ou
        # self.current_state += 1
        # self.current_state %= 3

def main00() -> None:
    traffic_light = TrafficLight00('00')
    while True:
        traffic_light.tic()
        
        
# ######################################  
# 
# Implémentation 01
#
# Utilisation d'un pseudo 'switch case' avec 
# un Enum comme flags de contrôle de l'état.
# Utilise des sleeps!

from enum import Enum, auto

class TrafficLight01:
    
    class State(Enum):
        RED = auto()
        GREEN = auto()
        YELLOW = auto()
    
    def __init__(self, name : str, initial_state : State = State.RED) -> None:
        self.name : str = name
        self.initial_state : TrafficLight01.State = initial_state
        self.current_state : TrafficLight01.State = self.initial_state

    def reset(self) -> None:
        self.current_state = self.initial_state

    def tic(self) -> None:
        if self.current_state == TrafficLight01.State.RED:
            print(f'\r{self.name}  Rouge', end='')
            sleep(1.0)
            self.current_state = TrafficLight01.State.GREEN
        elif self.current_state == TrafficLight01.State.GREEN:
            print(f'\r{self.name}  Vert ', end='')
            sleep(0.8)
            self.current_state = TrafficLight01.State.YELLOW
        elif self.current_state == TrafficLight01.State.YELLOW:
            print(f'\r{self.name}  Jaune', end='')
            sleep(0.2)
            self.current_state = TrafficLight01.State.RED

def main01():
    traffic_light = TrafficLight01('01', TrafficLight01.State.YELLOW)
    while True:
        traffic_light.tic()        




# ######################################
# 
# Implémentation 02
#
# Utilisation d'un LUT pour stocker les infos : nom, durée et état suivant.
# Utilise des entiers comme flags de contrôle de l'état 
# Branchless programming!
# Utilise des sleeps!
class TrafficLight02:
    
    StateInfo : TypeAlias = tuple[str, float, int] # Nom, durée, état suivant
    States : TypeAlias = tuple[StateInfo, ...]

    def __init__(self, name : str) -> None:
        self.name : str = name
        self._states_and_transit : TrafficLight02.States = (
            ('Rouge', 1.0, 1),
            ('Vert ', 0.8, 2),
            ('Jaune', 0.2, 0),
        )
        
        self._initial_state : int = 0
        self._current_state : int = self._initial_state

    def tic(self) -> None:
        state_name, state_duration, state_next_state = self._states_and_transit[self._current_state]
        print(f'\r{self.name}  {state_name}', end='')
        sleep(state_duration)
        self._current_state = state_next_state

def main02():
    traffic_light = TrafficLight02('02')
    while True:
        traffic_light.tic()




# ######################################
# 
# Implémentation 03
#
# Utilisation d'un Dict avec Enum pour stocker 
# les infos. Branchless programming!
# Utilise des sleeps!
class TrafficLight03:
    
    class State(Enum):
        RED = auto()
        GREEN = auto()
        YELLOW = auto()
        
    StateInfo : TypeAlias = tuple[str, float, State] # Nom, durée, état suivant
    States : TypeAlias = dict[State, StateInfo]
            
    def __init__(self, name : str) -> None:
        self.name : str = name
        self._states_and_transit : TrafficLight03.States = {
            TrafficLight03.State.RED : ('Rouge', 1.0, TrafficLight03.State.GREEN),
            TrafficLight03.State.GREEN : ('Vert ', 0.8, TrafficLight03.State.YELLOW),
            TrafficLight03.State.YELLOW : ('Jaune', 0.2, TrafficLight03.State.RED),
        }
        self._initial_state = TrafficLight03.State.RED
        self._current_state = self._initial_state

    def tic(self) -> None:
        state_name, state_duration, state_next_state = self._states_and_transit[self._current_state]
        print(f'\r{self.name}  {state_name}', end='')
        sleep(state_duration)
        self._current_state = state_next_state

def main03():
    traffic_light = TrafficLight03('03')
    while True:
        traffic_light.tic()




# ######################################
# 
# Implémentation 04
#
# Utilisation uniquement d'un Enum pour stocker 
# les infos. Branchless programming!
# Utilise des sleeps!
class TrafficLight04:
    
    class State(Enum):
        
        #        /¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯
        # ______/  Idéalement, cette approche!
        # RED = (auto(), 'Rouge', 1.0, TrafficLight04.State.GREEN)
        # GREEN = (auto(), 'Vert ', 0.8, TrafficLight04.State.YELLOW)
        # YELLOW = (auto(), 'Jaune', 0.2, TrafficLight04.State.RED)
        # ¯¯¯¯¯¯\  malheureusement, les Enums ne sont                  ^
        #        \   pas encore déclarés et ne peuvent                 |
        #         \    être référencés ici ----------------------------+
        #          ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯
        #  /¯¯'---,____/¯¯¯ Solution, le faire en 2 étapes 
        # V            \___ Voir la fonction _define_next
        RED = (auto(), 'Rouge', 1.0)
        GREEN = (auto(), 'Vert ', 0.8)
        YELLOW = (auto(), 'Jaune', 0.2)
        
        def __init__(self, id, name, duration) -> None:
            self.id : int = id
            self.state_name : str = name
            self.duration : float = duration

        @staticmethod
        def _define_next() -> None:
            state_map : tuple[tuple[TrafficLight04.State, TrafficLight04.State], ...] = (
                    (TrafficLight04.State.RED, TrafficLight04.State.GREEN),
                    (TrafficLight04.State.GREEN, TrafficLight04.State.YELLOW),
                    (TrafficLight04.State.YELLOW, TrafficLight04.State.RED)
                )
            for cur_state, next_state in state_map:
                cur_state.next_state = next_state

    def __init__(self, name : str) -> None:
        self.name : str = name
        self.current_state : TrafficLight04.State = TrafficLight04.State.RED

    def tic(self) -> None:
        print(f'\r{self.name}  {self.current_state.state_name}', end='')
        sleep(self.current_state.duration)
        self.current_state = self.current_state.next_state

# ATTENTION, cet exemple est plutôt pédagogique que pertinent car l'appel 
# de la fonction suivante est obligatoire pour initialiser entièrement le 
# Enum! Obliger un appel de fonction formel ainsi est généralement 
# considéré comme une mauvaise pratique.
TrafficLight04.State._define_next()

def main04():
    traffic_light = TrafficLight04('04')
    while True:
        traffic_light.tic()








# ######################################
# 
# Implémentation 05
#
# Utilisation de classes dédiées pour les 
# états et la machine d'états 
# Branchless programming!
# Utilise des sleeps!
class StateMachine:
    
    class State:
        
        def __init__(self, name : str, duration : float, next_state : 'State') -> None:
            self.name : str = name
            self.duration : float = duration
            self.next_state : StateMachine.State = next_state

        def __repr__(self) -> str:
            return f'{self.__class__.__name__}({self.name}, {self.duration}, {self.next_state.name})'
        
        def __str__(self) -> str:
            return self.name
    
    def __init__(self, name : str, states : list[State], initial_state : State) -> None:
        self._name : str = name
        self._states : tuple[StateMachine.State, ...] = states
        self._current_state : StateMachine.State = initial_state
        # should validate that the initial state is in the list of states

    def tic(self) -> None:
        print(f'\r{self._name}  {self._current_state}', end='')
        sleep(self._current_state.duration)
        self._current_state = self._current_state.next_state


class TrafficLight05:
    
    def __init__(self, name : str) -> None:
        red_state = StateMachine.State('Rouge', 1.0, None)
        green_state = StateMachine.State('Vert ', 0.8, None)
        yellow_state = StateMachine.State('Jaune', 0.2, None)
        
        red_state.next_state = green_state
        green_state.next_state = yellow_state
        yellow_state.next_state = red_state

        self._state_machine = StateMachine('05', (red_state, green_state, yellow_state), red_state)
        
    def tic(self) -> None:
        self._state_machine.tic()


def main05():
    traffic_light = TrafficLight05('05')
    
    while True:
        traffic_light.tic()




# ##########################################        
# ##########################################        
# ##########################################        
if __name__ == '__main__':
    main02()
