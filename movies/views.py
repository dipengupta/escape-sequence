from django.shortcuts import render
from django.views.generic.detail import DetailView
from movies.models import AllMovies, Dipen, Ankur, Shantnu, Ashesh, Jayant, UpcomingReviews
from django.db.models import Q
from django.core.paginator import Paginator



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

This is the function to display what the user will see when they first visit the site

Input: nothing
Returns: render of "Landing" page (essentially index page)

'''
def displayLandingPage(request):
    return render(request, 'movies/landingPage.html')


    


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



    #This is for Upcoming Movie Reviews 
    try:
        upcoming_reviews = UpcomingReviews.objects.all().order_by('-id')[:3]
    except:
        upcoming_reviews = None



    #This is for Movies that all 5 of us liked
    try:
        listOfMoviesWithFiveLikes = []
        allMovies = AllMovies.objects.all()

        for movie in allMovies:
            if movie.getOverallRating().get('totalLikes') == 5:
                listOfMoviesWithFiveLikes.append(movie)

        #this line is to take only the last 4 of those
        listOfMoviesWithFiveLikes = listOfMoviesWithFiveLikes[:3]
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

The search queries the "AllMovies" model for the following: {movieTitle, movieGenres, movieMoods, movieDirectors, movieActors}

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
            lookups= Q(movieTitle__icontains=query) | Q(movieGenres__icontains=query) | Q(movieMoods__icontains=query) | Q(movieDirectors__icontains=query) | Q(movieActors__icontains=query)  

            results= AllMovies.objects.filter(lookups).distinct()

            context={'results': results,
                     'submitbutton': submitbutton}

            return render(request, 'movies/searchResults.html', context)

        else:
            return render(request, 'movies/searchResults.html')

    else:
        return render(request, 'movies/searchResults.html')







'''
This is a helper function to get a list of querysets of movies of a particular genre

input: String: genreName
output: releavent [<querySet>] 
'''
def getMoviesWithThisGenre(request, genreName):

    listOfMoviesWithThisGenre = []

    try:
        allMovies = AllMovies.objects.all().order_by('-id')
        for movie in allMovies:

            retreivedData = movie.getMovieGenres().splitlines()

            if genreName in retreivedData:
                listOfMoviesWithThisGenre.append(movie)

    except:
        allMovies = None
   
    return listOfMoviesWithThisGenre





'''
This is a helper function to get a list of querysets of movies of a particular mood

input: String: moodName
output: releavent [<querySet>] 
'''
def getMoviesWithThisMood(request, moodName):

    listOfMoviesWithThisMood = []

    try:
        allMovies = AllMovies.objects.all().order_by('-id')
        for movie in allMovies:
            
            retreivedData = movie.getMovieMoods().splitlines()

            if moodName in retreivedData:
                listOfMoviesWithThisMood.append(movie)

    except:
        allMovies = None
   
    return listOfMoviesWithThisMood






'''
This is the function to call Ankur's personal page. Customize it however
'''
def displayPersonalPageAnkur(request):

    lomWithGenreComedy = getMoviesWithThisGenre(request,'comedy')

    masterDict = {
        'lomWithGenreComedy' : lomWithGenreComedy        
    }   

    return render(request, 'movies/personalPages/personalPage_ankur.html', masterDict)





'''
This is the function to call Dipen's personal page. Customize it however
'''
def displayPersonalPageDipen(request):

    lomWithMoodHighOnLife = getMoviesWithThisMood(request,'high-on-life')

    masterDict = {
        'lomWithMoodHighOnLife' : lomWithMoodHighOnLife        
    }   

    return render(request, 'movies/personalPages/personalPage_dipen.html', masterDict)





'''
This is the function to call Jayant's personal page. Customize it however
'''
def displayPersonalPageJayant(request):

    lomWithGenreAbsoluteClassics = getMoviesWithThisGenre(request,'absolute-classics')

    masterDict = {
        'lomWithGenreAbsoluteClassics' : lomWithGenreAbsoluteClassics        
    }   

    return render(request, 'movies/personalPages/personalPage_jayant.html', masterDict)





'''
This is the function to call Ashesh's personal page. Customize it however
'''
def displayPersonalPageAshesh(request):

    lomWithMoodScaredShitless = getMoviesWithThisMood(request,'scared-shitless')

    masterDict = {
        'lomWithMoodScaredShitless' : lomWithMoodScaredShitless        
    }   

    return render(request, 'movies/personalPages/personalPage_ashesh.html', masterDict)





'''
This is the function to call Shantnu's personal page. Customize it however
'''
def displayPersonalPageShantnu(request):

    lomWithGenreDocumentary = getMoviesWithThisGenre(request,'documentary')

    masterDict = {
        'lomWithGenreDocumentary' : lomWithGenreDocumentary        
    }   

    return render(request, 'movies/personalPages/personalPage_shantnu.html', masterDict)






'''
This is a function that will pass data to /movies/
'''
def displayMoviesPage(request):

    #This is for all Movies
    try:
        all_movies = AllMovies.objects.all().order_by('-id')
            

        #This is for Movies for the "ratings" tab
        listOfMoviesWithFiveLikes = []
        listOfMoviesWithThreeLikes = []

        for movie in all_movies:
            if movie.getOverallRating().get('totalLikes') == 5:
                listOfMoviesWithFiveLikes.append(movie)
            if movie.getOverallRating().get('totalLikes') == 3:
                listOfMoviesWithThreeLikes.append(movie)



    except:
        all_movies = None

    finally:

        #this is to enable pagination for "All Movies"
        paginator = Paginator(all_movies, 9) # Show 9 movies per page.

        page_number = request.GET.get('page')
        all_movies_page_obj = paginator.get_page(page_number)


        #this line is to take only the last 'n' of those
        listOfMoviesWithFiveLikes = listOfMoviesWithFiveLikes[:3]
        listOfMoviesWithThreeLikes = listOfMoviesWithThreeLikes[:5]




    #these are function calls to get LOMs by Genre
    lomWithGenreMindBending = getMoviesWithThisGenre(request,'mind-bending')[:3]
    lomWithGenreSuperhero = getMoviesWithThisGenre(request,'superhero')[:3]
    lomWithGenreComedy = getMoviesWithThisGenre(request,'comedy')[:3]
    lomWithGenreAbsoluteClassics = getMoviesWithThisGenre(request,'absolute-classics')[:3]
    lomWithGenreDocumentary = getMoviesWithThisGenre(request,'documentary')[:3]



    #these are function calls to get LOMs by Mood
    lomWithMoodScaredShitless = getMoviesWithThisMood(request,'scared-shitless')[:3]
    lomWithMoodHighOnLife = getMoviesWithThisMood(request,'high-on-life')[:3]
    lomWithMoodEasyWatching = getMoviesWithThisMood(request,'easy-watching')[:3]



    masterDict = {

        'all_movies_page_obj' : all_movies_page_obj,
        'listOfMoviesWithFiveLikes' : listOfMoviesWithFiveLikes,
        'listOfMoviesWithThreeLikes' : listOfMoviesWithThreeLikes,
        'lomWithMoodScaredShitless' : lomWithMoodScaredShitless,
        'lomWithMoodHighOnLife' : lomWithMoodHighOnLife,
        'lomWithMoodEasyWatching':lomWithMoodEasyWatching,
        'lomWithGenreMindBending' : lomWithGenreMindBending,
        'lomWithGenreSuperhero' : lomWithGenreSuperhero,
        'lomWithGenreComedy' : lomWithGenreComedy,
        'lomWithGenreAbsoluteClassics' : lomWithGenreAbsoluteClassics,
        'lomWithGenreDocumentary' : lomWithGenreDocumentary,

    }   


    return render(request, 'movies/movieIndex.html', masterDict)







'''

This is essentially the one-stop function to display all movies of the clicked genre

Input: Primary key of the mood (from the URL, also refer Django-Notes for the complete dict)
Returns: Dict of QuerySets with the relevent movie data, and title

'''
def displayAllMoviesWithThisGenre(request, primKey):

    all_movies_data = None
    page_title = "Genre"
    
    # 1. Mind Bending
    if primKey == "1":
        try:
            all_movies_data = getMoviesWithThisGenre(request,'mind-bending')
        except:
            all_movies_data = None
        finally:
            page_title = "Mind Bending"

    # 2. Documentaries
    if primKey == "2":
        try:
            all_movies_data = getMoviesWithThisGenre(request,'documentary')
        except:
            all_movies_data = None
        finally:
            page_title = "Documentaries"

    # 3. Comic Book Superheroes
    if primKey == "3":
        try:
            all_movies_data = getMoviesWithThisGenre(request,'superhero')
        except:
            all_movies_data = None
        finally:
            page_title = "Comic Book Superheroes"

    # 4. Absolute Classics
    if primKey == "4":
        try:
            all_movies_data = getMoviesWithThisGenre(request,'absolute-classics')
        except:
            all_movies_data = None
        finally:
            page_title = "Absolute Classics"

    # 5. Qualifies as Comedy
    if primKey == "5":
        try:
            all_movies_data = getMoviesWithThisGenre(request,'comedy')
        except:
            all_movies_data = None
        finally:
            page_title = "Qualifies as Comedy"
    


    masterDict = {
        'all_movies_data': all_movies_data, 
        'page_title' : page_title
    }


    return render(request, 'movies/moviePages/allMoviesWithThisGenre.html', masterDict)









'''

This is essentially the one-stop function to display all movies of the clicked mood

Input: Primary key of the mood (from the URL, also refer Django-Notes for the complete dict)
Returns: Dict of QuerySets with the relevent movie data, and title

'''
def displayAllMoviesWithThisMood(request, primKey):

    all_movies_data = None
    page_title = "Mood"
    
    # 1. Easy Watching
    if primKey == "1":
        try:
            all_movies_data = getMoviesWithThisMood(request,'easy-watching')
        except:
            all_movies_data = None
        finally:
            page_title = "Easy Watching"

    # 2. High on Life
    if primKey == "2":
        try:
            all_movies_data = getMoviesWithThisMood(request,'high-on-life')
        except:
            all_movies_data = None
        finally:
            page_title = "High on Life"

    # 3. Scared Shitless
    if primKey == "3":
        try:
            all_movies_data = getMoviesWithThisMood(request,'scared-shitless')
        except:
            all_movies_data = None
        finally:
            page_title = "Scared Shitless"


    masterDict = {
        'all_movies_data': all_movies_data, 
        'page_title' : page_title
    }


    return render(request, 'movies/moviePages/allMoviesWithThisMood.html', masterDict)









'''
This is a function that will pass data to /test/, it's just to test out stuff before adding it to main page
'''
def moviesFilter(request):

    #This is for Recently Reviewed Movies
    try:
        all_movies = AllMovies.objects.all().order_by('-id')
    except:
        all_movies = None



    paginator = Paginator(all_movies, 9) # Show 9 movies per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)


    masterDict = {
        'listOfMoviesWithThisMood' : getMoviesWithThisMood(request,'scared-shitless'),
        'listOfMoviesWithThisGenre' : getMoviesWithThisGenre(request,'mind-bending'),
        'page_obj': page_obj
    }   

    return render(request, 'movies/moviesFilter.html', masterDict)