#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


# readlines() itu balikin list nama di invited_names.txt
# jadi masing-masing nama bisa dipanggil pakai loop
with open("day024_snakegame-v2_mailmerge/mail-merge/Input/Names/invited_names.txt") as file:
    daftar_tamu = file.readlines()
    for i in range(len(daftar_tamu)):
        daftar_tamu[i] = daftar_tamu[i].strip("\n")

# print(daftar_tamu) 
# buat ngetes aja

# ini kita read dan masukin starting_letter.txt ke variabel template, biar bisa dimodif [name] nya pakai replace() ntar
with open("day024_snakegame-v2_mailmerge/mail-merge/Input/Letters/starting_letter.txt") as file:
    template = file.read()

# print(template)
# buat ngetes aja

for nama in daftar_tamu:
    # pakai replace() buat nge-replace [name] di template dari starting_letter.txt
    undangan = template.replace("[name]", nama)

    # bikin file baru, manfaatin penamaan file pakai f string, 
    # lalu isi undangannya sama template yang udah direplace [name] nya barusan
    with open(f"day024_snakegame-v2_mailmerge/mail-merge/Output/ReadyToSend/letter_for_{nama}.txt", mode='w') as undangan_baru:
        undangan_baru.write(undangan)
