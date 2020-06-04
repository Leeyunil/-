from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta 

movie=db.movies.find_one({"title":"매트릭스"})
movie_star = movie["star"]
print(movie_star)

same_star_movies = list(db.movies.find({'star':movie_star}))
for same_star_movie in same_star_movies:
    print(same_star_movie['title'])

db.movies.update_many({'star':movie_star},{ '$set': {"star":0}})