import numpy as np

def constant_velocity(vel, dimX, dimZ):

    velocity    = np.zeros((dimZ, dimX))      # campo de velocidades    

    for k in range(dimX):
        for i in range(int(dimZ/3)):
            velocity[i, k] = vel
        for i in range(int(dimZ/3), int(dimZ)):
            velocity[i, k] = vel

    return velocity


def parallel_layers(vel, dimX, dimZ):

    velocity    = np.zeros((dimZ, dimX))      # campo de velocidades    

    for k in range(dimX):
        for i in range(int(dimZ/4)):
            velocity[i, k] = vel[0]
        for i in range(int(dimZ/4), int(dimZ)):
            velocity[i, k] = vel[1]

    return velocity
