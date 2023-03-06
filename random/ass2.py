i = int(input("Input integer value : "))

while True:
    print(int(i))
    if i != 1 :
        if i % 2 == 0 :
            i = i / 2
        else :
            i = i * 3 + 1
    else :
        break
