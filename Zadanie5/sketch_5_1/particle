class Particle(object):
    
    def __init__(self, l):
        self.acceleration = PVector(0, 0.1)
        self.velocity = PVector(random(-3, 3), random(-5, 0))
        self.location = l.get()
        self.lifespan = 255.0
        
    def run(self):
        self.update()
        self.display()
        
    def update(self):
        self.velocity.add(self.acceleration)
        self.location.add(self.velocity)
        self.lifespan -= 3.0
        
    def display(self):
        stroke(200, 70, 70, self.lifespan)
        strokeWeight(3)
        fill(255, 100, 100, self.lifespan)
        ellipse(self.location.x, self.location.y, 40, 40)
        
    def isDead(self):
        return self.lifespan < 0.0