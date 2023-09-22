import smtplib
import random
my_gmail = "shinozski@gmail.com"
gmail_pass = "ixnkexhjukqnbxpo"
my_yahoo = "feu_yishin24@yahoo.com"
yahoo_pass = "lnphgvyehgkfutwx"
# #"smtp.gmail.com"
# # "smtp.mail.yahoo.com"
# with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
#     connection.starttls()
#     connection.login(user=my_yahoo, password=yahoo_pass)
#     connection.sendmail(from_addr=my_yahoo, to_addrs=my_gmail,
#                         msg="Subject: Hello\n\nHey how are you?")

import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
today = now.weekday()
if today == 0:
    with open("quotes.txt") as data:
        data = data.readlines()
        quote = random.choice(data)
    print(quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(my_gmail, gmail_pass)
        connection.sendmail(from_addr=my_gmail, to_addrs=my_gmail,
                            msg=f"Subject:Quote for today.\n\n{quote}"
                            )




# date_of_birth = dt.datetime(year=2020, month=12, day=12, hour=0)
# print(date_of_birth)


