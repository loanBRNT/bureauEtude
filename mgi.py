import numpy as np
from donnee import *


def mgi(x, y, z, teta):

    # calcul de Q3
    q3 = z - h1 - h2

    # calcul de Q2

    Z1 = x - L5 * np.cos(teta) - L1
    Z2 = y - L5 * np.sin(teta)
    W = L2
    W2 = (L4 + L3)
    c2 = (Z1 ** 2 + Z2 ** 2 - W ** 2 - W2 ** 2) / (2 * W * W2)
    #ici 2 solutions possible pour q2
    s2_1 = np.sqrt(1 - c2 ** 2)
    s2_2 = -np.sqrt(1 - c2 ** 2)

    q2_1 = np.arctan2(s2_1, c2)
    q2_2 = np.arctan2(s2_2, c2)

    #calcul de q1 avec 1 solution pour chaque q2
    B1 = W + W2 * c2
    B2_1 = W2 * s2_1
    B2_2 = W2 * s2_2

    s1_1 = (B1 * Z2 - B2_1 * Z1) / (B1 ** 2 + B2_1 ** 2)
    c1_1 = (B1 * Z1 + B2_1 * Z2) / (B1 ** 2 + B2_1 ** 2)

    s1_2 = (B1 * Z2 - B2_2 * Z1) / (B1 ** 2 + B2_2 ** 2)
    c1_2 = (B1 * Z1 + B2_2 * Z2) / (B1 ** 2 + B2_2 ** 2)

    q1_1 = np.arctan2(s1_1, c1_1)
    q1_2 = np.arctan2(s1_2, c1_2)
    #calcul de q4 avec 1 solution pour chaque paire (q2,q1)

    q4_1 = -q1_1 - q2_1 + teta
    q4_2 = -q1_2 - q2_2 + teta

    sol1 = [q1_1, q2_1, q3, q4_1]
    sol2 = [q1_2, q2_2, q3, q4_2]

    return sol1, sol2
