def setup():
    size(400, 600)
    frameRate(10)                      
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
    iteracja_programu +=1            
                                      
    stroke(0,0,255,80)                
    stroke(*slownik_kolorow["niebieski"])
    point(width/2,height/2)           
    fill(*lista_kolorow[iteracja_programu%len(lista_kolorow)])
                                      
   
    translate(60,150)
  
    rect(60,iteracja_programu,width/20,height/20)                   
    

    
    if mousePressed:
        exit()
    

# powtarzamy kolekcje (typy złożone wbudowane):
# krotka () stosujemy gdy potrzeba przechować wartości tylko do odczytu
# zbiór {} stosujemy, gdy chcemy zachować tylko wartości oryginalne, wczytywać bez powtórzeń 
# lista [] stosujemy w większości przypadków
# słownik {:} w praktyce stosujemy, gdy będziemy stosowali komuikację programu z zewnętrznymi komponentami (np.innymi programami, gdyż świetnie się mapuje na uniwersjalne pliki json i xml)
