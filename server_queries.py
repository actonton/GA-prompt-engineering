import json
import random
import requests
from server import SERVER_ENDPOINT

def parse_query(query: str):
    return query.split()


# def test_query_server(initial_words, target_score):
#     response = requests.post(SERVER_ENDPOINT + '/prompt', json={"initial_words": parse_query(initial_words),"target_score": target_score})
#     print(response.json())

def random_genre():
    genres = [
    "Action",
    "Adventure",
    "Comedy",
    "Drama",
    "Horror",
    "Science Fiction (Sci-Fi)",
    "Fantasy",
    "Mystery",
    "Thriller",
    "Crime",
    "Romance",
    "Musical",
    "Historical",
    "Biography",
    "War",
    "Western",
    "Animation",
    "Family",
    "Documentary",
    "Experimental/Art House",
    "Mockumentary",
    "Sports",
    "Superhero",
    "Political",
    "Romantic Comedy (Rom-Com)"
]
    return genres[random.randint(0, len(genres) - 1)]


def query_server(initial_words, genre):
    if genre == "":
        genre = random_genre()

    return requests.post(SERVER_ENDPOINT + '/prompt', json={"initial_words": parse_query(initial_words)})

print(query_server("happy joyful","").json())