import numpy as np
import matplotlib.pyplot as plt
from mdi import*
from mgi import*
from mgd import*
from traj import*

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
        correctA = False
        correctB = False
        correctV = False
        correctTeta = False

        # Tests individuels

        while not correctA:
            print("\nEntrez les coordonnees du point A : ")
            xA = int(input("\nxA = "))
            yA = int(input("\nyA = "))
            zA = int(input("\nzA = "))
            if (np.sqrt(xA ** 2 + yA ** 2) <= rayon) and (zA <= h1 + h2 + 2) and (zA >= h1 + h2 + 1):
                correctA = True
            else:
                print("\nValeur(s) hors limites, reessayez...")

        while not correctB:
            print("\nEntrez les coordonnees du point B : ")
            xB = int(input("\nxB = "))
            yB = int(input("\nyB = "))
            zB = int(input("\nzB = "))
            if (np.sqrt(xB ** 2 + yB ** 2) <= rayon) and (zB <= h1 + h2 + 2) and (zB >= h1 + h2 + 1):
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
            teta = int(input("\nteta = "))
            if (teta <= 2 * np.pi / 2) and (teta >= -(2 * np.pi / 2)):
                correctTeta = True
            else:
                print("\nValeur hors limites, reessayez...")

        # Tests generaux
        if verifConfig(xA, yA, zA, teta) and verifConfig(xB, yB, zB, teta):
            correctConfig = True

    return [xA, yA, zA], [xB, yB, zB], teta, V

print("\n======== BERNAT GAUDILLAT MISSIER SOUBIRANT =========")

#saisie des entrees
A, B, teta, V = saisieEtVerifEntree()

'''V = 10
teta = 0
A=[3,1,2]
B=[3,1,3]'''

#debut de l'algo
dico = traj(A,B,V)
sol1={'q1':[],'q2':[],'q3':[],'q4':[]}
sol2={'q1':[],'q2':[],'q3':[],'q4':[]}
L = len(dico['x'])
for i in range(L):
    sol1i, sol2i = mgi(dico['x'][i],dico['y'][i],dico['z'][i],teta)
    sol1['q1'].append(sol1i[0])
    sol1['q2'].append(sol1i[1])
    sol1['q3'].append(sol1i[2])
    sol1['q4'].append(sol1i[3])
    sol2['q1'].append(sol2i[0])
    sol2['q2'].append(sol2i[1])
    sol2['q3'].append(sol2i[2])
    sol2['q4'].append(sol2i[3])

    #Il faudra retirer le # pour tester le mdi, une fois bon, faut juste ajouter dans des listes et afficher a la suite
    #print(mdi(dico['xpoint'],dico['ypoint'],dico['zpoint'],sol1i[0],sol1i[1],sol1i[2],sol1i[3]))

plt.figure(4)
plt.plot(dico['t'],sol1['q1'], label="q1")
plt.legend()
plt.show()
plt.figure(5)
plt.plot(dico['t'],sol1['q2'], label="q2")
plt.legend()
plt.show()
plt.figure(6)
plt.plot(dico['t'],sol1['q3'], label="q3")
plt.legend()
plt.show()
plt.figure(7)
plt.plot(dico['t'],sol1['q4'], label="q4")
plt.legend()
plt.show()
