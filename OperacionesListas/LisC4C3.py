def LisC4C3(Base4):
    if Base4 == 0:
        return [['10']]
    else: return LisC4C3_aux(Base4)
def LisC4C3(Base4):
    if Base4 == 0:
        return [ ]
    else: return LisC4C3(Base4//10)+[[C4(Base4%10), C3(Base4%10)]]
def C4(N):
    return Bin(4-N)
def C3(N):
    return Bin(int(4-N-0.25))
def Bin(Dec):
    if Dec == 0 or Dec ==1:
        return "0" + str(Dec)
    elif Dec==2:
        return "10"
    else:
        return "11"
