# Command line: python -m pytest test_simulator.py

import pytest 
from simulator import Particle, ParticleSimulator

def test_evolve():
    particles = [Particle( 0.3, 0.5, +1),
                Particle( 0.0, -0.5, -1),
                Particle(-0.1, -0.4, +3)]
    
    simulator = ParticleSimulator(particles)
    simulator.evolve(0.1)

    p0, p1, p2 = particles

    def fequal(a, b, eps=1e-5):
        return abs(a-b) < eps

    assert fequal(p0.x, 0.210269)