def setup():
    global jj
    size(400,300) 
    jj = loadImage("jj.png")
    noFill()
    imageMode(CENTER)

def draw():
    try:
        image(jj, 200, 200) # tylko tą linijkę sprawdzamy pod kątem błędu
    except:
        textSize(12)
        fill(255,0,0)
        text("nie znaleziono pliku", 143, 200)
        stroke(255,0,0)
    else:
        stroke(0,191,255)
    finally:
        rect(140, 140, 120, 120)

def mousePressed():
    exit()
    
# 1,5pkt
