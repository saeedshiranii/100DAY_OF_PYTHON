import requests


def get_question():
    questions_list = []
    find = requests.get(url="https://opentdb.com/api.php?amount=10&type=boolean")
    find.raise_for_status()
    recent_data = find.json()["results"]
    for i in range(len(recent_data)):
        questions_list.append(recent_data[i])
    return recent_data

question_data = get_question()
