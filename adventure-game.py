# Welcome message
print("Choose your own adventure! ")

# User adds their name
name = input("What is your name? ")

# User adds their age
age = int(input("What is your age? "))

print("Hello", name, "you are", age, "years old.")

if age >= 18:
    print("You are old enough to play!")
    wants_to_play = input("Do you want to play? (yes/no) ")
    if wants_to_play == "yes":
        print("Let's play!")
else:
    print("Unfortunately, you are not old enough to play...")