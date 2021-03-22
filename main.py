##################### Extra Hard Starting Project ######################
import datetime
import pandas
import smtplib
import random



def letter_maker(name):
    rand = random.randint(1,3)
    with open(f"letter_templates/letter_{rand}.txt", mode="r") as letter:
        content = letter.read()
        print(name)
        new_content = content.replace("[NAME]", name)
    return new_content
    
MY_EMAIL = "programmerboi777@gmail.com"
MY_PASSWORD = "SqgH4#wp1vI%Je7"
def send_mail(to_mail, name):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=to_mail, msg=f"Subject:Happy Birthday\n\n{letter_maker(name)}")



now = datetime.datetime.now()
curr_month = now.month
curr_date = now.day
#  print(curr_month,curr_date)
data = pandas.read_csv("birthdays.csv")
#  print(data["month"])

dictdata = data.to_dict(orient="records")

for dictionary in dictdata:
    bd_month = dictionary["month"]
    bd_date = dictionary["day"]
    print(f"{bd_month} {bd_date}")
    if bd_date == curr_date and bd_month == curr_month:
        send_mail(dictionary["email"], dictionary["name"])
        print("success")

print(dictdata)



