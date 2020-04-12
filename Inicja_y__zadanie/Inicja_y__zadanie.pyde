def setup():
    size(400, 400)
    printArray(PFont.list())
    f = createFont("Georgia", 70)
    textFont(f)
def draw():
    clear()
    if mousePressed: # nie na kliknięcie a na najechanie miało być
        textFont = f 
        fill(40, 117, 22, 200)    
        text("M", width/2-60, height/2+60) 
        fill(40, 117, 22, 80)
        text("M", width/2-57, height/2+62) 

    if keyPressed: # nie na każdy klawisz, a na S
        fill(40, 117, 22, 200)
        text("S", width/2+50, height/2+80) 
        fill(40, 117, 22, 80)
        text("S", width/2+53, height/2+82) 
    
             
    a = createShape() 
    a.beginShape()
    a.fill(40,120,40,80) 
    a.stroke(100,100,40,80)
    a.vertex(100, height/3*2) 
    a.vertex(150, height/3*2-20)
    a.vertex(width/2, height/3*2)
    a.vertex(width-150, height/3*2+20)
    a.vertex(width-100, height/3*2)
    a.endShape(CLOSE)
    shape(a, 25, 25)

# brakuje też obsługi stzałek

# w tym stanie 0,75pkt, ale masz jeszcze czas dopisać
