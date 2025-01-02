# tujuan: ambil nama dari list friends secara random

import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
jumlah_orang = len(friends)

random_numbers = random.randint(0, jumlah_orang - 1)

# belum belajar loop
# jadi pakai if else dulu
print("cara paling bertele-tele")
if random_numbers == 0:
    print(friends[0])
elif random_numbers == 1:
    print(friends[1])
elif random_numbers == 2:
    print(friends[2])
elif random_numbers == 3:
    print(friends[3])
else:
    print(friends[4])

print("\ncara ga terlalu bertele-tele")
print(friends[random_numbers])

# Ternyata bener bisa pakai yang seq itu, dari dokumentasi module random
# lebih simpel, cuma 1 line aja jadi
print("\ncara simpel")
print(random.choice(friends))
