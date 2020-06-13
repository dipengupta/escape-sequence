from django.shortcuts import render
from django.views.generic.detail import DetailView
from movies.models import AllMovies, Dipen, Ankur, Shantnu, Ashesh, Jayant, UpcomingReviews
from django.db.models import Q



'''

This is essentially the one-stop function to display info and reviews for that movie

Input: Primary key of the movie (from the URL)
Returns: Dict of QuerySets with the relevent movie data

'''
def displayAllReviewsForMovie(request, primKey):

    try:
        movie_post = AllMovies.objects.get(id=primKey)
    except:
        movie_post = None


    try:
        ankur_post = Ankur.objects.get(post=primKey)
    except:
        ankur_post = None


    try:
        dipen_post = Dipen.objects.get(post=primKey)     
    except:
        dipen_post = None


    try:
        shantnu_post = Shantnu.objects.get(post=primKey)
    except:
        shantnu_post = None


    try:
        ashesh_post = Ashesh.objects.get(post=primKey) 
    except:
        ashesh_post = None


    try:
        jayant_post = Jayant.objects.get(post=primKey)

    except:
        jayant_post = None


    try:
        verdictDict = AllMovies.objects.get(id=primKey).getOverallRating()
    except:
        verdictDict = None

        
    finally:
        masterDict = {
            'movie_post': movie_post, 
            'ankur_post': ankur_post, 
            'dipen_post': dipen_post, 
            'shantnu_post': shantnu_post, 
            'ashesh_post': ashesh_post, 
            'jayant_post': jayant_post,
        }

        masterDict.update(verdictDict)


    return render(request, 'movies/allReviewsForMovie.html', masterDict)





'''

This is the function to display the home screen

Input: nothing
Returns: Dict of QuerySets with the relevent movie data

'''
def displayHomePage(request):


    #This is for Recently Reviewed Movies
    try:
        recently_reviewed = AllMovies.objects.all().order_by('-id')[:3]
    except:
        recently_reviewed = None



    #This is for Ucoming Movie Reviews 
    try:
        upcoming_reviews = UpcomingReviews.objects.all().order_by('id')[:3]
    except:
        upcoming_reviews = None



    #This is for Movies that all 5 of us liked
    try:
        listOfMoviesWithFiveLikes = []
        allMovies = AllMovies.objects.all()
        for movie in allMovies:
            if movie.getOverallRating().get('totalLikes') == 5:
                listOfMoviesWithFiveLikes.append(movie)
    except:
        allMovies = None



    finally:
        masterDict = {
            'recently_reviewed' : recently_reviewed,
            'upcoming_reviews' : upcoming_reviews,
            'listOfMoviesWithFiveLikes' : listOfMoviesWithFiveLikes
        }


    return render(request, 'movies/home.html', masterDict)





'''

This is the function to display the about-us screen

Input: nothing
Returns: render of "About Us" page

'''
def displayAboutUsPage(request):
    return render(request, 'movies/aboutUs.html')





'''
This is the implementation for the search functionality.

The search queries the "AllMovies" model for the following: {movieTitle, movieGenre, movieDirectors, movieActors}

'''
def searchMovies(request):
    if request.method == 'GET':
        query= request.GET.get('q')



        #this little bit is to handle empty strings, it will just display the home page
        if len(query) == 0:
            return displayHomePage(request)



        #this little bit is to remove a trailing space from the query
        if query[-1] == ' ':
            query = query[:-1]
            

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
This is a function that will pass data to /test/, it's just to test out stuff before adding it to main page
'''
def moviesFilter(request):

    listOfMoviesWithFiveLikes = []

    try:
        allMovies = AllMovies.objects.all()
        for movie in allMovies:
            if movie.getOverallRating().get('totalLikes') == 5:
                listOfMoviesWithFiveLikes.append(movie)

    except:
        allMovies = None

    finally:
        moviesWithFiveLikes = {
            'listOfMoviesWithFiveLikes' : listOfMoviesWithFiveLikes
        }   

  
    return render(request, 'movies/moviesFilter.html', moviesWithFiveLikes)