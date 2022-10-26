import numpy as np

from mgi import*
from mgd import*
print("\n")

x,y,z,teta = mgd(0,0,1,0)
print("x=",x," y=",y," z=",z, " teta=",teta)
x,y,z,teta = mgd(np.pi/2,0,1,0)
print("x=",x," y=",y," z=",z, " teta=",teta)
x,y,z,teta = mgd(3*np.pi/2,np.pi,1,0)
print("x=",x," y=",y," z=",z

















      , " teta=",teta)



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


