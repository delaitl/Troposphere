import pandas
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Polygon
from scipy.integrate import quad


    
def func(theta):
    R_earth = 6371000
    Altitude = 850000
    a = R_earth/(R_earth+Altitude)
    gamma = np.arccos(a*np.cos(theta)) - theta
    gamma_thetamin = np.arccos(a)
    gamma_thetamax = 0
    #print("gamma = ", gamma)
    G = (1+a**2-2*a*np.cos(gamma))/(1-a*np.cos(gamma))

    NUM = G*np.sin(gamma)
    DENO = (np.sqrt((np.cos(gamma_thetamax))**2-(np.cos(gamma))**2)*np.arccos(np.cos(gamma_thetamin)))
    P = NUM/DENO
    return P

angle = np.linspace(0,89, 10)/180*np.pi
print(angle)
weights= np.zeros(9)

for i in range(9):
    weights[i] = quad(func, angle[i], angle[i+1])[0]
print(weights)
print(sum(weights))