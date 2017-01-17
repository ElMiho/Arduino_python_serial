import serial
port = raw_input("Please enter port: ")
ser = serial.Serial()
ser.port = port
ser.open()

from flask import Flask, request
app = Flask(__name__)

@app.route("/")
def hello():
        return "hello"

@app.route("/turn_on")
def on():
    ser.write("onX")
    return "LED is on"

@app.route("/turn_off")
def off():
    ser.write("offX")
    return "LED is off"

@app.route("/test")
def test():
    return '<form action="/action" method="POST"><input name="text"><input type="submit" value="Echo"></form>'

@app.route("/action", methods = ['POST'])
def action():
    text = request.form.get('text')
    if text == "turn_on":
        ser.write("onX")
        return "LED is on"
    elif text == "turn_off":
        ser.write("offX")
        return "LED is off"
    else:
        return str(text).upper()


if __name__ == "__main__":
    app.run(host="0.0.0.0")


def echo(input):
    ser.reset_input_buffer()
    ser.write(input)
    return ser.read(len(input))
