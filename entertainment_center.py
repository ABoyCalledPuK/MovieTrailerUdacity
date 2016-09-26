import user_input
import fresh_tomatos

# gets the movie list
user_input_list = user_input.User_Input_Class

# Gives short explinantion on how to input movie ID's to user
print('Film ID\'s can be found \"www.themoviedb.org\", To exit type any string')

fresh_tomatos.open_movies_page(user_input_list.movie_list) 

