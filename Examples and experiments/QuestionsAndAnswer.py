import json

with open("Questions.json", 'r') as file:
    content = file.read()

data = json.loads(content)

score = 0
for question in data:
    print(question["Question_text"])
    for index, alternative in enumerate(question["alternatives"]):
        print(index + 1, "-", alternative)
    user_choice = int(input("What is your answer?: "))
    question["user_choice"] = user_choice
    if question["user_choice"] == question["correct_answer"]:
        score = score + 1
        print("Well Done")
    elif question["user_choice"] != question["correct_answer"]:
        if question["correct answer"] == 3:
            print("A dolphin is a mammal. ")
        elif question["correct answer"] == 2:
            print("Water covers most of the earth's surface. ")

print(score, "/", len(data))

