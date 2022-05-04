from operator import index
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


links = links[:29:]
titles = titles[:29:]

max_score = max(score_list)
max_score_index = score_list.index(max_score)



print(max_score_index)
print(score_list)
[print(i,titles[i],score_list[i]) for i in range(len(titles))]
print(F"The high score is for {titles[max_score_index]} with score {max_score}")
print(F"you can read this news with this link: {links[max_score_index]}")


# when score is 0 there is no number or related tag for 0 what should i do
