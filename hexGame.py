

name = input("Enter your name: ")
print("Hello, " + name)

# (white, red, green, blue, chartreuse)
buttons = ["White","Red", "Blue","Green", "Chartreuse"]

# Question 1
bool = 0

while bool == 0:
    first_q = input("Hex code 000000. Enter Color:")
    if first_q == "White":
        bool = 1
        print("Great job! you got the first button!")
    else:
        print("Oops wrong button. Try again.")


# Question 2
bool = 0

while bool == 0:
    first_q = input("Hex code FF0000. Enter Color:")
    if first_q == "Red":
        bool = 1
        print("Great job! you got the second button!")
    else:
        print("Oops wrong button. Try again.")

# Question 3
bool = 0

while bool == 0:
    first_q = input("Hex code 0000FF. Enter Color:")
    if first_q == "Blue":
        bool = 1
        print("Great job! you got the third button!")
    else:
        print("Oops wrong button. Try again.")

# Question 4
bool = 0

while bool == 0:
    first_q = input("Hex code 00FF00. Enter Color:")
    if first_q == "Green":
        bool = 1
        print("Great job! you got the fourth button!")
    else:
        print("Oops wrong button. Try again.")


# Question 5
bool = 0

while bool == 0:
    first_q = input("Hex code DFFF00. Enter Color:")
    if first_q == "Chartreuse":
        bool = 1
        print("Great job! you got the Last button!")
    else:
        print("Oops wrong button. Try again.")


print("Congradulations! Hex the Hamster can get hone!")







