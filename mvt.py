from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
import numpy as np


def mvt(A, B, V):
    fig = plt.figure()
    ax = plt.axes(projection='3d')

    z = [A[0], B[0]]
    x = [A[1], B[1]]
    y = [A[2], B[2]]

    #ax.plot3D(x, y, z, c='red')
    ax.scatter(A[0],A[1],A[2], c='blue')
    ax.scatter(B[0], B[1], B[2], c='red')
    ax.set_title('Test')
    plt.show()


A = [0, 0, 0]
B = [5, 5, 5]
V = 10

mvt(A, B, V)
