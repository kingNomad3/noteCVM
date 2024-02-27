# LOOK UP TABLE
COLORS = [0,0,0]

def f1():
    print("f1")

def f2():
    print("f2")
    
def f3():
    print(COLORS)


lut = (f1, f2, f3, None, f1)
d = {"left": f1, "right": f2, "up": f3, "down": None}


KEY = 4   
if lut[KEY] :
    lut[KEY]()
KEY  = "fdsfsdfsd"

if KEY in d:
    if d[KEY]:
        d[KEY]()



# LOOK UP TABLE
COLORS = [0,0,0]

def f1():
    print("f1")

def f2():
    print("f2")
    
def f3():
    robot.set_color(COLORS)


lut = (f1, f2, f3, None, f1)
d = {"left": f1, "right": f2, "up": f3, "down": None}