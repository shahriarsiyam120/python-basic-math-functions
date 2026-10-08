def cheack_interest(P,R,T):
    SI=P*R*T/100
    total=P+SI
    return total,SI

P=int(input("enter principal:"))
R=float(input("enter rate:"))
T=int(input("enter time:"))

print(cheack_interest(P,R,T))