import numpy as np
from donnee import*

def verif(M):
    if M[0][0] != M[1][1] or M[1][0] != -M[0][1]:
        return False
    return True

def mgd(q1,q2,q3,q4):

    T01 = np.array([[np.cos(q1), -np.sin(q1), 0, L1],
                    [np.sin(q1), np.cos(q1), 0, 0],
                    [0, 0, 1, 0],
                    [0, 0, 0, 1]])

    T12 = np.array([[np.cos(q2), -np.sin(q2), 0, L2],
                    [np.sin(q2), np.cos(q2), 0, 0],
                    [0, 0, 1, h1],
                    [0, 0, 0, 1]])

    T23 = np.array([[1, 0, 0, L3],
                    [0, 1, 0, 0],
                    [0, 0, 1, q3],
                    [0, 0, 0, 1]])

    T34 = np.array([[np.cos(q4), -np.sin(q4), 0, L4],
                    [np.sin(q4), np.cos(q4), 0, 0],
                    [0, 0, 1, 0],
                    [0, 0, 0, 1]])

    T45 = np.array([[1, 0, 0, L5],
                    [0, 1, 0, 0],
                    [0, 0, 1, h2],
                    [0, 0, 0, 1]])

    T35 = np.dot(T34,T45)
    T25 = np.dot(T23, T35)
    T15 = np.dot(T12, T25)
    T05 = np.dot(T01, T15)

    x=T05[0][3]
    y=T05[1][3]
    z=T05[2][3]

    if not verif(T05):
        print("error")
        return None,None,None,None
    te = np.arccos(T05[0][0])

    return x,y,z,te


