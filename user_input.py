#Import from 
from media import Movie
import fresh_tomatos
import apiRequest

class User_Input_Class():

	# Gives short explinantion on how to input movie ID's to user
	print('Film ID\'s can be found \"www.themoviedb.org\", To exit type any string')

	movie_id = 862 # set up movie ID variable 
	movie_json = "" # set up json variable

	is_true = True

	movie_list = [] # list of Movies

	def RepresentsInt(s): # Function to check if input is an int
		try:
			int(s)
			return True
		except ValueError:
			return False

	while is_true == True: # loop to continue while user still inputs movie id's

		movie_id = raw_input('Please Enter ID ') # user input of movie id

		is_true = RepresentsInt(movie_id) # calls the functuion to check if user inputs
												# was an int

		if is_true == False: # will break from loop if user didnt input an int
			break

		movie_json = apiRequest.Movie_API(movie_id) # calls to the api module, creating a
														# variable with json file

		# calls to the Movie class in media.py the arguments are fed from the api module

		movie_media = Movie(movie_json.movie["original_title"],
		                    movie_json.movie["overview"],
		                    movie_json.IMG_URL + movie_json.movie["poster_path"],
		                    "https://www.youtube.com/watch?v=m8e-FF8MsqU")
			
		movie_list.append(movie_media) # adds each movie to a list
