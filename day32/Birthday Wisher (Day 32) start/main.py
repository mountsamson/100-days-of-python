# import smtplib

# my_email ="carl.francis.samson@gmail.com"
# password= "xifvjcwdzfimbxnq"

# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email, 
#         to_addrs="napa_4@live.com", 
#         msg="Subject:Hello\n\nThis is the body of my email"
#         )

# import datetime as dt

# now = dt.datetime.now()
# year = now.year
# month = now.month
# day_of_week = now.weekday()
   
# print(day_of_week)

# date_of_birth = dt.datetime(year=1995, month=5, day=4, hour=5)
# print(date_of_birth)

import smtplib
import datetime as dt
import random

MY_EMAIL = "carl.francis.samson@gmail.com"
MY_PASSWORD = "xifvjcwdzfimbxnq"

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 0:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)
        
    print(quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:Monday Motivation\n\n{quote}"
        )

        
        
    