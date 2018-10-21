def cont_list_aux(Lista,Resultado):
    if Lista==[]:
        return Resultado
    else:
        if isinstance(Lista[0], list):
            return cont_list_aux(Lista[0],0)+ cont_list_aux(Lista[1:], Resultado)
           #Note que se tuvo que ajustar la variable Resultado a cero para asi
           # usar la misma funcion recursiva
        else:
            Resultado+=1
            return cont_list_aux(Lista[1:], Resultado)
