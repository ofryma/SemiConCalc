# This script will show a graph of the threshold voltage according to the doping concentration
# for silicon and silicon oxide MOSFET transistor


import subprocess
import sys
import os

import matplotlib.pyplot

try:
    import math
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", 'math'])
finally:
    import math
try:
    import matplotlib.pyplot as plt
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", 'matplotlib'])
finally:
    import matplotlib.pyplot as plt

try:
    import numpy as np
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", 'numpy'])
finally:
    import numpy as np


k_bolts = 8.61733 * pow(10,-5)  # in [eV/K]
e = 1.60217*pow(10,-19)  # in [C]
epsilon_0 = 8.85 * pow(10,-14)  # in [F/cm]

class Material_OX:
    def __init__(self,name,e_r,t ,color, label):
        self.name = name
        self.e_r = e_r
        self.t = t
        self.plot_color = color
        self.label = label


    def calc_C_insolator(self):
        return (self.e_r * epsilon_0)/self.t

class Material_SC:
    def __init__(self,name,e_r,n_i):
        self.name = name
        self.e_r = e_r
        self.n_i = n_i


    def calc_fi_f(self, N_D , T = 300):
        # This method return the fi_f for a certain doping concentration
        # if not given, T = 300 kelvin

        return k_bolts * T * math.log(N_D/self.n_i)
    def calc_Q_dep(self,N_D , T =300):
        Q = 2 * self.e_r * e * N_D * 2 * self.calc_fi_f(N_D,T)
        return pow(Q,0.5)


    def show_V_t_to_temp_change(self, from_temp , to_temp , doping_concentratiion , oxide):
        T_vector = np.arange(from_temp,to_temp,to_temp/100)
        c = doping_concentratiion
        V_T = []
        for T in T_vector:
            fi_f = self.calc_fi_f(c , T)
            Q_d = self.calc_Q_dep(c , T)
            C_ins = oxide.calc_C_insolator()
            V_T.append(2 * fi_f - (Q_d / C_ins))

        # axis[1].semilogx(T_vector, V_T, color=oxide.plot_color, label=oxide.label)
        axis[1].plot(T_vector, V_T, color=oxide.plot_color, label=oxide.label)

        axis[1].set_title('V treshold vs. Temperature')
        axis[1].set_xlabel('')
        axis[1].set_ylabel('')
        axis[1].legend()
        axis[1].grid()


    def show_V_t_to_thickness_change(self, from_concentraion , to_concentration , oxide_list):



        N_D_vector = np.arange(from_concentraion,to_concentration,to_concentration/1000)

        for OX in oxide_list:
            V_T = []
            for c in N_D_vector:

                fi_f = self.calc_fi_f(c)
                Q_d = self.calc_Q_dep(c)
                C_ins = OX.calc_C_insolator()
                V_T.append(2 * fi_f - (Q_d / C_ins))

            axis[0].semilogx(N_D_vector,V_T,color = OX.plot_color, label=OX.label)


        axis[0].set_title('V treshold vs. N_D')
        axis[0].set_xlabel('')
        axis[0].set_ylabel('')
        axis[0].legend()
        axis[0].grid()



        return axis



def micrometer_to_centimeter(num):
    return num * pow(10 , -4)
def nanometer_to_centimeter(num):
    return num * pow(10, -7)

figure , axis = plt.subplots(2,1)

Si = Material_SC('Sillicon' , 11.8 , 1.5 * pow(10,-4))
OX_1 = Material_OX('SiO2' , 3.9 , micrometer_to_centimeter(0.01) , 'r' , '0.01 micrometer')
OX_2 = Material_OX('SiO2' , 3.9 , micrometer_to_centimeter(0.02) , 'b' , '0.02 micrometer')
OX_3 = Material_OX('SiO2' , 3.9 , micrometer_to_centimeter(0.05) , 'g' , '0.05 micrometer')
OX_4 = Material_OX('SiO2' , 3.9 , micrometer_to_centimeter(0.1) , 'y' , '0.1 micrometer')

SiO2_list = [OX_1 , OX_2 , OX_3 , OX_4]
Si.show_V_t_to_thickness_change(pow(10,14) , pow(10,18) , SiO2_list)


Si.show_V_t_to_temp_change(
    from_temp= 200 ,
    to_temp= 400,
    doping_concentratiion= pow(10,16),
    oxide= Material_OX('SiO2' , 3.9 , nanometer_to_centimeter(100) , 'b' , '100 nanometer')
)

plt.show()