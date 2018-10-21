
#=========================2
def tres_cinco(N):
    """Tecnologico de Costa Rica
Ingeniería en computadores
Grupo 02
Milton Villegas Lemus

Jarod De la O
Pablo Gonzalez
Entradas: valor numerico
Salidas: Lista con 3 y 8s que lo componen
Restricciones: Debe ser mayor a 8"""
    if N<8:
        return "favor ingrese un valor mayor a 8"
    else:
        return tcaux(N,0,[])

def tcaux(N,x,res):
    if N==0:
        return res
    elif N%5==0 and N!=0:
        N-=5
        res+=[5]
        return tcaux(N,x,res)
    else:
        N-=3
        res+=[3]
        return tcaux(N,x,res)



    
    
      
    
    
