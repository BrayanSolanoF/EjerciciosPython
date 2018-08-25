def notas(nota,alumno):
if isinstance (alumno,str) and isinstance(nota,int):
    return notas_aux(nota, alumno)
else:
    return"Imbecil debe ingresar un nombre y un numero, no sea imbecil!!!"
def notas_aux(nota, alumno):
    alumno="Indique el nombre del alumno: "
    if nota>= 70:
        return "Aprobado"
    else:
        return "Reprobado"
