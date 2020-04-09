def setup():
    global x, y, dx, dy
    x = 0 
    y = 0 
    dx = 1 
    dy = 1 
    size(1000, 1000) 
    frameRate(60) 
    global slownik_kolorow 

    slownik_kolorow = {"czerwony":(255,0,0, 80), "niebieski":(0,0,255,80), "zielony":(0,255,0,80)} 
    global lista_kolorow 
    lista_kolorow = [] 
    for klucz, wartosc in slownik_kolorow.items(): 
        lista_kolorow.append(wartosc) 

    global iteracja_programu 
    iteracja_programu = 0 

def draw(): 
    global iteracja_programu 
    iteracja_programu +=2
    background(225 ,225, 80) 
    fill(*lista_kolorow[iteracja_programu%len(lista_kolorow)]) 
    circle(x, y, 30) 
    global x, y, dx, dy
    x = x + dx 
    y = y + dy 
    if(x > 500):
         dy = -1
         if (x > 700):
             dx = -1 
             if ( x > -500): 
                 dy = 1
                 if (x > 500):
                    dx = -1
    if mousePressed: 
       exit()
       
#1,5p
  
 
 



            
