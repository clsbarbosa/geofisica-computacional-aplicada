import matplotlib.pyplot as plt
import numpy as np
from math import *

def plotting_seismic_signal(seismic_signal, image_name):

    plt.rcParams.update({'font.size':16})    

    # data to be plotted
    x = np.arange(0, len(seismic_signal))
 
    fig, ax = plt.subplots(figsize=(15,3))

    # plotting
    plt.xlabel("Number of Samples", fontsize=16)
    plt.ylabel("Amplitude (N/m2)", fontsize=16)

    ax.plot(x, seismic_signal, color ="red")
    plt.savefig(image_name, format='png', dpi=300, bbox_inches='tight')

    plt.show()