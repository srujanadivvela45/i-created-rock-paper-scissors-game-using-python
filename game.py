import random

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def decide_winner(user, computer):
    if user == computer:
        return "tie"
    elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        return "win"
    else:
        return "lose"

def play_game():
    user_score = 0
    computer_score = 0

    print("🎮 Welcome to Rock-Paper-Scissors Game!")
    print("👉 Choose: rock, paper, or scissors\n")

    while True:
        user_choice = input("Enter your choice: ").lower()

        if user_choice not in ["rock", "paper", "scissors"]:
            print("❌ Invalid choice! Please try again.\n")
            continue

        computer_choice = get_computer_choice()

        print(f"\n🧑 You chose: {user_choice}")
        print(f"💻 Computer chose: {computer_choice}")

        result = decide_winner(user_choice, computer_choice)

        if result == "win":
            print("🎉 You win this round!")
            user_score += 1
        elif result == "lose":
            print("😢 You lose this round!")
            computer_score += 1
        else:
            print("🤝 It's a tie!")

        print(f"\n📊 Score -> You: {user_score} | Computer: {computer_score}")

        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("\n👋 Thanks for playing!")
            break
        print("\n-----------------------------\n")

# Run the game
play_game()
