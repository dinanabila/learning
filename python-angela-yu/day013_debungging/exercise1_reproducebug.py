# belajar reproducing bug

# tujuannya: buat ngelabelin bug, dan membasminya

from random import randint

dice_images = ["⚀", "⚁", "⚂", "⚃", "⚄", "⚅"]
dice_num = randint(1, 6) # --> ini harusnya 0, 5. kan index list mulainya dari 0
print(dice_images[dice_num])
