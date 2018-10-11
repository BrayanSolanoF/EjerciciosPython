def cont_list(Lista):
    if isinstance (Lista,list):
        return cont_list_aux(Lista,0)
    else:
        return "error"

def cont_list_aux(Lista,Resultado):
    if Lista==[]:
        return Resultado
    else:
        if isinstance (Lista[0],list):
            return cont_list_aux(Lista[0],0)+ cont_list_aux(Lista[1:],Resultado)
        else:
            Resultado+=1
            return cont_list_aux(Lista[1:],Resultado)



#se puede utilizar con listas internas 
