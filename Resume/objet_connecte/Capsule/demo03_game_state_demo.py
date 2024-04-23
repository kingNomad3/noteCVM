from __future__ import annotations
from msvcrt import kbhit, getch


# --------------------------------------
# Exemple de boucle écoutant le clavier.
# --------------------------------------
def main() -> None:
    
    proceed = True
    while proceed:
        
        if kbhit():
            input_char = getch().lower().decode('UTF-8')
            
            if input_char == 'q':
                proceed = False
                
            else:
                print(input_char, end='')
                
    print('\nEnd!!!')
    
    
 # -------------------------------------
 # --------------------------------------
 # --------------------------------------
 
 
from time import sleep
from os import system
from typing import TypeAlias


# --------------------------------------
# Exemple de machine d'état pour gérer l'état principal d'une simulation de jeu.
# Utilise une approche de programmation procédurale, simple mais sans branchement.
# Principalement basé sur une structure de données personnalisée basée sur des assemblages de tuples et dictionnaire.
# Utilise 'sleep'
# --------------------------------------
class SnakeGameDemo001:
    # nom d'état
    Name : TypeAlias = str
    # numéro d'état
    State : TypeAlias = int
    # durée d'attente pour une transition temporelle
    Duration : TypeAlias = float
    # état terminal
    Terminal : TypeAlias = bool
    # transition temporel : (durée d'attente, prochain état) --- si non utilisé, (None, None)
    DurationTransition : TypeAlias = tuple[Duration | None, State | None]
    # transitions clavier : touche, next_state
    KeyboardTransitions : TypeAlias = dict[str, State]
    
    # Les informations pour chaque état
    StateInfo : TypeAlias = tuple[Name, DurationTransition, KeyboardTransitions, Terminal]
    StateInfos : TypeAlias = tuple[StateInfo, ...]
    
    def __init__(self):
        self._states_info : SnakeGameDemo001.StateInfos = (
                ('SplashScreen', (1.0,1), {}, False),
                ('Home', (None, None), {'q':5, 'g':2, 'c':3}, False),
                ('InGame', (None, None), {'h':1, 'p':4}, False),
                ('Config', (None, None), {'h':1}, False),
                ('Paused', (None, None), {'g':2, 'h':1}, False),
                ('Quit', (None, None), {}, True),
            )
        self._initial_state : SnakeGameDemo001.State = 0
        self._current_state : SnakeGameDemo001.State | None = None
        self._change_state(self._initial_state)

    def _change_state(self, new_state : State) -> bool:
        self._current_state = new_state
        state_info : SnakeGameDemo001.StateInfo = self._states_info[self._current_state]
        system('cls')
        print(state_info[0])
        if state_info[1][0]:
            sleep(state_info[1][0])
            self._change_state(state_info[1][1])
        
    def is_ended(self) -> bool:
        return self._states_info[self._current_state][3]
        
    def tic(self) -> None:
        if kbhit():
            input_char = getch().lower().decode('UTF-8')
            state = self._states_info[self._current_state]
            if input_char in state[2]:
                self._change_state(state[2][input_char])

def main001() -> None:
    demo = SnakeGameDemo001()

    while not demo.is_ended():
        demo.tic()
     


 # --------------------------------------
 # --------------------------------------
 # --------------------------------------
 
    
# exemple avec des Emums
# --------------------------------------
# Exemple de machine d'état pour gérer l'état principal d'une simulation de jeu.
# Utilise une approche de programmation procédurale, simple mais sans branchement.
# Principalement basé sur une structure de données basée sur des Enum.
# Utilise 'sleep'
# --------------------------------------

from enum import Enum, auto

class SnakeGameDemo002:
    
    class State(Enum):
        SPLASH_SCREEN = (auto(), 'SplashScreen', False)
        HOME = (auto(), 'Home', False)
        IN_GAME = (auto(), 'InGame', False)
        CONFIG = (auto(), 'Configuration', False)
        PAUSED = (auto(), 'Paused', False)
        QUIT = (auto(), 'Quit', True)
    
        def __init__(self, state_id, text, quitting):
            self.state_id = state_id
            self.text = text
            self.quitting = quitting

        @staticmethod
        def _finalize():
            SnakeGameDemo002.State.SPLASH_SCREEN.sleeping = (1, SnakeGameDemo002.State.HOME)
            SnakeGameDemo002.State.HOME.sleeping = (None, None)
            SnakeGameDemo002.State.IN_GAME.sleeping = (None, None)
            SnakeGameDemo002.State.CONFIG.sleeping = (None, None)
            SnakeGameDemo002.State.PAUSED.sleeping = (None, None)
            SnakeGameDemo002.State.QUIT.sleeping = (None, None)
            
            SnakeGameDemo002.State.SPLASH_SCREEN.keys = {}
            SnakeGameDemo002.State.HOME.keys = { 'q':SnakeGameDemo002.State.QUIT, 
                                                 'g':SnakeGameDemo002.State.IN_GAME, 
                                                 'c':SnakeGameDemo002.State.CONFIG
                                               }
            SnakeGameDemo002.State.IN_GAME.keys = { 'h':SnakeGameDemo002.State.HOME, 
                                                    'p':SnakeGameDemo002.State.PAUSED
                                                  }
            SnakeGameDemo002.State.CONFIG.keys = { 'h':SnakeGameDemo002.State.HOME }
            SnakeGameDemo002.State.PAUSED.keys = { 'g':SnakeGameDemo002.State.IN_GAME, 
                                                   'h':SnakeGameDemo002.State.HOME
                                                 }
            SnakeGameDemo002.State.QUIT.keys = {}
            
    def __init__(self):
        self.__initial_state : SnakeGameDemo002.State = SnakeGameDemo002.State.SPLASH_SCREEN
        self.__current_state : SnakeGameDemo002.State | None = None
        self.__change_state(self.__initial_state)
        
    def _change_state(self, new_state : State) -> bool:
        self.__current_state = new_state
        system('cls')
        print(self.__current_state.text)
        if self.__current_state.sleeping[0]:
            sleep_duration, sleep_nexst_state = self.__current_state.sleeping
            sleep(sleep_duration)
            self._change_state(SnakeGameDemo002.State(sleep_nexst_state))
        
    def is_ended(self) -> bool:
        return self.__current_state.quitting
        
    def tic(self) -> None:
        if kbhit():
            input_char = getch().lower().decode('UTF-8')
            if input_char in self.__current_state.keys:
                self._change_state(self.__current_state.keys[input_char])

SnakeGameDemo002.State._finalize()

def main002():
    demo = SnakeGameDemo002()

    while not demo.is_ended():
 
       demo.tic()
       


 # --------------------------------------
 # --------------------------------------
 # --------------------------------------




# Exemples avec des classes spécialisées
class GameState:
    
    def __init__(self, name: str, terminal: bool = False) -> None:
        self.name : str = name
        self.terminal : bool = terminal
        self.timed_transition : float | None = None
        self.keyboard_transitions : dict[str, GameState] = {}
        
    def set_timed_transition(self, time: float, gameState: GameState) -> None:
        self.timed_transition = (time, gameState)
        
    def add_keyboard_transition(self, keyboard_transition: str, gameState: GameState) -> None:
        self.keyboard_transitions[keyboard_transition] = gameState

    def is_keyboard_transiting(self, actual_key : str) -> None | GameState:
        return self.keyboard_transitions.get(actual_key, None)

    def wait_for_time_transiting(self) -> None | GameState:
        if self.timed_transition:
            sleep(self.timed_transition[0])
            return self.timed_transition[1]
        else:
            return None


class SnakeGameDemo003:
    def __init__(self):
        self.states : list[GameState] = []
        self.initial_state : GameState | None = None
        self.current_state : GameState | None = None
        
    def add_state(self, state: GameState) -> None:
        self.states.append(state)
        
    def set_initial_state(self, initial_state: GameState) -> None:
        if initial_state in self.states:
            self.initial_state = initial_state
            self.__set_new_state(self.initial_state)

    def __set_new_state(self, state : GameState) -> None:
        system('cls')
        self.current_state = state
        print(self.current_state.name)
        possible_next_state = self.current_state.wait_for_time_transiting()
        if possible_next_state:
            self.__set_new_state(possible_next_state)

    def tic(self) -> None:
        if kbhit():
            input_char = getch().lower().decode('UTF-8')
            possible_next_state = self.current_state.is_keyboard_transiting(input_char)
            if possible_next_state:
                self.__set_new_state(possible_next_state)
            
        
            
    
        
def main003():
    demo = SnakeGameDemo003()
    
    splashScreenState = GameState('SplashScreen', False)
    homeState = GameState('Home', False)
    configState = GameState('Configuration', False)
    inGameState = GameState('In Game', False)
    pausedState = GameState('Paused', False)
    quitState = GameState('Quit', True)
    
    splashScreenState.set_timed_transition(1, homeState)
    homeState.add_keyboard_transition('c', configState)
    homeState.add_keyboard_transition('g', inGameState)
    homeState.add_keyboard_transition('q', quitState)
    inGameState.add_keyboard_transition('h', homeState)
    inGameState.add_keyboard_transition('p', pausedState)
    configState.add_keyboard_transition('h', homeState)
    pausedState.add_keyboard_transition('g', inGameState)
    
    demo.add_state(splashScreenState)
    demo.add_state(homeState)
    demo.add_state(configState)
    demo.add_state(inGameState)
    demo.add_state(pausedState)
    demo.add_state(quitState)
    demo.set_initial_state(splashScreenState)
    
    while not demo.current_state.terminal:
        demo.tic()


          
 # --------------------------------------
 # --------------------------------------
 # --------------------------------------


    
if __name__ == '__main__':
    main003()
