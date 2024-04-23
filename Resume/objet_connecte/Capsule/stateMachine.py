import os
import time
import msvcrt
from enum import Enum

class State(Enum):
    SPLASH = 0
    HOME = 1
    GAME = 2
    END = 3
    CONFIG = 4
    PAUSE = 5

class GameState:
    def __init__(self):
        self.current_state = State.SPLASH
        self.proceed = True

    def handle_input(self, user_input):
        if self.current_state == State.HOME:
            self.handle_home_input(user_input)
        elif self.current_state == State.GAME:
            self.handle_game_input(user_input)
        elif self.current_state == State.CONFIG:
            self.handle_config_input(user_input)
        elif self.current_state == State.PAUSE:
            self.handle_pause_input(user_input)

    def handle_home_input(self, user_input):
        if user_input == 'g':
            self.current_state = State.GAME
        elif user_input == 'q':
            self.current_state = State.END
            self.proceed = False
        elif user_input == 'c':
            self.current_state = State.CONFIG
        elif user_input == 'h':
            self.current_state = State.PAUSE
        print(user_input + '\n', end='')

    def handle_game_input(self, user_input):
        if user_input == 'p':
            self.current_state = State.PAUSE
        elif user_input == 'h':
            self.current_state = State.HOME
        print(user_input + '\n', end='')

    def handle_config_input(self, user_input):
        if user_input == 'h':
            self.current_state = State.HOME
        print(user_input + '\n', end='')

    def handle_pause_input(self, user_input):
        if user_input == 'h':
            self.current_state = State.HOME
        elif user_input == 'g':
            self.current_state = State.GAME
        print(user_input + '\n', end='')

def main():
    gs = GameState()

    while gs.proceed:
        if gs.current_state == State.SPLASH:
            print("current state: ", gs.current_state)
            time.sleep(1)
            gs.current_state = State.HOME
        else:
            print("current state: ", gs.current_state)
            while True:
                if msvcrt.kbhit():
                    user_input = msvcrt.getch().lower().decode('utf-8')
                    gs.handle_input(user_input)
                    break

    print('\nEnd!!')

if __name__ == '__main__':
    main()
