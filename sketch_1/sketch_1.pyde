def setup():
    size(800, 800)
    rectMode(CORNER)

def draw():
    rect(width/2, height/2, 100, 100)
    if mousePressed: # tylko przy pierwszym kliknięciu widać efekt
        line(50,30,100,200)
    line(150, 25, mouseX, mouseY)
    
# 1,75 pkt
