import re
from flask import Flask


app = Flask(__name__)




@app.route("/")
def hello_world():
    return "Hello, World!"



def make_bold(func):

    def insider():
        return f"<b>{func()}</b>"
    return insider


def make_emphasis(func):
    def insider():
        return f"<em>{func()}</em>"
    return insider

def make_italic(func):
    def insider():
        return f"<i>{func()}</i>"
    return insider



@app.route('/bye')
@make_bold
@make_emphasis
@make_italic
def bye():
    return 'Bye!'


if __name__ == "__main__":
    app.run(debug=True)














