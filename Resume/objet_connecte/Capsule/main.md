from finite_state_machine import FiniteStateMachine
from state import State
from transition import Transition
import time


class LightsTransition(Transition):
    def __init__(self, next_state: State = None, duree : int = 1) -> None:
        self.duree = duree
        super().__init__(next_state)

    @property
    def is_transiting(self) -> bool:
        return True
    
    def _do_transiting_action(self) -> None:
        time.sleep(self.duree)        

class LightStates(State):
    def __init__(self, parameters: "State.Parameters", color = "red") -> None:
        self.color = color
        super().__init__(parameters)
    
    def _do_in_state_action(self):
        print(self.color)
        
class TraficLight(FiniteStateMachine):
    def __init__(self) -> None:
        parameters = LightStates.Parameters()
        layout = FiniteStateMachine.Layout()
        rouge = LightStates(parameters, 'red')
        jaune = LightStates(parameters, 'jaune')
        vert = LightStates(parameters, 'vert')
        transition_r_v = LightsTransition(vert, 5)
        transition_v_j = LightsTransition(jaune, 5)
        transition_j_r =  LightsTransition(rouge, 1)
        
        rouge.add_transition(transition_r_v)
        jaune.add_transition(transition_j_r)
        vert.add_transition(transition_v_j)
        
        states = [rouge,jaune,vert]
        layout.add_states(states)
        layout.initial_state = rouge
        
        super().__init__(layout, uninitialized=True)
    

def main():
    print("Fichier de test")
    
    fsm = TraficLight()
    fsm.reset()
    print(fsm.current_operational_state)
    print(fsm.current_applicative_state.color)
    for i in range(10):
        fsm.track()
        print(fsm.current_applicative_state.color)



if __name__ == "__main__":
    main()

