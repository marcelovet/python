# json.dumps e json.loads com strings + typing.TypedDict
import json
from pprint import pprint
from typing import TypedDict


class Movie(TypedDict):
    title: str
    original_title: str
    is_movie: bool
    imdb_rating: float
    year: int
    characters: str
    budget: None | float


string_json = """
{
  "title": "O Senhor dos Anéis: A Sociedade do Anel",
  "original_title": "The Lord of the Rings: The Fellowship of the Ring",
  "is_movie": true,
  "imdb_rating": 8.8,
  "year": 2001,
  "characters": ["Frodo", "Sam", "Gandalf", "Legolas", "Boromir"],
  "budget": null
}
"""
print(string_json)

# movie = json.loads(string_json)
# pprint(movie)
movie: Movie = json.loads(string_json)
pprint(movie)
print(movie['characters'][2])
print(movie['year'] + 10)

json_string = json.dumps(movie, ensure_ascii=False, indent=2)
print(json_string)