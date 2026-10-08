def cheack_BMI(weight,height):
    BMI=weight/(height*height)
    if BMI<18.5:
        return "underweight"
    elif BMI>=18.5 and BMI<24.9:
        return "normal weight"
    elif BMI>=25 and BMI<30:
        return "overweight"
    else:
        return "obesed" 
    
    
    
weight=float(input("enter weight"))
height=float(input("enter height"))
    
print(cheack_BMI(weight,height))