import smtplib
import datetime as dt
import random


sekarang = dt.datetime.now()
hari = sekarang.weekday()
if hari == 3: # 3 karena sekarang hari rabu, biar langsung bisa dites dan ga usah nunggu hari senin

    with open("day032_automatedmailbirthdaywisher/monday-motivator/quotes.txt") as file:
        quotes = file.readlines() # inget, readlines buat balikin ke dalam bentuk list
        # # ===============
        # # buat ngetes aja
        # print(quotes)
        # # ===============


    quote = random.choice(quotes)
    # ===============
    # buat ngetes aja
    print(quote)
    # ===============


    # belajar kirim email pakai python
    my_email = "dari@gmail.com"
    password = "asdfasg234t6y324w"

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection: # harus tambahin port biar ga kena TimeoutError
        connection.starttls() # biar connection nya secure
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email, 
            to_addrs="untuk@gmail.com", 
            msg=f"Subject: Semangat Senin! \n\n {quote}"
        )


# # belajar datetime

# import datetime as dt

# now = dt.datetime.now()
# print(now)
# print(now.year)
# month = now.month
# day_of_week = now.weekday()
# print(day_of_week)
# date_of_birth = dt.datetime(year=1940, month=12, day=3, hour=4)
# print(date_of_birth)