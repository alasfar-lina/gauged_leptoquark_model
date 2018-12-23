#! compile with python3
import flavio
from wilson import Wilson
import numpy as np
#======================================

# Wilson coeffecients Left-Handed chiral  Vector current (V-A structure )
# CVL_bctaunutau ( b -> c tau v_tau) ~ 10^-5
# CVL_bctaunumu (b->c tau v_mu) ~ 10^-4
# CV_bcmunutau (b->c mu v_tau) ~ 10^-7
#CV_bcmunumu (b -> c mu v_mu) ~10^-6
################################################
# w_c input at the EW scale, and standard basis 
w= Wilson({'CVL_bctaunutau':0.17,'CVL_bctaunumu':0.32,
	'CVL_bcmunutau':1e-3,'CVL_bcmunumu':1.7e-3}, scale=4.8,eft='WET',basis= 'flavio')
#the prediction for RD*
RD_star_np =flavio.np_prediction('Rtaul(B->D*lnu)',w)
RD_star_np_uncertainty =flavio.np_uncertainty('Rtaul(B->D*lnu)',w)
RD_star_sm =flavio.sm_prediction('Rtaul(B->D*lnu)')
RD_star_sm_uncertainty = flavio.sm_uncertainty('Rtaul(B->D*lnu)')
#LHCb result 
RD_star_obs = 0.366
RD_star_obs_sys = 0.030
RD_star_obs_stat = 0.027
##
values = [RD_star_np, RD_star_np_uncertainty, RD_star_sm,
RD_star_sm_uncertainty, RD_star_obs, np.sqrt(RD_star_obs_sys**2+RD_star_obs_stat**2) ]
## sigma deviation 
sigma_np_obs = (np.abs(values[0]-values[4]))/(np.sqrt(values[1]**2+values[5]**2))

print (values)
print (sigma_np_obs)
