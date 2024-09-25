#############OBLIGATOIRE ####################################   
#%matplotlib inline
from matplotlib import cm
import matplotlib.pyplot as plt
import numpy as np
import scipy
#### Pour mesure de temps
import time
#### Pour utiliser les fonctions d'optimisation de scipy.optimize
#from scipy.optimize import minimize
#from scipy.optimize import ????
#from scipy.optimize import ???

################ Pour jouer avec la 3D
#from mpl_toolkits.mplot3d import axes3d 
#from mpl_toolkits.mplot3d import proj3d



#################################################   
#### Paramètres du robot
a,b=10,10
#################################################   
# Calcul du MGD du robot RRR
# INPUT:  q = vecteur de configuration (deg, deg, deg)
# OUTPUT: Xc = vecteur de position (x,y,z) de OT
def mgd(qdeg):

    qrad=np.deg2rad(qdeg)
    c1= np.cos(qrad[0])
    s1=np.sin(qrad[0])
    c23= np.cos(qrad[2]+qrad[1])
    s23= np.sin(qrad[2]+qrad[1])
    c2=np.cos(qrad[1])
    s2=np.sin(qrad[1])
    x= a*c1*c2 + b*c1*c23
    y= a*s1*c2 + b*s1*c23
    z= a*s2 + b*s23
    Xd=np.array([x,y,z])
    return Xd

#################################################   
# Calcul de J(q) du robot RRR
# INPUT:  q = vecteur de configuration (deg, deg, deg)
# OUTPUT: jacobienne(q) analytique:
def jacobienne(qdeg):
    qrad=np.deg2rad(qdeg)
    c1= np.cos(qrad[0])
    s1=np.sin(qrad[0])
    c23= np.cos(qrad[2]+qrad[1])
    s23= np.sin(qrad[2]+qrad[1])
    c2=np.cos(qrad[1])
    s2=np.sin(qrad[1])
 
    Ja=np.array([[-a*s1*c2 -b*s1*c23, -a*c1*s2 -b*c1*s23,  -b*c1*s23], 
                [a*c1*c2 + b*c1*c23, -a*s1*s2 -b*s1*s23,  -b*s1*s23], 
                 [0, a*c2 + b*c23, b*c23]])

    return Ja


##### Test du MGD
# INPUT de q en degré #
qdeg = [90, 0, 90]
Xd= mgd(qdeg)
print("X=", Xd[0], "Y = ", Xd[1], "Z= ",Xd[2])

##### Test du MGD
# INPUT de q en degré #
qdeg = [90, 0, 90]
Xd= mgd(qdeg)
print("X=", Xd[0], "Y = ", Xd[1], "Z= ",Xd[2])

#pas variable
q_valeur=[]
e_valeur=[]


def q_suivant_pasvariable(q_actuel, pas_param,x_desire=(0,0,0),iterations=0) :
    
    #x-mgd= erreur
    erreur= x_desire-mgd(q_actuel)
    norme_erreur = np.linalg.norm(x_desire-mgd(q_actuel))
    critere_erreur=0.5*norme_erreur**2

    e_valeur.append(critere_erreur)


    if (critere_erreur < 0.01):
              
              plt.plot(range(iterations+1),e_valeur,marker ='o')
              plt.title("graph")
              plt.xlabel("Iterations")
              plt.ylabel("Erreur")
              plt.show()
              
              print ("Angles finaux et iterations:")
              return q_actuel,iterations
              #
              
    

    pas_param = max(0.01, pas_param * (0.5 ** iterations))
    print(pas_param)
    q_actuel=q_actuel + pas_param*np.dot(np.transpose(jacobienne(q_actuel)),erreur)
    return (q_suivant_pasvariable(q_actuel,pas_param,x_desire,iterations+1))





q_suivant_pasvariable((5,5,5),0.15,(10,0,5))