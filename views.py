#This function takes in the name of a template file as the first argument.
#It then automatically searches for the template file in our app/templates/ sub directory and loads it.
from flask import render_template
from app import app

#Views
@app.route('/')
def index():
#View root page function that returns the index page and its data
   #add a message variable to the view function
    message = "What's up bruv!"
    #pass the variable as an argument in our render_template() function
    return render_template('index.html', message=message)


#new movie view
#View movie page function that returns the movie details page and its data
@app.route('/movie/<int:movie_id>')
def movie(movie_id):
    # id = 45
    return render_template('movie.html', id = movie_id)

#view 3
    #View root page function that returns the index page and its data
@app.route('/')
def index():
    title = 'Home - Welcome to The best Movie Review Website Online'
    return render_template('index.html', title = title)
  