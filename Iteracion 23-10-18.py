def largo(Lista):
    Cont=0
    while Lista!=[]:
        Cont +=1
        Lista=Lista[1:]
    return Cont

def contar_pares(Lista):
    Cont=0 #contador de pares
    for Item in Lista:
        if Item%2==0:
            Cont+=1#actualizacion del contador
        #Lista=Lista[1:] #*
    return Cont
#* siginifica que la clausula no es necesaria

def cant_string(string):
    Cont=0
    for Char in string:
        Cont+=1
    return Cont

#Comparacion entre Iterativo y recursivo

#Forma Iterativa:

def digitos(Num):
    if isinstance(Num,int):
        if Num==0:
            return 1
        Dgts=0
        Num=abs(Num)
        while Num!=0:
            Num//=10
            Dgts+=1
        return Dgts #Note la sangria fuera del bloque


#Forma recursiva
def digitos(Num):
    if isinstance(Num,int):
        if Num!=0:
            return digitos_aux(abs(Num),0)
        else:
            return 1
def digitos_aux(Num,Dgts):
    if Num==0:
        return Dgts
    else:
        return digitos_aux(Num//10,1+Dgts)



#Determinar si un numero tiene al menos un digito par

def encont_par(Num):
    if isinstance(Num,int):
        return"No! Get Serious! Numbrer must be an integer"
    if  Num==0:
        return True
    Num=abs(Num)
    while Num!=0:
        if Num%2==0:
            return True
        Num=Num//10
    return False
#hacer el anterior pero con For
def tiene_par_for(Num):
    if not isinstance(Num,int):
        return"Error"
    Num=str(Num)
    for i in Num:
        if int(i)%2==0:
            return True
    return False
#uso de bandera o centinela para controlar la condicion de un ciclo:
def cont_par(Num):
    if not isinstance(Num,int):
        return "Error, numero debe ser un enetero"
    if Num==0:
        return True
        HayPar=False #ESTA ES LA ABNDERA O CENTINELA
        Num=abs(Num)
    while Num!=0 and not HayPar:
        if Num%2==0:
            HayPar=True
        else:
            Num//=10
            return HayPar


    
