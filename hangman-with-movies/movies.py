import csv
import re

# Data from:
# https://www.kaggle.com/tmdb/tmdb-movie-metadata/version/2
#

def get_movies():
    DESCRIPTION_MAX = 40
    movies = []
    
    with open ('movie_info.csv', encoding="utf8", errors='ignore') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=",")
        
        for row in csv_reader:
            movie = row[0].lower()
            
            if not re.match("[0-9]", movie):
                movie = re.sub("[^a-z ]", "", movie)
            
                movies.append(
                    (movie, format_string(row[1], DESCRIPTION_MAX), row[2]))
            
    return movies

def get_practice_movies():
    return [('jaws', 'A big shark eats stuff', 1975),
            ('the empire strikes back', 'Luke, I am your father', 1980),
            ('indiana Jjones', 'What professor lives are really like', 1981)]

def format_string(description, max_count):
    formatted = ""
    count = 0
    
    for word in description.split(" "):
        formatted += word + " "
        count += len(word) + 1
        
        if count >= max_count:
            formatted = formatted[0:-1] + "\n"
            count = 0
            
    return formatted[0:-1]
        
        