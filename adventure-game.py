# Welcome message
print("Choose your own adventure! ")

# User adds their name
name = input("What is your name? ")

# User adds their age
age = int(input("What is your age? "))

# Health
health = 10

print("Hello", name, "you are", age, "years old.")

# Program checks the age of the player
if age >= 18:
    print("You are old enough to play!")
    wants_to_play = input("Do you want to play? (yes/no) ").lower()
    if wants_to_play == "yes":
        print("Let's play!")
        print("You are starting with 10 health points.")
        left_or_right = input("First choice... left or right? ").lower()
        if left_or_right == "left":
            ans = input("Nice, you follow the path and reach a lake... do you swim across or go around (across/around)? ").lower()
            if ans == "around":
                print("Excellent!  You went around and reached the other side of the lake.")
            elif ans == "across":
                print("You managed to get across, but were bit by a sea cucumber and lost 5 health points.")
                health -= 5
            ans = input("You notice a house and a river.  Where do you go?  (river/house) ").lower()
            if ans == "house":
                print("You go to the house and are greeted by a guinea pig.  You gain 5 health points!")
                health += 5
                if health <= 0:
                    print("You now have 0 health and have lost the game.")
                else:
                    print("*** You win! ***")
            else:
                print("Oh, no!  You feel in the river, the current swept you away, and you lost.")
        else:
            print("Oh, no!  You lost!")
    else:
        print("Come back when you're older!")
else:
    print("Unfortunately, you are not old enough to play...")