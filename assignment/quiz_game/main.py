import sys

from data import question_data
from quiz_brain import QuizBrain

def input_qustion_no():
    while True:
        try:
            no_of_question = int(input(f"How many question want to ask? (1-{len(question_data)}): "))
            if 1 <= no_of_question <= len(question_data):
                return no_of_question
            else:
                raise ValueError
        except ValueError:
            print(f"Invalid input. Please enter a valid number range between 1-{len(question_data)}.")
        except KeyboardInterrupt:
            print("\nShuting down....")
            sys.exit()

if "__main__" == __name__:
    no_of_question = input_qustion_no()
    quiz_brain = QuizBrain(no_of_question=no_of_question, question_data=question_data)
    quiz_brain.take_quiz()
    quiz_brain.get_result()
        