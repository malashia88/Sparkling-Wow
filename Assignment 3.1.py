print("Welcome To Calculating The Cost of Installing Fiber Optic Cable")
company=input("Enter Company Name:")
feets=float(input("Enter the number of feet of cable needed to be installed:"))
if feets>=100:cost=feets*0.80
elif feets>=250:Cost=feets*0.70
elif feets>=250: cost=feets*0.50
else: cost=feets*0.87
print("Cost for the Company",company, "is", cost)