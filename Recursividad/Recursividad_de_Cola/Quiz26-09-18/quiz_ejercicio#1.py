"""
# Instituto Tecnologico de Costa Rica


# Ingenieria en Computadores


#Programa: fun_muestra
#Lenguaje: Python 3.6.4
#Autor: Brayan Solano Fonseca
#Version: 1.0
#Fecha Ultima Modificacion: Septiembre 26/2018
#Entradas: lista de calificaciones
#Restricciones: Ingresar valores en forma de lista
#Salida: Obtengo tres valores diferentes
1-NuevaLista con sin los extremos
2-Lista original
3-Diferencia entre promedios de lista
"""
#Lista por evaluar ([5,8,7,4,3,2])
########################################################

"""
Siete jueces dan su evaluacion sobre el desempeño de unos atletas.
Su evaluacion es una puntuacion de 1 a 10. Para eliminar el posible
sesgo de los jueces, la organizacion aplica la eliminacion de los puntajes extremos
(superior e inferior) para calcular el promedio. Construya un programa que muestre
la puntuacion obtenida por cada atleta con la eliminacion, la puntuacion sin la
eliminacion y la diferencia.

"""
#Retorna la lista Nueva despues de realizar la eliminacion.

def muestra(lista):
    min = get_min(lista, 10)
    max = get_max(lista, 0)
    Nueva = elimina(lista, min, [], 0)
    Nueva = elimina(Nueva, max, [], 0)
    return Nueva


def promedio(lista):
    if isinstance(lista, list) and lista != []:
        return aux_promedio(lista, 0, 0)
    else:
        return "Error"


def aux_promedio(lista, suma, contador):
    if lista == []:
        return suma / contador
    else:
        return aux_promedio(lista[1:], suma + lista[0], contador + 1)


def elimina(lista, elemento, res, indice):
    if lista == []:
        return res
    elif lista[0] != elemento:
        res += [lista[0]]
        return elimina(lista[1:], elemento, res, indice)
    else:
        if indice == 0:
            return elimina(lista[1:], elemento, res, indice + 1)
        else:
            res += [lista[0]]
            return elimina(lista[1:], elemento, res, indice + 1)


def get_min(lista, min):
    if lista == []:
        return min
    elif lista[0] < min:
        min = lista[0]
        return get_min(lista[1:], min)
    else:
        return get_min(lista[1:], min)


def get_max(lista, max):
    if lista == []:
        return max
    elif lista[0] > max:
        max = lista[0]
        return get_max(lista[1:], max)
    else:
        return get_max(lista[1:], max)


print(muestra([5,8,7,4,3,2]))
##############################################################

#Retorna la lista original sin realizar la eliminacion.

def muestra(lista):
    min = get_min(lista, 10)
    max = get_max(lista, 0)
    Nueva = elimina(lista, min, [], 0)
    Nueva = elimina(Nueva, max, [], 0)
    return lista


def promedio(lista):
    if isinstance(lista, list) and lista != []:
        return aux_promedio(lista, 0, 0)
    else:
        return "Error"


def aux_promedio(lista, suma, contador):
    if lista == []:
        return suma / contador
    else:
        return aux_promedio(lista[1:], suma + lista[0], contador + 1)


def elimina(lista, elemento, res, indice):
    if lista == []:
        return res
    elif lista[0] != elemento:
        res += [lista[0]]
        return elimina(lista[1:], elemento, res, indice)
    else:
        if indice == 0:
            return elimina(lista[1:], elemento, res, indice + 1)
        else:
            res += [lista[0]]
            return elimina(lista[1:], elemento, res, indice + 1)


def get_min(lista, min):
    if lista == []:
        return min
    elif lista[0] < min:
        min = lista[0]
        return get_min(lista[1:], min)
    else:
        return get_min(lista[1:], min)


def get_max(lista, max):
    if lista == []:
        return max
    elif lista[0] > max:
        max = lista[0]
        return get_max(lista[1:], max)
    else:
        return get_max(lista[1:], max)


print(muestra([5,8,7,4,3,2]))



########################################################

#Retorna la diferencias entre los promedios de ambas listas.

def muestra(lista):
    min = get_min(lista, 10)
    max = get_max(lista, 0)
    Nueva = elimina(lista, min, [], 0)
    Nueva = elimina(Nueva, max, [], 0)
    a = promedio(lista)
    b = promedio(Nueva)
    c = int(a) - int(b)
    return c


def promedio(lista):
    if isinstance(lista, list) and lista != []:
        return aux_promedio(lista, 0, 0)
    else:
        return "Error"


def aux_promedio(lista, suma, contador):
    if lista == []:
        return suma / contador
    else:
        return aux_promedio(lista[1:], suma + lista[0], contador + 1)


def elimina(lista, elemento, res, indice):
    if lista == []:
        return res
    elif lista[0] != elemento:
        res += [lista[0]]
        return elimina(lista[1:], elemento, res, indice)
    else:
        if indice == 0:
            return elimina(lista[1:], elemento, res, indice + 1)
        else:
            res += [lista[0]]
            return elimina(lista[1:], elemento, res, indice + 1)


def get_min(lista, min):
    if lista == []:
        return min
    elif lista[0] < min:
        min = lista[0]
        return get_min(lista[1:], min)
    else:
        return get_min(lista[1:], min)


def get_max(lista, max):
    if lista == []:
        return max
    elif lista[0] > max:
        max = lista[0]
        return get_max(lista[1:], max)
    else:
        return get_max(lista[1:], max)


print(muestra([5,8,7,4,3,2]))

