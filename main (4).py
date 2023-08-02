int_rate=float(input('Enter the annualized interest rate:'))
initial_investment=float(input('Enter the inital investment:'))
bal_amt=initial_investment
year=0
while bal_amt<2*initial_investment:
  bal_amt = bal_amt + (bal_amt*(int_rate/100))
  year+=1
print('The number of years it takes an investment to double is',year)