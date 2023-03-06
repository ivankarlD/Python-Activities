# Get Input Value
num1 = int(input("Input value for num1: "))
num2 = int(input("Input value for num2: "))

# Get Product
product = 0
for i in range(num2):
    product += num1

# Get Quotient and Remainder
quotient = 0
remainder = 0
dividend = num1
divisor = num2
while dividend >= divisor:
    dividend -= divisor
    remainder = dividend
    quotient += 1

print(f"The Product of {num1} and {num2}: {product}")
print(f"The integer quotient of {num1} and {num2}: {quotient}")
print(f"The integer remainder of {num1} and {num2}: {remainder}")