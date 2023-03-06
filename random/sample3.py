mealList = { 
    "A" : ["Chicken", 150], 
    "B" : ["Hamburger & Fries", 145], 
    "C" : ["Cheese Burger", 100], 
    "D" : { "D1" : ["Carbonara", 120], "D2" : ["Spaghetti", 110]}, 
    "E" : ["Pizza", 80]
}
drinkList = { 
   "S" : ["Small Drinks", 30], 
   "M" : ["Medium Drinks", 35], 
   "L" : ["Large Drinks", 40] 
}

def Order(meal, drink, quantity, sub) :
    orderedMeal = []
    orderedDrink = []

    if meal in mealList :
        if meal == "D" :
            if sub in mealList[meal] :
                orderedMeal = mealList[meal][sub]
            else :
                print("Invalid sub-item code")
                return
        else :
            orderedMeal = mealList[meal]
    else :
        print("Invalid meal code")
        return

    if drink in drinkList :
        orderedDrink = drinkList[drink]
    else :
        print("Invalid drink code")
        return

    if quantity <= 0 :
        print("Invalid quantity")
        return

    print(f"Order Details: {orderedMeal[0]} and {orderedDrink[0]}")
    print(f"Amount: {(orderedMeal[1]+orderedDrink[1])*quantity}")

meal = (input("Meal: "))
if meal == "D" :
    subItem = input("Sub-Item: ")
else :
    subItem = ""
drink = (input("Drinks: "))
quantity = int(input("Quantity: "))
Order(meal, drink, quantity, subItem)

