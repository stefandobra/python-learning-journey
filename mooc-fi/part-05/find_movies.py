def find_movies(database: list, search_term: str):
    new_list = []
    for movie in database:
        if search_term.lower() in movie["name"].lower():
            new_list.append(movie)

    return new_list

