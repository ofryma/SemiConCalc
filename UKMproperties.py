import subprocess
import sys
try:
    import math
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", 'math'])
finally:
    import math


# electron mass and effective electron and holes mass
me = 1.60217*pow(10,-19)
me_eff = 0.18 * me
mh_eff = 0.37 * me
k_bolts = 8.61733 * pow(10,-5)
h = 4.135667 * pow(10,-15)
e = 1.60217*pow(10,-19)
# holes mobility in room temperature
mobility = 1100


def calcMobility(mobility_in_rt,T,Eg):

    convert_mobility = mobility_in_rt*(pow((T/300),-1.5))
    NcNv = calcDOS(me_eff, T_val, 'Nc') * calcDOS(mh_eff, T_val, 'Nv')
    NcNv = math.sqrt(NcNv)

    n_mobility = 1/(e*NcNv*math.exp(-Eg/(2*k_bolts*T)))
    n_mobility -= convert_mobility

    return n_mobility
def calcEg(T,Resistivity):
    Eg = 0
    lnR = []
    Tinvert = []

    for i in range(0, len(Resistivity)):
        lnR.append(math.log(Resistivity[i]))
        Tinvert.append(1 / (T[i] + 273.15))

    for i in range(0, len(lnR)):
        try:
            Eg += (-2 * k_bolts * (lnR[i + 1] - lnR[i]) / (Tinvert[i + 1] - Tinvert[i]))
        except:
            pass

    return -Eg / len(lnR)
def calcD(T,mobility):
    return (k_bolts*T*mobility)/e
def calcDOS(m_eff,T,DOS_name):

    DOS = 2 * math.pi * m_eff * k_bolts * T
    DOS = DOS / pow(h,2)
    DOS = pow(DOS,3/2)
    DOS = DOS * 2

    return DOS


# experiment results
T = [15,30,80,110,125,160,175,195]
Resistivity = [7180,3170,345,120,75,28.5,20,12.5]
Eg = calcEg(T,Resistivity)

while True:
    try:
        T_val = float(input("Enter temprature [K]: "))
        if T_val < 0:

            print("*** Unvalid temprature, enter again")
            continue

    except:
        print("*** Unvalid temprature, enter again")
        continue


    Nc = calcDOS(me_eff, T_val, 'Nc')
    Nv = calcDOS(mh_eff, T_val, 'Nv')
    mobility = calcMobility(1100,T_val,Eg)
    D = calcD(T_val,mobility)


    print()
    print(f"Material Properties for a temprature of {T_val} Kelvin")
    print(f"Eg = {Eg} [eV] ")
    print(f"Nc = {Nc} [1/cm^3]")
    print(f"Nv = {Nv} [1/cm^3] ")
    print(f"Electron mobility = {mobility} [cm^2 / V sec]: ")
    print(f"Difussion coafisient of electrons = {D} [cm^2 / sec] ")
    print()
