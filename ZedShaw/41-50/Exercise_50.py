# ZedShaw Python Exercise #50
# This Exercise is all about...FLASK  INTRO

#few extra steps to get it displaying to a webpage but pretty cool
from flask import Flask

app = Flask(__name__)

@app.route('/')
def h_w():
    return "Hello World!"

if __name__ == "__main__":
    app.run()
