import time
from datetime import datetime as dt

hostsTemp = "hosts"
hostsPath = r"C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"
websiteList = ["www.facebook.com", "facebook.com", "www.twitter.com", "twitter.com"]
date = dt.now()

while True:
    currentYear = date.year
    currentMonth = date.month
    currentDay = date.day
    eightOclockAM = dt(currentYear, currentMonth, currentDay, 8)
    fourOclockPM = dt(currentYear, currentMonth, currentDay, 16)
    with open(hostsTemp, mode='r+') as file:
        if(eightOclockAM < dt.now() < fourOclockPM):
            content = file.read()
            for website in websiteList:
                if website in content:
                    pass
                else:
                    file.write(redirect + ' ' + website + '\n')
        else:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any (website in line for website in websiteList):
                    file.write(line)
            file.truncate()
    time.sleep(5)
