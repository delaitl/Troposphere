import pandas
import matplotlib.pyplot as plt
import numpy as np
import math as math

#on a 17 points en abscisse que sont les pourcentages on cherche le EIRP ppour ces 17 points
#apres on veut precisement les points pour 0.01 % , 0.1% , 0.5% et 1%


''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'''''''''''''''''''''''''''''''''37.5 GHz'''''''''''''''''''''''''''''''''
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

'''''''''''''''''''''''''''''''''L_tropo'''''''''''''''''''''''''''''''''
#extracti des donnees
colnames = ['siteNum', 'satNum', 'fre[GHz]', 'elev', 'proba_elev','time_exceeded' ,'att_oxy']

data = pandas.read_csv(r"C:\Users\Louis\Documents\_UNIVERSITE\MASTER1\LELEC2910 - Antennas and propagation\Porpagation_project\Data\Austria_37.5_2\output\ascii\total_37.csv", names=colnames)
attenuation_austria_37 = data.att_oxy.tolist() # y
proba_austria_37 = data.time_exceeded.tolist()[0:17] #x

#creation de la matrice de poids
weights = np.array([0.29674482, 0.20118051, 0.13596646, 0.09612554, 0.07232226, 0.05796506,
 0.04929544, 0.04429272, 0.04191487])
#attenuation moyenne computing
L_tropo_37 = [0] * 17

for i in range(17):
  L_tropo_37[i] =   attenuation_austria_37[i::17]   @   weights
  
#print(np.shape(L_tropo_37))
#print(np.shape(proba_austria_37))
  
  
'''''''''''''''''''''''''''''''''Autres param'''''''''''''''''''''''''''''''''
SNR = np.asarray([10]*17) #dB
N_37 = np.asarray([-185.08]*17) #dBW
L_path_37 =  np.asarray([192.87]*17)  #dB
G_R_37 = np.asarray([49.12]*17) #[dBi]

EIRP_37 = SNR + N_37 + L_tropo_37 +L_path_37 - G_R_37




''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'''''''''''''''''''''''''''''''''75 GHz'''''''''''''''''''''''''''''''''
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

'''''''''''''''''''''''''''''''''L_tropo'''''''''''''''''''''''''''''''''
#extracti des donnees
colnames = ['siteNum', 'satNum', 'fre[GHz]', 'elev', 'proba_elev','time_exceeded' ,'att_oxy']

data = pandas.read_csv(r"C:\Users\Louis\Documents\_UNIVERSITE\MASTER1\LELEC2910 - Antennas and propagation\Porpagation_project\Data\Austria_75_2\output\ascii\total_75.csv", names=colnames)
proba_austria_75 = data.proba_elev.tolist()
attenuation_austria_75 = data.att_oxy.tolist()
elev_austria_75 = data.elev.tolist()
proba_austria_75 = data.time_exceeded.tolist()[0:17]


#attenuation moyenne computing
L_tropo_75 = [0] * 17

print(np.shape(attenuation_austria_37))
print(np.shape(attenuation_austria_75))

for i in range(17):
  A = attenuation_austria_75[i::17]
  L_tropo_75[i] =     A @   weights
  
#print(np.shape(L_tropo_37))
#print(np.shape(proba_austria_37))
  
  
'''''''''''''''''''''''''''''''''Autres param'''''''''''''''''''''''''''''''''

L_path_75 =  np.asarray([192.87]*17)  #dB
G_R_75 = np.asarray([51]*17) #dBi
N_75 = np.asarray([-184.62]*17) #dBW

EIRP_75 = SNR + N_75 + L_tropo_75 +L_path_75 - G_R_75


''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'''''''''''''''''''''''''''''''''Plot'''''''''''''''''''''''''''''''''
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


x =(proba_austria_37)
plt.xscale("log")
y1= EIRP_37
y2= EIRP_75
plt.plot(x,y1,"r-",label='37.5 GHz')
plt.plot(x,y2,"r--",label='75 GHz')
plt.xlabel("percentage[%]")
plt.ylabel("EIRP [dBW]")
plt.legend();
plt.title('EIRP - Graz (Austria)')
plt.grid(True)
plt.show()