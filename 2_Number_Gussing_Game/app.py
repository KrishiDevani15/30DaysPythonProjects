from flask import Flask, render_template, request, redirect, url_for, session
import random

app = Flask(__name__)
app.secret_key = 'a3d6f2e7a3b24c5b8bdb38f6d4f6e7a1f1e8b9c8d7e3f2d4c6b8a1d2c3e4b5f6'  # Replace with your generated secret key

@app.route('/', methods=['GET', 'POST'])
def index():
    if 'number' not in session:
        session['number'] = random.randint(1, 100)
        session['attempts'] = 0

    if request.method == 'POST':
        guess = int(request.form['guess'])
        session['attempts'] += 1

        if guess < session['number']:
            message = "Your guess is too low!"
        elif guess > session['number']:
            message = "Your guess is too high!"
        else:
            message = f"Congratulations! You've guessed the number in {session['attempts']} attempts."
            session.pop('number', None)
            session.pop('attempts', None)
        
        return render_template('index.html', message=message)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True) # This exposes the app for Vercel
