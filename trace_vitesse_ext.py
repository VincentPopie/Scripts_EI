# -*- coding: utf-8 -*- 
# Vincent Popie

#############################################
# Module pour tracer les corrections de col #
#############################################
import numpy as np
import matplotlib.pyplot as plt
from math import pow

# Définition des paramètres généraux pour matplotlib
params = {'legend.fontsize': 25,
		  'lines.linewidth': 2,
		  'axes.linewidth' : 2,
		  'axes.formatter.limits' : [-3, 5],  # use scientific notation if log10
                                              # of the axis range is smaller than the
                                              # first or larger than the second
          
          'axes.formatter.use_locale' : False, # When True, format tick labels
									           # according to the user's locale.
											   # For example, use ',' as a decimal
                                               # separator in the fr_FR locale.
		   
		  'axes.formatter.use_mathtext': True, # When True, use mathtext for scientific
		                                       # notation.

		  'axes.formatter.useoffset' : False,   # If True, the tick label formatter
	                                            # will default to labeling ticks relative
												# to an offset when the data range is very
						                        # small compared to the minim
																				 
		  'xtick.major.width' : 2.0,
          'xtick.minor.width' : 2.0,  
		  'xtick.major.size'  : 6,      # major tick size in points
		  'xtick.minor.size'  : 4,      # minor tick size in points
		  'ytick.major.width' : 2.0,
		  'ytick.minor.width' : 2.0,  
		  'ytick.major.size'  : 6,      # major tick size in points
		  'ytick.minor.size'  : 6,      # minor tick size in points
		  'xtick.major.pad'   : 15,     # distance to major tick label in points
		  'xtick.minor.pad'   : 15,     # distance to the minor tick label in points
		  'ytick.major.pad'   : 10,     # distance to major tick label in points
          'ytick.minor.pad'   : 10,      # distance to the minor tick label in points
          'xtick.labelsize'   : 20,       
          'ytick.labelsize'   : 20       
	      }
plt.rcParams.update(params)


def trace_U_ext(r,modU,modU_Kelvin,save,show):

	ind_debut = 15
	r = r[ind_debut:]
	modU = modU[ind_debut:]
	modU_Kelvin = modU_Kelvin[ind_debut:]


	#Plot vitesse exterieure

	fig = plt.figure(1,figsize=(12,9))
	ax=fig.add_subplot(111)

	for item in ax.get_xticklabels():
		item.set_fontsize(25)
	for item in ax.get_yticklabels():
		item.set_fontsize(25)

	
	ax.plot(r,modU,'r-',label=r'$v_{\mathrm{t}}$',lw=4)
	ax.plot(r,modU_Kelvin,'b--',label=r'$v_{\mathrm{t}}^{\mathrm{K}}$',lw=4)

	ax.set_xlabel(r'$r$',fontsize=50)
	ax.set_ylabel(r'$v_{\mathrm{t}}$',fontsize=50)

	ax.set_xlim([0.9, 5])
	ax.set_ylim([0.0,0.2])

	ax.set_xticks([1,2,3,4,5])
	

	ax.legend()
	if save:
		#plt.savefig('Figure/vitesse_ext_zoom.png', format='png')
		plt.savefig('../Figure/vitesse_ext_zoom.pdf', format='pdf')
	if show:
		plt.show()

	###################################################################################

	#Plot vitesse exterieure zoom

	fig = plt.figure(2,figsize=(12,9))
	ax = fig.add_subplot(111)

	ax.plot(r,modU,'r-',label=r'$v_{\mathrm{t}}$',lw=4)
	ax.plot(r,modU_Kelvin,'b--',label=r'$v_{\mathrm{t}}^{\mathrm{K}}$',lw=4)

	ax.set_xlabel(r'$r$', fontsize=50)
	ax.set_ylabel(r'$v_{\mathrm{t}}$', fontsize=50)
	ax.set_xlim([0.9,1.5])
	ax.set_ylim([0.02,0.17])
	ax.legend()

	if save:
		#plt.savefig('Vitesse_ext_zoom_2.png', format='png')
		plt.savefig('../Figure/Vitesse_ext_zoom_2.pdf', format='pdf')
	if show:
		plt.show()

	plt.close('all')


def trace_U_ext_asympt(r,modU,modU_Kelvin,save,show):

	ind_debut = 15
	r_perfo = 1.0
	r_asympt = r[ind_debut:] - r_perfo
	modU_plot = modU[ind_debut:]


	nb_lignes = r_asympt.shape[0]

    #Pour que les asymptotes soient bien positionnees
	Asymptote_zero =  - 1.0/3.0*np.log10(r_asympt) - 1.2
	for i in range(0,nb_lignes):
		Asymptote_zero[i] = pow(r_asympt[i],-1.0/3.0) * pow(10,-1.3)

	b = np.log10(modU_plot[-2]) + 2.0*np.log10(r_asympt[-2]) + 0.2
	Asymptote_infty = b - 2.0*np.log10(r_asympt)

	for i in range(0,nb_lignes):
		Asymptote_infty[i] = pow(r_asympt[i],-2.0) * pow(10,b)


	# Trace la vitesse en log et les courbes asymptotiques
	fig = plt.figure(4,figsize=(12,9))
	ax = fig.add_subplot(111)


	ax.loglog(r_asympt,modU_plot,'r-',label=r'$\partial_{\mathrm{t}} u$')
	ax.loglog(r_asympt, Asymptote_infty,'g-',label=r'$\rho^{-2}$')
	ax.loglog(r_asympt, Asymptote_zero,'k-',label=r'$\rho^{-1/3}$')

	ax.set_xlabel(r'$\rho$',fontsize=30)
	ax.set_ylabel(r'$\partial_{\mathrm{t}} u$', fontsize=30)
	ax.legend()
	ax.set_ylim([-4.8,2.0])

	if show:
		plt.show()
	if save:
		plt.savefig('../Figure/asymptote.pdf', format='pdf')




