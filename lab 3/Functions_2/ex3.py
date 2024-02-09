from dictionary_of_movies import movies
def Category(film):
    for movie in movies:
        if movie['category'] == film:
            print(movie['name'])

film = input()
Category(film)