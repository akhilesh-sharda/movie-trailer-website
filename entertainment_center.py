#import python libraries that are going to be used.

import fresh_tomatoes
import media
import urllib


#object of movies and add required names, storyline, posters and trailers.

toy_story = media.Movie("toy story",
 						"a story of a boy and his toys that come to life",
 						"toy_story.jpg",
 						"https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar",
					"a marine on an alien planet", 
					"Avatar-Teaser-Poster.jpg",
					"https://www.youtube.com/watch?v=5PSNL1qE6VY")

poc =  media.Movie("pirates of the carribean: the curse of the black pearl",
				   "Will teams up with pirate Jack Sparrow to save his love.",
				   "Pirates_of_the_Caribbean_movie.jpg",
				   "https://www.youtube.com/watch?v=naQr0uTrH_s")

sev_pounds = media.Movie("Seven pounds",
							"IRS agent changes lives of seven people", 
							"Seven_Pounds_poster.jpg",
							"https://www.youtube.com/watch?v=5PSNL1qE6VY")

nbd = media.Movie("Never Back Down",
				  "new guy fights for his family and friends", 
				  "Never_back_down.jpg",
				  "https://www.youtube.com/watch?v=s8aGqjNM0k4")

warrior = media.Movie("Warrior",
					  "two brothers fight for glory", 
					  "Warrior_Poster.jpg",
					  "https://www.youtube.com/watch?v=I5kzcwcQA1Q")

#add all objects of movies to an array of movies.

movies = [toy_story, avatar, poc, sev_pounds,nbd, warrior]
fresh_tomatoes.open_movies_page(movies)

#link to fresh_tomatoes to open html page and use the movies from array.