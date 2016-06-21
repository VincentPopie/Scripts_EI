# -*- coding: utf-8 -*- 
# Vincent Popie

import numpy as np
import matplotlib.pyplot as plt

from lecture_fichier import lecture_interieur
from calcul_travail import calcul_travail_int


#Liste des fichiers et hauteur correspondante
#A ameliorer
liste_num_fichier = [50, 52, 55, 57, 60, 62, 65, 67, 70, 72, 75, 77, 80, 82, 85, 87, 90, 92, 95, 97, 100]
hauteur=[5,5.25,5.5,5.75,6,6.25,6.5,6.75,7,7.25,7.5,7.75,8,8.25,8.5,8.75,9,9.25,9.5,9.75,10]

nb_hauteur = len(hauteur)
W = np.empty(nb_hauteur)
U_zero = np.empty(nb_hauteur)

j = 0

for num_fichier in liste_num_fichier:
 
	[Condu, x, U] =	lecture_interieur(num_fichier)

	KR = float(Condu)
	nb_lignes = x.shape[0]

	r = np.sqrt(x[:,0]*x[:,0] + x[:,1]*x[:,1])

	U_zero[j] = KR/np.pi
	W[j] = calcul_travail_int(x,U)
	j = j +1


#Calcul de la correction de col interieure
W_Kelvin = U_zero*U_zero*hauteur
correction = (W-W_Kelvin)/W_Kelvin

#Plot de la correction pour le manuscrit
plt.figure(1,figsize=(12.5,12))

plt.plot(hauteur, correction, 'rx-',label=r'$\Delta h_{\mathrm{int}}/r_0$',lw=3)

plt.legend()
plt.xlabel(r'$H/R_0$',fontsize=50)
plt.ylabel(r'$\Delta h_{\mathrm{int}}/r_0$',fontsize=50)
ax = plt.gca()
ax.set_ylim([0.0,0.2])

plt.savefig('../Figure/correction_int.pdf', format='pdf')
#plt.show()


