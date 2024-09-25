#################################################   
# Import 
from matplotlib import cm
import matplotlib.pyplot as plt
import numpy as np
import scipy
import time
from random import *
from numpy.linalg import inv,cond
from scipy.optimize import root
from scipy.optimize import least_squares

#################################################   
# Lecture mesures de fichier mesuresX.dat

with open("mesuresX.dat", "r") as f:
    line= list()

    donnees= list()
    xdata= list()
    q1data= list()
    q2data= list()
    q3data= list()
    for line in f:
        if "#" in line:
            # on saute la ligne
            continue
        data = line.split()
        donnees.append((float(data[0]), float(data[1]),float(data[2]), float(data[3]), float(data[4]),float(data[5])))
        xdata.append([float(data[3]), float(data[4]),float(data[5])])
        q1data.append(float(data[0]))
        q2data.append(float(data[1]))
        q3data.append(float(data[2]))
        tt=(float(data[0])+ float(data[1])+float(data[2])- float(data[5]))
#        print(tt)
#donnees
#xdata
################################################# 
# Calcul du MGD du robot RRR réel
# pour simuler le robot réel
# INPUT:  q = vecteur de configuration (radian, mètre, radian)
# OUTPUT: Xc = vecteur de situation = (x,y, theta)
# ATTENTION: Paramètres du robot A RENTRER
################################################# 
##def mgdreel(qrad):
##    l=[? , ?, ?]
##    c1= np.cos(qrad[0])
##    s1=np.sin(qrad[0])
##    q12= qrad[0]+qrad[1]
##    c12= np.cos(q12)
##    s12=np.sin(q12)
##    theta= qrad[0]+qrad[1]+qrad[2]
##    c123=np.cos(theta)
##    s123=np.sin(theta)
##    x=l[0]*c1 + l[1]*c12 +l[2]*c123 + uniform(-0.1,0.2)
##    y=l[0]*s1 + l[1]*s12 +l[2]*s123 + uniform(-0.1,0.2)
##
##    Xd=[x,y,theta]
##    return Xd
