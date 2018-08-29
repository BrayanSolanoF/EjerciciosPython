·#Determinar si un numero tieen ceros usando procesos de Recursividad de Pila
def tiene_ceros(num):
    if isinstance(num, int):
        return aux_tiene_ceros(Num)
        #if num==0:
    else:
        return "No es un entero"
def aux_tiene_ceros(num):
    if num ==0:
        return False
    else:
        if(num%10)==0:
            return True
        else:
            return aux_tiene_ceros(num//10)
#Agregar si ingreso un cero que solo me de como resultado tener un cero

            
