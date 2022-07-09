

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


class Material:
    def __init__(self , k , V_g , type):
        self.k = k
        self.V_g = V_g
        self.type = type

    def I_vs_Vd(self , V_t , from_V , to_V , steps , graph_num):
        V_vector = np.arange(from_V,to_V,to_V/steps)
        Ids = []
        print(V_vector)
        for V in V_vector:
            # The sign of the current needs to get the sign of the Voltage - V_d
            # every other value get the abs value

            if abs(self.V_g - V_t) > abs(V):
                cur_I = self.k * (abs(self.V_g - V_t) * V)
            else:
                cur_I = self.k * pow((self.V_g - V_t) , 2) * (abs(V)/V)

            Ids.append(cur_I)

        axis[graph_num].plot(V_vector , Ids)
        axis[graph_num].grid()




figure , axis = plt.subplots(2,1)

V_t = float(input('Enter Vt value: '))
n_SC = Material(0.15 , 4 , 'n')
p_SC = Material(0.15 , -4 , 'p')
n_SC.I_vs_Vd(
    V_t = V_t,
    from_V=0,
    to_V=10,
    steps=2000,
    graph_num = 0
)
p_SC.I_vs_Vd(
    V_t = - V_t,
    from_V=0,
    to_V=-10,
    steps=2000,
    graph_num = 1
)


plt.show()








