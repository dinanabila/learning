student_score = [180, 124, 165, 173, 189, 169, 146]

# tujuan: bikin loop buat ngambil nilai maks dari list student_score
# max_score = 0
# for i in range(0, len(student_score) - 1): 
#     if student_score[i] > student_score[i+1]:
#         max_score = student_score[i]

# print(max_score)
# ini gagal, coba cara lain

max_score = 0
for score in student_score:
    if score > max_score:
        max_score = score

print(max_score)

# ah, yang sebelumnya gagal, harusnya gini:
# max_score = 0
# for i in range(0, len(student_score)): 
#     if student_score[i] > max_score:
#         max_score = student_score[i]

# print(max_score)
