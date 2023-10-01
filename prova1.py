import numpy as np
import matplotlib.pyplot as plt

# Define BetheBlock function with input parameters
# c = h\ = 1
# All values are expressed in MeV, g, cm^3
def betheblock(x,
               energy = 0,
               mass = 0,
               rho = None,
               q = 1,
               ZA = 0.5,
               I = 13*10**(-9)):
    
    #Fundamental Constant
    m_electron = 0.51099895000 # MeV/c^2
    const = 0.1535 # MeV*cm^2/g
    momentum = np.sqrt(energy**2 - mass**2)
    if energy != 0:
        beta = momentum/energy
    if mass != 0:
        gamma = energy/mass
    #x = beta*gamma
    
    if rho == None:
        bb01 = const*ZA*(q**2)*((1+x**2)/(x**2))*(np.log(((2*m_electron*x**2)/(I))**2)-2*((x**2)/(1+x**2)))
        return bb01 
    
    else:
        bb02 = const*ZA*rho*(q**2)*((1+x**2)/(x**2))*(np.log(((2*m_electron*x**2)/(I))**2)-2*((x**2)/(1+x**2)))
        return bb02
    
x = np.linspace(0.1,100000,10000000)
plt.plot(x, betheblock(x,I=322*10**(-9)), color='red')
plt.xscale("log")
plt.yscale("linear")
plt.grid(True)
plt.ylim((0,50))
plt.show()