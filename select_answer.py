import json
from bs4 import BeautifulSoup
import os

def select_answer_from_html(file_name):
	with open(file_name, "r", encoding="utf-8") as f:
		try:
			html = f.read()
		except UnicodeDecodeError as e:
			
			with open("errors.txt", "a", encoding="utf-8") as f_er:
				f_er.write(f"UnicodeDecodeError: {e} with {file_name} \n")
			return []

	soup = BeautifulSoup(html, "html.parser")

	answers = []

	for elem in soup.find_all("p"):
		elem_text = elem.get_text()
		if "sentiment" or "Sentiment" in elem_text:
			print(elem_text)
			answers.append(elem_text)

	return answers  # вернуть ответы

path = "recov"    
jsons_path = "bunchs"    

for file_ in os.listdir(path):
    print(file_)
    if not file_.endswith(".html"):
        continue
    answers = select_answer_from_html(path + "/" + file_)
    with open(jsons_path + "/" + file_.replace(".html", ".json"), "r", encoding="utf-8") as fp:
        data = json.load(fp)

    try:        
        data["sentiment_claim"] = answers[0]
    except IndexError:
        print("IndexError")
        with open("errors.txt", "a", encoding="utf-8") as f_er:
            f_er.write("IndexError with claim in " + file_ + "\n")
        data["sentiment_claim"] = "NOTHING"
    try:        
        data["sentiment_evidence"] = answers[1]
    except IndexError:
        print("IndexError")
        with open("errors.txt", "a", encoding="utf-8") as f_er:
            f_er.write("IndexError with evidence in " + file_ + "\n")
        data["sentiment_evidence"] = "NOTHING" 
    with open(jsons_path + "/" + file_.replace(".html", ".json"), "w", encoding="utf-8") as fp:
        json.dump(data, fp, indent=2)