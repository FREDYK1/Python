try:
    rectangle_length = float(input("Enter rectangle length: "))
    rectangle_height = float(input("Enter rectangle height: "))

    if rectangle_height == rectangle_length:
        exit("The rectangle looks like a square.")

    Area = rectangle_length * rectangle_height
    print(Area)
except ValueError:
    print("Input a number! ")
