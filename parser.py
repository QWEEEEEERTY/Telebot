from requests import *
from bs4 import BeautifulSoup

r = get("https://nukadeti.ru/skazki/luchshie?ysclid=lbjaqdmtry566131927")
html = BeautifulSoup(r.content, "html.parser")
data = html.tbody.find_all("tr")

story = []
for i in data:
    story.append({"name": i.a.text,
                  "link": i.a["href"],
                  "category": i.span.text})

for i in story:
    print(i["link"])
    temp_html = BeautifulSoup(get("https://nukadeti.ru" + i["link"]).content, "html.parser")
    i["text"] = (temp_html.p.text if temp_html.p is not None else "None")


