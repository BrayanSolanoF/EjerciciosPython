#Elaborado por:Raquel Gutierrez Mora, versión 3.7.0
#Fecha de creación:06/09/2018
#Fechade última modificación: 06/09/2018

cedula=input(str("Indique su número de cédula: "))
if len(cedula)==9 and str.isdigit(cedula):
    if (cedula[0]=="1"):
        print ("San José")
    elif (cedula[0]=="2"):
        print ("Alajuela")
    elif (cedula[0]=="3"):
        print("Cartago")
    elif (cedula[0]=="4"):
        print("Heredia")
    elif (cedula[0]=="5"):
        print ("Guanacaste")
    elif (cedula[0]=="6"):
        print ("Puntarenas")
    elif (cedula[0]=="7"):
        print ("Limón")
    else:
        print ("El libro es:", cedula[1:5])
        print ("El consecutivo es:",cedula[5:])