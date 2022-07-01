from question_model import Question
from data import question_data
from quiz_brain import Quiz

question_bank = []

for item in question_data:

    q = Question(text = item["text"], answer = item["answer"])
    question_bank.append(q)
    del q



quiz = Quiz(question_list = question_bank)
for i in range(len(question_bank)):

    user_answer = quiz.ask()

    if user_answer == "Break":
        break

    else:
        correct_answer =  question_bank[i].answer

        print(user_answer)
        print(correct_answer)

        a = quiz.answer(user_answer = user_answer, correct_answer = correct_answer)


        print(f"Right answers : {a} / {len(question_bank)}")


            

