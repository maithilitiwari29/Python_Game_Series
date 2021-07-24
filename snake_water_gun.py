import random

options = ["snake", "water", "gun"]

user_score = 0
Computer_score = 0

print("Please Enter any one of the following\n snake \n water \n gun")

i = 1
j = 7
while i < 7:
    print("You have ",j, "chances left \n")
    Player = input("Enter Your choice: ")
    Computer_choice = random.choice(options)

    if Player == Computer_choice:

        print(f" You Entered {Player} and computer Entered {Computer_choice}")
        print("Tie")

    elif Player == 'snake' and Computer_choice == 'water':

        print(f" You Entered {Player} and computer Entered {Computer_choice}")
        print("This point goes to You")
        user_score = user_score + 1

    elif Player == 'snake' and Computer_choice == 'gun':

        print(f" You Entered {Player} and computer Entered {Computer_choice}")
        print("This point goes to Computer")
        Computer_score = Computer_score + 1

    elif Player == 'water' and Computer_choice == 'snake':

        print(f" You Entered {Player} and computer Entered {Computer_choice}")
        print("This point goes to Computer")
        Computer_score = Computer_score + 1

    elif Player == 'water' and Computer_choice == 'gun':

        print(f" You Entered {Player} and computer Entered {Computer_choice}")
        print("This point goes to You")
        user_score = user_score + 1

    elif Player == 'gun' and Computer_choice == 'snake':

        print(f" You Entered {Player} and computer Entered {Computer_choice}")
        print("This point goes to You")
        user_score = user_score + 1

    elif Player == 'gun' and Computer_choice == 'water':

        print(f" You Entered {Player} and computer Entered {Computer_choice}")
        print("This point goes to Computer")
        Computer_score = Computer_score + 1

    else:

        print("Wrong Input")

    i = i + 1
    j = j - 1

if user_score > Computer_score:

    print("\nCongratulations You Won...... ")
    print(f" Your score is: {user_score} and Computer score is {Computer_score}")

elif user_score < Computer_score:

    print("\nAH! AH! You Loose....... ")
    print(f" Your score is: {user_score} and Computer score is {Computer_score}")

else:

    print("\nDraw....... ")
    print(f" Your score is: {user_score} and Computer score is {Computer_score}")
