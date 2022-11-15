import numpy as np
import matplotlib.pyplot as plt
import math


def traj(A, B, V):
    Fe = 10  # frequence d'echantillonage

    # calcul dAB
    dAB = np.sqrt((B[0] - A[0]) ** 2 + (B[1] - A[1]) ** 2 + (B[2] - A[2]) ** 2)
    print("\ndab : ", dAB)
    # calcul tf

    tf = 2 * dAB / V
    t1 = tf / 2
    print("tf : ", tf)

    t = np.arange(0, tf + 1 / Fe, 1 / Fe)  # t de 0 a tf selon la Fe
    s = np.arange(0, tf + 1 / Fe, 1 / Fe)
    spoint = np.arange(0, tf + 1 / Fe, 1 / Fe)
    sseconde = np.arange(0, tf + 1 / Fe, 1 / Fe)

    indext1 = len(s)//2
    # de 0 a t1 on suit une 1ere loi et de t1 a tf une seconde loi
    # calcul de s
    s[:indext1] = (V * (t[:indext1]**2)) / (2*t1) + 0
    s[indext1:] = (t[indext1:]**2 * -V) / (2 * t1) + (2 * V * t[indext1:]) - dAB
    # calcul de spoint
    spoint[:indext1] = V * t[:indext1] / t1
    spoint[indext1:] = t[indext1:] * (-V / t1) + 2 * V
    # calcul de sseconde
    sseconde[:indext1] = V / t1
    sseconde[indext1:] = -V / t1

    # affichage des 3 lois

    plt.figure(1)
    plt.plot(t, s, "r+", label="position")
    plt.legend()
    plt.show()
    plt.figure(2)
    plt.plot(t, spoint, "b+", label="vitesse")
    plt.legend()
    plt.show()
    plt.figure(3)
    plt.plot(t, sseconde, "g+", label="accélération")
    plt.legend()
    plt.show()
