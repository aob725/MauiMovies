from django.db import models
from datetime import datetime
import re, bcrypt



class LoginManager(models.Manager):

    def registerValidator(self, postData):
        errors = {}
        if len(postData['name']) < 3:
            errors['name'] = "Name must be at least 3 characters"
        if len(postData['username']) < 3:
            errors['username'] = "Username must be at least 3 characters"
        usernameInUse = User.objects.filter(username = postData['username'])
        if len(usernameInUse) > 1:
            errors['usernameInUse'] = "This username is already in use. Please choose a different one."
        return errors

    def loginValidator(self, postData):
        errors = {}
        usernameExists = User.objects.filter(username = postData['username'])
        if len(usernameExists) == 0:
            errors['usernameNotFound'] = "This username was not found. Please register first."
        else:
            user = usernameExists[0]
        return errors

class User(models.Model):
    name = models.CharField(max_length = 255)
    username = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = LoginManager()

class Movie(models.Model):
    title = models.CharField(max_length = 255)
    releaseDate = models.DateField()
    summary = models.CharField(max_length = 255)
    cast = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

class MovieManager(models.Model):
    def movieValidator(self, postData):
        errors = {}
        movieExists = Movie.objects.filter(name = postData['title'])

class Review(models.Model):
    comment = models.TextField()
    rating = models.PositiveIntegerField()
    user = models.ForeignKey(User, related_name='user_reviews', on_delete = models.CASCADE)
    movie = models.ForeignKey(Movie, related_name='movie_reviews', on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
