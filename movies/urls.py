from django.conf.urls import url, include
from django.urls import re_path
from . import views
from django.views.generic import ListView, DetailView
from movies.models import AllMovies, Dipen, Ankur, Shantnu, Ashesh, Jayant, UpcomingReviews


urlpatterns = [

	re_path(r'^$', views.displayLandingPage, name='landing-page'),
	re_path(r'home/', views.displayHomePage, name='home-page'),
	re_path(r'movie/(?P<primKey>\d+)', views.displayAllReviewsForMovie, name='movie-page'),
	re_path(r'movies$', ListView.as_view(queryset=AllMovies.objects.all(), template_name="movies/moviePages/allMoviesReviewed.html")),
	re_path(r'movies/genres$', views.displayMoviePageWithGenres, name='movie-genres'),
	re_path(r'movies/moods$', views.displayMoviePageWithMoods, name='movie-moods'),
	re_path(r'movies/ratings$', views.displayMoviePageWithRatings, name='movie-ratings'),
	re_path(r'test$', views.moviesFilter, name='movie-filter'),
	re_path(r'ankur', views.displayPersonalPageAnkur, name='personal-ankur'),
	re_path(r'dipen', views.displayPersonalPageDipen, name='personal-dipen'),
	re_path(r'jayant', views.displayPersonalPageJayant, name='personal-jayant'),
	re_path(r'ashesh', views.displayPersonalPageAshesh, name='personal-ashesh'),
	re_path(r'shantnu', views.displayPersonalPageShantnu, name='personal-shantnu'),
	re_path(r'aboutus/', views.displayAboutUsPage, name='about-us-page'),
	re_path(r'search', views.searchMovies, name='movie-search'),
]


