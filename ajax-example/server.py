from flask import Flask, request, render_template
import random

app = Flask(__name__, static_folder='static')

@app.route("/")
def index():
    return render_template('index.htm')
	
@app.route("/get_random_number")
def random_number():
	return str(random.randint(0, 100))

if __name__ == "__main__":
    app.run()