#!/usr/bin/env python
# coding: utf-8

# In[25]:


import scipy.integrate as integrate

def comovingd(z):

    H0=2.18e-18 #Hubble constant in s^-1
    c = 299792458*3.240778849899439e-26 #speed of light Gpc/s

    OmegaM=0.2726   #omega matter, parameter from cosmology
    OmegaL= 0.7274  #omega lambda, parameter from cosmology

    integrand = lambda x : 1/((1+x)**3 * OmegaM + OmegaL)**0.5

    results = integrate.quad(integrand, 0, z)
    inte = results[0]
    dist = c/H0 * inte

    return dist


#the main 

z=30.   #initial redshift
codist=[] #comoving distances list
lumdist = [] #luminous distances list
redsh=[] #redshift list
while(z>0.0):
    codist.append(comovingd(z)) #call looktime and append result
    redsh.append(z) #store z into list redsh
    lumdist.append(comovingd(z)*(1+z))
    z-=0.1
for i in range(len(codist)): #loop over the elements of look
    print("Redshift:    ", redsh[i],",", "Comoving distance:    ", codist[i], "Gpc,", "Luminous distance:    ", lumdist[i], "Gpc") #prints redshift and 
#corresponding look back time list




# In[28]:


import numpy as np
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size': 17}) #set default fontsize to 17

plt.plot(redsh, codist, 'r-')
plt.plot(redsh, lumdist, 'b-')
plt.axis([0, 30, 0, 140])
plt.xlabel('redshift z')
plt.ylabel('D$_c$, D$_L$ (Gpc)')
plt.tight_layout()
plt.show()


# In[ ]:




