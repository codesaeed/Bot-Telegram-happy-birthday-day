import requests
import jdatetime

# DataBase
birthdays = open("bd.txt", "r").readlines()
birthdays = [i.strip().split(",") for i in birthdays]
#Date To Jalali 
date = str(jdatetime.datetime.now()).split()[0]

today_happy = []

for i in birthdays:
    if date[5:] == i[1]:
        today_happy.append(i[0])

name = ",".join(today_happy)
name.strip()

message = f"{date} \n \U0001F970 happy birthday day \U0001F973  \n {name}"
# Token Yor Bot Telegram
token_id = "yor token bot "
# chat_id Yor account Telegram
my_id = "yor user id telegram"

url = f"https://api.telegram.org/bot{token_id}/sendMessage?chat_id={my_id}&text={message}"
requests.get(url)
