import random

def get_choices():
    options = ["rock", "paper", "scissors"]
    
    player_choice = input("Enter a choice (rock, paper, scissors): ")
    computer_choice = random.choice(options)
    choices = {"player": player_choice, "computer": computer_choice}
    return choices


def check_win(player, computer):
    print(f"Player chose {player}, computer chose {computer}")
    
    if player == computer:
        return "Tie!"
    #
    elif player == "rock":
        if computer == "scissors":
            return "Rock beats scissors! Player Wins"
        else:
            return "Paper beats rock! Computer Wins"
    
    #
    elif player == "scissors":
        if computer == "rock":
            return "Rock beats scissors! Computer Wins"
        else:
            return "Scissors beats paper! Player Wins"
    
    elif player == "paper":
        if computer == "rock":
            return "paper beats rock! Player Wins"
        else:
            return "Scissors beats paper! Computer Wins"



choices = get_choices()

result = check_win(choices["player"],choices["computer"])
print(result)