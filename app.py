from flask import Flask

app = Flask(__name__)

@app.route('/kigali')
def index():
    return "  I am in time the capital of Rwanda"
@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, %s!</h1>' % name

@app.route('/')
def index1():
    return '<h1>Hello World!</h1>'

@app.route("/greet/<name>")
def user2(name):
    return " <h2> Morning %s</h2>" % name
@app.route("/counter/<int:number>")
def counter(number):
        numbers =["number zero","number one","number two",'number three','number fwo','number five']
        if number <= 5:
            return numbers[number]
        else:
            return " the number is unknown"
if __name__ =='__main__':
    app.run(debug=True)

