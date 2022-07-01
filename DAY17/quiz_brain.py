class Quiz():

    def __init__(self, question_list):

        self.question_number = 0
        self.question_list = question_list
        self.right_answer = 0
       


    def ask(self):

        current_qeustion = self.question_list[self.question_number]
        self.question_number += 1

        return input(f"Q.{self.question_number }. : {current_qeustion.text} (True/False/Break)? ")
        


    def answer(self, user_answer, correct_answer):

        if user_answer == correct_answer:
            
            self.right_answer += 1 
            return self.right_answer

        else: 
            return self.right_answer
        
        