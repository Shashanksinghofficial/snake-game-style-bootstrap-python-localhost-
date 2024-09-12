# app.py
from flask import Flask, render_template, request
import random

app = Flask(__name__)

def get_computer_choice():
    choices = ['snake', 'water', 'gun']
    choice = random.choice(choices)
    return choice

def play_game(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    if user_choice == 'snake':
        return "You win!" if computer_choice == 'water' else "Computer wins!"
    if user_choice == 'water':
        return "You win!" if computer_choice == 'gun' else "Computer wins!"
    if user_choice == 'gun':
        return "You win!" if computer_choice == 'snake' else "Computer wins!"

@app.route('/')
def index():
    return render_template('index.html')  # Load the HTML page

@app.route('/play', methods=['POST'])
def play():
    user_choice = request.form.get('user_choice')
    computer_choice = get_computer_choice()
    result = play_game(user_choice, computer_choice)
    return render_template('index.html', user_choice=user_choice, computer_choice=computer_choice, result=result)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')