import numpy as np

from mgi import*
from mgd import*
from traj import*

'''
A=[1,1,1]
B=[6,1,1]
V=10
traj(A,B,V)
'''

print("\n")

x,y,z,teta = mgd(0,np.pi/2,np.pi/2,np.pi/2)
print("x=",x," y=",y," z=",z, " teta=",teta)
sol1, sol2 = mgi(x,y,z,teta)
print("1: ",sol1," 2: ",sol2)
print(mgd(sol1[0],sol1[1],sol1[2],sol1[3]))
print(mgd(sol2[0],sol2[1],sol2[2],sol2[3]))

'''
#Jacobienne
JQ_R01 = np.array([[np.cos(q1), -np.sin(q1), 0, 0, 0, 0],
                   [np.sin(q1), np.cos(q1), 0, 0, 0, 0],
                   [0, 0, 1, 0, 0, 0],
                   [0, 0, 0, np.cos(q1), -np.sin(q1), 0],
                   [0, 0, 0, np.sin(q1), np.cos(q1), 0],
                   [0, 0, 0, 0, 0, 1]])

JQ_R02 = np.array([[np.cos(q2), -np.sin(q2), 0, 0, 0, 0],
                   [np.sin(q2), np.cos(q2), 0, 0, 0, 0],
                   [0, 0, 1, 0, 0, 0],
                   [0, 0, 0, np.cos(q2), -np.sin(q2), 0],
                   [0, 0, 0, np.sin(q2), np.cos(q2), 0],
                   [0, 0, 0, 0, 0, 1]])

JQ_P34 = np.array([[1, 0, 0, 0, 0, 0],
                   [0, 1, 0, 0, 0, 0],
                   [0, 0, 1, 0, 0, 0],
                   [0, 0, 0, 1, 0, 0],
                   [0, 0, 0, 0, 1, 0],
                   [0, 0, 0, 0, 0, 1]])

JQ_pref = np.array([[np.sin(q2)*(L2+L3),0,0],
                    [np.cos(q2)*(L2+L3),L3,0,0],
                    [0,0,1,0],
                    [0,0,0,0],
                    [0,0,0,0],
                    [1,1,0,1]])

JQ = np.dot(JQ_R01,np.dot(JQ_R02,np.dot(JQ_P34,JQ_pref)))
'''


