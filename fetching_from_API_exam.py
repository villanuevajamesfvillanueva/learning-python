import requests_with_caching
import json

def get_movies_from_tastedive(query):
    baseURL = "https://tastedive.com/api/similar"
    params_dict = {}
    params_dict["q"] = query
    params_dict["type"] = "movies"
    params_dict["limit"] = "5"
    tastediveResponse = requests_with_caching.get(baseURL, params = params_dict)
    py_data = tastediveResponse.json()
    return py_data
    
def extract_movie_titles(dictionary):    #fix this to get results from get_movies_from_tastedive automatically
    suggestions = []
    hold = get_movies_from_tastedive(dictionary)
    for keys in hold["Similar"]["Results"]:
        suggestions.append(keys["Name"])
    return suggestions    #list

def get_related_titles(lst):
    suggs = []
    for item in lst:
        hold = extract_movie_titles(item) #hold for checking duplicates
        for i in hold:
            if i not in suggs:
                suggs.append(i)
    return suggs #returns list

def get_movie_data(movie):
    baseURL = "http://www.omdbapi.com/"
    parameters = {"t": movie, "r": "json"}
    movie_info = requests_with_caching.get(baseURL, params = parameters) #returns a response object
    #print(movie_info.url)
    return movie_info.json() #returns a dictionary
    

def get_movie_rating(dictionary):
    ratings = dictionary["Ratings"]
    for i in ratings:
        if i["Source"] == "Rotten Tomatoes":
            RT_score = i["Value"][:-1]
            RT_score = int(RT_score)
            break
        else:
            RT_score = 0
    return RT_score


def get_sorted_recommendations(lst):
    related = get_related_titles(lst)
    movie_with_rating = {}
    for i in related:
        rating = get_movie_rating(get_movie_data(i))
        movie_with_rating[i] = rating
    return sorted(movie_with_rating, key = lambda movie: (movie_with_rating[movie], movie), reverse = True) #sorted list

get_sorted_recommendations(["Bridesmaids", "Sherlock Holmes"])