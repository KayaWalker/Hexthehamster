
score = 0

# Question 1
bool = 0
firsttry = 0

while bool == 0:
    first_q = input("Hex code #FFFFFF. Click the color:")
    if first_q == "white":
        bool = 1
        print("Great job! you got the first button!")
    else:
        print("Oops wrong button. Try again.")
        firsttry = 1

if firsttry == 0:
    score += 1


# Question 2
bool = 0
firsttry = 0

while bool == 0:
    first_q = input("Hex code #FF0000. Click the color:")
    if first_q == "red":
        bool = 1
        print("Great job! you got the second button!")
    else:
        print("Oops wrong button. Try again.")
        firsttry = 1

if firsttry == 0:
    score += 1


# Question 3
bool = 0
firsttry = 0

while bool == 0:
    first_q = input("Hex code #0000FF. Click the color:")
    if first_q == "blue":
        bool = 1
        print("Great job! you got the third button!")
    else:
        print("Oops wrong button. Try again.")
        firsttry = 1

if firsttry == 0:
    score += 1


# Question 4
bool = 0
firsttry = 0

while bool == 0:
    first_q = input("Hex code #00FF00. Click the color:")
    if first_q == "green":
        bool = 1
        print("Great job! you got the fourth button!")
    else:
        print("Oops wrong button. Try again.")
        firsttry = 1

if firsttry == 0:
    score += 1


# Question 5
bool = 0
firsttry = 0

while bool == 0:
    first_q = input("Hex code #DFFF00. Click the color:")
    if first_q == "chartreuse":
        bool = 1
        print("Great job! you got the fith button!")
    else:
        print("Oops wrong button. Try again.")
        firsttry = 1

if firsttry == 0:
    score += 1

# Question 6
bool = 0
firsttry = 0

while bool == 0:
    first_q = input("Hex code #A020F0. Click the color:")
    if first_q == "purple":
        bool = 1
        print("Great job! you got the Last button!")
    else:
        print("Oops wrong button. Try again.")
        firsttry = 1

if firsttry == 0:
    score += 1

print("Congradulations! Hex the Hamster can get home! Your score was: " + str(score))







