from bs4 import BeautifulSoup
import requests

url = "https://www.empireonline.com/movies/features/best-movies-2/"
response = requests.get(url).text
soup = BeautifulSoup(response, 'html.parser')

all_movies = []
[all_movies.append(item.get('alt')) for item in soup.select('.lazyLoad img') if (item.get('alt')) != '']
all_movies.pop(0)
all_movies.reverse()
numbered_movies = []

num = 1
for entry in all_movies:
    numbered_movies.append(f'{num}) {entry}')
    num += 1

print(numbered_movies)

with open("movies.txt", mode="w") as file:
    for movie in numbered_movies:
        file.write(f"{movie}\n")
