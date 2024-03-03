import random

top_of_range = input("Type a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Please type a number larger than 0 next time. ")
        quit()

else:
    print("Please type a number next time. ")
    quit()


random_number = random.randint(0, top_of_range)
guesses = 0

while True:
    guesses += 1
    user_guest = input("Make a guess: ")
    if user_guest.isdigit():
        user_guest = int(user_guest)

    else:
        print("Please type a number next time. ")
        continue

    if user_guest == random_number:
        print("You got it!")
        break
    elif user_guest > random_number:
            print("You were above the number!")
    else:
            print("You were below the number!")

print("You got it in", guesses, "guesses")
