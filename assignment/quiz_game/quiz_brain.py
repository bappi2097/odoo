import random
from question_model import Question

class QuizBrain:
    def __init__(self, no_of_question, question_data):
        self.no_of_question = no_of_question
        self.questions = [Question(question_data[index]) for index in random.sample(range(1, len(question_data)), no_of_question)]
        self.score = 0

    def take_quiz(self):
        count = 1
        try:
            for question in self.questions:
                answer = question.get_answer(count)
                if question.check_answer(answer):
                    self.score += 1
                    print(f"You got it right!\nThe correct answer was: {question.correct_answer}.\nYour current score is: {self.score}/{count}")
                else:
                    print(f"That's wrong.\nThe correct answer was: {question.correct_answer}.\nYour current score is: {self.score}/{count}")
                count += 1
        except KeyboardInterrupt:
            print("\nShuting down....")

    def get_result(self):
        print(f"\n\nYou've completed the quiz\nYour final score was: {self.score}/{self.no_of_question}\n")
            
    
