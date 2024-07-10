from flask import Flask,render_template,request,redirect,url_for,session
import random
app = Flask(__name__)
app.secret_key = '420f80eec198fbb61ed705d4266d3490e735c4a176b745d7'

@app.route("/",methods=['GET','POST'])
def index():
    if 'number' not in session:
        session['number'] = random.randint(1,100)
        session['attempts'] = 0
    
    if request.method == 'POST':
        guess = int(request.form['guess'])
        session['attempts'] += 1

        if guess < session['number']:
            message = "Your! guess is too Low!"
        elif guess > session['number']:
            message = "Your! guess is too High!"
        else:
            message = f"Congratulations! You're guessed the number in {session['attempts']} attempts."
            session.pop('number',None)
            session.pop('attempts',None)

        return render_template('index.html',message=message)
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)