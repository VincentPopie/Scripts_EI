# -*- coding: utf-8 -*- 
# Vincent Popie

# On se place à une hauteur h fixé
# Ici h = 10
# L'ideal serait de le passer en parametre du script


import numpy as np
import matplotlib.pyplot as plt

from lecture_fichier import lecture_interieur

num_fichier = 100

[Condu, x, U] =	lecture_interieur(num_fichier)
KR = float(Condu)
nb_lignes = x.shape[0]

# Il doit y avoir moyen d'alleger cette ecriture
U_zero = np.empty((nb_lignes))
for i in range (0,nb_lignes):
	U_zero[i] = KR/np.pi

# Plot
save = True
show = False

# Pour centrer les abscisses
# Depend de la hauteur de la perforation
# Verifier si on peut faire mieux
x = x[:,2]
x = x + 5

fig = plt.figure(1,figsize=(12,10))
ax = fig.add_subplot(111)

ax.plot(x,U,'r-',label=r'$v_\mathrm{t}$',lw=4)
ax.plot(x,U_zero,'k--',label=r'$V_1^{\mathrm{perfo}}$',lw=4)

ax.set_xlabel(r'$x_1$',fontsize=50)
ax.set_ylabel(r'$v_\mathrm{t}$',fontsize=50)
ax.set_xlim([-5.2,5.2])
plt.legend(loc=9)

if save:
	#plt.savefig('Vitesse_int.png', format='png')
	plt.savefig('../Figure/Vitesse_int.pdf', format='pdf')
if show:
	plt.show()




