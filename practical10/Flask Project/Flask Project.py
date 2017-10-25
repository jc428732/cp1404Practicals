from flask import Flask

app = Flask(__name__)


def celsius_to_fahrenheit(celsius_temperature):
    fahrenheit_temperature = celsius_temperature * 9.0 / 5 + 32
    return str(fahrenheit_temperature)


def fahrenheit_to_celsius(fahrenheit_temperature):
    celsius_temperature = 5 / 9 * (fahrenheit_temperature - 32)
    return str(celsius_temperature)


@app.route('/')
def hello_world():
    return '<h1>Hello World :)</h1>'


@app.route('/greet')
@app.route('/greet/<name>')
def greet(name=""):
    return 'Hello {}'.format(name)


@app.route('/c')
@app.route('/c/<number>')
def c(number="0"):
    return fahrenheit_to_celsius(float(number))


@app.route('/f')
@app.route('/f/<number>')
def f(number="0"):
    return celsius_to_fahrenheit(float(number))

if __name__ == '__main__':
    app.run()
