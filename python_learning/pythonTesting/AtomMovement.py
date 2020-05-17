

from matplotlib import pyplot as plt 
from matplotlib import animation 



class Atom:
    def __init__(self, x, y,direction):
        self.x = x
        self.y = y
        self.direction = direction

        

class AtomMovement:
    def __init__(self, atoms):
        self.atoms = atoms

    def evolve(self,dir):
        timesteps = 0.00001
        nsteps = int(dir/timestamp)

        for i in range(nsteps):
            for j in self.atoms:
                normal = (j.x**2 + j.y**2)**0.5

                    # Direction
                vX = -j.y/normal
                vY = j.x/normal

                    #Displacement
                dX = timesteps * j.direction * vX 
                dY = timesteps * j.direction * vY

                j.x += dX
                j.Y += dY 



def visualize(movement):
    X = [ p.x for p in movement.atoms ]
    Y = [ p.y for p in movement.atoms ]
        
    fig = plt.figure()
    ax = plt.subplot(111,aspect='equal')
    line, = ax.plot(X,Y,'ro')

    plt.xlim(-1,1)
    plt.ylim(-1,1)


    def init():
        line.set_data([],[])
        return line,

    def animate(i):
        movement.evolve(0.01)

        X = [p.x for p in movement.atom]
        Y = [p.y for p in movement.atom]

        line.set_data(X,Y)
        return line, 

    anim = animation.FuncAnimation(fig,animate, init_function=init, blit = True, interval = 10)

    plt.show()


def test_visualize():
    atoms = [Atom(0.3,0.5,1), Atom(0.0,-0.5,-1), Atom(-0.1,0.4,3)]
    movement = AtomMovement(atoms)
    visualize(movement)

if __name__ == '__main__':
    test_visualize()

