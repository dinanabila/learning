from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

bank_soal = []
# ==========
# VERSI ACUU 
# ==========
# # bikin loop for buat nge-loop question_data di data.py
# for i in range(0, len(question_data)):

# # bikin object soal untuk setiap entri di question_data
#     bank_soal.append(Question(question_data[i]["text"], question_data[i]["answer"]))

# # append setiap object soal ke dalam list bank_soal
# ==============
# END VERSI ACUU 
# ==============


# ========
# ANGELA's
# ========

for soal in question_data:
    bank_soal.append(Question(soal["text"], soal["answer"]))

# ============
# END ANGELA's
# ============

quiz = QuizBrain(bank_soal)

while quiz.soal_masih_ada():
    quiz.soal_selanjutnya()

print("Quiz udah selesai!")
print(f"Skor akhir kamu: {quiz.score}/{quiz.question_number}")

# =====
# DEBUG
# =====
# print(len(bank_soal))
# print(bank_soal[0].soal)

