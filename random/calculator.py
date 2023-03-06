print("Welcome...")

firstNum=int(input("Enter the first number: "))
secondNum=int(input("Enter the second number: "))
operator=input("Enter the operator ( + | - | * | / | % ): ")

match operator:
    case "+":
         print(f"{firstNum} {operator} {secondNum} is equal to {firstNum + secondNum}");  
    case "-":
         print(f"{firstNum} {operator} {secondNum} is equal to {firstNum - secondNum}");  
    case "*":
         print(f"{firstNum} {operator} {secondNum} is equal to {firstNum * secondNum}");  
    case "/":
         print(f"{firstNum} {operator} {secondNum} is equal to {firstNum / secondNum}");  
    case "%":
         print(f"{firstNum} {operator} {secondNum} is equal to {firstNum % secondNum}");  
    case _:
         print(f"{operator} is not a operator");


