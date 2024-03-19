# State Machine

- contite a generalisation de la machine d'etat
- les element commes les if, elif, else, while, for, break, continue, return, yield, try, except, finally, with, assert, import, from, class, def, pass, global, nonlocal, lambda, del, raise, as, et les expressions conditionnelles (if-elif-else) sont des etats
- Il on qqchose de different a faire pour chaque etat

## Exemple
```python
    etat = 0
    swtitch(etat):
        case 0:
            print('etat 0')
            etat = 1
            break
        case 1:
            print('etat 1')
            etat = 2
            break
        case 2:
            print('etat 2')
            etat = 0
            break
        default:
            print('etat par defaut')
            etat = 0
            break
```

## Exercise 

- Ecrire 1 programme qui change d'etat de lumiere . Passer de vert a jaune apres 0.8 sec, puis de jaune a rouge apres 0.2 sec, puis de rouge a vert apres 1 sec
```python

import os
import time

class TrafficLight:
    def __init__(self):
        self.state = 0

    def change_state(self):
        if self.state == 0:
            print('vert')
            time.sleep(0.8)
            self.state = 1
        elif self.state == 1:
            print('jaune')
            time.sleep(0.2)
            self.state = 2
        elif self.state == 2:
            print('rouge')
            time.sleep(1)
            self.state = 0
        else:
            print('etat par defaut')
            self.state = 0

    def run(self):
        while True:
            os.system('color 0a')
            self.change_state()

traffic_light = TrafficLight()
traffic_light.run()
```