import json
from bs4 import BeautifulSoup
import os

def select_answer_from_html(file_name):
    chars = str()
    with open(file_name, "r", encoding="utf-8") as f:
        try:
            while True:
               char = f.read(1)
               chars += char
               
               if not char:
                   break
        except UnicodeDecodeError as e:
            
            with open("errors2.txt", "a", encoding="utf-8") as f_er:
                print("UnicodeDecodeError")
                f_er.write(f"UnicodeDecodeError: {e} with {file_name} \n")
            
    html = chars
   # print(html)
    soup = BeautifulSoup(html, "html.parser")

    

    divs = soup.find("div", class_="markdown") 

    if divs == None:
        return "NOTHING"

    answers = divs.get_text()
   # print(answers)
    return answers  # вернуть ответы    

path = "new"    
jsons_path = "bunchs"    

for file_ in os.listdir(path):
    print(file_)
    if not file_.endswith(".html"):
        continue
    answers = select_answer_from_html(path + "/" + file_)
    with open(jsons_path + "/" + file_.replace(".html", ".json"), "r", encoding="utf-8") as fp:
        data = json.load(fp)
    data["sentiment_claim"] = answers   
    data["sentiment_answer"] = answers 

    checking_ = ["sentiment", "Sentiment", "Negative", "negative", "Positive", "positive", "Mixed", "Claim", "mixed", "Neutral", "Uncertain"]
    if any(word.lower() in answers.lower() for word in checking_):
        answers = answers
    else:
        answers = "NOTHING"    

    print(answers)
    with open(jsons_path + "/" + file_.replace(".html", ".json"), "w", encoding="utf-8") as fp:
        json.dump(data, fp, indent=2)