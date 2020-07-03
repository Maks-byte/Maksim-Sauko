from abc import ABCMeta, abstractmethod # w Pythonie mechanizm klasy abstrakcyjnej nie jest wbudowany, ale umożliwia go standardowa biblioteka
class Pet():
    __metaclass__=ABCMeta # ta linia sprawia, że cała klasa jest abstrakcyjna i nie możemy stworzyć jej obiektu
    @abstractmethod # ta linia mówi, że poniższa metoda jest abstrakcyjna
    def speak(self): # ta metoda będzie występowała we wszystkich klasach pochodnych dokładnie tak samo się nazywając i przyjmując tyleż samo argumentów
        super().__init__()
        return 'no sound'
class Cat(Pet): # klasa Cat dziedziczy po Pet
    def __init__(self, name):
        self.name = name
    def speak(self): #W związku z czym musi mieć zaimplementowaną metodę abstrakcyjną o tej samej nazwie, spróbujcie zakomentować tą linię, odpalić program i przeczytać treść błędu :)
        text('meow', random(50, width-70), random(50, height-50))
        return 'meow'
class Dog(Pet):
    def __init__(self, name):
        self.name = name
    def speak(self):
        text('woof', random(50, width-70), random(50, height-50))
        return 'woof'
    def gimmePaw(self):
        image(loadImage("lapa.png"), random(50, width-70), random(50, height-100))
    def __add__(self, other):
        return self.name[0]+ ' i ' + other.name[0]
class Bunny(Pet):
    pass
class MyDog(Pet):
    def __init__(self, name):
        self.name = name 
    def speak(self): 
        text('PugPuG', random(50, width-70), random(50, height-50))
        return 'PugPuG'
    def gimmePaw2(self):
        image(loadImage("lapa2.png"), random(50, width-70), random(50, height-100))
    def __add__(self, other): # miało być odejmowanie
        return self.name[0]+ ' i ' + other.name[0]

def setup():
    size(400,400)
    fill(120)
    textSize(20)
    background(90, 50, 40)
    rex = Dog('Rex') # to psy mojej babci
    benio = Dog('Benio')
    skrypcik = Cat('Skrypcik') # mam kota o tym imieniu
    idon = MyDog('Idon')
    maya = MyDog('Maya')
    #janusz = Bunny() # odkomentujcie i sprawdźcie błąd, usuńcie dziedziczenie po Pet z klasy i sprawdźcie ponownie
    global list_of_pets
    list_of_pets = [rex, benio, skrypcik, idon, maya] # lista zawiera różne typy zwierząt
    print(isinstance(skrypcik, Pet)) # tak sprawdzamy, czy dany obiekt należy do danej klasy
    print(rex+benio) # to wypisze wynik nadpisanego dodawania
    print(isinstance(idon, Pet))
    print(idon+maya)
    #print(skrypcik + skrypcik) # to nie zadziała, bo nie wie jak dodawać do siebie koty, odkomentujcie i sprawdźcie błąd

def draw(): # mouseClicked nie zadziała bez draw
    pass
    
def mouseClicked():
    for pet in list_of_pets:
        pet.speak() # dla różnych typów (Cat, Dog) klas wywołujemy to samo polecenie jedną linijką - to właśnie przejaw polimorfizmu
        if isinstance(pet, Dog): # te które są charakterystyczne dla danego typu obiektu, musimy ująć w warunek, bo na niewłaściwym typie wywaliłoby błąd
            pet.gimmePaw()
        if isinstance(pet, MyDog): # nie ma potrzeby powtarzać warunków, to co jest wytabowane, jest nim objęte
            pet.gimmePaw2()

#1,25pkt    
