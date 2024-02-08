import json
from bs4 import BeautifulSoup

with open("x.html", "r", encoding="utf-8") as f:
    html = f.read()

soup = BeautifulSoup(html, "html.parser")

divs_answer = soup.find_all("div")

answers = []


for elem in soup.find_all("p"):
    elem_text = elem.get_text()
    if "sentiment" in elem_text:
        print(elem_text)

# print(divs_answer)

    

