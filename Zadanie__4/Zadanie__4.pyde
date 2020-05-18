
add_library('pdf') 
def setup():
    global img 
    size(400, 400) 
   
    
    img = loadImage("jeg.png")
    beginRecord(PDF, "jeg.pdf")
    


def draw():
    global img

    image(img, 0,0, height, width) 
    
    if key == CODED:
        if keyCode == RIGHT:
            img = loadImage("mes.png")
        
    if key == CODED:
        if keyCode == UP:
            img = loadImage("jeg.png")
    if key == CODED:
        if keyCode == LEFT:
            
            img = loadImage("mas.png")
            

            
    endRecord()

def mousePressed():
    exit()
