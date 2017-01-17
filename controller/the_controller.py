import serial
#port = raw_input("Please enter port: ")
ser = serial.Serial()
ser.port = "/dev/cu.usbmodem1421"
ser.open()

from flask import Flask, request, render_template
app = Flask(__name__, static_folder='static')

state = " "

@app.route("/")
def hello():
    return "hello"

@app.route("/turn_on")
def on():
    state = "onX"
    ser.write(state)
    return "LED is on"

@app.route("/turn_off")
def off():
    state = "offX"
    ser.write(state)
    return "LED is off"

@app.route("/test")
def test():
    return render_template('simple_template.html')

@app.route("/action", methods = ['POST'])
def action():
    text = request.form.get('text')
    if text == "turn_on":
        state = "onX"
        ser.write(state)
        return render_template('turned_on.html')
    elif text == "turn_off":
        state = "offX"
        ser.write(state)
        return render_template('turned_off.html')
    else:
        return str(text).upper()


if __name__ == "__main__":
    app.run(host="0.0.0.0")


def echo(input):
    ser.reset_input_buffer()
    ser.write(input)
    return ser.read(len(input))
