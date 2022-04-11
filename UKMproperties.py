
# electron mass and effective electron and holes mass
me = 1.60217*pow(10,-19)
me_eff = 0.18 * me
mh_eff = 0.37 * me

# holes mobility in room temperature
mobility = 1100

# experiment results
T = [15,30,80,110,125,160,175,195]
Resistivity = [7180,3170,345,120,75,28.5,20,12.5]


while True:
    try:
        T_val = float(input("Enter temprature [K]: "))
        if T_val < 0:

            print("*** Unvalid temprature, enter again")
            continue

    except:
        print("*** Unvalid temprature, enter again")
        continue

    print(f"Material Properties for a temprature of {} Kelvin")
    print(f"Eg [eV]: {}")
    print(f"Electron mobility [ADDUNITS]: {}")
    print(f"Difussion coafisient [ADDUNITS]: {}")
    print()
    print("Density of states - ")
    print(f"Nc [1/cm^3]: {}")
    print(f"Nv [1/cm^3]")