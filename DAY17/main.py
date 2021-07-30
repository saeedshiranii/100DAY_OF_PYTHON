from data import question_data
from question_model import Question
#from quiz_brain import QuizBrain

class QuestionList:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer


q_bank = []
for data in question_data:
    data_text = data["text"]
    data_answer = data["answer"]
    question = QuestionList(data_text, data_answer)
    q_bank.append(question)



