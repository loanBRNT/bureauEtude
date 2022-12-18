import numpy as np
from donnee import *

def mdi(xpoint,ypoint,zpoint,q1,q2,q3,q4):
    # Jacobienne preferencielle
    # Indice preferenciel : j = 2
    

    JQ_R01 = np.array([[np.cos(q1), -np.sin(q1), 0, 0, 0, 0],
                       [np.sin(q1), np.cos(q1), 0, 0, 0, 0],
                       [0, 0, 1, 0, 0, 0],
                       [0, 0, 0, np.cos(q1), -np.sin(q1), 0],
                       [0, 0, 0, np.sin(q1), np.cos(q1), 0],
                       [0, 0, 0, 0, 0, 1]])

    JQ_R12 = np.array([[np.cos(q2), -np.sin(q2), 0, 0, 0, 0],
                       [np.sin(q2), np.cos(q2), 0, 0, 0, 0],
                       [0, 0, 1, 0, 0, 0],
                       [0, 0, 0, np.cos(q2), -np.sin(q2), 0],
                       [0, 0, 0, np.sin(q2), np.cos(q2), 0],
                       [0, 0, 0, 0, 0, 1]])

                       
    JQ_P34 = np.array([[1, 0, 0, -L3],
                       [0, 1, 0, 0],
                       [0, 0, 1, -L3],
                       [0, 0, 0, 1]])

    JQ_pref = np.array([[np.sin(q2) * (L2 + L3), 0, 0, 0],
                        [np.cos(q2) * (L2 + L3), L3, 0, 0],
                        [0, 0, 1, 0],
                        [0, 0, 0, 0],
                        [0, 0, 0, 0],
                        [1, 1, 0, 1]])

    JQ= np.dot(JQ_P34, JQ_pref)
    JQ= np.dot(JQ_R12, JQ)
    JQ = np.dot(JQ_R01, JQ)
    return np.dot(np.linalg.inv(JQ),np.array([[xpoint],[ypoint],[zpoint]]))