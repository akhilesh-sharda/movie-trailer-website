import webbrowser

#passing details like title, story, poster and trailer using objects.

class Movie():
	def __init__(self, title, story, poster, trailer):
		self.title = title
		self.storyline = story
		self.poster_image_url = poster
		self.trailer_youtube_url = trailer

#using open function from python library webbrowser.

	def show_trailer(self):
		webbrowser.open(self.trailer)
