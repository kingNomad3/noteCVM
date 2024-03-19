import os
import time
import sys
import msvcrt


class GameState:
    def __init__(self):

        self.splash_state = 0
        self.home_state = 1
        self.game_state = 2
        self.end_state = 3
        self.config_state = 4
        self.pause_state = 5
        self.proceed = True

        self.current_state = self.splash_state
        self.input_char = None
        


    def splash(self):
        if self.current_state == self.splash_state:
            time.sleep(1)
            self.current_state = self.home_state
    
    def home(self):
        if self.input_char == 'g':
            self.current_state = self.game_state
        elif self.input_char == 'q':
            self.current_state = self.end_state
            self.proceed = False
        elif self.input_char == 'c':
            self.current_state = self.config_state
        elif self.input_char == 'h':
            self.current_state = self.pause_state
        print(self.input_char, end='')

    def game(self):
        if self.input_char == 'p':
            self.current_state = self.pause_state
        elif self.input_char == 'h':
            self.current_state = self.home_state
        print(self.input_char, end='')
    
    def config(self):
        if self.input_char == 'h':
            self.current_state = self.home_state
        print(self.input_char, end='')
        
    def pause(self):
        if self.input_char == 'h':
            self.current_state = self.home_state
        elif self.input_char == 'g':
            self.current_state = self.game_state
        print(self.input_char, end='')


def main():
    gs = GameState()

    while gs.proceed:
        
        # print("current state: ",gs.current_state)

        if gs.current_state == gs.splash_state :
                print("current state: ",gs.current_state)
                gs.splash()
                
                 

        if msvcrt.kbhit():
            user_input = msvcrt.getch().lower().decode('utf-8')

            # if user_input == 'q':
            #     gs.proceed = False

           
            if gs.current_state == gs.home_state:
                print("current state: ",gs.current_state)
                gs.home()
            elif gs.current_state == gs.game_state:
                print("current state: ",gs.current_state)
                gs.game()
            elif gs.current_state == gs.config_state:
                print("current state: ",gs.current_state)
                gs.config()
            elif gs.current_state == gs.pause_state:
                print("current state: ",gs.current_state)
                gs.pause()

            
        
            # print("current state: ",gs.current_state)
            

    print('\nEnd!!')


if __name__ == '__main__':
    main()