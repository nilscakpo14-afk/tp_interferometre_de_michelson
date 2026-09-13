# Tp d'interférence a deux ondes

# Importation des bibliothèques

import numpy as np

import matplotlib.pyplot as plt

import functions

import scipy as sp


# constantes du Tp

# Etude de l'interferometre de Michelson et de ses applications

# II. Mesure de la longueur d'onde de la lumière émise par un laser.

# d: distance de déplacement du mirroir mobile 2

# lambda: longueur d'onde du laser

# q: nombre de franges noires observées

d= np.array([3.69, 4, 4.30, 4.59, 6.81, 6.48, 6.16, 5.84, 5.51, 5.22])

q = np.array([12, 13, 14, 15, 22, 21, 20, 19, 18, 17])

lambdaa = 2*d/q

lambdaa_th = 0.63 #en micrometres

u_A = functions.uncertainty_A(lambdaa)[2]

lambdaa_exp = functions.uncertainty_A(lambdaa)[0]

standard_dev_lambdaa = functions.uncertainty_A(lambdaa)[1]

epsilon_lambdaa = functions.relative_difference(lambdaa_th, lambdaa_exp)

print(f"la longueur d'onde experimentale du laser néon est : {lambdaa_exp:.4f} +/- {u_A:.4f} micrometres")
print(f"l'écart relatif de la longueur d'onde lambda à la théorie est : {epsilon_lambdaa:.4f}")

# affichage des résultats

plt.plot(d, lambdaa, label = 'evolution de de lambda en fonction de la distance d')
plt.scatter(d, lambdaa, color = 'red', label = 'points expérimentaux')

plt.xlabel('distance d en micrometres')
plt.ylabel("longueur d'onde lambda en micrometres")

plt.title('Interférence de Michelson')

plt.legend()

plt.show()

# III. Analyse spectrale d'une source polychromatique

# Raie verte de la lampe Hg

# L_c: longueur de cohérence de la source

L_c = 4.60 #en mm

c = sp.constants.c # vitesse de la lumière dans le vide en m/s

d= np.array([6.02, 9.31]) # distance de déplacement du miroir 2 en micrometres

q = np.array([20, 31]) # nombre de franges noires observées

lambdaa = 2*d/q # longueur d'onde du laser d'hélium neon en micrometres

lambdaa_th = 0.55 #en micrometres

u_A = functions.uncertainty_A(lambdaa)[2]

lambdaa_exp = functions.uncertainty_A(lambdaa)[0]

standard_dev_lambdaa = functions.uncertainty_A(lambdaa)[1]

epsilon_lambdaa = functions.relative_difference(lambdaa_th, lambdaa_exp)

print(f"la longueur d'onde experimentale de la raie vetre de la lampe Hg est : {lambdaa_exp:.4f} +/- {u_A:.4f} micrometres")
print(f"l'écart relatif de la longueur d'onde lambda à la théorie est : {epsilon_lambdaa:.4f}")

# Détermination de l'incertitude sur lambda autrement (par la mesure de la longueur de cohérence L_c)

# calcul de delta_nu

delta_nu = c/(L_c*1e-3) # en Hz

delta_lambda = (delta_nu*lambdaa_exp**2*1e-12/c)*1e6 # en micrometres

print(f"la longueur d'onde experimentale de la raie verte de la lampe Hg avec l'incertitude associée selon le calcul de la longueur de cohérence Lc est: {lambdaa_exp:.4f} +/- {delta_lambda:.4f} micrometres")

# Raies jaunes de la lampe Hg (doublet jaune)

L_c = 4.60 # L_c: longueur de cohérence de la source en mm

c = sp.constants.c # vitesse de la lumière dans le vide en m/s

d= np.array([5.20, 8.11]) # distance de déplacement du miroir 2 en micrometres

q = np.array([18, 28]) # nombre de franges noires observées

lambdaa = 2*d/q # longueur d'onde du laser d'hélium neon en micrometres

lambdaa_th = 0.578 #en micrometres

u_A = functions.uncertainty_A(lambdaa)[2]

lambdaa_exp = functions.uncertainty_A(lambdaa)[0]

standard_dev_lambdaa = functions.uncertainty_A(lambdaa)[1]

epsilon_lambdaa = functions.relative_difference(lambdaa_th, lambdaa_exp)

print(f"la longueur d'onde experimentale de la raie jaune de la lampe Hg est : {lambdaa_exp:.4f} +/- {u_A:.4f} micrometres")
print(f"l'écart relatif de la longueur d'onde lambda à la théorie est : {epsilon_lambdaa:.4f}")

# Détermination de l'incertitude sur lambda autrement (par la mesure de la longueur de cohérence L_c)

# NB: Nous n'avons pas pu mesurer la longueur de cohérence de la source pour le doublet jaune donc nous ne pouvons pas déterminer l'incertitude sur lambda par cette méthode.

# Détermination de l'écart entre les longueurs d'onde du doulet jaune

d = 79.15 # distance parcourue par le miroir durant un lobe en micrometres

delta_lambda_1_2 = lambdaa_exp**2/(2*d)

print(f"l'écart entre les longueurs d'onde du doublet jaune de la lampe de Hg est : {delta_lambda_1_2:.4f} micrometres'")