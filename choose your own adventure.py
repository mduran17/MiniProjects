name = input("What is your name? :")
print("Welcome", name, "to this adventure!")

answer = input("You are on a dirt road, it has come to an end. Do you want to go left or right? ")


if answer == "left":
    answer = input("You come to a river, you can walk around it or swin scross? Type walk to talk around or swim to swim ")

    if answer == "swim":
        print("You swam across and were eaten by an alligator.")
    elif answer == "walk":
        print("You walked for many miles, you ran out of water and you lost the game. ")
    else:
        print("Not a valid option. You lose")

elif answer == 'right':
    answer = input("You come to a bridge, it loos wobbly, do you want to cross it or head back (cross/back")

    if answer == "back":
        print("You go back and lose.")
    elif answer == "cross":
        answer = input("You cross the bridge and meet an stranger. Do you talk to him? ")

        if answer == "yes":
            print("You talk to the stranger and they give you gold. You win!")
        elif answer == "no":
            print("You ignore the stranger ahd they get offended and then they shoot you. You lose")
    else:
        print("Not a valid option. You lose")
    print()

else:
    print("Not a valid option. You lose.")

print("Thank you for playing. Game over")
