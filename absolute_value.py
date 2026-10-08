def cheack(number):
    if number<0:
        return number *(-1)
    else:
        return number
    
number=int(input("enter a number"))

print("number is ",cheack(number))
