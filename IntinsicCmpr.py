import math

class material:

    def __init__(self,name,ni,Nc,Nv):
        self.name = name
        self.ni = ni
        self.Nc = Nc
        self.Nv = Nv
        # self.Eg = Eg





k_bolts = 8.61733 * pow(10,-5)
Si = material("Silicon",ni=1.5*pow(10,10),Nc=2.8*pow(10,19),Nv=1.04*pow(10,19))
# Ge = material("Germanium",Nc=1.04*pow(10,19),Nv=6.0*pow(10,18))


def calcEg(material,T):
    Eg = -k_bolts* T * math.log((pow(material.ni,2))/(material.Nc * material.Nv))
    print()
    print(f"Calculating Energy gap of {material.name} in {T} Kelvin: ")
    print(f"Eg(Si,T={T}) = -kTln((n^2)/NcNv)")
    print(f"Eg(Si,T={T}) = -{k_bolts}*{T}*{math.log((pow(material.ni,2))/(material.Nc * material.Nv))} = {Eg} [eV]")


    return Eg
def calcni(material,T):


    ni = math.sqrt(material.Nc * material.Nv) * math.exp((-calcEg(material,T))/(2* k_bolts*T))
    print()
    print(f"Calculating the intrinsic electron concentration of {material.name} in {T} Kelvin: ")
    print(f"ni^2(Si, T={T}) = NvNc exp(-Eg(T={T})/kT)")
    print(f"ni(Si, T={T}) = {ni} [1/cm^3]")
    return ni



calcni(Si,400)