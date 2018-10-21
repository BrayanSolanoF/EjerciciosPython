def cosvalidacion(x,n):
    if n>=3 and n<=20:
        return cosen(x,n)
    else:
        print("Error")

def cosen(x,n):
    if n==-1:
        return 0
    else:
        return (((((-1)**(n))*(x**(2*n)))/(facto(2*n))))+cosen(x,n-1)

def facto(X):
    if X == 0:
        return 1
    else:
        return X*facto(X-1)

def Compton(grados):
    k=0.0243
    try:
        return k*(1-cosvalidacion(gradosarad(grados),20))
    except:
        pass 
    


def gradosarad(x):
    rad=x*3.14159265/180
    return rad
