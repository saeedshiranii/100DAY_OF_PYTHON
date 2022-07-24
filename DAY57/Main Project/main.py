
from flask import Flask, render_template
import requests
import post


ENDPOINT_POST_LINK = "https://api.npoint.io/54c8ac8084403dbccbca"
result_dict = requests.get(ENDPOINT_POST_LINK).json()
post_list = list()
post_index = list()

for item_dict in result_dict:

    new_post_obj = post.Post(item_dict, result_dict)
    post_list.append(new_post_obj)

    post_index.append(item_dict)
    





app = Flask(__name__)

@app.route('/')
def home():
    return f"<a href='http://127.0.0.1:5000/post'> if you want to see posts, click this </a>"

@app.route('/post')
def renderall_post(data_list=post_list):
    return render_template("post.html", data_list=post_list)

@app.route("/post/<index>")
def show_post(index, index_list=post_index, data_dict=result_dict):

    if index in index_list:
        target_dict = data_dict[index]

        post_title = target_dict["title"]
        post_body = target_dict["post"]
        post_sub = target_dict["subtitle"]

    return render_template("index.html", title=post_title, sub=post_sub, body=post_body)




if __name__ == "__main__":
    app.run(debug=True)
