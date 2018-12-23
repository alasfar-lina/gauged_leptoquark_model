# # #====================================================================================================================
import matplotlib.pyplot as plt
from rootpy.plotting.style import get_style, set_style
import numpy as np
import matplotlib as mpl
# # #====================================================================================================================

set_style('lhcb', mpl=True)
#-----------------------------------
G_F = 1.11e+1  #Fermi's constant @ M_b in TeV^-2
V_ts=39.4e-3
err_Vts =2.3e-3
V_tb=1.01190
err_Vtb=0.025
err_ts_tb = (V_ts*V_tb)*((err_Vtb/V_tb)**2+(err_Vts/V_ts)**2)**(.5)
m= 0.85
g=1
c10_SM= -4.3
alpha_EM = 1/137
m_Bs=5366.28e-6 #TeV
err_Bs= 0.22e-6
#t_Bs=1.505e-12 #sec
t_Bs= 2.25e+15 # TeV^-1
factor = 16*np.pi**3
m_tau=1776.86e-6
err_m_tau=0.12e-6
f_Bs= 0.198e-3
err_f_Bs= 0.0083017e-3
#-----------------------------------

#-----------------------------------
def C9(x):
#-----------------------------------
    return 2**(.5)/(4*G_F)*(g**2/m**2)*(x/(V_ts*V_tb))
#-----------------------------------
def err_C9(x):
#-----------------------------------
    return C9(x)*err_ts_tb/(V_ts*V_tb)
#-----------------------------------
def C10(x):
#-----------------------------------
    return- 2**(.5)/(4*G_F)*(g**2/m**2)*(x/(V_ts*V_tb))
#-----------------------------------
def err_C10(x):
#-----------------------------------
    return C9(x)*err_ts_tb/(V_ts*V_tb)
#-----------------------------------------------------------
def Bs_to_tt(x):
#-----------------------------------------------------------
    #return (((G_F**2)*t_Bs/factor)*alpha_EM**2*f_Bs**2*m_Bs*m_tau**2*(V_ts*V_tb)**2*(c10_SM+C10(x))**2*(1-(4*m_tau**2/m_Bs**2))**(.5))*10**(10)
    return 0.4510*((c10_SM+C10(x))**2)
#-----------------------------------------------------------
#-----------------------------------------------------------
def err_Bs_to_tt(x):
#-----------------------------------------------------------
    qcd_un= Bs_to_tt(x)*2*err_f_Bs/f_Bs
    return (qcd_un**2+err_C10(x)**2)**(.5)

#-----------------------------------------------------------
def B_to_Ktt(x):
#-----------------------------------------------------------
    return 1.20+0.15*C9(x)-0.42*C10(x)+0.02*C9(x)**2+0.05*C10(x)**2
#-----------------------------------------------------------
def err_B_to_Ktt(x):
#-----------------------------------------------------------
    un= 0.12+0.02*C9(x)-0.04*C10(x)+0.01*C9(x)**2+0.08*C10(x)**2
    return (un**2+err_C9(x)**2+err_C10(x)**2)**(.5)
#-----------------------------------------------------------
def B_to_Kstt(x):
#-----------------------------------------------------------
    return 0.98+0.38*C9(x)-0.14*C10(x)+0.05*C9(x)**2+0.02*C10(x)**2

#-----------------------------------------------------------
def err_B_to_Kstt(x):
#-----------------------------------------------------------
    un= 0.09+0.03*C9(x)-0.01*C10(x)
    return (un**2+err_C9(x)**2+err_C10(x)**2)**(.5)

#-----------------------------------------------------------
def B_to_phitt(x):
#-----------------------------------------------------------
    return 0.86+0.34*C9(x)-0.11*C10(x)+0.05*C9(x)**2+0.01*C10(x)**2

#-----------------------------------------------------------
def err_B_to_phitt(x):
#-----------------------------------------------------------
    un= 0.06+0.02*C9(x)
    return np.sqrt(un**2+err_C9(x)**2+err_C10(x)**2)

#===================================================================================
x=np.linspace(0,1, 200, endpoint=True)
f = plt.figure(figsize=(10, 10))
ax = plt.subplot(1,1,1)
mpl.rcParams['text.latex.preamble'] = [ r'\usepackage{amsmath}',  r'\usepackage{hepunits}',r'\usepackage{mathpazo}']
# #=========================================================================================================
Bstt, =plt.plot(x ,Bs_to_tt(x)  , "C1",lw=1,label=r'$\mathcal{B}(B_s \to \tau^+ \tau^-)$  {\Large total}' )
ax.fill_between(x,Bs_to_tt(x)- err_Bs_to_tt(x),Bs_to_tt(x)+ err_Bs_to_tt(x),facecolor="C1",alpha=0.2,label=r'NRQCD uncertainty')
# BKtt, =plt.plot(x ,B_to_Ktt(x)  , "C3",lw=1)
# ax.fill_between(x,B_to_Ktt(x)- err_B_to_Ktt(x),B_to_Ktt(x)+ err_B_to_Ktt(x),facecolor="C3",alpha=0.2,label=r'$\mathcal{B}(B \to K \tau^+ \tau^-)$  {\Large$ q^2 \in [ 15,22[\, \GeV^2 $} ')
# BKstt, =plt.plot(x ,B_to_Kstt(x)  , "C4",lw=1)
# ax.fill_between(x,B_to_Kstt(x)- err_B_to_Kstt(x),B_to_Kstt(x)+ err_B_to_Kstt(x),facecolor="C4",alpha=0.2,label=r'$\mathcal{B}(B \to K^* \tau^+ \tau^-)$  {\Large$ q^2 \in [ 15,19[\, \GeV^2 $}')
# BPhitt, =plt.plot(x ,B_to_phitt(x)  , "C2",lw=1)
# ax.fill_between(x,B_to_phitt(x)- err_B_to_phitt(x),B_to_phitt(x)+ err_B_to_phitt(x),facecolor="C2",alpha=0.2,label=r'$\mathcal{B}(B_s \to \phi \tau^+ \tau^-)$  {\Large $ q^2 \in [ 15,18.8[\, \GeV^2 $}')
ax.semilogx()
ax.yaxis.set_minor_locator(plt.MultipleLocator(0.25))
plt.xlabel(r'$\mathcal{U}_{b\tau} \mathcal{U}^*_{s\tau}$')
plt.ylabel(r'$\mathcal{BR} \times 10^{-7}$')
#plt.legend(loc=, bbox_to_anchor=(1.05, 1)) # if you want it outside
plt.legend(loc=2)
plt.show()
