####Recursividad por cola
def mayor(Lista):
    if Lista ==[]:
        return "Error"
    else:
        return mayor_aux(Lista[0], Lista[1:])
def mayor_aux(Result,Lista):
    if Lista==[]:
        return Result
    elif Lista [0] > Result:
        return mayor_aux(Lista[0], Lista[1:])
    else:
        return mayor_aux(Result, Lista[1:])




