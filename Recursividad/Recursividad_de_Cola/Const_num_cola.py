##Cola
##Apartir de digitos pares de un numero construir otro numero conservando el orden del peso
def nue_par(Num):
    if isinstance(Num, int):
        if Num == 0:
            return 0
        else:
            a = nue_par_aux(Num,-1,0)
            return a
    else:
        return "El numero debe ser entero"
def nue_par_aux(Num,Exp,NumPar):
    if Num == 0: #Condicion de terminacion
        return NumPar #Valor de retorno
    else:
        if (Num%10)%2==0:
            NumPar = NumPar + (Num%10*10**(Exp+1))
            return nue_par_aux(Num//10,Exp+1,NumPar)
        else:
            return nue_par_aux(Num//10, Exp, NumPar)
