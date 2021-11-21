import pandas
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Polygon
'''

theta = np.linspace(0,1.5533,91)
#print("les anlges" , x)


R_earth = 6371000
Altitude = 850000
a = R_earth/(R_earth+Altitude)

gamma = np.arccos(a*np.cos(theta)) - theta
gamma_thetamin = np.arccos(a)
gamma_thetamax = 0
#print("gamma = ", gamma)
G = (1+a**2-2*a*np.cos(gamma))/(1-a*np.cos(gamma))

NUM = G*np.sin(gamma)
print((NUM))
DENO = (np.sqrt((np.cos(gamma_thetamax))**2-(np.cos(gamma))**2)*np.arccos(np.cos(gamma_thetamin)))
print((DENO))
P = NUM/DENO

plt.plot(theta,P,"m-")
plt.xlabel("elevation")
plt.ylabel("pdf of elevation")
plt.legend();
plt.title('')
plt.grid(True)
plt.show()
'''


    
def func(theta):
    gamma = np.arccos(a*np.cos(theta)) - theta
    gamma_thetamin = np.arccos(a)
    gamma_thetamax = 0
    #print("gamma = ", gamma)
    G = (1+a**2-2*a*np.cos(gamma))/(1-a*np.cos(gamma))

    NUM = G*np.sin(gamma)
    DENO = (np.sqrt((np.cos(gamma_thetamax))**2-(np.cos(gamma))**2)*np.arccos(np.cos(gamma_thetamin)))
    P = NUM/DENO
    return P



theta = np.linspace(0,1.5533,91)

#print("les anlges" , x)
R_earth = 6371000
Altitude = 850000
a = R_earth/(R_earth+Altitude)
y = func(theta)
gamma = np.arccos(a*np.cos(theta)) - theta
gamma_thetamin = np.arccos(a)
gamma_thetamax = 0
#print("gamma = ", gamma)
G = (1+a**2-2*a*np.cos(gamma))/(1-a*np.cos(gamma))

NUM = G*np.sin(gamma)
print((NUM))
DENO = (np.sqrt((np.cos(gamma_thetamax))**2-(np.cos(gamma))**2)*np.arccos(np.cos(gamma_thetamin)))
print((DENO))
P = NUM/DENO

print("les angles",np.linspace(5,85, 9))
angle = np.linspace(0,89, 10)/180*np.pi
print("les angles en rad",angle)
fig, ax = plt.subplots()
ax.plot(theta, P, 'm', linewidth=2)
ax.set_ylim(bottom=0)

# Make the shaded region
f,g = angle[0], angle[1]
ix = np.linspace(f, g)
iy = func(ix)
verts = [(f, 0), *zip(ix, iy), (g, 0)]
poly = Polygon(verts, facecolor='0.9', edgecolor='0.5')
ax.add_patch(poly)

# Make the shaded region
f,g = angle[1], angle[2]
ix = np.linspace(f, g)
iy = func(ix)
verts = [(f, 0), *zip(ix, iy), (g, 0)]
poly = Polygon(verts, facecolor='0.9', edgecolor='0.5')
ax.add_patch(poly)

# Make the shaded region
f,g = angle[2], angle[3]
ix = np.linspace(f, g)
iy = func(ix)
verts = [(f, 0), *zip(ix, iy), (g, 0)]
poly = Polygon(verts, facecolor='0.9', edgecolor='0.5')
ax.add_patch(poly)


# Make the shaded region
f,g = angle[3], angle[4]
ix = np.linspace(f, g)
iy = func(ix)
verts = [(f, 0), *zip(ix, iy), (g, 0)]
poly = Polygon(verts, facecolor='0.9', edgecolor='0.5')
ax.add_patch(poly)


# Make the shaded region
f,g = angle[4], angle[5]
ix = np.linspace(f, g)
iy = func(ix)
verts = [(f, 0), *zip(ix, iy), (g, 0)]
poly = Polygon(verts, facecolor='0.9', edgecolor='0.5')
ax.add_patch(poly)


# Make the shaded region
f,g = angle[5], angle[6]
ix = np.linspace(f, g)
iy = func(ix)
verts = [(f, 0), *zip(ix, iy), (g, 0)]
poly = Polygon(verts, facecolor='0.9', edgecolor='0.5')
ax.add_patch(poly)

# Make the shaded region
f,g = angle[6], angle[7]
ix = np.linspace(f, g)
iy = func(ix)
verts = [(f, 0), *zip(ix, iy), (g, 0)]
poly = Polygon(verts, facecolor='0.9', edgecolor='0.5')
ax.add_patch(poly)

# Make the shaded region
f,g = angle[7], angle[8]
ix = np.linspace(f, g)
iy = func(ix)
verts = [(f, 0), *zip(ix, iy), (g, 0)]
poly = Polygon(verts, facecolor='0.9', edgecolor='0.5')
ax.add_patch(poly)

# Make the shaded region
f,g = angle[8], angle[9]
ix = np.linspace(f, g)
iy = func(ix)
verts = [(f, 0), *zip(ix, iy), (g, 0)]
poly = Polygon(verts, facecolor='0.9', edgecolor='0.5')
ax.add_patch(poly)

plt.ylabel("pdf")
plt.xlabel("elevation angle (rad)")
plt.title('probability density function of elevation')
plt.grid(True)
plt.show()
plt.show()