import random

#list of items 

items = ['paper', 'rock', 'scissors']

"""

items[0] = papel
items[1] = piedra
items[2] = tijera


"""

# State initialization
state = 0

while state == 0:

# Recieving input from user
    player = input('Choose an item: ')

# storing computer's random choice into a variable
    computer = random.choice(items)

# Verification

    if player in items:
        print("\nAll good")

        # printing player's choice
        print(f'You chose: {player}')

        # printing computer's choice
        print(f'computer chose: {computer}')

        if computer == player:
            print("\nIt's a Tie!!")

        elif (computer == "rock" and player == 'scissors') or (computer == 'paper' and player == "rock") or (computer == 'scissors' and player == 'paper'):
            print("\nYou lost!")

        else:
            print("\nYou win!")

        print("\nDo you what want to keep playing!")
        print("1: Yeah I feel lucky!\n2: No, I'm good!")

        try:
            continuar = int(input("Enter your answer: "))

            if continuar == 2:
                break
        
        except ValueError:
            print("\nPlease, insert a valid number!\n")
    
    else:
        print("\nPlease, insert a proper item")


