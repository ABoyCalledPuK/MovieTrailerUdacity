from media import Movie
import fresh_tomatos

clockwork_orange = Movie("clockwork orange", 
						"dystopian world",
						"http://retromovieposter.com/wp-content/uploads/2015/03/1971-A-Clockwork-Orange.jpg",
						"https://www.youtube.com/watch?v=SPRzm8ibDQ8")

resident_evil = Movie("Resident Evil",
						"Zombies",
						"https://cinefilles.files.wordpress.com/2013/04/resident-evil-poster.jpg",
						"https://www.youtube.com/watch?v=u6uDnd_v5Bw")

matrix = Movie("The Matrix",
				"Robots",
				"http://moviefiles.alphacoders.com/288/poster-28.jpg",
				"https://www.youtube.com/watch?v=m8e-FF8MsqU")

movie_list = [clockwork_orange, resident_evil, matrix]

fresh_tomatos.open_movies_page(movie_list)