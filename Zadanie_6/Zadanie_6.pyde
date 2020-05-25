class Ellipse():
    def __init__(self, side):
        self.side = side
    def sketch(self, x, y):
        self.x = x
        self.y = y
        ellipse(self.x, self.y, self.side, self.side)
        
class LineEllipse(Ellipse):
    def sketchLines(self, x, y, lines): 
        Ellipse.sketch(self, x, y) 
        space = self.side/lines 
        _xLinii_ = 0 
        for lines in range(0, lines): 
            line(x+_xLinii_, y, x+_xLinii_, y+self.side)
            _xLinii_ +=space
            
# miałaś dopisać klasę dziedziczącą z moich (np. rysującą kolorowy pasiasty kwadrat, albo kwadrat w kropki...), a nie zamienić moim nazwy i nazwę jednej funkcji (kwadratu na koło)
# proszę o poprawienie
        
def setup():
    size(500, 500)
    fill(270, 80, 80, 50)
    littleEllipse = Ellipse(90.0) 
    littleEllipse.sketch(330, 250) 
    fill(270, 80, 80, 50)
    duzyLineEllipse  = LineEllipse(120.0)
    duzyLineEllipse.sketchLines(275, 190, 12)
    
