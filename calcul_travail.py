# -*- coding: utf-8 -*- 
# Vincent Popie

#####################################
# Module pour le calcul du travail  #
#####################################

import numpy as np

def calcul_travail_ext(x,modU):
	"""
	Calcule la correction exterieure
	 
	Parametre d'entree :
	x[:,3] : les coordonnees
	modU[:] : le module de la vitesse

	Calcule l'integrale de r|U|^2 et la renvoie
	"""
	r = np.sqrt(x[:,0]*x[:,0] + x[:,1]*x[:,1])
	f = r[:]*modU[:]*modU[:]
	W = PointMilieu(r,f)
	return W

def calcul_travail_int(x,U):
	"""
	Calcule la correction interieure
	 
	Parametre d'entree :
	x[:,3] : les coordonnees
	U[:] : le module de la vitesse

	Calcule l'integrale de |U|^2 et la renvoie
	"""

	Ucarre = U[:]*U[:]
	W = PointMilieu(x[:,2],Ucarre)
	return W


def PointMilieu(x,f):
	""" 
	Calcule l'integrale d'une fonction par la formule des point milieux

	Parametre d'entree:
	x[:] : les coordonnees
	f[:] : la fonction a integrer

	Renvoie S, la valeur de l'integrale
	"""
	Nx = f.shape[0]
	S=0.0
	for i in range(0,Nx-1):
		S=S+f[i]*(x[i+1]-x[i])      
	return S


