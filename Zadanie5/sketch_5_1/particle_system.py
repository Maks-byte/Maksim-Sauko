from particle import Particle
from crazy_particle import CrazyParticle

class ParticleSystem(object):
    
    def __init__(self, num, v):
        self.particles = []
        self.origin = v.get()
        for i in range(num):
            self.particles.append(Particle(self.origin))
            
    def run(self):
        for i in reversed(range(len(self.particles))):
            p = self.particles[i]
            p.run()
            if p.isDead():
                del self.particles[i]
                
    def addParticle(self):
        p = None
        if int(random(0, 7)) == 0:
            p = Particle(self.origin)
        else:
            p = CrazyParticle(self.origin)
        self.particles.append(p)
        
    def dead(self):
        return self.particles.isEmpty() 