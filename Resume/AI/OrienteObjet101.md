# oriente objet 
```python

class Tower:

        #self est comme le this 
    def __init__(self, pos_x,pos_y): # attention au valeur par defaut ne JAMAIS utiliser un type modifiable  def __init__(self, pos_x = [0,0],pos_y = 0): 
       
        self.pos_x = pos_x
        self.pos_y = pos_y
    
    def move(self,x,y):
        self.pos_x = pos_x
        self.pos_y = pos_y

    #s'il n'y a pas de self c'est une methode statique 
    def target():
        print('targeting')

    @staticmethod
    #va modifier la methode en enlevant le paramettre implicite du self, mais on peut lui passer d'autre variable en parametre 
    def trarget_2()
        print('targeting v2 ')

    @staticmethod
    #va modifier la methode en enlevant le paramettre implicite du self, mais on peut lui passer d'autre variable en parametre 
    def trarget_3(color)
        print(f'targeting v2 : {color}')


 #un underscore avamt la variale est priver (par convention)
    #self._pos_x = pos_x 
 # double underscore est private
    #self.__pos_x = pos_x <<<Name mangling le nom __post_x  => _Tower_post_x
    # print(tower._Tower_pos_x)




#la fonction declar le parametre de facon explicition
# une fonction membre pass toujorus le premier paramettre de facon implicite dans ce cas ci le self. c;est l'usage implicite
tower = Tower(2,2)
tower.move(0,1) #move(tower,0,1)

#peut etre appeler sois a partie de la class ou de l'objet 
Tower.target()
tower.target()#move(tower) un self a ete passer, ne va pas marcher a cause du self

#va fonctionner 
Tower.trarget_2()
tower.trarget_2()

Tower.trarget_3('black')
tower.trarget_3('black')

#Les porporitete (pas de getter et setter)
#sa simule un acces publique par un getter et setter cacher a l'interieur 

@proprerty
    def pos_x(self):#conceptuellement un accesseur (getter)
        return self.__pos_x 

    @pos_x.setter
    def pos_x(self,x): #conceptuellement un mutateur (setter)
    if x>100 or > 200:
        rase ValueError("ayoye...arrange ton code")
    self.__pos_x = abs(x)
    #clamping 
    self.__pos_z = max(100,min(z,200))

#pas de parenthese
tower.pos_x = 777 # on peut faire ceci grace au setter 
print(tower.pos_x)


class Tower:
    
    def __init__(self, pos_x = 0, pos_y = 0): # attention aux valeurs par défaut, ne JAMAIS utiliser un type modifiable
        self.__pos_x = pos_x # private 
        # ^^^ NAME MANGLING __pos_x => _Tower__pos_x
        self._pos_y = pos_y # protected
        
    @property
    def pos_x(self): # conceptuellement un accesseur
        return self.__pos_x
    
    @pos_x.setter
    def pos_x(self, x): # conceptuellement un mutateur
        if x < 100 or x > 200:
            raise ValueError('Ayoye... arrange ton code espèce de moron...')
        self.__pos_x = x
        
    def move(self, x, y):
        self.__pos_x += x
        self._pos_y += y
        
    def target():
        print('targeting...')
        
    @staticmethod
    def target_v2(color):
        print(f'targeting v2 : {color}')
        
    
tower = Tower(2, 2)
tower.move(0, 1) # move(tower, 0, 1)
tower.pos_x = 666
print(tower.pos_x)

Tower.target()
#tower.target() # target(tower)

Tower.target_v2('black')
tower.target_v2('black')
pass



````