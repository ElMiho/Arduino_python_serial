import serial
port = raw_input("Please enter port: ")
ser = serial.Serial()
ser.port = "/dev/cu.usbmodem1421"
ser.open()

from flask import Flask, request, render_template
app = Flask(__name__, static_folder='static')

state = " "

def check_current_state():
    ser.write("stateX")
    if ser.inWaiting() == 2:
        return render_template('turned_on.html')
    elif ser.inWaiting() == 3:
        return render_template('turned_off.html')

@app.route("/")
def hello():
    return "hello"

@app.route("/turn_on")
def on():
    check_current_state()
    state = "onX"
    ser.write(state)
    return render_template('turned_on.html')

@app.route("/turn_off")
def off():
    check_current_state()
    state = "offX"
    ser.write(state)
    return render_template('turned_off.html')

@app.route("/test")
def test():
    check_current_state()
    return render_template('simple_template.html')

@app.route("/action", methods = ['POST'])
def action():
    check_current_state()
    value = request.form.get('value')
    print "I got " + str(value)
    if value == "turn_on":
        state = "onX"
        ser.write(state)
        #return render_template('turned_on.html')
    elif value == "turn_off":
        state = "offX"
        ser.write(state)
        #return render_template('turned_off.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0")


def echo(input):
    ser.reset_input_buffer()
    ser.write(input)
    return ser.read(len(input))
