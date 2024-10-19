#################################################   
# Import 
from matplotlib import cm
import matplotlib.pyplot as plt
import numpy as np
from random import uniform
from scipy.optimize import least_squares


################################################
#PARTIE 1
#################################################   
#ouverture fichier

with open("Mesures/mesuresAngle33.0.dat", "r") as f:
    donnees = []
    xdata = []
    q1data = []
    q2data = []
    q3data = []
    for line in f:
        if "#" in line:
            continue
        data = line.split()
        donnees.append((float(data[0]), float(data[1]), float(data[2]), float(data[3]), float(data[4]), float(data[5])))
        xdata.append([float(data[3]), float(data[4])])  
        q1data.append(float(data[0]))
        q2data.append(float(data[1]))
        q3data.append(float(data[2]))

################################################# 
# Fonction MGD du robot RRR réel
# INPUT:  q = [q1, q2, q3] = vecteur d'angles des articulations
# OUTPUT: Xd = [x, y, theta] = position finale du robot (x, y) et orientation (theta)
################################################# 


def mgdreel(qrad, l):
    # l = [l1, l2, l3] longueurs des liaisons
    c1 = np.cos(qrad[0])
    s1 = np.sin(qrad[0])
    q12 = qrad[0] + qrad[1]
    c12 = np.cos(q12)
    s12 = np.sin(q12)
    theta = qrad[0] + qrad[1] + qrad[2]
    c123 = np.cos(theta)
    s123 = np.sin(theta)
    
    x = l[0] * c1 + l[1] * c12 + l[2] * c123  
    y = l[0] * s1 + l[1] * s12 + l[2] * s123  
    
    Xd = [x, y, theta]
    return Xd


#################################################
# Fonction de résidus pour moindres carrés
def residut(l, q1data, q2data, q3data, xdata):
    res = []
    for i in range(len(q1data)):
        qrad = [q1data[i], q2data[i], q3data[i]]
        Xd = mgdreel(qrad, l) #xd mesure et xdata calcul

        res.append(Xd[0] - xdata[i][0]) 
        res.append(Xd[1] - xdata[i][1])
    return res


#################################################
def ajuster_longueurs(q1data, q2data, q3data, xdata):
    n = len(q1data)
    A = np.zeros((n * 2, 3))  
    b = np.zeros((n * 2, 1))   

    for i in range(n):
        qrad = [q1data[i], q2data[i], q3data[i]]
        
        Xd = mgdreel(qrad, [1.0, 1.0, 1.0])  
        A[2 * i, :] = [np.cos( qrad[0]), np.cos(qrad[0] + qrad[1]), np.cos(qrad[0] + qrad[1] + qrad[2])]
        A[2 * i + 1, :] = [np.sin(qrad[0]), np.sin(qrad[0] + qrad[1]), np.sin(qrad[0] + qrad[1] + qrad[2])]
        b[2 * i, 0] = xdata[i][0]  

        b[2 * i + 1, 0] = xdata[i][1] 

   
    A_transpose = A.T
    H = A_transpose @ A  

    A_b = A_transpose @ b  
    
    l_optimal = np.linalg.inv(H) @ A_b

    return l_optimal.flatten() 






#################################################
#tests
def main_partie1():
    
    verification = mgdreel([-1.570796, -2.094395, -1.570796], [6.0, 18.00, 7.99])
    

    l_optimal_calcule = ajuster_longueurs(q1data, q2data, q3data, xdata)
    
    print("Longueurs l1,l2,l3 analytiques:", l_optimal_calcule)
   
    
    l_initial = [1.0, 1.0, 1.0]
    
    
    print("Verification de la position calculee:", verification)


#################################################
#PARTIE 2
#################################################

def mgd_avec_d(qrad, l, d):
    """Calculate position considering offset d."""
    l3 = 10.0  # Length of the third link

    q12 = qrad[0] + qrad[1]
    q123 = q12 + qrad[2]

    c1, s1 = np.cos(qrad[0]), np.sin(qrad[0])
    c12, s12 = np.cos(q12), np.sin(q12)
    c123, s123 = np.cos(q123), np.sin(q123)

    cos_q123_d = c123 - s123 * d
    sin_q123_d = s123 + c123 * d

    x = l[0] * c1 + l[1] * c12 + l3 * cos_q123_d
    y = l[0] * s1 + l[1] * s12 + l3 * sin_q123_d

    return [x, y, q123 + d]

def calculer_residu(params, q1data, q2data, q3data, xdata):
    l1, l2, d = params  
    res = []

    for i in range(len(q1data)):
        qrad = [q1data[i], q2data[i], q3data[i]]
        Xd = mgd_avec_d(qrad, [l1, l2], d)
        
        res.append(Xd[0] - xdata[i][0])
        res.append(Xd[1] - xdata[i][1])
    
    return res

def construire_matrice_A_B(q1data, q2data, q3data, l3):

    N = len(q1data)
    A = np.zeros((2 * N, 3)) 
    B = np.zeros(2 * N)  
    
    for i in range(N):
        q123 = q1data[i] + q2data[i] + q3data[i]

        A[2 * i, 0] = np.cos(q1data[i])
        A[2 * i, 1] = np.cos(q1data[i] + q2data[i])
        A[2 * i, 2] = -l3 * np.sin(q123)
        B[2 * i] = l3 * np.cos(q123)

        A[2 * i + 1, 0] = np.sin(q1data[i])
        A[2 * i + 1, 1] = np.sin(q1data[i] + q2data[i])
        A[2 * i + 1, 2] = l3 * np.cos(q123)
        B[2 * i + 1] = l3 * np.sin(q123)

    return A, B

def main_partie2():
    l3 = 10.0  
    A, B = construire_matrice_A_B(q1data, q2data, q3data, l3)

    measured_positions = np.array(xdata).flatten()

    assert A.shape[0] == len(measured_positions), "Probleme dimension"

    A_T = A.T
    X_star = np.linalg.inv(A_T @ A) @ A_T @ (measured_positions - B)

    l1_opt_analytic, l2_opt_analytic, d_opt_analytic = X_star

    print("Valeurs analytiques: ", l1_opt_analytic, l2_opt_analytic, d_opt_analytic)
    
    
    #Partie3
    initial_params = [1.0, 1.0, 0.0]  
    result = least_squares(calculer_residu, initial_params, args=(q1data, q2data, q3data, xdata))
    
    l1_opt, l2_opt, d_opt = result.x  
    print("Valeurs optimisees avec least_squares: l1 =", l1_opt, ", l2 =", l2_opt, ", d =", d_opt)
    
    l1_diff = l1_opt - l1_opt_analytic
    l2_diff = l2_opt - l2_opt_analytic
    d_diff = d_opt - d_opt_analytic

    print("Differences :")
    print(f"l1 : {l1_diff:.20f}, l2 : {l2_diff:.20f}, d : {d_diff:.20f}")

    


if __name__ == "__main__":
    #main_partie1()
    print("\n")
    main_partie2()
    print("\n")
