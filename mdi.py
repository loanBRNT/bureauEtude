import numpy as np
from donnee import*

def mdi(xpoint,ypoint,zpoint,tetapoint=0):
    Jacob = np.array([0, 0, 0, 0],
                     [L2 + L3 + L4, L3 + L4, 0, 0],
                     [0, 0, 1, 0],
                     [0, 0, 0, 0],
                     [0, 0, 0, 0],
                     [1, 1, 0, 1])
