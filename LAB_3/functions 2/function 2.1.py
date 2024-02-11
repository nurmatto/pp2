movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
}
         ]
def score_checker(movies):
	return movies['imdb']>5.5
for movie in movies:
	print(score_checker(movie))