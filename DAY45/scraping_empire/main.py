from bs4 import BeautifulSoup
from requests import get


html_response = get('https://www.empireonline.com/movies/features/best-movies-2/').text


soup = BeautifulSoup(html_response, 'html.parser')
names = soup.find_all(name="h3", class_="title")


movie_list = []
for item in names:
    movie_list.append(item.text.strip())


print(movie_list)
