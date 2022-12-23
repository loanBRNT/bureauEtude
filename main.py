import numpy as np
import matplotlib.pyplot as plt
from mdi import*
from mgi import*
from mgd import*
from traj import*

#####################################################################################

def verifConfig(x,y,z,teta):
    Z1 = x - (L5 * np.cos(teta)) - L1
    Z2 = y - (L5 * np.sin(teta))
    W = L2
    W2 = (L4 + L3)
    c2 = round((Z1 ** 2 + Z2 ** 2 - W ** 2 - W2 ** 2) / (2 * W * W2), 2)
    if 1 - c2 * c2 < 0:
        return False
    return True

def saisieEtVerifEntree():
    correctConfig = False
    rayon = L1 + L2 + L3 + L4 + L5

    while not correctConfig:
        correctB = False
        correctV = False
        correctTeta = False

        # Tests individuels

        while not correctB:
            print("\nEntrez les coordonnees du point B : ")
            xB = int(input("\nxB = "))
            yB = int(input("\nyB = "))
            zB = int(input("\nzB = "))
            if (np.sqrt(xB ** 2 + yB ** 2) <= rayon) and (zB <= h1 + h2 + 2) and (zB >= h1 + h2):
                correctB = True
            else:
                print("\nValeur(s) hors limites, reessayez...")

        while not correctV:
            print("\nEntrez la vitesse V du robot : ")
            V = int(input("\nV = "))
            if (V > 0) and (V <= Vmax):
                correctV = True
            else:
                print("\nValeur hors limites, reessayez...")

        while not correctTeta:
            print("\nEntrez l'angle Teta : ")
            teta = float(input("\nteta = "))
            if (teta <= 2 * np.pi / 2) and (teta >= -(2 * np.pi / 2)):
                correctTeta = True
            else:
                print("\nValeur hors limites, reessayez...")

        # Tests generaux
        if verifConfig(xB, yB, zB, teta):
            correctConfig = True
        else:
            print("La configuration demandee est impossible")

    return [xB, yB, zB], teta, V

def relanceProg(point,teta):
    print(f"Le robot est bien arrive en x={point[0]}, y={point[1]}, z={point[2]}, teta={teta}")
    print("----------------------------------------------------------")
    print("Que voulez vous faire ?")
    print("1 - Repartir a la position initiale")
    print("2 - Commander le robot a partir de sa position actuelle")
    print("3 - Stopper le programme")
    print("----------------------------------------------------------")
    return int(input("Num choisi :"))

###############################################################################################
print("\n======== BERNAT GAUDILLAT MISSIER SOUBIRANT =========")

#position initiale
A=pos_initiale
teta=teta_initial
#Boucle du programme
stop=False
while not stop:
    print(f"Le Robot est en position : x={A[0]}, y={A[1]}, z={A[2]}, teta={teta}")
    #saisie des entrees
    B, teta, V = saisieEtVerifEntree()

    #debut de l'algo
    dicoTraj = traj(A,B,V)

    sol1={'q1':[],'q2':[],'q3':[],'q4':[],'dq1':[],'dq2':[],'dq3':[],'dq4':[]}
    sol2={'q1':[],'q2':[],'q3':[],'q4':[],'dq1':[],'dq2':[],'dq3':[],'dq4':[]}
    L = len(dicoTraj['x'])
    for i in range(L):
        #MGI
        sol1i, sol2i = mgi(dicoTraj['x'][i],dicoTraj['y'][i],dicoTraj['z'][i],teta)
        sol1['q1'].append(sol1i[0])
        sol1['q2'].append(sol1i[1])
        sol1['q3'].append(sol1i[2])
        sol1['q4'].append(sol1i[3])
        sol2['q1'].append(sol2i[0])
        sol2['q2'].append(sol2i[1])
        sol2['q3'].append(sol2i[2])
        sol2['q4'].append(sol2i[3])

        #MDI
        dsol1i = mdi(dicoTraj['xpoint'][i],dicoTraj['ypoint'][i],dicoTraj['zpoint'][i],sol1i[0],sol1i[1],sol1i[2],sol1i[3])
        dsol2i = mdi(dicoTraj['xpoint'][i],dicoTraj['ypoint'][i],dicoTraj['zpoint'][i], sol2i[0], sol2i[1], sol2i[2], sol2i[3])
        sol1['dq1'].append(dsol1i[0])
        sol1['dq2'].append(dsol1i[1])
        sol1['dq3'].append(dsol1i[2])
        sol1['dq4'].append(dsol1i[3])
        sol2['dq1'].append(dsol2i[0])
        sol2['dq2'].append(dsol2i[1])
        sol2['dq3'].append(dsol2i[2])
        sol2['dq4'].append(dsol2i[3])

    print("--------- Choix de l'affichage ----------")
    print("1 - Visualisation des qi pour la solution 1")
    print("2 - Visualisation des dqi pour la solution 1")
    print("3 - Visualisation des qi pour la solution 2")
    print("4 - Visualisation des dqi pour la solution 2")
    print("5 - Visualisation de la trajectoire")
    print("-----------------------------------------")
    choix = input("Vous pouvez entrer plusieurs chiffres :")
    if "1" in choix:
        plt.figure(5)
        plt.title("SOLUTION 1 - Affichage des différents q")
        plt.plot(dicoTraj['t'], sol1['q1'], "r", label="q1")
        plt.plot(dicoTraj['t'], sol1['q2'], "b", label="q2")
        plt.plot(dicoTraj['t'], sol1['q3'], "g", label="q3")
        plt.plot(dicoTraj['t'], sol1['q4'], "y", label="q4")
        plt.legend()
        plt.show()
    if "2" in choix:
        plt.figure(7)
        plt.title("SOLUTION 1 - Affichage des différents dq")
        plt.plot(dicoTraj['t'], sol1['dq1'], "r", label="dq1")
        plt.plot(dicoTraj['t'], sol1['dq2'], "b", label="dq2")
        plt.plot(dicoTraj['t'], sol1['dq3'], "g", label="dq3")
        plt.plot(dicoTraj['t'], sol1['dq4'], "y", label="dq4")
        plt.legend()
        plt.show()
    if "3" in choix:
        plt.figure(6)
        plt.title("SOLUTION 2 - Affichage des différents q")
        plt.plot(dicoTraj['t'], sol2['q1'], "r", label="q1")
        plt.plot(dicoTraj['t'], sol2['q2'], "b", label="q2")
        plt.plot(dicoTraj['t'], sol2['q3'], "g", label="q3")
        plt.plot(dicoTraj['t'], sol2['q4'], "y", label="q4")
        plt.legend()
        plt.show()
    if "4" in choix:
        plt.figure(8)
        plt.title("SOLUTION 2 - Affichage des différents dq")
        plt.plot(dicoTraj['t'], sol2['dq1'], "r", label="dq1")
        plt.plot(dicoTraj['t'], sol2['dq2'], "b", label="dq2")
        plt.plot(dicoTraj['t'], sol2['dq3'], "g", label="dq3")
        plt.plot(dicoTraj['t'], sol2['dq4'], "y", label="dq4")
        plt.legend()
        plt.show()
    if "5" in choix:
        plt.figure(1)
        plt.title("Evolution de la position")
        plt.plot(dicoTraj['t'], dicoTraj["s"], "+", label="s(t)")
        plt.plot(dicoTraj['t'], dicoTraj["x"], "b+", label="x(t)")
        plt.plot(dicoTraj['t'], dicoTraj["y"], "r+", label="y(t)")
        plt.plot(dicoTraj['t'], dicoTraj["z"], "g+", label="z(t)")
        plt.legend()
        plt.show()
        plt.figure(2)
        plt.title("Evolution de la vitesse")
        plt.plot(dicoTraj['t'], dicoTraj["spoint"], "+", label="ds(t)")
        plt.plot(dicoTraj['t'], dicoTraj["xpoint"], "b+", label="dx(t)")
        plt.plot(dicoTraj['t'], dicoTraj["ypoint"], "r+", label="dy(t)")
        plt.plot(dicoTraj['t'], dicoTraj["zpoint"], "g+", label="dz(t)")
        plt.legend()
        plt.show()
        plt.figure(3)
        plt.title("Evolution de l'acceleration'")
        plt.plot(dicoTraj['t'], dicoTraj["sseconde"], "+", label="dds(t)")
        plt.plot(dicoTraj['t'], dicoTraj["xseconde"], "b+", label="ddx(t)")
        plt.plot(dicoTraj['t'], dicoTraj["yseconde"], "r+", label="ddy(t)")
        plt.plot(dicoTraj['t'], dicoTraj["zseconde"], "g+", label="ddz(t)")
        plt.legend()
        plt.show()

    choix = relanceProg(B,teta)
    if choix == 1:
        print("Reset du robot...")
        teta=teta_initial
    elif choix == 2:
        A=B
    else:
        stop=True

print("\n======== BERNAT GAUDILLAT MISSIER SOUBIRANT =========")
exit(0)