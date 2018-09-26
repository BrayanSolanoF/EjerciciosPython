"""
La recursividad de cola siempre tieen una funcion auxiliar
en la que lleva un argumento que va a contener el resultado!!!

""" 



##cola
##Cantidad de digitos de un numero entero
def cardin(Num):
    if isinstance(Num,int): #Condicion de terminacion
        if Num!= 0:
            return  cardin2_aux(abs(Num), 0)
        else: return 1
def cardin2_aux(Num,Dig):
    if Num==0:
        return Dig
    else:
        return cardin2_aux(Num//10, 1 +Dig)
    





