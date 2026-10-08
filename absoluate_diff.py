def cheack(num1,num2):
     num3=num1-num2
     if num3<0:
         return num3*(-1)
     else:
         return num3
     
num1=int(input("enter a number"))     
num2=int(input("enter a number"))

print("absolute diff ",cheack(num1,num2))