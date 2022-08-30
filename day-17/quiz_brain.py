class QuizBrain:
    def __init__(self, questions_list):
        self.questions_list = questions_list
        self.question_index = 0
        self.score = 0

    def next_question(self):
        current_question = self.questions_list[self.question_index]
        self.check_answer(input(f"Q.{self.question_index + 1} {current_question.text} (True/False)?: "))
        self.question_index += 1

    def still_has_questions(self):
        return self.question_index < len(self.questions_list)

    def check_answer(self, answer):
        if answer.lower() == self.questions_list[self.question_index].answer.lower():
            self.score += 1
