from crazy_particle import CrazyParticle
from particle import Particle
from particle_system import ParticleSystem

systems = None

def setup():
    global systems
    size(750, 750)
    systems = []
    
def draw():
    background(255)
    for ps in systems:
        ps.run()
        ps.addParticle()
        
def mousePressed():
    systems.append(ParticleSystem(3, PVector(mouseX, mouseY))) 
