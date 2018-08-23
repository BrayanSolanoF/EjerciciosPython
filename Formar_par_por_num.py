#con 2018
#Obtengo 208
#Formar un numero con los digitos pares de un numeros
#Si no tiene pares retornar FALSE
def num_par(num):
    if isinstance(num, int):
        return aux_num_par(num)
    else:
        return "Miss, Mrs or Mr. User: be care!! it Must be an integer Number"
def aux_num_par(num):
    if num ==0:
        return 0
    else:
        Dig = num%10
        if Dig % 2=1:
            return aux_num_par(num//10)
        else:
            return Dig + 10*aux_num_par(num//10)
#Solucion Dos
    
