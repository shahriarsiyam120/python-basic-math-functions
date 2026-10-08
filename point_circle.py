def circle(x,y,h,k,r):
    d=(x-h)**2+(y-k)**2
    if d<r**2:
        return "inside"
    elif d>r**2:
        return "outside"
    else:
        d==r**2
        return "on"
    
x=float(input("enter x: "))
y=int(input('enter y: '))
h=int(input("enter h:"))
k=int(input("enter k:"))
r=int(input("enter r:"))

print(circle(x,y,h,k,r))