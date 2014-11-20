from flask import Flask,make_response

app = Flask(__name__)

@app.route('/kigali')
def index():
    response = make_response( "  I am in time the capital of Rwanda")
    return  response
@app.route('/user/<name>')
def user(name):
    return make_response('<h1>Hello, %s!</h1>' % name)

@app.route('/')
def index1():
    return make_response('<h1>Hello World!</h1>')

@app.route("/greet/<name>")
def user2(name):
    return  make_response(" <h2> Morning %s</h2>" % name)
@app.route("/counter/<int:number>")
def counter(number):
        numbers =["number zero","number one","number two",'number three','number fwo','number five']
        if number <= 5:
            response = make_response( numbers[number])
            return  response
        else:
            response = make_response( " the number is unknown")
            return response
if __name__ =='__main__':
    app.run(debug=True)

