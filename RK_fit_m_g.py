import flavio
import flavio.statistics.fits
from flavio.plots import likelihood_contour
from collections import OrderedDict
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
import matplotlib as mpl
################################
#initial fitting of the CVL_tau parametres, using fast fit..



meas = []
for mname, mobj in flavio.Measurement.instances.items():
    if mobj.experiment == 'LHCb':
        for obs in mobj.all_parameters:
            if isinstance(obs, tuple) and '<Rmue>' in obs[0]:
                meas.append(mname)

#define the observables, here RD and RD*
observables = [
 ('<Rmue>(B+->Kll)',1.0, 6.0),
  ('<Rmue>(B0->K*ll)', 1.1, 6.0),
  ('<Rmue>(B0->K*ll)', 0.045, 1.1),
 ('<P5p>(B0->K*mumu)',1.1,2.5)
]

# The function of the wilson coof.. in terms of g_LQ  @ M_b, and the mixing matrix elements
#physics constants:
G_F = 1.11e+1  #Fermi's constant @ M_b in TeV^-2
V_cb=0.04	# CKM matrix element
	# LQ (V) mass squared in GeV^2 ~ i.e. LQ at TeV scale
################################
#define the CVL function in terms of the fitting parameters
# here u = U_btau U^*_c nu, this fit is a consistency check of the flavour structure 
# the product u should be of ~ 0.02 if it is the product of the CKM and PMNS
def wc_fct(g,m):
    return { 'C9_bsmumu':((2**0.5/4)*(g**2/G_F)*m**2 )*(0.005/(0.04*0.99)),'C10_bsmumu':((-2**0.5/4)*(g**2/G_F)*m**2 )*(0.005/(0.04*0.99))}
#fitting functions
def fastfit_obs(name, obslist):
    return flavio.statistics.fits.FastFit(
                name = name,
                observables = observables,
                fit_wc_function = wc_fct,
                input_scale = 4.8,
		#include_measurements=meas
            )
#=================================================================
fits = OrderedDict()
fits['RK']=['<Rmue>(B+->Kll)']
fits['RKs']=['<Rmue>(B0->K*ll)']
fits['P5p']=['<P5p>(B0->K*mumu)']
#==================================================================
#preform the fitting per each observable
obs_fastfits={}
for k, v in fits.items():
    obs_fastfits[k] = fastfit_obs('C9_10 fit '+ k, v)
#global fitting
global_fastfit = fastfit_obs('C9_110 fit global', observables)

#Labels for the plot 
labels = {
'RK':flavio.Observable.get_instance(fits['RK'][0]).tex,
'RKs':flavio.Observable.get_instance(fits['RKs'][0]).tex,
'P5p':flavio.Observable.get_instance(fits['P5p'][0]).tex
}
# make psedomeasurments, later load the real values... this is a good approximation
for k, v in fits.items():
    obs_fastfits[k].make_measurement(threads=4)
global_fastfit.make_measurement(threads=4)
#=============================== The plot ===================================================
fig=plt.figure(figsize=(4,4))
ax=plt.subplot(1,1,1)
x_max=0.75
plt.xlim([0.1,1])
plt.ylim([0.5,10])
mpl.rcParams['text.latex.preamble'] = [ r'\usepackage{amsmath}',  r'\usepackage{hepunits}',r'\usepackage{mathpazo}']





for i, f in enumerate(fits):
    	likelihood_contour(obs_fastfits[f].log_likelihood,
                                    0.1, 1, 0.5, 10, col=i+1, label=labels[f],
                                    interpolation_factor=3, threads=4)

likelihood_contour(global_fastfit.log_likelihood,
                                0.1, 1, 0.5, 10, n_sigma=(1), col=0,
                                interpolation_factor=10, threads=4, label='global')

# labels, legend
ax.xaxis.set_major_locator(MultipleLocator(0.1))
ax.xaxis.set_minor_locator(MultipleLocator(0.025))
ax.yaxis.set_major_locator(MultipleLocator(1))
ax.yaxis.set_minor_locator(MultipleLocator(0.25))
plt.xlabel(r'$g_{LQ}$')
plt.ylabel(r'$M_{V}$ / \TeV ')
#plt.legend(loc=2, bbox_to_anchor=(1.05, 1)) # if you want it outside 
plt.legend(loc=1,fontsize=16)
plt.show()
