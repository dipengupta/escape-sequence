from django.conf.urls import url, include
from django.urls import re_path
from . import views
from django.views.generic import ListView, DetailView
from movies.models import AllMovies, Dipen, Ankur, Shantnu, Ashesh, Jayant, UpcomingReviews


urlpatterns = [

	re_path(r'^$', views.displayHomePage, name='home-page'),
	re_path(r'movies$', ListView.as_view(queryset=AllMovies.objects.all(), template_name="movies/movieIndex.html")),
	re_path(r'movie/(?P<primKey>\d+)', views.displayAllReviewsForMovie, name='movie-page'),
	re_path(r'aboutus/', views.displayAboutUsPage, name='about-us-page'),
	re_path(r'search', views.searchMovies, name='movie-search'),
	re_path(r'ankur/(?P<primKey>\d+)', views.displayAnkursReview, name='ankurs-review'),
	re_path(r'dipen/(?P<primKey>\d+)', views.displayDipensReview, name='dipens-review'),
	re_path(r'shantnu/(?P<primKey>\d+)', views.displayShantnusReview, name='shantnus-review'),
	re_path(r'ashesh/(?P<primKey>\d+)', views.displayAsheshsReview, name='asheshs-review'),
	re_path(r'jayant/(?P<primKey>\d+)', views.displayJayantsReview, name='jayants-review'),
	
]

