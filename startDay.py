import requests
import os
from datetime import date
import browser_cookie3

cj = browser_cookie3.firefox()
if not ("advent" in str(cj)):
    cj = browser_cookie3.chrome()
    

exit()
day = date.today().strftime("%d").lstrip("0")

print(f"Initializing day {day}")

if not os.path.exists(f"day{day}"):
    os.mkdir(f"day{day}")
    os.chdir(f"day{day}")
    r = requests.get(f"https://adventofcode.com/2019/day/{day}/input", cookies = cj)
    with open(f"input{day}","w") as f:
        f.write(r.text)


