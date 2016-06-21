# -*- coding: utf-8 -*- 
# Vincent Popie

import numpy as np
import matplotlib.pyplot as plt

from lecture_fichier import lecture_exterieur
from calcul_travail import calcul_travail_ext

#Liste des fichiers et hauteur correspondante
#A ameliorer
liste_num_fichier = [50, 52, 55, 57, 60, 62, 65, 67, 70, 72, 75, 77, 80, 82, 85, 87, 90, 92, 95, 97, 100]
hauteur=[5,5.25,5.5,5.75,6,6.25,6.5,6.75,7,7.25,7.5,7.75,8,8.25,8.5,8.75,9,9.25,9.5,9.75,10]

nb_hauteur = len(hauteur)
W = np.empty(nb_hauteur)
W_Kelvin = np.empty(nb_hauteur)
U_zero = np.empty(nb_hauteur)


j = 0

for num_fichier in liste_num_fichier:
 
	[Condu, x, U, modU] =	lecture_exterieur(num_fichier,False)
	[Condu, x, U_Kelvin, modU_Kelvin] = lecture_exterieur(num_fichier,True)

	KR = float(Condu)
	nb_lignes = x.shape[0]

	r = np.sqrt(x[:,0]*x[:,0] + x[:,1]*x[:,1])
	#print r[16]

	U_zero[j] = KR/np.pi
	W[j] = calcul_travail_ext(x,modU)
	W_Kelvin[j] = calcul_travail_ext(x,modU_Kelvin)
	j = j +1

# Calcul des corrections extérieures
correction_ext = 2*W/(U_zero*U_zero)
correction_ext_Kelvin = 2*W_Kelvin/(U_zero*U_zero)

# Plot pour le manuscrit
plt.figure(1,figsize=(13,12))

plt.plot(hauteur, correction_ext, 'rx-',label=r'$\Delta h/r_0$', lw=2)
plt.plot(hauteur, correction_ext_Kelvin, 'bo-',label=r'$\Delta h_{\mathrm{Kelvin}}/r_0$',lw=2)

plt.legend(loc=7)
plt.xlabel(r'$H/R_0$',fontsize=50)
plt.ylabel(r'$\Delta h/r_0$',fontsize=50)
plt.ylim=([0.5,1])

plt.savefig('../Figure/correction_ext.pdf', format='pdf')
#plt.show()


