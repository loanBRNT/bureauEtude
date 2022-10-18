
import numpy as np

def mgi(T01,T12,T23,T34,Te04):
    T10 = np.linalg.inv(T01)
    T21 = np.linalg.inv(T12)
    Te14 = np.dot(T10,Te04)
    Te24 = np.dot(T21,Te14)
    print(Te24[0][0])
    return 0