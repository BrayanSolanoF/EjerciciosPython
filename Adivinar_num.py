import random
def mago(AdivineNum1to6):
    Temp = int(random.uniform(1,7))
    if AdivineNum1to6 == Temp:
        return("Felicitaciones adivino el numero:" ,Temp)
    else:
        return("No adivino, No  compre loteria Ud. dijo", AdivineNum1to6, "y salio:", Temp)
