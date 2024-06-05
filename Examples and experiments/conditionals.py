gender = input("What is your gendr?: ")
grade = float(input("What is your grade point?: "))

if gender == "Male":
    if grade >= 2.5:
        print("Passed")
    else:
        print("Failed")
else:
    if grade >= 2.0:
        print("Passed")
    else:
        print("Failed")

