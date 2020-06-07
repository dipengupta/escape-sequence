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


'''




'''
This serves the sole purpose to just have movies in-line to review. This is not related to any table.
'''
class UpcomingReviews(models.Model):
	movieTitle = models.CharField(max_length=300)
	releaseYear = models.IntegerField()
	moviePoster = models.ImageField(upload_to='movies/upcoming', default='movies/posters/defaultPoster.jpg')
	movieSummary = models.TextField(blank=True)
	movieGenre = models.TextField()
	movieAgeRating = models.TextField(blank=True)
	movieDirectors = models.TextField(blank=True)
	movieActors = models.TextField(blank=True)

	def __str__(self):
   		return self.movieTitle

	class Meta:
		verbose_name_plural = "Upcoming Reviews"






'''
This is the main "table" where data for movies will be stored
'''
class AllMovies(models.Model):
	movieTitle = models.CharField(max_length=300)
	releaseYear = models.IntegerField()
	moviePoster = models.ImageField(upload_to='movies/posters', default='movies/posters/defaultPoster.jpg')
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

	So, the idea behind this function is to get the data for who all gave it a "Thumbs Up".
	This is quite a crude solution to a problem that should not exist in a good DB design, but hey, it works

	Future improvement: right now, it will query for the same data over and over. We should have it run once and store it in the DB.


	returns: dictionary with total likes and the int "1" which signifies that the person gave it a thumbs up
	
	IMP: the critera for comparison should be that "None" will be returned if the person gave it a thumbs down  
	'''
	def getOverallRating(self):

		totalLikes = 0
		like_ankur = None
		like_dipen = None
		like_ashesh = None
		like_shantnu = None
		like_jayant = None

		primKey = self.id 


		try:
			movie_post = AllMovies.objects.get(id=primKey)
		except:
			movie_post = None


		try:
			ankur_post = Ankur.objects.get(post=primKey)
			if ankur_post.verdict == 'thumbs_up':
				totalLikes+=1
				like_ankur = 1
		except:
			ankur_post = None


		try:
			dipen_post = Dipen.objects.get(post=primKey)
			if dipen_post.verdict == 'thumbs_up':
				totalLikes+=1
				like_dipen = 1        
		except:
			dipen_post = None


		try:
			shantnu_post = Shantnu.objects.get(post=primKey)
			if shantnu_post.verdict == 'thumbs_up':
				totalLikes+=1
				like_shantnu = 1
		except:
			shantnu_post = None


		try:
			ashesh_post = Ashesh.objects.get(post=primKey)
			if ashesh_post.verdict == 'thumbs_up':
				totalLikes+=1
				like_ashesh = 1   
		except:
			ashesh_post = None


		try:
			jayant_post = Jayant.objects.get(post=primKey)
			if jayant_post.verdict == 'thumbs_up':
				totalLikes+=1
				like_jayant = 1    
		except:
			jayant_post = None


		finally:

			verdictDict = {
				'totalLikes': totalLikes,
				'like_ankur' : like_ankur,
				'like_dipen' : like_dipen,
				'like_ashesh' : like_ashesh,
				'like_shantnu' : like_shantnu,
				'like_jayant' : like_jayant
			}

		return verdictDict






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