date = input("Enter today's date: ")
mood = input("How do you rate your mood today from 1 to 10? ")
Thoughts = input("Let your thoughts flow:\n")

with open(f"{date}.txt", "w") as file:
    file.write(f"Your mood today is rated {mood+ 2 * "\n"}" )
    file.write(f"Today's Thoughts:  {Thoughts}")