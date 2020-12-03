<p align="center">
  <img src="MauiMoviesApp/static/img/mmcLogo.png" style="width: 40%" />
</p>

# Maui Movie Central v1.0

 Maui Movie Central (MMC) is a movie review website where users can add movies, review movies, and respond to reviews. Users create an account using just a username(for now).Users provide a movie title and year released and MMC pulls the rest of the information using OMDb API, an online movie API. The movie view page includes information about the movie and displays the movie poster. There, the reviewer can leave a review for the movie including a header/review title, review score, and detailed review. That score is then taken, aggregated, and averaged with the rest of the user scores for that movie which is then displayed along with the other review scores (Rotten Tomatoes, IMDb, Metacritic).

# Motivation

 Quick story: I began a coding bootcamp the Monday that COVID-19 quarantine started. My friends and I devised a way to pass the time and expand the boundaries of our movie watching. We created a movie group where each week, 3 people were selected randomly and each would propose a movie to watch based on a category such as foreign, animated, comedy, etc. I wanted a way to have each of us rate the movie so I began sending out survey monkeys and keeping the results in a horrible Excel document. What people thought of the movie and the score they gave it was lost in the wind and working with the Excel document was an absolute pain. I wanted a nice, clean database to have our thoughts and ratings for the movies we watched. Finally, 9 months later, MMC was born.

 # Tech/Framwork Used
* Python
* Django Framework
* OMDb API - http://www.omdbapi.com/
* JavaScript
* HTML5
* CSS3
* Bootstrap v4.0

# Features

* Movie information auto fills using just title and year and is added to movie table
* User can select movie to see details and reviews
* User can score and write a review for a movie
* Other users can comment on a review
* MMC score is automatically calculated and displayed on the page
* Pagination - 25 titles per page on the home table
* Search bar by title


# How to Use

1. Simply create an account using a username (password field may be added later)
2. View movie table and add movie if is not there add it using title and release year
3. Click on "Go To" on movie table to view movie details and leave a review

# Screenshots 




# Maui

This project is named after my 7 month old kitten that my roommate and I adopted in May 2020. She was only 1 month old and loves to wrestle, chase, and cuddle!
<p align="center">
  <img src="MauiMoviesApp/static/img/maui.jpg" style="width: 40%" />
</p>


&#169; Adam Brady
