import random
min = 1
max = 6

roll_again = "yes"

while roll_again == "yes" or roll_again == "y":
    print("Rolling the dices...")
    player1 = random.randint(min, max)
    print("Player 1's roll: " + str(player1))
    player2 = random.randint(min, max)
    print("Player 2's roll: " + str(player2))

    if(player1 == player2):
        print("There is a tie!")
    elif(player1 > player2):
        print("Player 1 won!")
    else:
        print("Player 2 won!")

    roll_again = input("Roll the dices again?")