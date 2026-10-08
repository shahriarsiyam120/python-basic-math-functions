def compound_interest(p,r,t):
    A=p*(1+r/100)**t
    ci=A-p
    return A,ci

p=int(input("enter pricipal:"))
r=int(input("enter rate:"))
t=int(input("enter time:"))

print(compound_interest(p,r,t))