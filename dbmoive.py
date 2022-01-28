from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@cluster0.7tst7.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta

moive = db.movies.find_one({'title':'가버나움'})
star = moive['star']

all_movies = list(db.movies.find({'star':star},{'_id':False}))

for m in all_movies:
    print(m)