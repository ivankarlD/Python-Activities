name = str(input("Name: "))
math = int(input("Enter the grade in Math: "))
science = int(input("Enter the grade in Science: "))
english = int(input("Enter the grade in English: "))
history = int(input("Enter the grade in History: "))
economics = int(input("Enter the grade in Economics: "))
foreignLanguage = int(input("Enter the grade in Foreign Language: "))
arts = int(input("Enter the grade in Arts: "))
socialStudies = int(input("Enter the grade in Social Studies: "))

ave = (math + science + english + history + economics + foreignLanguage + arts + socialStudies) / 8

if ave >= 75 and math >= 75 and science >= 75 and english >= 75 and history >= 75 and economics >= 75 and foreignLanguage >= 75 and arts >= 75 and socialStudies >= 75:
    print("Congratulations!")
    print("You passed the semester with an average grade of " + format(ave, '.2f'))
elif ave >= 75 and (math < 75 or science < 75 or english < 75 or history < 75 or economics < 75 or foreignLanguage < 75 or arts < 75 or socialStudies < 75):
    print("You passed the semester with an average grade of " + format(ave, '.2f'))
    print("But you need to retake the following subject(s):")
    print("List of the subject(s) failed:")
    if math < 75:
        print("Math")
    if science < 75:
        print("Science")
    if english < 75:
        print("English")
    if history < 75:
        print("History")
    if economics < 75:
        print("Economics")
    if foreignLanguage < 75:
        print("Foreign Language")
    if arts < 75:
        print("Arts")
    if socialStudies < 75:
        print("Social Studies")
else:
    print("You failed the semester!")