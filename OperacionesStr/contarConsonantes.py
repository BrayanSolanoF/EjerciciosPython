def contarConsonantes(pal):
    if isinstance(pal, str):
        return contarConsonantes_aux(pal)
    else: return "El valor ingresado no es una palabra"
def contarConsonantes_aux(pal):
    if pal== ' ' :
        return False
    elif (pal[0]=='a' or pal[0]=='e' or pal[0]=='i' or pal[0]=='o' or pal[0]=='u'):
        return contarConsonantes_aux(pal[1:])
    else: return 1 + contarConsonantes_aux(pal[1:])
