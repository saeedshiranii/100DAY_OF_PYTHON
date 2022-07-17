import re
from flask import Flask
import random




random_number = int(random.randint(0, 9))
print(random_number)
# user_entery_num = int(input("Guess a number between 0 and 9: "))

app = Flask(__name__)







HOME_IMG = "https://media2.giphy.com/media/ne3xrYlWtQFtC/giphy.gif?cid=ecf05e47yjgt9y84wl05w10lhn3nxokwkz81qqwncgoaj42x&rid=giphy.gif&ct=g"


@app.route("/")
def home(img=HOME_IMG):
    return f'<h1>Guess a number between 0 and 9</h1><img src="{img}"alt="A animate gif of numbers"/>'




# now create a random number and get a guess from user and checck it
@app.route("/<int:user_entery_num>")
def number_check(user_entery_num):

    
    if random_number == user_entery_num: 

        answer = "True"
        answer_img = "https://media3.giphy.com/media/l2YWo6rKKWTxjyAb6/giphy.gif?cid=ecf05e47vl3cpl930v7in8bc0a5zpbmx7ruf4t9p8s07zot4&rid=giphy.gif&ct=g"
        return f'<h1>That is {answer}.</h1><img scr="{answer_img}"alt="A animate gif of numbers"/>'
        
    elif random_number > user_entery_num:

        answer = "Too Low"
        answer_img = "https://media0.giphy.com/media/wHB67Zkr63UP7RWJsj/200.webp?cid=ecf05e479mqk0nq1iqazt9x299khspdbu0oqe1p2ddrly6rb&rid=200.webp&ct=g"
        return f'<h1>That is {answer}.</h1><img scr="{answer_img}"alt="A animate gif of numbers"/>'

    else:

        answer = "Too Hight"
        answer_img = "https://media0.giphy.com/media/TgmiJ4AZ3HSiIqpOj6/giphy.gif?cid=ecf05e47s2difi7ug6y4gud8egd1r84spylgi5yfxfwgz86s&rid=giphy.gif&ct=g"
        return f'<h1>That is {answer}.</h1><img scr="{answer_img}"alt="A animate gif of numbers"/>'



if __name__ == "__main__":
    app.run(debug=True)