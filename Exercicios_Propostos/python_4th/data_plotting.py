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



# Rotina para exbição do sismograma gerado
def plotting_seismogram(dimX, dimZ, Ntotal, dt, h, sis, name):

    ## Eixos em dimensões reais
    scaleX = 1.0 / 1000
    scaleZ = 1

    Xmin = (0 * h) * scaleX
    Xmax = (dimX * h) * scaleX
    Zmin = (0 * dt) * scaleZ
    Zmax = (Ntotal * dt) * scaleZ

    data = sis / np.max(np.abs(sis))   # nomalizando o sismograma (sis)

    ## Eixo horizontal no topo da figura
    plt.rcParams['xtick.bottom'] = False
    plt.rcParams['xtick.labelbottom'] = False
    plt.rcParams['xtick.top'] = True
    plt.rcParams['xtick.labeltop'] = True

    plt.rc('xtick', labelsize=16)
    plt.rc('ytick', labelsize=16)
    plt.rcParams.update({'font.size':16})

    ## Formatação do plot
    fig, ax = plt.subplots(figsize=(12,12))
    ax.xaxis.set_label_position('top')
    im = ax.imshow(data, cmap='gray', vmin=-0.05,vmax=0.05,extent=[Xmin,Xmax,Zmax,Zmin], interpolation='bicubic', aspect=2)
    cbar = fig.colorbar(im, ax=ax, fraction=0.04, pad=0.08, label='Amplitude', aspect=15)
    plt.xlabel('Distance (Km)', fontsize=16)
    plt.ylabel('Time (s)', fontsize=16)
    plt.savefig(name, dpi=300,bbox_inches='tight')

    plt.show()
