add_library('pdf') 
def setup():
    global img 
    size(400, 400) # to nie są proporcje zdjęcia dokumentowego
   
    img = loadImage("jeg.png")
    beginRecord(PDF, "jeg.pdf")
    
    
def draw():
    global img

    image(img, 0,0, height, width) 
    if keyPressed:
        if key == CODED:
            if keyCode == RIGHT:
                img = loadImage("mes.png")
        if key == CODED:
            if keyCode == UP:
                img = loadImage("jeg.png")
        if key == CODED:
            if keyCode == LEFT:
                img = loadImage("mas.png")
                
        endRecord() # dzięki umieszczeniu pod tym warunkiem nie wykona się w pierwszej klatce, a dopiero po kliknięicu, dziei czemu możemy zapisać z dodatkowym obrazkiem

def mousePressed():
    exit()
    
# 1,5pkt
