# This script calculates the Energy gap for a given material as a function of the
# temperature and plotting the graph for it.
# when running this script, a menu will appear with some predefined material and an option
# for creating a new material and adding it to the menu.
# For plotting a graph all you need to do is run the script, enter one of the values for the
# predefined materials and press enter. If you choose to add a new material, another menu will
# appear that will guide you throw what values you need to enter

import subprocess
import sys
try:
    import matplotlib.pyplot as plt
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", 'matplotlib'])
finally:
    import matplotlib.pyplot as plt



# creating a global temprature vector from 0 to 1000
T_range = []
Materials = []
for i in range(0,1001):
    T_range.append(i)


# creaing a class for every material given and its properties
class material:
    def __init__(self,name,Eg,alpha,beta):
        self.name = name
        self.Eg = Eg
        self.alpha = alpha
        self.beta = beta

    def EgCahge(self,T):
        EgT = []
        for i in range(0,len(T)):
            cur_val1 = (self.alpha*T[i]*T[i])
            cur_val2 = (T[i]+self.beta)
            cur_val = cur_val1/cur_val2
            cur_val = self.Eg - cur_val

            EgT.append(cur_val)

        plt.title(f"{self.name} Energy Gap as a function of Tamprature")
        plt.ylabel("Enrgy [eV]")
        plt.xlabel("Temprature [k]")
        plt.plot(T,EgT)
        plt.grid()
        plt.show()


        return EgT


# define Silicon and Gallium Arsenide properties and adding them to the list
Si = material("Silicon",Eg=1.17,alpha=0.000473,beta=636)
GaAs = material("Gallium Arsenide",Eg=1.519,alpha=0.0005405,beta=204)
Materials.append(Si)
Materials.append(GaAs)





print("This Program will calculate the energy gap for a given material")
while True:
    print("Choose From the options below:")
    print()

    for i in range(0,len(Materials)):
        print(f"    {i+1}. {Materials[i].name}")

    print(f"    {len(Materials) + 1}. Add new material")
    print(f"    {len(Materials)+2}. Exit program")
    print()
    try:
        c = input("Enter your choise: ")
        c = int(c) - 1
        if c == len(Materials):
            print("Enter new material properties")
            new_name = input("Material's name: ")
            temp_Eg = float(input("Zero celsius energy gap value [eV]: "))
            print(temp_Eg)
            temp_alpha = float(input("Alpha value [eV/K]: "))
            print(temp_alpha)
            temp_beta = float(input("Beta value [K]: "))
            print(temp_beta)
            new_one = material(name=new_name,Eg=temp_Eg,alpha=temp_alpha,beta=temp_beta)
            Materials.append(new_one)
            Materials[c].EgCahge(T_range)

        elif c == len(Materials) + 1:
            print("Goodbye...")
            break
        else:
            Materials[c].EgCahge(T_range)

    except:
        print("*** Input error! please try again")
        pass




