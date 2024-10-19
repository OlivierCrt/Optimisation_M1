import numpy as np
from scipy.optimize import minimize
import matplotlib.pyplot as plt
"""Executer le fichier les deux graphiques vont s'afficher"""




def aire_triangle(positions):
    x1, y1, x2, y2, x3, y3 = positions
    return -0.5 * abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) 

# Contraintes
def staubli(positions):
    x1, y1, x2, y2, x3, y3 = positions
    return 1000 - np.sqrt(x1**2 + y1**2)

def mitsubishi(positions):
    x1, y1, x2, y2, x3, y3 = positions
    return 2000 - np.sqrt(x2**2 + y2**2)

def epson(positions):
    x1, y1, x2, y2, x3, y3 = positions
    return 750 - np.sqrt(x3**2 + y3**2)

# Contrainte de longueur du bus
def taille_bus(positions):
    x1, y1, x2, y2, x3, y3 = positions
    dist12 = np.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    dist23 = np.sqrt((x3 - x2)**2 + (y3 - y2)**2)
    dist31 = np.sqrt((x1 - x3)**2 + (y1 - y3)**2)
    return 6520 - (dist12 + dist23 + dist31)

# Contrainte de hauteur maximale
def contraite_hauteur_max(positions):
    x1, y1, x2, y2, x3, y3 = positions
    return min(750 - y1, 750 - y2, 750 - y3)

# Conditions initiales
init = [500, 500, 800, 1000, 250, 250]

# Liste des contraintes
contrainte_dictio = [
    {'type': 'ineq', 'fun': staubli},
    {'type': 'ineq', 'fun': mitsubishi},
    {'type': 'ineq', 'fun': epson},
    {'type': 'ineq', 'fun': taille_bus},
    {'type': 'ineq', 'fun': contraite_hauteur_max}
]


#TEST

aire_opti = minimize(aire_triangle, init, constraints=contrainte_dictio)

x1_opt, y1_opt, x2_opt, y2_opt, x3_opt, y3_opt = aire_opti.x

aire_finale = -aire_triangle([x1_opt, y1_opt, x2_opt, y2_opt, x3_opt, y3_opt])

print(f"Positions optimisees : STAUBLI({x1_opt:.2f}, {y1_opt:.2f}), MITSUBISHI({x2_opt:.2f}, {y2_opt:.2f}), EPSON({x3_opt:.2f}, {y3_opt:.2f})")
print(f"Aire finale du triangle : {aire_finale:.2f} mm2")

def plot_result(x1, y1, x2, y2, x3, y3, aire_finale):
    plt.figure()

    plt.scatter(x1, y1, c='blue', label="STAUBLI", zorder=2)
    plt.scatter(x2, y2, c='red', label="MITSUBISHI", zorder=2)
    plt.scatter(x3, y3, c='green', label="EPSON", zorder=2)
    
    plt.scatter(0, 0, c='black', marker='x', label="Centre de la tâche (0, 0)", zorder=2)

    plt.fill([x1, x2, x3], [y1, y2, y3], 'cyan', alpha=0.3, zorder=1, label="Triangle formé par les robots")

    plt.text(0.5 * (x1 + x2 + x3), 0.5 * (y1 + y2 + y3), f"Aire = {aire_finale:.2f} mm²", color='black', fontsize=12, ha='center')

    plt.title("PARTIE 1")
    plt.xlabel("X [mm]")
    plt.ylabel("Y [mm]")
    plt.legend()
    plt.grid(True)
    plt.show()

plot_result(x1_opt, y1_opt, x2_opt, y2_opt, x3_opt, y3_opt, aire_finale)




##################PARTIE 2####################

def temps_parcours(positions):
    x1, y1, x2, y2, x3, y3 = positions
    v1, v2, v3 = 2000, 50, 100  
    dist12 = np.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    dist23 = np.sqrt((x3 - x2)**2 + (y3 - y2)**2)
    dist31 = np.sqrt((x1 - x3)**2 + (y1 - y3)**2)
    return (dist12 / v1) + (dist23 / v2) + (dist31 / v3)



aire_opti = aire_finale  
def contrainte_aire(positions):
    return -aire_triangle(positions) - aire_opti + 1  
contrainte_dictio.append({'type': 'ineq', 'fun': contrainte_aire})







# TEST 
resultat_optimal = minimize(temps_parcours, init, constraints=contrainte_dictio)

x1_opt, y1_opt, x2_opt, y2_opt, x3_opt, y3_opt = resultat_optimal.x

temps_final = temps_parcours([x1_opt, y1_opt, x2_opt, y2_opt, x3_opt, y3_opt])
print("\n")
print(f"Positions optimisees : STAUBLI({x1_opt:.2f}, {y1_opt:.2f}), MITSUBISHI({x2_opt:.2f}, {y2_opt:.2f}), EPSON({x3_opt:.2f}, {y3_opt:.2f})")
print(f"Temps final du parcours : {temps_final:.2f} s")

def plot_result(x1, y1, x2, y2, x3, y3, temps_final):
    plt.figure()

    plt.scatter(x1, y1, c='blue', label="STAUBLI", zorder=2)
    plt.scatter(x2, y2, c='red', label="MITSUBISHI", zorder=2)
    plt.scatter(x3, y3, c='green', label="EPSON", zorder=2)
    
    plt.scatter(0, 0, c='black', marker='x', label="Centre de la tâche (0, 0)", zorder=2)

    plt.fill([x1, x2, x3], [y1, y2, y3], 'cyan', alpha=0.3, zorder=1, label="Triangle formé par les robots")

    plt.text(0.5 * (x1 + x2 + x3), 0.5 * (y1 + y2 + y3), f"Temps = {temps_final:.2f} s", color='black', fontsize=12, ha='center')

    plt.title("PARTIE 2")
    plt.xlabel("X [mm]")
    plt.ylabel("Y [mm]")
    plt.legend()
    plt.grid(True)
    plt.show()

plot_result(x1_opt, y1_opt, x2_opt, y2_opt, x3_opt, y3_opt, temps_final)