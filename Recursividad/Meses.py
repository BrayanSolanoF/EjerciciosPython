def meses(Mes):
    if isinstance(Mes, str) and len(Mes)==3:
        listaMeses = ['Ene','Feb','Mar','Abr','May','Jun','Jul',"Ago",'Set','Oct','Nov','Dic']
        diasMeses = [31,28,31,30,31,30,31,31,30,31,30,31]
        return aux_Mes(Mes,listaMeses,diasMeses,0)
    else:
        return 'Error'
def aux_Mes(Mes, listaMeses, diasMeses, indice ):
    if listaMeses[indice] == Mes:
        return diasMeses[indice]
    elif listaMeses[indice] != Mes:
        return aux_Mes(Mes, listaMeses, diasMeses, indice + 1)
    else:
        return "No ha sido encontrado", False