from bs4 import BeautifulSoup
from requests import get

# get api of hacker news
response = get('https://news.ycombinator.com/news').text


# create a buts object
soup = BeautifulSoup(response, "html.parser")
all_articles = soup.find_all(name= "a", class_="titlelink")
all_scores = soup.find_all(name="span", class_="score")



links = []
titles = []

for article in all_articles:
    links.append(article.get("href"))
    titles.append(article.text.strip())

score_list = []
for score in all_scores:
    single_score = int(score.text.strip().split(" ")[0])
    score_list.append(single_score)
    
    
max_score_index = score_list.index(max(score_list))
print(links, len(links))
print(titles, len(titles))
print((score_list), len(score_list))
