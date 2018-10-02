"""def biseccion(Num):
    if isinstance(Num, int):
        return raiz_bis_aux(num,error,0,)"""





def raiz_bis_aux(Num,Err,LimInf,LimSup,RaizAprox):
    RaizAprox=(LimInf+LimSup)/2
    if abs(Num-RaizAprox**2)<=Err:
        return RaizAprox
    if RaizAprox**2>Num:
        return raiz_bis_aux(Num,Err,LimInf,RaizAprox,RaizAprox)
    else: return raiz_bis_aux(Num,Err,RaizAprox,LimSup,RaizAprox)


"""Prueba
raiz_bis_aux(2,0.0001,0,2,0)
1.4141857

"""
