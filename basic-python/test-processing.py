import string
import re

def text_lowercase(text):
    return text.lower()

input_str = "Hey, did you know that the summer break is coming? Amazing right!! It's only 5 more days!!"
print( text_lowercase(input_str) )

def remove_whitespace(text):
    return " ".join(text.split())

input_str = "we don't need   the given questions"

print(remove_whitespace(input_str))

def remove_number(text):
    result = re.sub(r'\d+', '', text)
    return result

input_str = "There are 3 balls in this bag, and 12 in the other one."
print(remove_number(input_str))