
import math
import matplotlib.pyplot as plt


# electron mass and effective electron and holes mass
me = 1.60217*pow(10,-19)
me_eff = 0.18 * me
mh_eff = 0.37 * me
k_bolts = 8.61733 * pow(10,-5)
h = 4.135667 * pow(10,-15)
e = 1.60217*pow(10,-19)
# holes mobility in room temperature
mobility = 1100

# experiment results
T = [15,30,80,110,125,160,175,195]
Resistivity = [7180,3170,345,120,75,28.5,20,12.5]
lnR = []
Tinvert = []

for i in range(0,len(Resistivity)):
    lnR.append(math.log(Resistivity[i]))
    Tinvert.append(1/(T[i]+273.15))

def calcMobilitychange(mobility_in_rt,T):

    return mobility_in_rt*(pow((T/300),-1.5))
def calcEg(T,Resistivity):
def calcD(T):

def calcDOS(m_eff,T,DOS_name):

    DOS = 2 * math.pi * m_eff * k_bolts * T
    DOS = DOS / pow(h,2)
    DOS = pow(DOS,3/2)
    DOS = DOS * 2

    return DOS

while True:
    try:
        T_val = float(input("Enter temprature [K]: "))
        if T_val < 0:

            print("*** Unvalid temprature, enter again")
            continue

    except:
        print("*** Unvalid temprature, enter again")
        continue





    print(f"Material Properties for a temprature of {T_val} Kelvin")
    print(f"Eg = {} [eV] ")
    print(f"Electron mobility = {} [ADDUNITS]: ")
    print(f"Difussion coafisient of electrons = {} [ADDUNITS] ")
    print()
    print("Density of states - ")
    print(f"Nc = {calcDOS(me_eff,T_val,'Nc')} [1/cm^3]")
    print(f"Nv = {calcDOS(mh_eff,T_val,'Nv')} [1/cm^3] ")