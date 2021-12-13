class Question:

    def __init__(self, q_text, q_answer):
        self.text = q_text
        self.answer = q_answer


new_q = Question("3+2=5", "True")
print(f"{new_q.text} and {new_q.answer}")