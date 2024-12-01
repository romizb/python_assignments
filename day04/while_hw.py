import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    while True:
        # Generate a random number between 1 and 20
        hidden_number = random.randint(1, 20)
        print("\nThe computer has chosen a number between 1 and 20.")
        attempts = 0
        
        while True:
            user_input = input("Enter your guess (or 'x' to exit, 'n' to start a new game, 's' to show the number): ").strip().lower()
            
            if user_input == 'x':
                print("Thanks for playing! Goodbye!")
                return
            
            if user_input == 'n':
                print("Starting a new game...")
                break
            
            if user_input == 's':
                print(f"The hidden number is: {hidden_number}")
                continue
            
            # Validate if the input is a number
            if not user_input.isdigit():
                print("Please enter a valid number, 'x', 'n', or 's'.")
                continue
            
            guess = int(user_input)
            attempts += 1
            
            # Compare the guess with the hidden number
            if guess < hidden_number:
                print("Too small!")
            elif guess > hidden_number:
                print("Too big!")
            else:
                print(f"Congratulations! You've guessed the number {hidden_number} in {attempts} attempts.")
                break
        
        # Ask if the user wants to play again
        play_again = input("Do you want to play another game? (yes/no): ").strip().lower()
        if play_again != 'yes':
            print("Thanks for playing! Goodbye!")
            break

# Run the game
number_guessing_game()
