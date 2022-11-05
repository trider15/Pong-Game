from bs4 import BeautifulSoup
import requests

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
movie_web_page = response.text


soup = BeautifulSoup(movie_web_page, "html.parser")

movies = soup.find_all(name="h3", class_="title")

movie_rank = []
for item in movies:
    movie = item.getText()
    movie_rank.append(movie)

ascendingMovieRanking = movie_rank[::-1]
print(ascendingMovieRanking)

with open("movies.txt", mode="w") as file:
    for title in ascendingMovieRanking:
        file.write(f"{title}\n")

