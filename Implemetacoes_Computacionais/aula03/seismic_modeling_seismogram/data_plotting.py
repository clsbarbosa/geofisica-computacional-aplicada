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
    plt.ylabel("Amplitude N/m2", fontsize=16)

    ax.plot(x, seismic_signal, color ="red")
    plt.savefig(image_name, format='png', dpi=300, bbox_inches='tight')

    plt.show()



# Rotina para exbição do sismograma gerado
def plotting_seismogram(Ntotal, Nrec, seismogram, name):

    data = seismogram / np.max(np.abs(seismogram))   # nomalizando o sismograma (sis)

    ## Eixo horizontal no topo da figura
    plt.rcParams['xtick.bottom'] = False
    plt.rcParams['xtick.labelbottom'] = False
    plt.rcParams['xtick.top'] = True
    plt.rcParams['xtick.labeltop'] = True

    plt.rc('xtick', labelsize=16)
    plt.rc('ytick', labelsize=16)
    plt.rc('legend', fontsize=48)
    plt.rcParams.update({'font.size':16})

    # Scaling the axis to the original dimension
    xmin = 0
    xmax = Nrec
    zmin = 0
    zmax = Ntotal

    ## Formatação do plot
    fig, ax = plt.subplots(figsize=(8,12))
    ax.xaxis.set_label_position('top')
    im = ax.imshow(data, cmap='gray', vmin=-0.05,vmax=0.05, interpolation='bicubic', extent=[xmin,xmax,zmax,zmin], aspect=0.2)
    cbar = fig.colorbar(im, ax=ax, fraction=0.061, pad=0.02)

    cbar.set_label(label='Amplitude (N/m2)', size=18)
    cbar.ax.tick_params(labelsize=16)
    plt.xlabel('Number of Receivers', fontsize=18)
    plt.ylabel('Number of Samples', fontsize=18)

    plt.savefig(name, dpi=300,bbox_inches='tight')

    plt.show()
