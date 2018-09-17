#1
#E:Una lista  S:Num promedio de calificaciones  R:La lista debe ser de elementos

def calificacion(lista):
    if isinstance (lista, list)and(len(lista)==10):
        return calificacion_aux(lista, elimMayor(lista,1), elimMenor(lista,1))
    else:
        return "Error"

def elimMayor(lista):
    if lista==[]:
        return []
    elif lista[0]>=lista[1]:
        return elimMayor(lista[1:])
#################################################################################
#2
#E:lista y num  S:lista  R:lista no puede estar vacía y el num debe ser entero

def elimine(lista, num):
    if isinstance(lista, list)and(lista!=[])and(num, int):
        return elimine_aux(lista, num, len(lista)-1, 0)
    else:
        return "Error"

def elimine_aux(lista, num, indic, veces):
    if lista==[]:#Caso Base
        return []
    elif lista[indic]==num:
        if veces>0:
            return elimine_aux(lista[:indic-1], num, indic-1, veces)+[]
            #return elimine_aux(lista[:len(lista)-1], num, indic-1, veces)+[] ##Estas son las correctas. Con esta si funciona
            
        else:
            return elimine_aux(lista[:indic-1-1], num,indic-1, 1)+[lista[indic]]
            #return elimine_aux(lista[:len(lista)-1], num,indic-1, 1)+[lista[indic]] ##Estas son las correctas. Con esta si funciona
        
    else:
        return elimine_aux(lista[:indic-1-1], num, indic-1, veces)+[lista[indic]]
        #return elimine_aux(lista[:len(lista)-1], num, indic-1, veces)+[lista[indic]] ##Estas son las correctas. Con esta si funciona

"""PRUEBA
>>>elimine([4,8,2,4,0,1],4)
elimine_aux([4,8,2,4,0],4,4,0)+[1]
elimine_aux([4,8,2,4],4,3,0)+[0]
elimine_aux([4,8,2],4,2,0)+[4]
elimine_aux([4,8],4,1,0)+[2]
elimine_aux([4],4,0,0)+[8]
elimine_aux([],4,-1,0)+[]
[8,2,4,0,1]"""
#################################################################################
#3
#E:2 números  S:lista  R:2 números enteros

def diferencia(num1, num2):
    if isinstance (num1, int)and(num2, int):
        num1=abs(num1)
        num2=abs(num2)
        return diferencia_aux(diferencia1(num1, num2),diferencia2(num1, num2))
    else:
        "Error"

def diferencia1(num1, num2):
    if num1==0:#Caso base
        return []
    elif num1%10!=num2%10:
        if num2!=0:
            return diferencia1(num1//10, num2//10)+[num1%10]
        else:
            return diferencia1(num1//10, num2//10)+[num1%10]
    else:
        return diferencia1(num1//10, num2//10)

def diferencia2(num1, num2):
    if num2==0:#Caso base
        return []
    elif num2%10!=num1%10:
        if num1!=0:
            return diferencia2(num1//10, num2//10)+[num2%10]
        else:
            return diferencia2(num1//10, num2//10)+[num2%10]
    else:
        return diferencia2(num1//10, num2//10)

def diferencia_aux(dif1,dif2):
    return dif1+dif2
"""diferencia(1234, 254)
diferencia_aux(diferencia1, diferencia2)
diferencia1(123, 25)+[]
diferencia1(12, 2)+[3]
diferencia1(1, 0)+[]
diferencia1(0, 0)+[1]
diferencia2(123, 25)+[]
diferencia2(12, 2)+[5]
diferencia2(1, 0)+[]
[1,3,5]"""

#################################################################################
#4
#E:Num  S:Num  R:Num que entra debe ser entero
def parejas(num):
    if isinstance(num, int):
        num=abs(num)
        return parejas_aux(num, 0)
    else:
        return "Error"

def parejas_aux(num, numTemp):
    numTemp=num%10
    if num==0:#Caso base
        return 0
    elif numTemp==(num//10)%10:
        return 1+parejas_aux(num//100, 0)
    else:
        return parejas_aux(num//10,0)

"""parejas(9991222)
1+parejas_aux(99912,0)
parejas_aux(9991,0)
parejas_aux(999,0)
1+parejas_aux(9,0)
parejas_aux(0,0)
2"""
