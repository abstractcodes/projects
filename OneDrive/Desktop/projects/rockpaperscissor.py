import random

def play():
    user_input = input("Enter 'R' for rock,'S' for scissor or 'P' for paper: ")
    computer_input = random.choice(['R','P','S'])
    if user_input == computer_input:
        return 'It\'s a tie'
    
    if is_win(user_input,computer_input):
        return "You won the game"
    
    return "You lost the game"

def is_win(user_choice, computer_choice):
    if(user_choice=='P' and computer_choice=='R') or (user_choice=='S'and computer_choice=='P') or\
        (user_choice=='R' and computer_choice=='S'):
            return True
        
print(play())