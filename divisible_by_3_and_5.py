def cheack(number):
    if number %3==0 and number %5==0:
        return True
    else:
        return False
    
    
number= int(input("enter a number"))    
print(cheack(number))