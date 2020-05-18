
def setup():

    size(400, 400)
    printArray(PFont.list())
    f = createFont("Georgia", 70)
    textFont(f)
def draw():

    clear()
    textFont = f 

    if (mouseX < width/2-60) and (mouseY < height/2+60):# skoro czcionka jest ustawiona na 70pkt, to różnica 120 to trochę za dużo
        fill(40, 117, 22, 200)    
        text("M", width/2-60, height/2+60) 
        fill(40, 117, 22, 80)
        text("M", width/2-57, height/2+62) 
    else:
         fill (130,0,0)
         text("M", width/2-57, height/2+62) 
   



    if keyPressed:
        if key == 's' or key == 'S':
             fill(40, 117, 22, 200)
             text("S", width/2+50, height/2+80) 
             fill(40, 117, 22, 80)
             text("S", width/2+53, height/2+82)
    else:
        fill (120,0,0)
        text("S", width/2+53, height/2+82)
   
    if key == CODED:
        if keyCode == RIGHT:
            fill(200, 70, 22, 200)    
            text("M", width/2-60, height/2+60) 
            fill(200, 80, 22, 80)
            text("M", width/2-57, height/2+62)
    if key == CODED:
        if keyCode == LEFT:
            fill(210, 120, 22, 200)
            text("S", width/2+50, height/2+80) 
            fill(210, 120, 22, 80)
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
    
#1,5p
