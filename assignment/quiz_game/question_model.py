class Question:
    def __init__(self, question):
        self.category = question["category"]
        self.type = question["type"]
        self.difficulty = question["difficulty"]
        self.question = question["question"]
        self.correct_answer = question["correct_answer"]
        self.incorrect_answers = question["incorrect_answers"]
    
    def get_answer(self, question_no):
        while True:
            try:
                answer = input(f"\n\nQ.{question_no}: {self.question} (True/False):").capitalize()
                if answer not in ["True", "False"]:
                    raise ValueError
                return answer
            except ValueError:
                print("Invalid Input. Input should True/False")
    
    def check_answer(self, answer):
        return answer == self.correct_answer