from flask import Flask, render_template, request, redirect, url_for, session
import random

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for session handling

# Initialize a new game
def initialize_game():
    session['hidden_number'] = random.randint(1, 20)
    session['attempts'] = 0
    session['last_guess'] = None
    session['last_feedback'] = None

@app.route('/', methods=['GET', 'POST'])
def index():
    if 'hidden_number' not in session:
        initialize_game()

    message = None

    if request.method == 'POST':
        guess_input = request.form['guess'].strip().lower()

        if guess_input == 'x':
            message = "Thanks for playing! Goodbye!"
            initialize_game()
        elif guess_input == 'n':
            initialize_game()
            message = "Starting a new game. The computer has chosen a new number between 1 and 20."
        elif guess_input == 's':
            message = f"The hidden number is: {session['hidden_number']}"
        elif guess_input.isdigit():
            guess = int(guess_input)
            session['attempts'] += 1

            if guess < session['hidden_number']:
                if session['last_feedback'] == 'too small':
                    message = f"Still too small! Try a bigger number. (Attempt {session['attempts']})"
                else:
                    message = f"Too small! Try again. (Attempt {session['attempts']})"
                session['last_feedback'] = 'too small'
            elif guess > session['hidden_number']:
                if session['last_feedback'] == 'too big':
                    message = f"Still too big! Try a smaller number. (Attempt {session['attempts']})"
                else:
                    message = f"Too big! Try again. (Attempt {session['attempts']})"
                session['last_feedback'] = 'too big'
            else:
                message = f"Congratulations! You've guessed the number {session['hidden_number']} in {session['attempts']} attempts."
                initialize_game()

            session['last_guess'] = guess
        else:
            message = "Invalid input! Please enter a valid number, 'x' to exit, 'n' to start a new game, or 's' to show the number."

    return render_template('index.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)
