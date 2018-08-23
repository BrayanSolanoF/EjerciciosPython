def lenn(NumEnt):
    if isinstance(NumEnt, int):
        if NumEnt != 0:
            return nuev_lenn(abs(NumEnt))
        else:
            return:"No es un entero"

def lenn(NumEnt):
    try:
         NumEnt = int(NumEnt)
         except:
             return "Este no es mi tipo"
