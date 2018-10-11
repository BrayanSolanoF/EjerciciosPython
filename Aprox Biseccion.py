def raiz_bis(Num,Err):
    if isinstance (Num,int):
        return raiz_bis_aux(Num,Err,0,Num,0)
    else:
        return "Error"

def raiz_bis_aux(Num,Err,LimInf,LimSup,RaizAprox):
    RaizAprox = (LimInf + LimSup)/2
    if abs(Num-RaizAprox**2) <= Err:
        return RaizAprox
    if RaizAprox**2 > Num:
        return raiz_bis_aux(Num,Err,LimInf,RaizAprox,RaizAprox)
    else:
        return raiz_bis_aux(Num,Err,RaizAprox,LimSup,RaizAprox)
