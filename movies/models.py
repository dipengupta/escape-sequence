from django.db import models
from django.conf import settings



'''

The following follows a simple one-to-many DB scheme
(i.e, one movie can have many reviews) 

Points to note:

 * One class may have only one post entry per Primary Key
 * def __str__(self): will return the string that will be seen in Django's Admin Form
 * class Meta: will be what the model shows up as in Django Admin


Things to implement:

# Change the uploaded file's name to it's PK so that it does not clutter media folder


#### incorporate the metric element of each person ####

'''



'''
This is the main "table" where data for movies will be stored
'''
class AllMovies(models.Model):
	movieTitle = models.CharField(max_length=300)
	releaseYear = models.IntegerField()
	moviePoster = models.ImageField(upload_to='movies/posters', default='movies/posters/defaultPoster.jpg')
	movieStill = models.ImageField(upload_to='movies/stills', default='movies/stills/defaultStill.jpg')
	movieSummary = models.TextField()
	movieGenre = models.TextField()
	movieAgeRating = models.TextField(blank=True)
	movieDirectors = models.TextField(blank=True)
	movieActors = models.TextField(blank=True)

	def __str__(self):
   		return self.movieTitle

	class Meta:
		verbose_name_plural = "All Movies"



'''
This is Dipen's "table", which will store reviews written by Dipen
'''
class Dipen(models.Model):

	final_verdict = (
		('thumbs_up','Thumbs Up'),
		('thumbs_down','Thumbs Down'),
	)

	post = models.OneToOneField(AllMovies, on_delete=models.CASCADE)
	reviewTitle = models.CharField(max_length=300)
	reviewBody = models.TextField()
	reviewDate = models.DateTimeField()
	verdict = models.CharField(max_length=11, choices=final_verdict, default='thumbs_up')

	def __str__(self):
		return self.reviewTitle

	class Meta:
		verbose_name_plural = "Dipen's Reviews"




'''
This is Ankur's "table", which will store reviews written by Ankur
'''
class Ankur(models.Model):

	final_verdict = (
		('thumbs_up','Thumbs Up'),
		('thumbs_down','Thumbs Down'),
	)

	post = models.OneToOneField(AllMovies, on_delete=models.CASCADE)
	reviewTitle = models.CharField(max_length=300)
	reviewBody = models.TextField()
	reviewDate = models.DateTimeField()
	verdict = models.CharField(max_length=11, choices=final_verdict, default='thumbs_up')

	def __str__(self):
		return self.reviewTitle

	class Meta:
		verbose_name_plural = "Ankur's Reviews"




'''
This is Shantnu's "table", which will store reviews written by Shantnu
'''
class Shantnu(models.Model):

	final_verdict = (
		('thumbs_up','Thumbs Up'),
		('thumbs_down','Thumbs Down'),
	)

	post = models.OneToOneField(AllMovies, on_delete=models.CASCADE)
	reviewTitle = models.CharField(max_length=300)
	reviewBody = models.TextField()
	reviewDate = models.DateTimeField()
	verdict = models.CharField(max_length=11, choices=final_verdict, default='thumbs_up')

	def __str__(self):
		return self.reviewTitle

	class Meta:
		verbose_name_plural = "Shantnu's Reviews"




'''
This is Ashesh's "table", which will store reviews written by Ashesh
'''
class Ashesh(models.Model):

	final_verdict = (
		('thumbs_up','Thumbs Up'),
		('thumbs_down','Thumbs Down'),
	)

	post = models.OneToOneField(AllMovies, on_delete=models.CASCADE)
	reviewTitle = models.CharField(max_length=300)
	reviewBody = models.TextField()
	reviewDate = models.DateTimeField()
	verdict = models.CharField(max_length=11, choices=final_verdict, default='thumbs_up')

	def __str__(self):
		return self.reviewTitle

	class Meta:
		verbose_name_plural = "Ashesh's Reviews"




'''
This is Jayant's "table", which will store reviews written by Jayant
'''
class Jayant(models.Model):

	final_verdict = (
		('thumbs_up','Thumbs Up'),
		('thumbs_down','Thumbs Down'),
	)

	post = models.OneToOneField(AllMovies, on_delete=models.CASCADE)
	reviewTitle = models.CharField(max_length=300)
	reviewBody = models.TextField()
	reviewDate = models.DateTimeField()
	verdict = models.CharField(max_length=11, choices=final_verdict, default='thumbs_up')

	def __str__(self):
		return self.reviewTitle

	class Meta:
		verbose_name_plural = "Jayant's Reviews"