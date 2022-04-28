# Ex 3

import subprocess
import sys
import os
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


# electron mass and effective electron and holes mass
me = 9.1093*pow(10,-31)
me_eff = 0.18 * me
mh_eff = 0.37 * me
k_bolts = 8.61733 * pow(10,-5)
h = 4.135667 * pow(10,-15)
e = 1.60217*pow(10,-19)
# holes mobility in room temperature
holes_mobility = 1100
# experiment results
T = [15,30,80,110,125,160,175,195]
Resistivity = [7180,3170,345,120,75,28.5,20,12.5]


def calcEg(T,Res):
    for i in range(0, len(T)):
        T[i] += 273.15

    iT = []
    lnR = []

    for i in range(0, len(Res)):
        iT.append(1 / T[i])
        lnR.append(math.log(Res[i]))

    z = np.polyfit(iT, lnR, 1)
    return z[0] * 2 * (k_bolts)
def calcElectronMobility(holes_mob_rt,Eg_rt,Nc_rt,Nv_rt,target_T):
    # This function calculates the mobility of the elctrons for a given temperature
    # All the values (Eg,Nv,Nc and holes_mob) need to be for the room temp. (300K)

    # claculate the elecrton mobility in room temp. (300K)
    e_mob_rt =  (math.exp(Eg_rt/(k_bolts*target_T))) / ((math.sqrt(Nc_rt*Nv_rt) * e))
    e_mob_rt -= holes_mob_rt


    return e_mob_rt*pow((target_T/300),-1.5)
def calcD(T,mobility):
    return (k_bolts*T*mobility)
def calcDOS(m_eff,T,DOS_name):
    DOS = 2 * math.pi * m_eff * k_bolts * e * T
    DOS = DOS / pow(h*e,2)
    DOS = pow(DOS,1.5)
    DOS = DOS * pow(100,-3)

    return DOS
while True:
    try:
        T_val = float(input("Enter temprature [K]: "))
        if T_val < 0:

            print("*** Unvalid temprature, enter again")
            continue
        else:
            break

    except:
        print("*** Unvalid temprature, enter again")
        continue


Eg = calcEg(T,Resistivity)
Nc = calcDOS(me_eff, T_val, 'Nc')
Nv = calcDOS(mh_eff, T_val, 'Nv')
e_mobility = calcElectronMobility(holes_mobility,Eg,calcDOS(me_eff,300,'Nc'),calcDOS(mh_eff,300,'Nv'),T_val)
e_D = calcD(T_val,e_mobility)

os.system('cls')

print()
print(f"Material Properties for a temprature of {T_val} Kelvin")
print(f"Eg = {Eg} [eV] ")
print(f"Nc = {Nc} [1/cm^3]")
print(f"Nv = {Nv} [1/cm^3] ")
print(f"Electron's mobility = {e_mobility} [cm^2 / V sec]: ")
print(f"Electron's diffusion coefficient = {e_D} [cm^2 / sec] ")
print()

python filename.py
