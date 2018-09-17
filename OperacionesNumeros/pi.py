def sum(N):
    if N<=1:
        return 1
    else: return sum(N-1)+(1.0/(N**2))

def pi(N):
    return (6*sum(N))**0.5
print (pi(995))
