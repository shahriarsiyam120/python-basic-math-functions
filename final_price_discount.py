def discount(p,d):
    Discount_Amount=p*d/100
    Final_price=p-Discount_Amount
    return Discount_Amount,Final_price

p=int(input("orginal price: "))
d=int(input("discount:"))

print(discount(p,d))