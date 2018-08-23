def x_p(X,P):
    if P==0:
        return 1
    else:
        P=P-1
        print("los valores:" X,P)
        return X*x_p(X,P)
