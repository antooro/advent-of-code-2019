import requests
import os
from datetime import date
import browser_cookie3
import sys

cj = browser_cookie3.firefox()
if not ("advent" in str(cj)):
    cj = browser_cookie3.chrome()
    

day_today = date.today().strftime("%d").lstrip("0")

if len(sys.argv) > 1:
    day = int(sys.argv[1])
    if day<0 or day>31 or day>int(day_today):
        exit("Day is not valid")
else:
    day = day_today


print(f"Initializing day {day}")
exit()
if not os.path.exists(f"day{day}"):
    os.mkdir(f"day{day}")
    os.chdir(f"day{day}")
    r = requests.get(f"https://adventofcode.com/2019/day/{day}/input", cookies = cj)
    with open(f"input{day}","w") as f:
        f.write(r.text)


