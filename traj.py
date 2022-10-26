import numpy as np

def traj(A,B,V):

    Fe=10       #frequence d'echantillonage

    #calcul dAB
    dAB= np.sqrt((B[0]-A[0])**2 + (B[1]-A[1])**2 + (B[2]-A[2])**2)

    #calcul tf

    tf= 2*dAB/V
    t1=tf/2

    t=np.arange(0,tf+1/Fe,1/Fe) #t de 0 a tf selon la Fe


    # tant que t < t1, s = s1, ensuite s=s2 .....
    #A CODER
    #de 0 a t1
    s1 = V/t1 * ((t**2)/2)
    s1point = V*t/t1
    s1seconde = V/t1

    #sinon de t1 a tf
    s2 = (t**2)*(-V/2*t1) + (2*V*t) - (V*t1/2)
    s2point = t*(-V/t1) + 2*V
    s2seconde = -V/t1

    #objectif: afficher s spoint et sseconde sur graphe 