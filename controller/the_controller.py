import serial
#port = raw_input("Please enter port: ")
ser = serial.Serial()
ser.port = "/dev/cu.usbserial-A800eUrB"
ser.open()

from flask import Flask, request, render_template
app = Flask(__name__, static_folder='static')

state = " "

def check_current_state():
    ser.write("stateX")
    if ser.inWaiting() == 2:
        return render_template('index.html')
    elif ser.inWaiting() == 3:
        return render_template('index.html')

@app.route("/")
def index():
    check_current_state()
    return render_template('index.html')

@app.route("/turn_on")
def on():
    check_current_state()
    state = "onX"
    ser.write(state)
    return "ok"
    #return render_template('index.html')

@app.route("/turn_off")
def off():
    check_current_state()
    state = "offX"
    ser.write(state)
    return "ok"
    #return render_template('index.html')


@app.route("/action", methods = ['GET'])
def action():
    check_current_state()
    value = request.args.get('value')
    print "I got " + str(value)
    if value == "turn_on":
        state = "onX"
        ser.write(state)
        return render_template('index.html')
    elif value == "turn_off":
        state = "offX"
        ser.write(state)
        return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0")


def echo(input):
    ser.reset_input_buffer()
    ser.write(input)
    return ser.read(len(input))
