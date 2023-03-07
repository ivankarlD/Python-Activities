def calculateElectricBill(startReading, endReading):
    if endReading < startReading:
        print("End reading cannot be less than start reading.")
        return

    unitsConsumed = endReading - startReading
    bill = 0

    if unitsConsumed <= 100: bill = unitsConsumed * 1.5
    elif unitsConsumed <= 300: bill = unitsConsumed * 2
    elif unitsConsumed <= 500: bill = unitsConsumed * 2.5
    elif unitsConsumed <= 1000: bill = unitsConsumed * 3.25
    else: bill = unitsConsumed * 4.75

    print("Total Consumption: ",unitsConsumed)
    print("Electricity Bill: ",bill)

print("Electric Bill Calculator")
startReading = int(input("Input the Start Reading: "))
endReading = int(input("Input the End Reading: "))
calculateElectricBill(startReading, endReading)