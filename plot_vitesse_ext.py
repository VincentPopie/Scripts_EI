# -*- coding: utf-8 -*- 
# Vincent Popie

# On se place à une hauteur h fixé
# Ici h = 10
# L'ideal serait de le passer en parametre du script


import numpy as np
import matplotlib.pyplot as plt

from lecture_fichier import lecture_exterieur
from trace_vitesse_ext import trace_U_ext, trace_U_ext_asympt

num_fichier = 100 #Correspond à h = 10

[KR, x, U, modU] =	lecture_exterieur(num_fichier,False)
[KR, x_Kelvin, U_Kelvin, modU_Kelvin] = lecture_exterieur(num_fichier,True)

nb_lignes = x.shape[0]

r = np.sqrt(x[:,0]*x[:,0] + x[:,1]*x[:,1])

save = True
show = False

trace_U_ext(r,modU,modU_Kelvin,save,show)
trace_U_ext_asympt(r,modU,modU_Kelvin,save,show)




