

def setup():
    global jj
    
    size(400,300) 
   
    jj = loadImage("jj.png")
    

    


def draw():
    try:
        
        imageMode(CENTER)
        image(jj, 200, 200)
        stroke(0,191,255)
        noFill()
        rect(140, 140, 120, 120)
    except:
        textSize(12)
        fill(255,0,0)
        text("nie znaleziono pliku", 143, 200)
        stroke(255,0,0)
        noFill()
        rect(140, 140, 120, 120)

            


def mousePressed():
    exit()
