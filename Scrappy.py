from inspect import classify_class_attrs
from bs4 import BeautifulSoup
import requests
import time

html_text = requests.get("https://news.google.com/topstories?hl=en-IN&gl=IN&ceid=IN:en").text

soup = BeautifulSoup(html_text, "lxml")

header = soup.find("div", class_="cp7Yvc").h2.span.text
mains = soup.find_all("div", class_= "DBQmFf NclIid BL5WZb Oc0wGc xP6mwf j7vNaf")

for main in mains:
    print(f"\n{header}")
    title = main.find("h3", class_="ipQwMb ekueJc RD0gLb")
    print(f"Title:  {title.text}")
    headlines = main.find_all("h4", class_="ipQwMb ekueJc RD0gLb")
    for headline in headlines:
        print(f"-------{headline.text}")
        print(f"link: {headline.a['href']}")



# titles = soup.find_all("h3")
# # # heads = soup.find_all("h4")

# for titles in titles:
#     print(titles.text)

# for head in heads:
#     print(head.text)

# for main in mains:
#     print(header)
    # head = main.find("h4",class_="ipQwMb ekueJc RD0gLb").a.text
    # titles = main.find_all("h4",class_="ipQwMb ekueJc RD0gLb")
    # print(head)
    # for title in titles:
    #     print(title.text)
    





