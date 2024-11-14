#calculator with python
value1=int(input("Enter the first value:"))
value2=int(input("Enter the Second value:"))
operand=input("Enter The Operand..")
if operand == "+":
     print (value1+value2)
elif operand == "-":
     print(value1-value2)
elif operand == "*":
     print (value1*value2)
elif operand == "/":
     print (value1/value2)
else:
     print("invalid Operand entered....")

#Python program for simple interest.
principal=int(input("enter the principal value"))
rate=int(input("enter the rate value"))
time=int(input("enter the time value"))
simpleinterest=principal*rate*time
print("the simple interest is",simpleinterest)

#currency converter calculator
from forex_python.converter import CurrencyRates
cr = CurrencyRates()
amount=int(input("Enter amount: "))
currencyfrom=input ("Enter your currency")).upper()
currencysto=input("In which currency you want to change").upper()
result=cr.convert(currencyfrom,currencyto,amount)
print(result)