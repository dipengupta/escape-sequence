from django.shortcuts import render
from django.views.generic.detail import DetailView
from movies.models import AllMovies, Dipen, Ankur, Shantnu, Ashesh, Jayant
from django.db.models import Q

'''

This is essentially the one-stop function to display info and reviews for that movie

Input: Primary key of the movie (from the URL)
Returns: Dict of QuerySets with the relevent movie data

'''
def displayAllReviewsForMovie(request, primKey):

    totalLikes = 0
    like_ankur = None
    like_dipen = None
    like_ashesh = None
    like_shantnu = None
    like_jayant = None


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
        masterDict = {
            'movie_post': movie_post, 
            'ankur_post': ankur_post, 
            'dipen_post': dipen_post, 
            'shantnu_post': shantnu_post, 
            'ashesh_post': ashesh_post, 
            'jayant_post': jayant_post,
            'totalLikes': totalLikes,
            'like_ankur' : like_ankur,
            'like_dipen' : like_dipen,
            'like_ashesh' : like_ashesh,
            'like_shantnu' : like_shantnu,
            'like_jayant' : like_jayant
        }


    return render(request, 'movies/allReviewsForMovie.html', masterDict)






def displayAboutUsPage(request):
    return render(request, 'movies/aboutUs.html')






def searchMovies(request):
    if request.method == 'GET':
        query= request.GET.get('q')

        submitbutton= request.GET.get('submit')

        if query is not None:
            lookups= Q(movieTitle__icontains=query) | Q(movieGenre__icontains=query) | Q(movieDirectors__icontains=query) | Q(movieActors__icontains=query)  

            results= AllMovies.objects.filter(lookups).distinct()

            context={'results': results,
                     'submitbutton': submitbutton}

            return render(request, 'movies/searchResults.html', context)

        else:
            return render(request, 'movies/searchResults.html')

    else:
        return render(request, 'movies/searchResults.html')







'''

#Note: The below functions are essentially redundant, but can be used for a feature where 
all movie reviews written by author is needed

'''





'''
This function is to essentally pass the correct QueryObject of the movie to movieReview.html
'''
def displayAnkursReview(request, primKey):
    try:
        ankur_post = Ankur.objects.get(post=primKey)
    except:
        ankur_post = None
    finally:
        author = "Ankur"
    return render(request, 'movies/movieReview.html', {'final_post': ankur_post, 'author':author})


'''
This function is to essentally pass the correct QueryObject of the movie to movieReview.html
'''
def displayDipensReview(request, primKey):
    try:
        dipen_post = Dipen.objects.get(post=primKey)
    except:
        dipen_post = None
    finally:
        author = "Dipen"
    return render(request, 'movies/movieReview.html', {'final_post': dipen_post, 'author':author})


'''
This function is to essentally pass the correct QueryObject of the movie to movieReview.html
'''
def displayShantnusReview(request, primKey):
    try:
        shantnu_post = Shantnu.objects.get(post=primKey)
    except:
        shantnu_post = None
    finally:
        author = "Shantnu"
    return render(request, 'movies/movieReview.html', {'final_post': shantnu_post, 'author':author})



'''
This function is to essentally pass the correct QueryObject of the movie to movieReview.html
'''
def displayAsheshsReview(request, primKey):
    try:
        ashesh_post = Ashesh.objects.get(post=primKey)
    except:
        ashesh_post = None
    finally:
        author = "Ashesh"
    return render(request, 'movies/movieReview.html', {'final_post': ashesh_post, 'author':author})


'''
This function is to essentally pass the correct QueryObject of the movie to movieReview.html
'''
def displayJayantsReview(request, primKey):
    try:
        jayant_post = Jayant.objects.get(post=primKey)
    except:
        jayant_post = None
    finally:
        author = "Jayant"
    return render(request, 'movies/movieReview.html', {'final_post': jayant_post, 'author':author})