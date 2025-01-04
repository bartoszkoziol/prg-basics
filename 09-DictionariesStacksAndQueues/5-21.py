import json

fav_movie={
    "title": "The Matrix",
    "genre": "Sci-fi",
    "director": "Wachowski Brothers",
    "release_year": 1999,
    "rating": 8.7

}

file_name = "favourite.json" 

with open(file_name, 'w') as file:
    json.dump(fav_movie, file, indent=4)

print(f"Data has been written to {file_name}")