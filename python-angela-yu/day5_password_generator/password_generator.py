#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

# pakai concat str ga sih? cobain:
letter = ""
symbol = ""
number = ""

for i in range(0, nr_letters):
    random_letter = random.choice(letters)
    letter += random_letter # ternyata + concat bisa += juga (baru tau)

for i in range(0, nr_symbols):
    random_symbol = random.choice(symbols)
    symbol += random_symbol

for i in range(0, nr_numbers):
    random_number = random.choice(numbers)
    number += random_number

print("\npassword lemah: ")
print(letter + symbol + number)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

# gimana cara randomin posisinya ya?
# disatuin aja ga sih 3 list di atas itu?

# eh, atau, jadiin list aja itu si hasil terakhir tadi
# coba = list(letter + symbol + number)
# print(coba)
# ternyata outputnya beneran jadi list yang isinya masing-masing char str
# tapi gimana ngerandomin posisi nya aku belum kebayang kalau udah gitu

# OH! HAPUS GA SIH, HAPUS ELEMENNYA KALAU UDAH MUNCUL

# pw_izi = list(letter + symbol + number)
# print(pw_izi)
# pw_hard = ""
# for karakter in pw_izi:
#     karakter = random.choice(pw_izi)
#     pw_hard += karakter
#     pw_izi.remove(karakter)
#     print(pw_izi)
#     print(pw_hard)
# print(pw_hard)

# ini juga gagal, soalnya jumlah list yang berkurang ngefek di loop for. 

# jadiiiii, searching google, bisa ga ngacak posisi elemen dalam list
# ternyata ada, pakai random.shuffle()

list_pw = list(letter + symbol + number)
random.shuffle(list_pw)

# print(str(list_pw)) ---> ga bisa ternyata langsung ubah jadi str
# harus gini dulu, based on nyari di google (datacamp):
# src: https://www.datacamp.com/tutorial/how-to-convert-a-list-to-a-string-in-python?utm_source=google&utm_medium=paid_search&utm_campaignid=19589720824&utm_adgroupid=157156376311&utm_device=c&utm_keyword=&utm_matchtype=&utm_network=g&utm_adpostion=&utm_creative=684592140434&utm_targetid=aud-1459190388940:dsa-2218886984100&utm_loc_interest_ms=&utm_loc_physical_ms=9072592&utm_content=&utm_campaign=230119_1-sea~dsa~tofu_2-b2c_3-row-p2_4-prc_5-na_6-na_7-le_8-pdsh-go_9-nb-e_10-na_11-na&gad_source=1&gclid=CjwKCAiAg8S7BhATEiwAO2-R6udO4LIVWOb4eP_TBFsU1NPjf3MjKxvecvaJ2y6kc8mCg7L5Es2CohoCp_gQAvD_BwE

delimiter = "" # define a delimiter
pw = delimiter.join(list_pw)
print("\npassword kuat: ")
print(pw, "\n")
