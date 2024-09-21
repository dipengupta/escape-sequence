from django.db import models
from django.db.models.signals import post_delete, pre_save
from django.dispatch import receiver
import os

from django.core.files.base import ContentFile
from PIL import Image
import io

'''
The following follows a simple one-to-many DB scheme
(i.e, one movie can have many reviews) 

Points to note:

 * One class may have only one post entry per Primary Key
 * def __str__(self): will return the string that will be seen in Django's Admin Form
 * class Meta: will be what the model shows up as in Django Admin
 * By default, deleting a Model's Object does not delete the uploaded files. Added code to take care of that.
'''









'''
This serves the sole purpose to just have movies in-line to review. This is not related to any table.
'''
class UpcomingReviews(models.Model):
    movieTitle = models.CharField(max_length=300)
    releaseYear = models.IntegerField()
    moviePoster = models.ImageField(upload_to='movies/upcoming', default='movies/posters/defaultPoster.jpg')

    def __str__(self):
        return self.movieTitle

    class Meta:
        verbose_name_plural = "Upcoming Reviews"






'''
This is the main "table" where data for movies will be stored

IMP: 
    - here, "movieGenres" and "movieMoods" are essentially meant to act as tags that we can filter the movie out by later on.
    - these can have multiple values, always put the new one on the next line, and use '-' instead of spaces

    Eg:

    movieGenres:
    [
        comedy
        coming-of-age
    ]
'''
def upload_to(instance, filename):
    ext = filename.split('.')[-1]  # Get file extension
    filename = f"{instance.pk}_{instance.movieTitle}.{ext}"  # Create new filename
    return os.path.join('movies/posters', filename)

class AllMovies(models.Model):
    movieTitle = models.CharField(max_length=300)
    releaseYear = models.IntegerField()
    moviePoster = models.ImageField(upload_to=upload_to, default='movies/posters/defaultPoster.jpg')
# 	moviePoster = models.ImageField(upload_to='movies/posters', default='movies/posters/defaultPoster.jpg')
    movieSummary = models.TextField()
    movieGenres = models.TextField()
    movieMoods = models.TextField(blank=True)
    movieAgeRating = models.TextField(blank=True)
    movieDirectors = models.TextField(blank=True)
    movieActors = models.TextField(blank=True)

    # def save(self, *args, **kwargs):
    #     # Save the instance first to ensure the primary key is set
    #     if not self.pk:
    #         super().save(*args, **kwargs)
    #     # Update the file name with the primary key
    #     self.moviePoster.name = upload_to(self, self.moviePoster.name)
    #     # Save the instance again to apply the new file name
    #     super().save(*args, **kwargs)


    def save(self, *args, **kwargs):
        if not self.pk:
            super().save(*args, **kwargs)
        
        if self.moviePoster:
            self.resize_image()
        
        self.moviePoster.name = upload_to(self, self.moviePoster.name)
        super().save(*args, **kwargs)

    def resize_image(self):
        img = Image.open(self.moviePoster)
        target_size = (600, 900)
        
        # Calculate the aspect ratio
        aspect_ratio = img.width / img.height
        target_ratio = target_size[0] / target_size[1]

        if aspect_ratio > target_ratio:
            # Image is wider, scale based on width
            new_size = (target_size[0], int(target_size[0] / aspect_ratio))
        else:
            # Image is taller, scale based on height
            new_size = (int(target_size[1] * aspect_ratio), target_size[1])

        # Resize the image, upscaling if necessary
        img = img.resize(new_size, Image.LANCZOS)

        # If the image is smaller than the target, create a new image with padding
        if new_size[0] < target_size[0] or new_size[1] < target_size[1]:
            background = Image.new('RGB', target_size, (0, 0, 0))  # Black background
            offset = ((target_size[0] - new_size[0]) // 2, (target_size[1] - new_size[1]) // 2)
            background.paste(img, offset)
            img = background

        img_io = io.BytesIO()
        img.save(img_io, format='JPEG', quality=85)
        self.moviePoster.save(self.moviePoster.name, ContentFile(img_io.getvalue()), save=False)



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



    def getMovieMoods(self):
        return self.movieMoods



    def getMovieGenres(self):
        return self.movieGenres






""" 
Whenever ANY model is deleted, if it has a file field on it, delete the associated file too
"""
@receiver(post_delete)
def delete_files_when_row_deleted_from_db(sender, instance, **kwargs):
    for field in sender._meta.concrete_fields:
        if isinstance(field,models.ImageField):
            instance_file_field = getattr(instance,field.name)
            delete_file_if_unused(sender,instance,field,instance_file_field)
            


""" 
Delete the file if something else get uploaded in its place
"""
@receiver(pre_save)
def delete_files_when_file_changed(sender,instance, **kwargs):
    # Don't run on initial save
    if not instance.pk:
        return
    for field in sender._meta.concrete_fields:
        if isinstance(field,models.ImageField):
            #its got a file field. Let's see if it changed
            try:
                instance_in_db = sender.objects.get(pk=instance.pk)
            except sender.DoesNotExist:
                # We are probably in a transaction and the PK is just temporary
                # Don't worry about deleting attachments if they aren't actually saved yet.
                return
            instance_in_db_file_field = getattr(instance_in_db,field.name)
            instance_file_field = getattr(instance,field.name)
            if instance_in_db_file_field.name != instance_file_field.name:
                delete_file_if_unused(sender,instance,field,instance_in_db_file_field)



""" 
Only delete the file if no other instances of that model are using it
"""    
def delete_file_if_unused(model,instance,field,instance_file_field):
    dynamic_field = {}
    dynamic_field[field.name] = instance_file_field.name
    other_refs_exist = model.objects.filter(**dynamic_field).exclude(pk=instance.pk).exists()
    if not other_refs_exist:
        instance_file_field.delete(False)





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