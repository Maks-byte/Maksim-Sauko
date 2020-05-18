from particle import Particle

class CrazyParticle(Particle):
    
    def __init__(self, l):
        super(CrazyParticle, self).__init__(l)
        self.theta = 0.0
        
    def update(self):
        super(CrazyParticle, self).update()
        theta_vel = (self.velocity.x * self.velocity.mag()) / float(10.0)
        self.theta += theta_vel
        
    def display(self):
        super(CrazyParticle, self).display()
        with pushMatrix():
            translate(self.location.x, self.location.y)
            rotate(self.theta)
            stroke(255, 200, 200, self.lifespan)
            line(0, 0, 25, 0)