import random

def get_choice():
    choice = input("Enter rock, paper or scissors: ").lower()
    while choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice.")
        choice = input("Enter again: ").lower()
    return choice

def decide_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (user == 'rock' and computer == 'scissors') or \
         (user == 'paper' and computer == 'rock') or \
         (user == 'scissors' and computer == 'paper'):
        return "You win!"
    else:
        return "Computer wins!"

def play():
    user_score = 0
    computer_score = 0

    while True:
        user = get_choice()
        computer = random.choice(['rock', 'paper', 'scissors'])

        print(f"You: {user} | Computer: {computer}")
        result = decide_winner(user, computer)
        print(result)

        if "You win" in result:
            user_score += 1
        elif "Computer wins" in result:
            computer_score += 1

        print(f"Score - You: {user_score}, Computer: {computer_score}")

        again = input("Play again? (yes/no): ").lower()
        if again != 'yes':
            break

if __name__ == "__main__":
    play()