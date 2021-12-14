import random
# Constants
computer_score = 0
player_score = 0
throw_options = ["rock", "paper", "scissors", "games", "current"]
# Instructions
print("\nWelcome to Rock, Paper, Scissors!\nType Rock, Paper or Scissors to play.\nType 'score' to see your score.\nType 'quit' to end the game.\n")
# Game Engine
while True:
    random_number = random.randint(0,2)
    computer_input = throw_options[random_number]
    user_input = input("Type Here:").lower()
    if user_input == "quit":
        break
    elif user_input == "score":
        print(f"Player: {player_score} | Computer: {computer_score}")
    elif user_input not in throw_options:
        print("invalid input, try again")
        continue
    else:
        if user_input == "rock" and computer_input == "scissors":
            print(f"The computer chose {computer_input}, you won!")
            player_score += 1
        elif user_input == "scissors" and computer_input == "paper":
            print(f"The computer chose {computer_input}, you won!")
            player_score += 1
        elif user_input == "paper" and computer_input == "rock":
            print(f"The computer chose {computer_input}, you won!")
            player_score += 1
        elif user_input == computer_input:
            print(f"The computer chose {computer_input}, there was a tie.")
        else:
            print(f"The computer chose {computer_input}, you lost :(.")
            computer_score += 1