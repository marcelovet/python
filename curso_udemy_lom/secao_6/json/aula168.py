# json.dump e json.load com strings + typing.TypedDict
import json
# import os
from pathlib import Path

FILE_NAME = "aula168.json"
FILE_PATH = Path(__file__).parent / FILE_NAME

print(FILE_PATH)

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

movie = json.loads(string_json)
with FILE_PATH.open(mode="w", encoding="utf-8") as file:
    json.dump(movie, file, ensure_ascii=False, indent=2)

with FILE_PATH.open(mode="r", encoding="utf-8") as file:
    movie_from_json = json.load(file)

print(movie_from_json)
