"""

Instituto Tecnológico de Costa Rica

Autores:
Anthony Acuña
Pablo González

Quiz#4

Version 1.0
Python 3.6



1)Contar los elementos impares de una lista

 #E:Una lista con elementos numericos
 #S:La suma de los elementos impares de la lista
 #R: Que sea una la lista no este vacia y los elementos sean enteros   





    

2)Obtener pares de una lista
#E:Una lista con elementos numericos
#S:Una lista nueva con los elementos pares de la lista anterior    
#R:Que sea una Lista no vacia y elementos enteros


3)Determinar si una lista contiene al menos  tres numeros pares    
    
#E:Una lista con elementos numericos
#S:un booleano determinando si es False o True
#R:Que sea una lista no vacia y elementos enteros   

    

""" 
############################*1*####################################

def contar(lista):
    if not isinstance(lista,list) or lista==[]:
        return None
    return contar_aux(lista)

def contar_aux(lista):
    if lista==[]:
        return 0
    if lista[0]%2==0:
        return 0 + contar_aux(lista[1:])
    else:
        return 1 + contar_aux(lista[1:])

############################*2*####################################


def pares(lista):
    if not isinstance(lista,list) or lista==[]:
        return None
    return pares_aux(lista,[])

def pares_aux(lista,lista2):
    if lista==[]:
        return lista2
    if lista[0]%2==0:
        return pares_aux(lista[1:],lista2+[lista[0]])
    else:
        return  pares_aux(lista[1:],lista2)

    
###########################*3*#####################################

def paresTres(lista):
    if not isinstance(lista,list) or lista==[]:
        return None
    return paresTres_aux(lista,0)

def paresTres_aux(lista,cont):
    if lista==[]:
        return False
    if cont==3:
        return True
    if lista[0]%2==0:
        return paresTres_aux(lista[1:],cont+1)
    else:
        return  paresTres_aux(lista[1:],cont)
