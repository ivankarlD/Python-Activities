mealList = [ ["A", "Chicken", 150], ["B", "Hamburger & Fries", 145], ["C", "Cheese Burger", 100], ["D", ["D1", "Carbonara", 120], ["D2", "Spaghetti", 110]], ["E", "Pizza", 80] ]
drinkList = [ ["S", "Small Drinks", 30], ["M", "Medium Drinks", 35], ["L", "Large Drinks", 40] ]

def Order(meal, drink, quantity, sub) :
    orderedMeal = []
    orderedDrink = []

    if meal == "A" : orderedMeal = mealList[0]
    elif meal == "B" : orderedMeal = mealList[1]
    elif meal == "C" : orderedMeal = mealList[2]
    elif meal == "D" :
        if sub == "D1" : orderedMeal = mealList[3][1]
        elif sub == "D2" : orderedMeal = mealList[3][2]
        else : 
            print("Error: Invalid Meal Code")
            return
    elif meal == "E" : orderedMeal = mealList[4]
    else : 
        print("Error: Invalid Meal Code") 
        return

    if drink == "S" : orderedDrink = drinkList[0]
    elif drink == "M" : orderedDrink = drinkList[1]
    elif drink == "L" : orderedDrink = drinkList[2]
    else :
        print("Error: Invalid Drink Code")        
        return

    print(f"Order Details: {orderedMeal[1]} and {orderedDrink[1]}")
    print(f"Amount: {(orderedMeal[2]+orderedDrink[2])*quantity}")

meal = (input("Meal: "))
if meal == "D" :
    subItem = input("Sub-Item: ")
else :
    subItem = ""
drink = (input("Drinks: "))
quantity = int(input("Quantity: "))
Order(meal, drink, quantity, subItem)

