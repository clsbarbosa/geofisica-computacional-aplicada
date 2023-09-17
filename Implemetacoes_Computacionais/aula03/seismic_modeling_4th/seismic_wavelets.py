import numpy as np
from math import *

def ricker_wavelet(cut_frequency, dt, Ntotal):

    t = np.zeros(Ntotal)
    seismic_source = np.zeros(Ntotal)

    TF = 2 * sqrt(pi) / cut_frequency       # Período da função Gaussiana
    fc = cut_frequency / (3. * sqrt(pi))    # Frequência central

    for n in range(Ntotal):
        t[n] = ((n) * dt - TF)
        seismic_source[n] = -(-exp(-pi * (pi * fc * t[n]) ** 2) * (1 - 2 * pi * (pi * fc * t[n]) * (pi * fc * t[n])))


    return seismic_source
