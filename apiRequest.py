import requests
from pprint import pprint

#Split api url to enable movie searches
class Movie_API():

	IMG_URL = "https://image.tmdb.org/t/p/w500"

	def __init__(self, movieID):

		self.api_movie_id = movieID
		self.API_URL = "https://api.themoviedb.org/3/movie/"
		self.API_KEY = "?api_key=8db74f4569adf8f312df969c6a59dc77"

		self.response = requests.get(self.API_URL + str(self.api_movie_id) + self.API_KEY)
		self.movie = self.response.json()

