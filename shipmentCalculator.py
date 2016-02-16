totalCharge = 0
country = ""
orderTotal = 0
province = ""
GST = .05
HAR = .13
PRO = .06

orderTotal = float(input ("What is your order total? "))
print (orderTotal)
country = input ("What country are you from? ").upper()
if country.upper() == "CANADA" :
    province = input ("Which province in Canada? ").upper()
    if country.upper() == "CANADA" and province.upper() == "ALBERTA" :
        totalCharge = orderTotal + orderTotal * GST
    elif country.upper() == "CANADA" and province.upper() == "ONTARIO" or province.upper() == "NEW BRUNSWICK" or province.upper() == "NOVA SCOTIA"  :
        totalCharge = orderTotal + orderTotal * HAR
    else:
        totalCharge = orderTotal * PRO + orderTotal * GST + orderTotal
else:
    totalCharge = orderTotal

print ("The total order plus taxex is: ") 
print (totalCharge)

print("Your total including taxes comes to $%.2f " % totalCharge)