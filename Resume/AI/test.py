import random
class Gestion():
    def __init__(self, height,width):
        self.width =  width
        self.height = height
        self.arr = self.create_matrice(height,width)


    def create_matrice(self,height,width):
        return  [[(random.randint(0, 1)) for i in range(width)], [((random.randint(0, 1))) for i in range(height)]]
       
       

t = Gestion(3,200)

# print(t.width)
# print(t.height)     
            
print(t.arr)
        
    
