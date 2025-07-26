import random

# Step 1: Show welcome message
print("Welcome to Rock, Paper, Scissors Game!")

# Step 2: List of possible choices
options = ["rock", "paper", "scissors"]

# Step 3: Start the game loop
while True:
    # Ask the player to choose
    user_choice = input("Choose rock, paper or scissors: ").lower()
    
    # Check if the input is valid
    if user_choice not in options:
        print("That’s not a valid choice. Try again.")
        continue
    
    # Let the computer make a random choice
    computer_choice = random.choice(options)
    
    # Show both choices
    print("You chose:", user_choice)
    print("Computer chose:", computer_choice)

    # Step 4: Decide who wins
    if user_choice == computer_choice:
        print("It's a tie!")
    elif user_choice == "rock" and computer_choice == "scissors":
        print("You win! Rock beats scissors.")
    elif user_choice == "paper" and computer_choice == "rock":
        print("You win! Paper beats rock.")
    elif user_choice == "scissors" and computer_choice == "paper":
        print("You win! Scissors beats paper.")
    else:
        print("Computer wins!")

    # Step 5: Ask to play again
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("Thanks for playing! Goodbye.")
        break
