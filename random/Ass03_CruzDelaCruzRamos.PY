credNum = str(input("Input Credit Card Number: \n"))

set1 = ""
sum1 = 0 
sum2 = 0 

for x in range(len(credNum)) :
    if x % 2 == 0 : set1 = str(int(credNum[x])*2) + set1 
    else : sum2 = sum2 + int(credNum[x])

for x in range(len(set1)) : sum1 = sum1 + int(set1[x])

if (sum1 + sum2) % 10 == 0 : print(f"############{credNum[-4:]} number is valid")
else : print(f"############{credNum[-4:]} number is invalid")
