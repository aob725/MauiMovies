from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
from django.db.models import Sum, Avg
import requests
import math
from django.core.paginator import Paginator
import config


def index(request):
    return render(request, 'login.html')

def register(request):
    errors = User.objects.registerValidator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        newuser = User.objects.create(name = request.POST['name'], username = request.POST['username'])
        request.session['loggedinId'] = newuser.id
        return redirect('/home')

def login(request):
    errors = User.objects.loginValidator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        user = User.objects.get(username = request.POST['username'])
        request.session['loggedinId'] = user.id
        return redirect('/home')

def home(request):
    if 'loggedinId' not in request.session:
        return redirect('/')
    loggedinuser = User.objects.get(id = request.session['loggedinId'])
    movie_list = Movie.objects.all().order_by('title')
    paginator = Paginator(movie_list, 25)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'loggedinuser' : loggedinuser,
        'page_obj' : page_obj
    }
    return render(request, 'home.html', context)

def newMovie(request):
    if 'loggedinId' not in request.session:
        return redirect('/')
    loggedinuser = User.objects.get(id = request.session['loggedinId'])
    context = {
        'loggedinuser' : loggedinuser,
    }
    return render(request, 'newMovie.html', context)

def createMovie(request):
    errors = Movie.objects.movieValidator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/newMovie')
    else:
        payload = {'t': request.POST['title'], 'y': request.POST['releaseDate'], 'apikey': config.omdb_key} 
        r = requests.get('http://www.omdbapi.com/', params=payload)
        if r.ok == True:
            data = r.json()
            error = 0
            print(data["Response"])
            if data["Response"] == "False":
                error += 1
                if error > 0:
                    print(error)
                    return redirect('/movieErrorPage')
            else:
                print(r.status_code)
                runtime = data["Runtime"]
                summary = data["Plot"]
                cast = data["Actors"]
                ratings = data["Ratings"]
                imdbID = data["imdbID"]
                title = data["Title"]
                genre = data["Genre"]
                director = data["Director"]
                writer = data["Writer"]
                newmovie = Movie.objects.create(title = title, releaseDate = request.POST['releaseDate'], summary = summary, cast = cast, genre = genre, director = director, writer = writer)
                return redirect('/home')
        else:
            print(r.status_code)
            redirect('/home')

def viewMovie(request, movieid):
    if 'loggedinId' not in request.session:
        return redirect('/')
    loggedinuser = User.objects.get(id = request.session['loggedinId'])
    movieToView = Movie.objects.get(id = movieid)
    print(movieToView)
    movie_reviews = Review.objects.filter(movie = Movie.objects.get(id = movieid))

    # id_review = movie_reviews["pk"]
    # print(id_review)
    # review_comments = ReviewComment.objects.filter(review=Review.objects.get(id = id_review.pk))
    
    
    movie_score = movie_reviews.values('rating').aggregate(Avg('rating'))
    payload = {'t': movieToView.title, 'y': movieToView.releaseDate, 'plot' : 'full', 'apikey': config.omdb_key} 
    

    r = requests.get('http://www.omdbapi.com/', params=payload)
    data = r.json()
    runtime = data["Runtime"]
    summary = data["Plot"]
    cast = data["Actors"]
    ratings = data["Ratings"]
    imdbID = data["imdbID"]
    title = data["Title"]
    posterPayload = {'i': imdbID, 'apikey': 'd2bc3c9c'}

    # Movie poster request from OMDB
    posterRequest = requests.get('http://img.omdbapi.com/', params=posterPayload)
    poster_url = posterRequest.url

    # Updating movie object to include rating score in DB
    movieToView.mmc_score = movie_score['rating__avg']
    movieToView.cast = cast
    movieToView.title = title
    movieToView.save()
    
    context = {
        'movieinfo' : movieToView,
        'loggedinuser' : loggedinuser,
        'movie_reviews' : movie_reviews,
        'movie_score' : movie_score,
        'title' : title,
        'runtime' : runtime,
        'summary' : summary,
        'cast' : cast,
        'ratings' : ratings,
        'imdbID' : imdbID,
        'poster_url' : poster_url,
        # 'review_comments' : review_comments,
    }
    return render(request, 'movie.html', context)

def reviewMovie(request, movieid):
    if 'loggedinId' not in request.session:
        return redirect('/')
    loggedinuser = User.objects.get(id = request.session['loggedinId'])
    movieToView = Movie.objects.get(id = movieid)
    newreview = Review.objects.create(heading = request.POST['heading'], comment = request.POST['comment'], rating = request.POST['rating'], user = loggedinuser, movie = movieToView)
    return redirect('/movie/' + movieid)

def logout(request):
    request.session.clear()
    return redirect('/')

def about(request):
    if 'loggedinId' not in request.session:
        return redirect('/')
    loggedinuser = User.objects.get(id = request.session['loggedinId'])

    context = {
        'loggedinuser' : loggedinuser,
    }
    return render(request, 'about.html', context)

def search(request):
    loggedinuser = User.objects.get(id = request.session['loggedinId'])
    if request.method == 'GET':
        search = request.GET.get('search')
        movies = Movie.objects.all().filter(title__contains=search)
        context = {
            'movies' : movies,
            'loggedinuser' : loggedinuser,
        }
        return render(request, 'search.html', context)

def message(request, reviewid):
    loggedinuser = User.objects.get(id = request.session['loggedinId'])
    reviewToCommentOn = Review.objects.get(id = reviewid)
    newMessage = ReviewComment.objects.create(message = request.POST['message'], review = reviewToCommentOn, user = loggedinuser)
    return redirect('/movieReview/' + reviewid)

def reviewPageMessage(request, reviewid):
    loggedinuser = User.objects.get(id = request.session['loggedinId'])
    reviewToCommentOn = Review.objects.get(id = reviewid)
    newMessage = ReviewComment.objects.create(message = request.POST['message'], review = reviewToCommentOn, user = loggedinuser)
    return redirect('/movieReview/' + reviewid)

def deleteMessage(request, reviewcommentid):
    loggedinuser = User.objects.get(id = request.session['loggedinId'])
    ReviewComment.objects.get(id = reviewcommentid).delete()
    return redirect('/home')

def deleteReview(request, reviewid):
    loggedinuser = User.objects.get(id = request.session['loggedinId'])
    Review.objects.get(id = reviewid).delete()
    return redirect('/home')

def movieReview(request, reviewid):
    context = {
        'review_comments' : ReviewComment.objects.filter(review=Review.objects.get(id = reviewid)),
        'review' : Review.objects.get(id=reviewid),
        'loggedinuser' : User.objects.get(id = request.session['loggedinId']),
    }
    return render(request, 'review.html', context)

def movieErrorPage(request):
    return render(request, 'movieErrorPage.html')

def contact(request):
    return render(request, 'contact.html')