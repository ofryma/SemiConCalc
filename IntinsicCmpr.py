import math

class material:
    def __init__(self,name,Eg,alpha,beta,Nc,Nv):
        self.name = name
        self.Eg = Eg
        self.alpha = alpha
        self.beta = beta
        self.Nv = Nv
        self.Nc = Nc

    def ni(self,T):
        # print(math.exp((-self.EgCahge(T)) / (2 * k_bolts * T)))
        # print(math.sqrt(self.Nc * self.Nv))
        return math.sqrt(self.Nc * self.Nv) * math.exp((-self.EgCahge(T)) / (2 * k_bolts * T))


    def EgCahge(self,T):
        try:
            cur_val1 = (self.alpha * T * T)
            cur_val2 = (T + self.beta)
            cur_val = cur_val1 / cur_val2
            Eg = self.Eg - cur_val
        except:
            Eg = self.Eg

        return Eg

k_bolts = 8.61733 * pow(10,-5)
Si = material("Silicon",Eg=1.17,alpha=0.000473,beta=636,Nc=2.8*pow(10,19),Nv=1.04*pow(10,19))
Ge = material("Germanium",Eg=0.67,alpha=None,beta=None,Nc=1.04*pow(10,19),Nv=6.0*pow(10,18))


target_ni = Ge.ni(300)
for i in range(0,10000):
    if Si.ni(i+1) >= target_ni:
        print(f"Temperature is: {i+1}K")
        break
