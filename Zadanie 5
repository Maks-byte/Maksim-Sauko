class Bubble(): 
    

    ilosc = 0 
    def __init__(self, arg_x, arg_y, arg_r): 
        self.obrot = 0 
        self.wcisniety = False
        self.x = arg_x 
        self.y = arg_y 
        self.r = arg_r
    def rysuj(self): 
        triangle(30, 75, 58, 20, 86, 75)
        arc(self.x, self.y, self.r, self.r, 0+radians(self.obrot+165), PI+ radians(self.obrot+270), PIE)
    def obroc(self, stopnie): 
        self.obrot += stopnie
    def wcisnij(self):
        Bubble.ilosc +=1 
        self.wcisniety = not self.wcisniety 
        if self.wcisniety:
            fill(255, 255, 0)
        else:
            fill(70, 70, 0)
        
def setup():
    size(400, 400)
    global bubble 
    bubble = Bubble(width/2, height/2, 50)

def mouseClicked(): 
    bubble.wcisnij()
def mouseWheel(event): 
    bubble.obroc(10) 
    print(bubble.obrot) 
    
def draw(): 
    background(120)
    bubble.rysuj() 
    print(Bubble.ilosc) 
    
