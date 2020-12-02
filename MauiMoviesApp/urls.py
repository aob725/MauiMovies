from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('login', views.login),
    path('home', views.home),
    path('newMovie', views.newMovie),
    path('createMovie', views.createMovie),
    path('movie/<movieid>', views.viewMovie),
    path('review/<movieid>', views.reviewMovie),
    path('logout', views.logout),
    path('about', views.about),
    path('search', views.search),
    path('message/<reviewid>', views.message),
    path('movieReview/<reviewid>', views.movieReview),
    path('deleteMessage/<reviewcommentid>', views.deleteMessage),
    path('deleteReview/<reviewid>', views.deleteReview),
    path('movieErrorPage', views.movieErrorPage),
    path('contact', views.contact),
]
