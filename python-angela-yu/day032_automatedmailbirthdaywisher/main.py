##################### Extra Hard Starting Project ######################
import pandas as pd
import datetime as dt
import random
import smtplib

my_email = "dari@gmail.com"
password = "tg4w5ujw4r5jnrt"

# 1. Update the birthdays.csv
data = pd.read_csv("day032_automatedmailbirthdaywisher/birthdays.csv")
data_ultah = data.to_dict(orient="records")
print(data_ultah)

# 2. Check if today matches a birthday in the birthdays.csv
sekarang = dt.datetime.now()
tanggal_hari_ini = sekarang.day
bulan_ini = sekarang.month

print(sekarang)
print(tanggal_hari_ini)
print(bulan_ini)


letter_1 = "day032_automatedmailbirthdaywisher/letter_templates/letter_1.txt"
letter_2 = "day032_automatedmailbirthdaywisher/letter_templates/letter_2.txt"
letter_3 = "day032_automatedmailbirthdaywisher/letter_templates/letter_3.txt"
letter = [letter_1, letter_2, letter_3]

comot_surat = random.choice(letter)

for i in range(len(data_ultah)):
    if tanggal_hari_ini == data_ultah[i]["day"] and bulan_ini == data_ultah[i]["month"]:
    # 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
        with open(comot_surat) as file:
            template = file.read()
            surat_ucapan = template.replace("[NAME]", data_ultah[i]["name"])
            print(surat_ucapan)
# 4. Send the letter generated in step 3 to that person's email address.
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=data_ultah[i]["email"],
                msg=f"Subject: Happy Birthday!\n\n{surat_ucapan}"
            )


