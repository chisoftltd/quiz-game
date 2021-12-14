
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for text in question_data:
    new_question = Question(text['color'], text['value'])
    question_bank.append(new_question)
#
# for i in range(0, len(question_data)-1):
#     print(question_bank[i].answer)
#     print(question_bank[i].text)

quiz = QuizBrain(question_bank)


while quiz.still_has_questions():
    quiz.next_question()

print("You have completed the Quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")


