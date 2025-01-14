student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (haiiii, value) in student_dict.items():
    # print(haiiii)
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (haiakuindex, haiakurow) in student_data_frame.iterrows():
    # print(haiakurow)
    # print(haiakurow.student)
    #Access index and row
    #Access row.student or row.score
    pass

# print(student_data_frame)

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}


# ============================
# INI PROGRAM BUAT NGEJA HURUF
# ============================

# kalau ngeja nama kita ke orang, misalkan, 
# mungkin banget kalau orang itu salah denger ejaan kita
# soalnya, ada huruf yang kedengeran mirip kalau disebut
# kek, b sama d sama p kan mirip
# atau, m sama n juga mirip
# makanya kita bikin program ini
# pakai nato alphabet
# jadi, kita ngejanya bukan huruf doang
# tapi, jadi kek gini contohnya:
# 'bella', diejanya jadi:
# 'bebek', 'ember', 'lontong', 'lontong', 'awas'


#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
data_nato = pandas.read_csv("day026_nato-alphabet/nato_phonetic_alphabet.csv")
# ~~~~~~~
# TESTING
# ~~~~~~~
# for (akuindex, akurow) in data_nato.iterrows():
#     print(akurow.code)
# ~~~~~~~~~~~
# END TESTING
# ~~~~~~~~~~~

nato_dict = {akurow.letter:akurow.code for (akuindex, akurow) in data_nato.iterrows()}

# ~~~~~
# DEBUG
# ~~~~~
# print(nato_dict)
# ~~~~~~~~~
# END DEBUG
# ~~~~~~~~~

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
kata_yang_mau_dieja = input("Ketik kata yang mau dieja: ").upper()
huruf_yang_harus_dieja = [huruf for huruf in kata_yang_mau_dieja]

# ~~~~~
# DEBUG
# ~~~~~
# print(huruf_yang_harus_dieja)
# ~~~~~~~~~
# END DEBUG
# ~~~~~~~~~

# versi panjang yang biasanya:

# nato_yang_harus_dieja = []
# for huruf in huruf_yang_harus_dieja:
#     if huruf in nato_dict:
#         nato_yang_harus_dieja.append(nato_dict[huruf])


# sekarang coba bangun versi pendeknya:
nato_yang_harus_dieja = [nato_dict[huruf] for huruf in huruf_yang_harus_dieja if huruf in nato_dict]

print(f"Ini ejaan nato-nya: {nato_yang_harus_dieja}")