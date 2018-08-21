#Calcular el volumen de un cuboide, con validacion de instruciones
#Entradas:Alto, largo y ancho.
#Salidas:Volumen
def volumen_cuboide(Largo, Ancho, Alto):
    if Largo > 0 and Ancho > 0 and Alto > 0:
        Volumen = Largo*Ancho*Alto
        return Volumen
    else:
        return "Error en las entradas"
