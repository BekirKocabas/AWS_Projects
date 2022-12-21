from flask import Flask

app = Flask(__name__)

@app.route('/')
def head():
    return "hello world bekir"

@app.route('/second')
def second():
    return 'This is second page'

@app.route('/third')
def third():
    return 'This is third page'

@app.route('/forth/<string:id>')
def forth(id):
    return f'Id of this page is {id}'

if __name__ == '__main__':
    app.run(port=2000, debug=True)

