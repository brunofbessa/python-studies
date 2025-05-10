from matplotlib import pyplot as plt
from matplotlib import animation
from random import uniform
import timeit
from utils import *


def visualize(simulator):
    X = [p.x for p in simulator.particles]
    Y = [p.y for p in simulator.particles]

    fig = plt.figure()
    ax = plt.subplot(111, aspect="equal")
    (line,) = ax.plot(X, Y, "ro")

    # Axis limits
    plt.xlim(-1, 1)
    plt.ylim(-1, 1)

    def init():
        line.set_data([], [])
        return (line,)
    
    def animate(i):
        simulator.evolve(0.1)
        X = [p.x for p in simulator.particles]
        Y = [p.y for p in simulator.particles]
        line.set_data(X, Y)
        return (line,)
    
    # Call the animate function each 10 ms
    anim = animation.FuncAnimation(fig, animate, 
                                   init_func=init, 
                                   blit=True, 
                                   interval=10)
    plt.show()


def test_visualize():
    particles = [
        Particle(0.3, 0.5, 1.7),
        Particle(0.0, -0.5, -0.1)
    ]
    simulator = ParticleSimulator(particles)
    visualize(simulator)

def benchmark():
    particles = [
        Particle(uniform(-1.0, 1.0), 
                 uniform(-1.0, 1.0), 
                 uniform(-5.0, 5.0))
                for i in range (20)]
    simulator = ParticleSimulator(particles)
    simulator.evolve(0.1)
    #visualize(simulator)

if __name__ == '__main__':

    benchmark()
