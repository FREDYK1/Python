def get_average():
    with open("../Temperature.txt", 'r') as file:
        temperatures = file.readlines()
        print(temperatures)
    values = temperatures[1:]
    values = [float(i) for i in values]

    average_local = sum(values) / len(values)
    return average_local


average = get_average()

print(average)