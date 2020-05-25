class Kwadrat():
    def __init__(self, bok ):
        self.bok = bok
    def sketch(self, x, y):
        self.x = x
        self.y = y
        rect(self.x, self.y, self.bok, self.bok)

    
class PasiastyKwadrat(Kwadrat): #
    def sketchPasiasty(self, x, y, paski): 
        Kwadrat.sketch(self, x, y) 
        space = self.bok/paski 
        _xLinii_ = 0 
        for pasek in range(0, paski): 
            line(x+_xLinii_, y, x+_xLinii_, y+self.bok)
            _xLinii_ +=space
            
            
class KwadratColorowy(Kwadrat): #dodana klasa ktura dziedziczy z bazowej klasy konstruktor 
    def sketchColor(self, x, y):
        fill(19, 80, 60, 70)
        Kwadrat.sketch(self, x, y,)
    
        


        

    
    
def setup():
    size(500, 500)
    malyKwadrat = Kwadrat(50.0) 
    malyKwadrat.sketch(200, 300) 
    duzyKwadrat = Kwadrat(200.0)
    duzyKwadrat.sketch(50, 75)
    malyKwadrat.sketch(100, 200)
    malyPasiastyKwadrat = PasiastyKwadrat(30.0) 
    malyPasiastyKwadrat.sketchPasiasty(300, 300, 5) 
    malyPasiastyKwadrat.sketchPasiasty(100,300, 8) 
    duzyPasiastyKwadrat  = PasiastyKwadrat(120.0)
    duzyPasiastyKwadrat.sketchPasiasty(300, 50, 12)
    duzyPasiastyKwadrat.sketch(350, 300) 


    duzyKwadratColorowy = KwadratColorowy(120.0)
    duzyKwadratColorowy.sketchColor(200, 200)
