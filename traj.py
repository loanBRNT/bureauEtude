import numpy as np
import matplotlib.pyplot as plt
import math


def traj(A, B, V):
    Fe = 100  # frequence d'echantillonage

    # Calcul dAB
    diffx = B[0] - A[0]
    diffy = B[1] - A[1]
    diffz = B[2] - A[2]
    dAB = np.sqrt(diffx **2 + diffy**2 + diffz**2)
    # Calcul tf

    tf = 2* dAB / V
    t1 = tf / 2

    t = np.arange(0, tf + 1 / Fe, 1 / Fe)  # t de 0 a tf selon la Fe
    s = np.arange(0, tf + 1 / Fe, 1 / Fe)
    spoint = np.arange(0, tf + 1 / Fe, 1 / Fe)
    sseconde = np.arange(0, tf + 1 / Fe, 1 / Fe)

    indext1 = len(s)//2
    # De 0 a t1 on suit une 1ere loi et de t1 a tf une seconde loi
    # Calcul de s
    s[:indext1] = (V * (t[:indext1]**2)) / (2*t1) + 0
    s[indext1:] = (t[indext1:]**2 * -V) / (2 * t1) + (2 * V * t[indext1:]) - dAB
    # Calcul de spoint
    spoint[:indext1] = V * t[:indext1] / t1
    spoint[indext1:] = t[indext1:] * (-V / t1) + 2 * V
    # Calcul de sseconde
    sseconde[:indext1] = V / t1
    sseconde[indext1:] = -V / t1

    # Calcul de x(s), y(s) et z(s)
    x = A[0] + s * (diffx/dAB)
    y = A[1] + s * (diffy/dAB)
    z = A[2] + s * (diffz/dAB)

    # Calcul de Xpoint Ypoint Zpoint
    xpoint = spoint * (diffx / dAB)
    ypoint = spoint * (diffy / dAB)
    zpoint = spoint * (diffz / dAB)

    # Calcul de Xseconde Yseconde Zseconde
    xseconde = sseconde * (diffx / dAB)
    yseconde = sseconde * (diffy / dAB)
    zseconde = sseconde * (diffz / dAB)

    # Affichage

    dico = {"x":x,"y":y,"z":z,"t":t,"s":s,
            "xpoint":xpoint,"ypoint":ypoint,"zpoint":zpoint,"spoint":spoint,
            "xseconde":xseconde,"yseconde":yseconde,"zseconde":zseconde,"sseconde":sseconde}

    return dico

