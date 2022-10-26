#connaitre vitesse de l'OT
import numpy as np
from donnee import  *


def mcd(vq1,vq2,vq3,vq4):
    Jacob=np.array([0, 0, 0, 0],
                   [L2+L3+L4, L3+L4, 0, 0],
                   [0, 0, 1, 0],
                   [0, 0, 0, 0],
                   [0, 0, 0, 0],
                   [1, 1, 0, 1])
    vX = np.dot(Jacob,np.array([[vq1] , [vq2] , [vq3] , [vq4]]))
    return vX