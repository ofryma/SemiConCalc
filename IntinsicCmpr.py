import math

class material:

    def __init__(self,name,symbol,ni,Nc,Nv):
        self.name = name
        self.symbol = symbol
        self.ni = ni
        self.Nc = Nc
        self.Nv = Nv
        # self.Eg = Eg

k_bolts = 8.61733 * pow(10,-5)
Si = material("Silicon",symbol="Si",ni=1.5*pow(10,10),Nc=2.8*pow(10,19),Nv=1.04*pow(10,19))
Ge = material("Germanium",symbol="Ge",ni=2.4*pow(10,13),Nc=1.04*pow(10,19),Nv=6.0*pow(10,18))


def calcEg(material,T,show_calc):



    new_Nc = calcDOS(material.Nc,T,DOS_name="Nc",show_calc=show_calc)
    new_Nv = calcDOS(material.Nv,T,DOS_name="Nv",show_calc=show_calc)
    Eg = -k_bolts * T * math.log((pow(material.ni, 2)) / (new_Nc * new_Nv))

    if(show_calc):
        print()
        print(f"Calculating Energy gap of {material.name} in {T} Kelvin: ")
        print(f"Eg({material.symbol},T={T}) = -kTln((n^2)/NcNv)")
        print(f"Eg({material.symbol},T={T}) = -{k_bolts}*{T}*{math.log((pow(material.ni,2))/(new_Nc * new_Nv))} = {Eg} [eV]")


    return Eg
def calcni(material,T,show_calc):


    ni = math.sqrt(material.Nc * material.Nv) * math.exp((-calcEg(material,T,show_calc=show_calc))/(2* k_bolts*T))
    if show_calc:
        print()
        print(f"Calculating the intrinsic electron concentration of {material.name} in {T} Kelvin: ")
        print(f"ni^2({material.symbol}, T={T}) = NvNc exp(-Eg(T={T})/kT)")
        print(f"ni({material.symbol}, T={T}) = {ni} [1/cm^3]")
    return ni
def calcDOS(DOS_in_rt , T , DOS_name,show_calc):
    new_DOS = DOS_in_rt * pow(T / 300, 3 / 2)
    if show_calc:
        print()
        print(f"Calculating the change in {DOS_name} from 300K to {T}K: ")
        print(f"{DOS_name}(T={T}K) = Nc(300K) * ({T}/300)^(3/2)")
        print(f"{DOS_name}(T={T}K) = {new_DOS} [1/cm^3]")
    return new_DOS


target_ni = calcni(Ge,300,show_calc=True)
delta = 0.000001
i=1
print()
print("Brute-force calculating temperature:")
while i < pow(10,4):
    cur_ni = calcni(Si, 0+i+1,False)
    if(cur_ni/pow(10,13) >= target_ni/pow(10,13) - delta and cur_ni/pow(10,13) <=target_ni/pow(10,13) + delta):
        print(f"Temperature needed: {i}K")
        break

    i += 0.000001
    if i >= pow(10, 4):
        print("Could'nd find temprature in the range of [0.000001 - 10000] K")




