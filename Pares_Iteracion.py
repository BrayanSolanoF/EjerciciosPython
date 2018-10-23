def contar_pares(Lista):
    Cont=0 #contador de pares
    for Item in Lista:
        if Item%2==0:
            Cont+=1#actualizacion del contador
        #Lista=Lista[1:] #*
    return Cont
#* siginifica que la clausula no es necesaria
