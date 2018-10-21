#*****************************************************************************************
# Instituto Tecnologico de Costa Rica


# Ingenieria en Computadores


#Programa: funcaptura_frase
#Lenguaje: Python 3.6.4
#Autor: Brayan Solano Fonseca
#Version: 1.0
#Fecha Ultima Modificacion: Octubre 18/2018
#Entradas:Frase que incluye numeros, caracteres, signo de exclamacion y numeral
#Restricciones: Si es un caracter diferente a los ingresados en la entrada debe seer eliminado
#Salida: Nueva frase eliminando caracteres no admitidos.


#****************************************************************************************








def captura_frase(frase):
    lista1=[]
    i=0
    #input("Ingrese una afirmacion terminada en #, o una pregunta terminada en ?")
    lista0=list(frase)
    if lista0==[]:
        return "Error, debe ingresar una entrada valida"
    else: frase_aux(lista0, lista1, i)
def frase_aux(lista0, lista1, i):
     
     if (lista0[i]==""):
         lista0.split(i)
         print(lista1)
         return frase_aux(lista0, lista1, i+1)
     elif (lista0[i]==str) or (lista0[i]==int) or (lista0[i]=="?") or (lista0[i]=="#"):
         lista0[i].lower()
         lista1.append (lista0[i])
         frase_aux(lista0,lista1, i+1)
         print(lista1)
         
   
         
     
     
