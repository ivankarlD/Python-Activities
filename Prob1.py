def Compute(name, grades) :
    total = 0
    for grade in grades : total = total + grades[grade]
    ave = total/len(grades)

    failedSubjects = 0
    if ave >= 75 :
        for grade in grades :
            if grades[grade] < 75 :
                failedSubjects = failedSubjects + 1

        if failedSubjects == 0 :
            print("Congratulations!")
            print("You passed the semester with an average grade of " + format(ave, '.2f'))
        else :
            print("You passed the semester with an average grade of " + format(ave, '.2f'))
            print("But you need to retake the following subject(s):")
            for grade in grades :
                if grades[grade] < 75 :
                    print(grade);
    else :
        print("You failed the semester!")

name = str(input("Name: "))
grades = {}
grades["math"] = int(input("Enter the grade in Math: "))
grades["science"] = int(input("Enter the grade in Science: "))
grades["english"] = int(input("Enter the grade in English: "))
grades["history"] = int(input("Enter the grade in History: "))
grades["economics"] = int(input("Enter the grade in Economics: "))
grades["foreignLanguage"] = int(input("Enter the grade in Foreign Language: "))
grades["arts"] = int(input("Enter the grade in Arts: "))
grades["socialStudies"] = int(input("Enter the grade in Social Studies: "))
Compute(name, grades)
