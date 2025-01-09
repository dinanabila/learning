from question_model import Question
from data2 import data_soal
from quiz_brain import QuizBrain

bank_soal = []

for soal in data_soal:
    bank_soal.append(Question(soal["question"], soal["correct_answer"]))

quiz = QuizBrain(bank_soal)

while quiz.soal_masih_ada():
    quiz.soal_selanjutnya()

print("Quiz udah selesai!")
print(f"Skor akhir kamu: {quiz.score}/{quiz.question_number}")

