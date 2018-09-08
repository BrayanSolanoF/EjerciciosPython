def mes(iniciales,dia):
    meses31=['Ene','Mar','May','Jul','Ago',"Oct","Dic"]
    meses30=['Abr','Jun','Set','Nov']
    meses29=['Feb']
    if iniciales in meses31:
        print('31-dia')
    elif iniciales in meses30:
        print('30-dia')
    elif iniciales in meses29:
        print('29-dia')
    else: print('Mes incorrecto')



