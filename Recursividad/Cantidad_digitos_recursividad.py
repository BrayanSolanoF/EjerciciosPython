def lenn(NumEnt):
    if NumEnt == 0: #Condicion de terminacion
        return 0
    else:
        return 1 + lenn(NumEnt//10) #Llamada Recursiva
