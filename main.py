
from question_model import Question
from data import question_data

question_bank = []
for text in question_data:
    new_question = Question(text['text'], text['answer'])
    question_bank.append(new_question)

print(question_bank[0].answer)
print(question_bank[0].text)