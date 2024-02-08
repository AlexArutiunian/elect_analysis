import json
from bs4 import BeautifulSoup
import os

def select_answer_from_html(file_name):

	with open(file_name, "r", encoding="utf-8") as f:
		html = f.read()

	soup = BeautifulSoup(html, "html.parser")

	divs_answer = soup.find_all("div")

	answers = []

	for elem in soup.find_all("p"):
		elem_text = elem.get_text()
		if "sentiment" in elem_text:
		    print(elem_text)
    return answers
    
path = "htmls"    
jsons_path = "bunchs"    
    
for file_ in os.listdir(path):
    answers = select_answer_from_html(path + "/" + file_)
    with open(json_path + "/" + file_.replace(".html", ".json"), "r", encoding="utf-8") as fp:
        data = json.load(fp)
    data["sentiment_claim"] = answer[0]
    data["sentiment_evidence"] = answer[1]
    with open(json_path + "/" + file_.replace(".html", ".json"), "w", encoding="utf-8") as fp:
        json.dump(data, fp, indent=2)
            		    

# print(divs_answer)

    

