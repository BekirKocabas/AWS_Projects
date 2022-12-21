from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')

def head():
    return render_template('index.html', number1 = 23, number2=45)

@app.route('/carp')

def carpim():
    return render_template('body.html', num1=3, num2=5)

if(__name__ == '__main__'):
    app.run(port=80)
