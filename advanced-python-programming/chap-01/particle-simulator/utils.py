import math 

class Particle:

    def __init__(self, x, y, ang_vel):
        self.x = x
        self.y = y
        self.ang_vel = ang_vel

    
class ParticleSimulatorUnderPerformance:
    
    def __init__(self, particles):
        self.particles = particles

    def evolve(self, dt):
        TIMESTEP = 0.000_01
        nsteps = int(dt/TIMESTEP)

        for i in range(nsteps):
            for p in self.particles:
                # 1 - calculate the directional derivsatives:
                norm = math.sqrt(p.x**2 + p.y**2)
                v_x = -p.y/norm
                v_y = p.x/norm

                #2 - calculate the displacement during dt:
                dx = TIMESTEP * p.ang_vel * v_x
                p.x += dx

                dy = TIMESTEP * p.ang_vel * v_y
                p.y += dy

                #3 - repeat for nsteps

class ParticleSimulator:
    
    def __init__(self, particles):
        self.particles = particles

    def evolve(self, dt):
        TIMESTEP = 0.000_01
        nsteps = int(dt/TIMESTEP)

        for p in self.particles:
            t_x_ang = TIMESTEP * p.ang_vel

            for i in range(nsteps):
                norm = math.sqrt(p.x**2 + p.y**2)
                p.x = p.x-t_x_ang * p.y/norm
                p.y = p.y+t_x_ang * p.x/norm

