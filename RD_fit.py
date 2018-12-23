import flavio
import flavio.statistics.fits
from flavio.plots import likelihood_contour
from collections import OrderedDict
import matplotlib.pyplot as plt
################################
#initial fitting of the CVL_tau parametres, using fast fit..

#define the observables, here RD and RD*
observables = [
  'Rtaul(B->Dlnu)','Rtaul(B->D*lnu)'
]

# The function of the wilson coof.. in terms of g_LQ  @ M_b, and the mixing matrix elements
#physics constants:
G_F = 1.11e-5   #Fermi's constant @ M_b in GeV^-2
V_cb=0.04	# CKM matrix element
M2_LQ=1e-6	# LQ (V) mass squared in GeV^2 ~ i.e. LQ at TeV scale
################################
#define the CVL function in terms of the fitting parameters
# here u = U_btau U^*_c nu, this fit is a consistency check of the flavour structure 
# the product u should be of ~ 0.02 if it is the product of the CKM and PMNS
def wc_fct(g,u):
    return { 'CVL_bctaunutau':((2**0.5/4)*(g**2/G_F)*M2_LQ )*(1/V_cb)*u}

#fitting functions
def fastfit_obs(name, obslist):
    return flavio.statistics.fits.FastFit(
                name = name,
                observables = obslist,
                fit_wc_function = wc_fct,
                input_scale = 4.8,
            )
#=================================================================
fits = OrderedDict()
fits['RD']=['Rtaul(B->Dlnu)']
fits['RDs']=['Rtaul(B->D*lnu)']
#==================================================================
#preform the fitting per each observable
obs_fastfits={}
for k, v in fits.items():
    obs_fastfits[k] = fastfit_obs('CVL fit '+ k, v)
#global fitting
global_fastfit = fastfit_obs('CVL fit global', observables)

#Labels for the plot 
labels = {
'RD':flavio.Observable.get_instance(fits['RD'][0]).tex,
'RDs':flavio.Observable.get_instance(fits['RDs'][0]).tex
}
# make psedomeasurments, later load the real values... this is a good approximation
for k, v in fits.items():
    obs_fastfits[k].make_measurement(threads=4)
global_fastfit.make_measurement(threads=4)
#=============================== The plot ===================================================

fig=plt.figure(figsize=(4,4))
x_max=2
plt.xlim([0,2])
plt.ylim([0,2])

for i, f in enumerate(fits):
    	likelihood_contour(obs_fastfits[f].log_likelihood,
                                    0, x_max, 0, x_max, col=i+1, label=labels[f],
                                    interpolation_factor=3, threads=4)

likelihood_contour(global_fastfit.log_likelihood,
                                0, x_max, 0, x_max, n_sigma=(1, 2), col=0,
                                interpolation_factor=10, threads=4, label='global')

# labels, legend
plt.xlabel(r'$g_{LQ}$')
plt.ylabel(r'$\mathcal{U}_{b \tau}\mathcal{U}^*_{c \nu}$')
#plt.legend(loc=2, bbox_to_anchor=(1.05, 1)) # if you want it outside 
plt.legend()
plt.show()
