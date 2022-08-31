from forex_python.converter import CurrencyRates

cr = CurrencyRates()

amount = int(input("Enter amount: "))
fcurr = input("Enter currency code (Before): ").upper()
lcurr = input("Enter currency code (After): ").upper()

print('---------------------------------------')
print("Amount before Coversion: " + str(amount))
output = round(cr.convert(fcurr, lcurr, amount), 3)
print("Amount after Conversion: " + str(output))
