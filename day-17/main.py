from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = list(map(lambda item: Question(item['text'], item['answer']), question_data))

quiz_brain = QuizBrain(question_bank)

while quiz_brain.still_has_questions():
    quiz_brain.next_question()

print("\nYou've complete the Quiz")
print(f"Your score is {quiz_brain.score} out of {len(question_bank)}")
