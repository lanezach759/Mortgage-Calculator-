import time
import math

print ("Welcome to the mortgage calculator")
time.sleep(2)


home_price = input("What is the price of the home?\n")
print ("Just to check, you said " + home_price)
first_answer = input("Is that correct? yes/no\n")

# Home price loop
while first_answer == "no":
  home_price = input("What is the price of the home?\n")
  print ("Just to check, you said " + home_price)
  first_answer = input("Is that correct?\n")

# Down payment calculator using 5% of home price
down_payment = float(home_price) * 0.05
print ("Down payment: $" + str(down_payment))

loan = float(home_price) - float(down_payment)

# Average CA APR + monthly APR rate
apr = .0294
monthly_apr = float(apr) / 12
monthly_loan = float(loan) / 360

## Bottom half of equation
#i1 = float(monthly_apr) + 1.0
#print ("i1 = " + str(i1))

#i2 = float(i1) ** float(-360)
#print ("i2 = " + str(i2))

#i3 = float(1) - float(i2)
#print ("i3 = " + str(i3))

#i4 = float(monthly_apr) / float(i3)
#print ("i4 = " + str(i4))

# Test function
def mortgagecalc(monthly_apr, loan):
  i1 = float(monthly_apr) + 1.0
  i2 = float(i1) ** float(-360)
  i3 = float(1) - float(i2)
  i4 = float(monthly_apr) / float(i3)
  m = loan * i4
  return m


#m = loan * i4


print (mortgagecalc(monthly_apr, loan))



