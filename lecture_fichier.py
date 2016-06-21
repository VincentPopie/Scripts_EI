# -*- coding: utf-8 -*- 
# Vincent Popie

###############################################################
# Module de lecture des fichiers dpressions_exterieur_hauteur #
###############################################################

import numpy as np

def lecture_exterieur(num_fichier,cste):
	"""
	Fonction qui lit le fichier dpressions_exterieur_hauteur
	ou dpressions_exterieur_cst_hauteur
	
	Parametre d'entree :
	int num_fichier : le numero associé au fichier
	bool cste : fichier cst ou non
	
	Retourne :
	float KR : la conductivite de Rayleigh
	x(nb_points,3) : les coordonnees des points de mesures
	Uext(nb_points,3) : les vitesses exterieures
	modUext(nb_points) :  le module de la vitesse
	"""

	if cste:
		nom_fichier = ('../DATA/Hauteur/dpressions_exterieur_cst_hauteur%d.out' %(num_fichier))
	else:
		nom_fichier = ('../DATA/Hauteur/dpressions_exterieur_hauteur%d.out' %(num_fichier))

	id=open(nom_fichier,'r')

	print
	print('Lecture du fichier', nom_fichier)

	line = id.readline().split()
	nb_points=int(line[3])-1
	KR = line[5]

	x = np.empty((nb_points,3),dtype='f8')
	Uext = np.empty((nb_points,3),dtype='f8')
	modUext = np.empty((nb_points),dtype='f8')

	for j in range(0,nb_points):
		line = id.readline().split()
		x[j,:]=line[0:3]
		Uext[j,:]=line[3:6]
		modUext[j]=line[6]

	id.close()
	print('Conductivite = ', KR)
	return KR, x, Uext, modUext


def lecture_interieur(num_fichier):
	"""
	Fonction qui lit le fichier dpressions_interieur_hauteur
	
	Parametre d'entree :
	int num_fichier : le numero associé au fichier
	
	Retourne :
	float KR : la conductivite de Rayleigh
	x(nb_points,3) : les coordonnees des points de mesures
	Uint(nb_points) :  la vitesse interieure
	"""

	nom_fichier = ('../DATA/Hauteur/dpressions_interieur_hauteur%d.out' %(num_fichier))

	print
	print('Lecture du fichier', nom_fichier)

	id=open(nom_fichier,'r')
	line = id.readline().split()
	nb_points=int(line[1])-1
	KR = line[2]

	x = np.empty((nb_points,3),dtype='f8')
	Uint = np.empty((nb_points),dtype='f8')

	for j in range(0,nb_points):
		line = id.readline().split()
		x[j,:]=line[0:3]
		Uint[j]=line[3]
	
	id.close()
	print('Conductivite = ', KR)

	return KR, x, Uint


