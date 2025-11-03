import random
print("Welcome to the 'rock, paper, scissors' game by Fernando Ramirez")
rock = '''
    _____
---'   ____)
      (_____)
      (_____)
      (____)
---.__(__)
'''

paper = '''
    _____
---'   ____)
          _______)
          ________)
         ________)
---._________)
'''

scissors = '''
    ______
---'   ____)____
          ________)
       __________)
      (____)
---.__(___)
'''
symbols = [rock, paper, scissors]
list = ["rock", "paper", "scissors"]
game = input("Would you like to play?\nPlease enter 'yes' to start the game or 'no' to close the game: ").lower()
while game != "no":
    try:
        number = int(input("Please enter '1' for rock, '2' for paper or '3' for scissors: "))
        if number <= 0:
            raise IndexError
        number -= 1
        user_choice =  list[number]
        index_user = list.index(user_choice)
        symbol_choice_user = symbols[index_user]
        computer_choice = random.choice(list)
        index = list.index(computer_choice)
        symbol_choice_computer = symbols[index]
        if user_choice == computer_choice:
            print(f"You chose: {user_choice}\n{symbol_choice_user}The computer chose: {computer_choice}\n{symbol_choice_computer}")
            print("It is a tie!")
        elif user_choice == "rock" and computer_choice == "'paper" or user_choice == "paper" and computer_choice == "scissors" or user_choice == "scissors" and computer_choice == "rock":
            print(f"You chose: {user_choice}\n{symbol_choice_user}The computer chose: {computer_choice}\n{symbol_choice_computer}")
            print("You lost!")
        else:
            print(f"You chose: {user_choice}\n{symbol_choice_user}The computer chose: {computer_choice}\n{symbol_choice_computer}")
            print("You won! Congratulations!")
    except IndexError:
        print("Your selection was out of range, please choose '1', '2'. or '3'")
    except ValueError:
        print("Please enter a number")
    else:
        new_game = input("Do you want to play again?\nPlease enter 'yes' to start a new game or 'no' to close the game: ").lower()
        if  new_game == "no":
            print("Come back soon\nHave a good day! Bye!")
            break
else:
    print("Come back soon\nHave a good day! Bye!")


