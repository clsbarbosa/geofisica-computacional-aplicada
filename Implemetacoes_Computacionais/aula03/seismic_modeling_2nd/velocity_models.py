import numpy as np

def constant_velocity(vel, dimX, dimZ):

    velocity    = np.zeros((dimZ, dimX))      # campo de velocidades    

    for k in range(dimX):
        for i in range(int(dimZ/3)):
            velocity[i, k] = vel
        for i in range(int(dimZ/3), int(dimZ)):
            velocity[i, k] = vel

    return velocity
