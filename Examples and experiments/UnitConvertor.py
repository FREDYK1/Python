feet_inches = input("Enter feet and inches:")


def sep(feet_inches):
    parts = feet_inches.split(" ")
    feet = float(parts[0])
    inches = float(parts[1])
    return {"feet": feet, "inches": inches}


def convert(feet, inches):
    meters = feet * 0.3048 + inches * 0.0254
    return meters


sept = sep(feet_inches)

result = convert(sept["feet"], sept["inches"])

print(f"{sept["feet"]} feet and {sept['inches']} inches is {result} meters")

if result < 1:
    print("Kid is too small.")
else:
    print("Kid can use the slide.")
