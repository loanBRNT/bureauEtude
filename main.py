import numpy as np
import matplotlib.pyplot as plt
from mdi import*
from mgi import*
from mgd import*
from traj import*


print("\n======== BERNAT GAUDILLAT MISSIER SOUBIRANT =========")
'''
#saisie des entrees
correctA = false
correctB = false
correctV = false
correctTeta = false
rayon = L1 + L2 + L3 + L4 + L5

while !correctA :
    print("\nEntrez les coordonnees du point A : ")
    xA = int(input("\nxA = "))
    yA = int(input("\nyA = "))
    zA = int(input("\nzA = "))
    if ((np.sqrt(xA**2 + yA**2) <= rayon) and (zA <= h1+h2+2) and (zA >= h1+h2+1)):
        correctA = true
    else :
        print("\nValeur(s) hors limites, reessayez...")     

while !correctB :
    print("\nEntrez les coordonnees du point B : ")
    xB = int(input("\nxB = "))
    yB = int(input("\nyB = "))
    zB = int(input("\nzB = "))
    if ((np.sqrt(xB**2 + yB**2) <= rayon) and (zB <= h1+h2+2) and (zB >= h1+h2+1)):
        correctB = true
    else :
        print("\nValeur(s) hors limites, reessayez...")  
        
while !correctV : 
    print("\nEntrez la vitesse V du robot : ")
    V = int(input("\nV = "))
    if ((V > 0) and (V <= Vmax)) :
        correctV = true
    else : 
        print("\nValeur hors limites, reessayez...")
  
while !correctTeta :      
    print("\nEntrez l'angle Teta : ")
    teta = int(input("\nteta = "))
    if ((teta <= 2*np.pi/2) and (teta >= -(2*np.pi/2))) :
        correctTeta = true
    else :
        print("\nValeur hors limites, reessayez...")

A = [xA, yA, zA]
B = [xB, yB, zB]
'''

V = 10
teta = 0
A=[3,1,2]
B=[3,1,3]

#x,y,z,teta = -2.0, 1, 2.0, np.pi
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
